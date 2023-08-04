import common_viewmodel_parser
import project_helper
import exceptions
import response_helper
import httpStatusCode


def createProject(request):
  name = request.get_json().get('name') #create request helper for this TODO
  description = request.get_json().get('description')
  missingProperties = []

  for property in ['name', 'description']:
     if not  request.get_json().get(property):
        missingProperties.append(property)

  if missingProperties:
    return exceptions.createBadRequestException(f"Please provide properties [{', '.join(missingProperties)}] in body")

  return project_helper.createProject(
     name=name,
     description=description
    ), httpStatusCode.HTTP_CREATED

def getAllEmployeeNamesWithId():
  projectNamesWithTheirId = common_viewmodel_parser.sparqlResultToJsonFormat(project_helper.getAllProjectNamesWithId())
  viewmodel = []

  for project in projectNamesWithTheirId:
    projectCompanies = common_viewmodel_parser.sparqlResultToJsonFormat(project_helper.getProjectCompanies(project.get("id")))
    
    companies = []
    for projectCompany in projectCompanies:
      name = projectCompany["name"]
      companies.append(name)

    viewmodel.append({
      "id": project.get("id"),
      "name": project.get("name"),
      "companies": companies,
    })

  return response_helper.createJsonResponse(
      viewmodel=viewmodel
  ), httpStatusCode.HTTP_OK

def getProjectById(projectId):
  projects = common_viewmodel_parser.sparqlResultToJsonFormat(project_helper.getProjectById(projectId))

  if len(projects) != 1:
    return exceptions.createNotFoundException(f"Could not find project with id `{projectId}`") 
  
  return response_helper.createJsonResponse(
    viewmodel=projects[0]
  ), httpStatusCode.HTTP_OK

def getEmployeesOnProject(projectId):
  return response_helper.createJsonResponse(
    viewmodel=common_viewmodel_parser.sparqlResultToJsonFormat(project_helper.getProjectEmployees(projectId))
  ), httpStatusCode.HTTP_OK

def getProjectCompanies(projectId):
  return response_helper.createJsonResponse(
    viewmodel=common_viewmodel_parser.sparqlResultToJsonFormat(project_helper.getProjectCompanies(projectId))
  ), httpStatusCode.HTTP_OK

def addEmployeesToProject(projectId, request):
  employeeIdsFromJsonBody = request.get_json().get('employees') #create request helper for this TODO

  if not employeeIdsFromJsonBody:
    return exceptions.createBadRequestException("Please provide property `employees` with array of employee ids in body")

  # move this to a usecase method
  for employeeId in employeeIdsFromJsonBody:
   project_helper.addEmployeeToProject(projectId, employeeId)

  return response_helper.createJsonResponse(viewmodel=[]), httpStatusCode.HTTP_CREATED

def addCompaniesToProject(projectId, request):
  companyIdsFromJsonBody = request.get_json().get('companies') #create request helper for this TODO

  if not companyIdsFromJsonBody:
    return exceptions.createBadRequestException("Please provide property `companies` with array of company ids in body")

  # move this to a usecase method
  for companyId in companyIdsFromJsonBody:
   project_helper.addCompanyToProject(projectId, companyId)

  return response_helper.createJsonResponse(viewmodel=[]), httpStatusCode.HTTP_CREATED