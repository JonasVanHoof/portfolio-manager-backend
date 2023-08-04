import uuid
import helpers
import logging
from string import Template
import helpers

PROJECT_KEYWORD = "PERSONAL_PROJECT_PROJECT" # if you change this you have to create a migration that will update all items to use the new keyword

def createProject(name, description):
  str_uuid = str(uuid.uuid4())
  query_template = Template("""
  PREFIX schema: <http://schema.org/>

  INSERT DATA {
    GRAPH <http://mu.semte.ch/application> {
      <http://mu.semte.ch/application/projects/$uuid>
      schema:name "$name";
      schema:description "$description";
      schema:keywords "$project_keyword" ;
      schema:identifier "$uuid" .
    }
  } 
  """)
  query_string = query_template.substitute(
    uuid=str_uuid,
    name=name,
    description=description,
    project_keyword=PROJECT_KEYWORD
  )
  helpers.update(query_string)

  return str_uuid

def getAllProjectNamesWithId():
  query_template = Template("""
  SELECT ?id ?name ?description
  WHERE {          
    ?s <http://schema.org/keywords> "$project_keyword" .
    ?s <http://schema.org/identifier> ?id .
    ?s <http://schema.org/name> ?name .
    ?s <http://schema.org/description> ?description .
  }      
  """)
  query_string = query_template.substitute(project_keyword=PROJECT_KEYWORD)
  
  return helpers.query(query_string)

def getProjectById(projectId):
  query_template = Template("""
  SELECT ?id ?name ?description
  WHERE {          
    <http://mu.semte.ch/application/projects/$projectId> <http://schema.org/identifier> ?id .
    <http://mu.semte.ch/application/projects/$projectId> <http://schema.org/name> ?name .
    <http://mu.semte.ch/application/projects/$projectId> <http://schema.org/description> ?description .
  }         
  """)
  query_string = query_template.substitute(projectId=projectId)

  return helpers.query(query_string)

def getProjectEmployees(projectId):
  query_template = Template("""
  SELECT ?id ?firstName ?lastName
  WHERE {          
    <http://mu.semte.ch/application/projects/$projectId> <http://schema.org/employee> ?employee .
    ?employee <http://schema.org/identifier> ?id .
    ?employee <http://schema.org/givenName> ?firstName .
    ?employee <http://schema.org/familyName> ?lastName .
  }          
  """)
  query_string = query_template.substitute(projectId=projectId)

  return helpers.query(query_string)

def getProjectCompanies(projectId):
  query_template = Template("""
  SELECT ?id ?name ?description
  WHERE {          
    <http://mu.semte.ch/application/projects/$projectId> <http://schema.org/Organization> ?company .
    ?company <http://schema.org/name> ?name .
    ?company <http://schema.org/identifier> ?id .
  }          
  """)
  query_string = query_template.substitute(projectId=projectId)

  return helpers.query(query_string)

def addEmployeeToProject(projectId, employeeId):
  query_template = Template("""
  PREFIX schema: <http://schema.org/>
  INSERT DATA INTO <http://mu.semte.ch/application/projects/>
  { 
    <http://mu.semte.ch/application/projects/$projectId> schema:employee <http://mu.semte.ch/application/employees/$employeeId> .
  }          
  """)
  query_string = query_template.substitute(projectId=projectId, employeeId=employeeId)

  return helpers.query(query_string)

def addCompanyToProject(projectId, companyId):
  query_template = Template("""
  PREFIX schema: <http://schema.org/>
  INSERT DATA INTO <http://mu.semte.ch/application/projects/>
  { 
    <http://mu.semte.ch/application/projects/$projectId> schema:Organization <http://mu.semte.ch/application/companies/$companyId> .
  }          
  """)
  query_string = query_template.substitute(projectId=projectId, companyId=companyId)

  return helpers.query(query_string)