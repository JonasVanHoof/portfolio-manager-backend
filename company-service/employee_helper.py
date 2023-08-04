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

EMPLOYEE_KEYWORD = "PERSONAL_PROJECT_EMPLOYEE" # if you change this you have to create a migration that will update all items to use the new keyword
  

def createEmployee(firstName, lastName):
  str_uuid = str(uuid.uuid4())
  query_template = Template("""
  PREFIX schema: <http://schema.org/>

  INSERT DATA {
    GRAPH <http://mu.semte.ch/application> {
      <http://mu.semte.ch/application/employees/$uuid>
      schema:givenName "$firstName";
      schema:familyName "$lastName";
      schema:keywords "$employee_keyword" ;
      schema:identifier "$uuid" .
    }
  } 
  """)
  query_string = query_template.substitute(
    uuid=str_uuid,
    firstName=firstName,
    lastName=lastName,
    employee_keyword=EMPLOYEE_KEYWORD
  )
  helpers.update(query_string)

  return str_uuid

def getEmployeeById(employeeId):
  query_template = Template("""
  SELECT ?id ?firstName ?lastName
  WHERE {          
    <http://mu.semte.ch/application/employees/$employeeId> <http://schema.org/identifier> ?id .
    <http://mu.semte.ch/application/employees/$employeeId> <http://schema.org/givenName> ?firstName .
    <http://mu.semte.ch/application/employees/$employeeId> <http://schema.org/familyName> ?lastName .
  }         
  """)
  query_string = query_template.substitute(employeeId=employeeId)

  return helpers.query(query_string)

def getAllEmployeeNamesWithId():
  query_template = Template("""
  SELECT ?id ?firstName ?lastName
  WHERE {          
    ?s <http://schema.org/keywords> "$employee_keyword" .
    ?s <http://schema.org/identifier> ?id .
    ?s <http://schema.org/givenName> ?firstName .
    ?s <http://schema.org/familyName> ?lastName .
  }      
  """)
  query_string = query_template.substitute(employee_keyword=EMPLOYEE_KEYWORD)
  
  return helpers.query(query_string)

def getCompaniesForEmployee(employeeId):
  query_template = Template("""
  SELECT ?id ?name
  WHERE {          
    <http://mu.semte.ch/application/employees/$employeeId> <http://schema.org/Organization> ?company .
    ?company <http://schema.org/identifier> ?id .
    ?company <http://schema.org/name> ?name .
  }          
  """)
  query_string = query_template.substitute(employeeId=employeeId)

  return helpers.query(query_string)

def getProjectsForEmployee(employeeId):
  query_template = Template("""
  SELECT ?id ?name
  WHERE {          
    <http://mu.semte.ch/application/employees/$employeeId> <http://schema.org/Project> ?project .
    ?project <http://schema.org/identifier> ?id .
    ?project <http://schema.org/name> ?name .
    ?project <http://schema.org/description> ?description .
  }          
  """)
  query_string = query_template.substitute(employeeId=employeeId)

  return helpers.query(query_string)

def addCompanyToEmployee(employeeId, companyId):
  query_template = Template("""
  PREFIX schema: <http://schema.org/>
  INSERT DATA INTO <http://mu.semte.ch/application/employees/>
  { 
    <http://mu.semte.ch/application/employees/$employeeId> schema:Organization <http://mu.semte.ch/application/companies/$companyId> .
  }          
  """)
  query_string = query_template.substitute(employeeId=employeeId, companyId=companyId)

  return helpers.query(query_string)

def addProjectToEmployee(employeeId, projectId):
  query_template = Template("""
  PREFIX schema: <http://schema.org/>
  INSERT DATA INTO <http://mu.semte.ch/application/employees/>
  { 
    <http://mu.semte.ch/application/employees/$employeeId> schema:Project <http://mu.semte.ch/application/projects/$projectId> .
  }          
  """)
  query_string = query_template.substitute(employeeId=employeeId, projectId=projectId)

  return helpers.query(query_string)



