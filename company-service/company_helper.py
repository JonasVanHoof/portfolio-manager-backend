import uuid
import helpers
import logging
from string import Template
import helpers
  
logging.basicConfig(
  format="%(asctime)s %(process)d,%(threadName)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S",
  level=logging.INFO,
)
logger = logging.getLogger(__name__)

COMPANY_KEYWORD = "PERSONAL_PROJECT_COMPANY" # if you change this you have to create a migration that will update all items to use the new keyword
  

def createCompany(name):
  str_uuid = str(uuid.uuid4())
  query_template = Template("""
  PREFIX schema: <http://schema.org/>

  INSERT DATA {
    GRAPH <http://mu.semte.ch/application> {
      <http://mu.semte.ch/application/companies/$uuid>
      schema:name "$companyName";
      schema:keywords "$company_keyword" ;
      schema:identifier "$uuid" .
    }
  } 
  """)
  query_string = query_template.substitute(uuid=str_uuid, companyName=name, company_keyword=COMPANY_KEYWORD)
  helpers.update(query_string)

  return str_uuid

def getCompanyById(companyId):
  query_template = Template("""
  SELECT ?id ?name
  WHERE {          
    <http://mu.semte.ch/application/companies/$companyId> <http://schema.org/identifier>  ?id .
    <http://mu.semte.ch/application/companies/$companyId> <http://schema.org/name> ?name .
  }         
  """)
  query_string = query_template.substitute(companyId=companyId)

  return helpers.query(query_string)

def getAllCompanyNamesWithId():
  query_template = Template("""
  SELECT ?id ?name
  WHERE {          
    ?s <http://schema.org/keywords> "$company_keyword" .
    ?s <http://schema.org/name> ?name .
    ?s <http://schema.org/identifier> ?id .
  }      
  """)
  query_string = query_template.substitute(company_keyword=COMPANY_KEYWORD)
  
  return helpers.query(query_string)

def getCompanyEmployees(companyId):
  query_template = Template("""
  SELECT ?id ?firstName ?lastName
  WHERE {          
    <http://mu.semte.ch/application/companies/$companyId> <http://schema.org/employee> ?employee .
    ?employee <http://schema.org/identifier> ?id .
    ?employee <http://schema.org/givenName> ?firstName .
    ?employee <http://schema.org/familyName> ?lastName .
  }          
  """)
  query_string = query_template.substitute(companyId=companyId)

  return helpers.query(query_string)

def getCompanyEmployeesCount(companyId):
  query_template = Template("""
  SELECT DISTINCT (COUNT(?id) as ?count)
  WHERE {          
    <http://mu.semte.ch/application/companies/$companyId> <http://schema.org/employee> ?employee .
    ?employee <http://schema.org/identifier> ?id .
  }          
  """)
  query_string = query_template.substitute(companyId=companyId)

  return helpers.query(query_string)

def addEmployeeToCompany(companyId, employeeId):
  query_template = Template("""
  PREFIX schema: <http://schema.org/>
  INSERT DATA INTO <http://mu.semte.ch/application/companies/>
  { 
    <http://mu.semte.ch/application/companies/$companyId> schema:employee <http://mu.semte.ch/application/employees/$employeeId> .
  }          
  """)
  query_string = query_template.substitute(companyId=companyId, employeeId=employeeId)

  return helpers.query(query_string)

def addProjectToCompany(companyId, projectId):
  query_template = Template("""
  PREFIX schema: <http://schema.org/>
  INSERT DATA INTO <http://mu.semte.ch/application/companies/>
  { 
    <http://mu.semte.ch/application/companies/$companyId> schema:Project <http://mu.semte.ch/application/projects/$projectId> .
  }          
  """)
  query_string = query_template.substitute(companyId=companyId, projectId=projectId)

  return helpers.query(query_string)

def getCompanyProjects(companyId):
  query_template = Template("""
  SELECT ?id ?name ?description
  WHERE {          
    <http://mu.semte.ch/application/companies/$companyId> <http://schema.org/Project> ?project .
    ?project <http://schema.org/identifier> ?id .
    ?project <http://schema.org/name> ?name .
    ?project <http://schema.org/description> ?description .
  }          
  """)
  query_string = query_template.substitute(companyId=companyId)

  return helpers.query(query_string)

def getCompanyProjectsCount(companyId):
  query_template = Template("""
  SELECT DISTINCT (COUNT(?id) AS ?count)
  WHERE {          
    <http://mu.semte.ch/application/companies/$companyId> <http://schema.org/Project> ?project .
    ?project <http://schema.org/identifier> ?id .
  }          
  """)
  query_string = query_template.substitute(companyId=companyId)

  return helpers.query(query_string)