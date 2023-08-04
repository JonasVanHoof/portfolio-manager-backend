import common_viewmodel_parser
import employee_helper
import exceptions
import response_helper
import httpStatusCode


def createEmployee(request):
  firstName = request.get_json().get('firstName') #create request helper for this TODO
  lastName = request.get_json().get('lastName')
  missingProperties = []

  for property in ['firstName', 'lastName']:
     if not  request.get_json().get(property):
        missingProperties.append(property)

  if missingProperties:
    return exceptions.createBadRequestException(f"Please provide properties [{', '.join(missingProperties)}] in body")

  return employee_helper.createEmployee(
     firstName=firstName,
     lastName=lastName
    ), httpStatusCode.HTTP_CREATED

def getEmployeeById(employeeId):
  employees = common_viewmodel_parser.sparqlResultToJsonFormat(employee_helper.getEmployeeById(employeeId))

  if len(employees) != 1:
    return exceptions.createNotFoundException(f"Could not find employee with id `{employeeId}`") 
  
  return response_helper.createJsonResponse(
    viewmodel=employees[0]
  ), httpStatusCode.HTTP_OK

def getAllEmployeeNamesWithId():
  return response_helper.createJsonResponse(
      viewmodel=common_viewmodel_parser.sparqlResultToJsonFormat(employee_helper.getAllEmployeeNamesWithId())
  ), httpStatusCode.HTTP_OK

def getCompaniesForEmployee(employeeId):
  return response_helper.createJsonResponse(
    viewmodel=common_viewmodel_parser.sparqlResultToJsonFormat(employee_helper.getCompaniesForEmployee(employeeId))
  ), httpStatusCode.HTTP_OK

def getProjectsForEmployee(employeeId):
  return response_helper.createJsonResponse(
    viewmodel=common_viewmodel_parser.sparqlResultToJsonFormat(employee_helper.getProjectsForEmployee(employeeId))
  ), httpStatusCode.HTTP_OK

def addCompaniesToEmployee(employeeId, request):
  companyIdsFromJsonBody = request.get_json().get('companies') #create request helper for this TODO

  if not companyIdsFromJsonBody:
    return exceptions.createBadRequestException("Please provide property `companies` with array of company ids in body")

  # move this to a usecase method
  for companyId in companyIdsFromJsonBody:
    employee_helper.addCompanyToEmployee(employeeId, companyId)

  return response_helper.createJsonResponse(viewmodel=[]), httpStatusCode.HTTP_CREATED

def addProjectsToEmployee(employeeId, request):
  projectIdsFromJsonBody = request.get_json().get('projects') #create request helper for this TODO

  if not projectIdsFromJsonBody:
    return exceptions.createBadRequestException("Please provide property `projects` with array of project ids in body")

  # move this to a usecase method
  for projectId in projectIdsFromJsonBody:
    employee_helper.addProjectToEmployee(employeeId, projectId)

  return response_helper.createJsonResponse(viewmodel=[]), httpStatusCode.HTTP_CREATED