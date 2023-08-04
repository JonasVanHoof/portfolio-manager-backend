import common_viewmodel_parser
import company_helper
import exceptions
import response_helper
import httpStatusCode

def createCompany(request):
  companyName = request.get_json().get('name') #create request helper for this TODO

  if not companyName:
    return exceptions.createBadRequestException("Please provide property `name` in body")

  return company_helper.createCompany(companyName), httpStatusCode.HTTP_CREATED

def getCompanyById(companyId):
  companies = common_viewmodel_parser.sparqlResultToJsonFormat(company_helper.getCompanyById(companyId))

  if len(companies) != 1:
    return exceptions.createNotFoundException(f"Could not find company with id `{companyId}`")

  return response_helper.createJsonResponse(
    viewmodel=companies[0]
  ), httpStatusCode.HTTP_OK

def getCompanyListInformation():
  companieNamesWithTheirId = common_viewmodel_parser.sparqlResultToJsonFormat(company_helper.getAllCompanyNamesWithId())
  viewmodel = []

  for company in companieNamesWithTheirId:
    employeesCount = common_viewmodel_parser.sparqlResultToValueOfSingleProperty(company_helper.getCompanyEmployeesCount(company.get("id")), "count")
    projectCount = common_viewmodel_parser.sparqlResultToValueOfSingleProperty(company_helper.getCompanyProjectsCount(company.get("id")), "count")
    viewmodel.append({
      "id": company.get("id"),
      "name": company.get("name"),
      "employeeCount": employeesCount,
      "projectCount": projectCount,
    })

  return response_helper.createJsonResponse(
    viewmodel=viewmodel
  ), httpStatusCode.HTTP_OK

def getCompanyEmployees(companyId):
  return response_helper.createJsonResponse(
    viewmodel=common_viewmodel_parser.sparqlResultToJsonFormat(company_helper.getCompanyEmployees(companyId))
  ), httpStatusCode.HTTP_OK

def getCompanyEmployeesCount(companyId):
  return response_helper.createJsonResponse(
    viewmodel=common_viewmodel_parser.sparqlResultToValueOfSingleProperty(company_helper.getCompanyEmployeesCount(companyId), "count")
  ), httpStatusCode.HTTP_OK

def addEmployeesToCompany(companyId, request):
  employeeIdsFromJsonBody = request.get_json().get('employees') #create request helper for this TODO

  if not employeeIdsFromJsonBody:
    return exceptions.createBadRequestException("Please provide property `employees` with array of employee ids in body")

  # move this to a usecase method
  for employeeId in employeeIdsFromJsonBody:
   company_helper.addEmployeeToCompany(companyId, employeeId)

  return response_helper.createJsonResponse(viewmodel=[]), httpStatusCode.HTTP_CREATED

def addProjectsToCompany(companyId, request):
  projectIdsFromJsonBody = request.get_json().get('projects') #create request helper for this TODO

  if not projectIdsFromJsonBody:
    return exceptions.createBadRequestException("Please provide property `projects` with array of project ids in body")

  # move this to a usecase method
  for projectId in projectIdsFromJsonBody:
    company_helper.addProjectToCompany(companyId, projectId)

  return response_helper.createJsonResponse(viewmodel=[]), httpStatusCode.HTTP_CREATED

def getCompanyProjects(companyId):
  return response_helper.createJsonResponse(
    viewmodel=common_viewmodel_parser.sparqlResultToJsonFormat(company_helper.getCompanyProjects(companyId))
  ), httpStatusCode.HTTP_OK

def getCompanyProjectsCount(companyId):
  return response_helper.createJsonResponse(
    viewmodel=common_viewmodel_parser.sparqlResultToJsonFormat(company_helper.getCompanyProjectsCount(companyId))
  ), httpStatusCode.HTTP_OK