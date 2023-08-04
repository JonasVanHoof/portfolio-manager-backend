from flask import Response
import json

ACCEPTED_ORIGINS = [
  "http://localhost:4200",
]

def createJsonResponse(viewmodel):
    response = Response(json.dumps(viewmodel))
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = ', '.join(ACCEPTED_ORIGINS)

    return response