(in-package :mu-cl-resources)

(define-resource company ()
  :class (s-prefix "schema:Organization")
  :properties `((:name :string ,(s-prefix "schema:name"))
                (:description :string ,(s-prefix "schema:description"))
                (:address :string ,(s-prefix "schema:adress")))
  :has-many `((employee :via ,(s-prefix "schema:Person"):as "employees")
              (project :via ,(s-prefix "schema:Project"):as "projects"))
  :resource-base (s-url "http://mu.semte.ch/application/portfolio-manager/companies/")
  :on-path "companies")

(define-resource employee ()
  :class (s-prefix "schema:Person")
  :properties `((:given-name :string ,(s-prefix "schema:givenName"))
                (:family-name :string ,(s-prefix "schema:familyName"))
                (:bio :string ,(s-prefix "schema:description"))
                (:telephone :string ,(s-prefix "schema:telephone"))
                (:job-title :string ,(s-prefix "schema:jobTitle"))
                (:address :string ,(s-prefix "schema:address"))
                (:email :string ,(s-prefix "schema:email")))
  :has-many `((company :via ,(s-prefix "schema:Organization"):as "companies")
              (project :via ,(s-prefix "schema:Project"):as "projects"))
  :resource-base (s-url "http://mu.semte.ch/application/portfolio-manager/employees/")
  :on-path "employees")

(define-resource project ()
  :class (s-prefix "schema:Project")
  :properties `((:name :string ,(s-prefix "schema:name"))
               (:description :string ,(s-prefix "schema:description")))
  :has-many `((company :via ,(s-prefix "schema:Organization"):as "companies")
              (employee :via ,(s-prefix "schema:Person"):as "employees"))
  :resource-base (s-url "http://mu.semte.ch/application/portfolio-manager/projects/")
  :on-path "projects")