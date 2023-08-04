defmodule Dispatcher do
  use Matcher
  define_accept_types [
    html: [ "text/html", "application/xhtml+html" ],
    json: [ "application/json", "application/vnd.api+json" ]
  ]

  # @any %{}
  @json %{ accept: %{ json: true } }
  # @html %{ accept: %{ html: true } }

  match "/search/*path", @json do
    Proxy.forward conn, path, "http://search/"
  end

  match "/companies/*path", @json do
    Proxy.forward conn, path, "http://resource/companies/"
  end
   
  match "/employees/*path", @json do
    Proxy.forward conn, path, "http://resource/employees/"
  end
  
  match "/projects/*path", @json do
    Proxy.forward conn, path, "http://resource/projects/"
  end

  match "/*_", %{ last_call: true } do
    send_resp( conn, 404, "Route not found.  See config/dispatcher.ex" )
  end
end
