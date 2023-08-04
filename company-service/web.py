import company_endpoints
import employee_endpoints
from flask import request
import project_endpoints

# COMPANY
@app.route("/company/create", methods = ['POST'])
def createCompany():
  return company_endpoints.createCompany(request)

@app.route("/company/id/<companyId>", methods = ['GET'])
def getCompanyById(companyId):
  return company_endpoints.getCompanyById(companyId)

@app.route("/company/list", methods = ['GET'])
def getAllCompanyNamesWithId():
  return company_endpoints.getCompanyListInformation()

@app.route("/company/<companyId>/employees/add", methods = ['POST'])
def addEmployeesToCompany(companyId):
  return company_endpoints.addEmployeesToCompany(companyId, request)

@app.route("/company/<companyId>/projects/add", methods = ['POST'])
def addProjectsToCompany(companyId):
  return company_endpoints.addProjectsToCompany(companyId, request)

@app.route("/company/<companyId>/employees", methods = ['GET'])
def getCompanyEmployees(companyId):
  return company_endpoints.getCompanyEmployees(companyId)

@app.route("/company/<companyId>/projects", methods = ['GET'])
def getCompanyProjects(companyId):
  return company_endpoints.getCompanyProjects(companyId)

# EMPLOYEE
@app.route("/employee/create", methods = ['POST'])
def createEmployee():
  return employee_endpoints.createEmployee(request)

@app.route("/employee/id/<employeeId>", methods = ['GET'])
def getEmployeeById(employeeId):
  return employee_endpoints.getEmployeeById(employeeId)

@app.route("/employee/list", methods = ['GET'])
def getAllEmployeeNamesWithId():
 return employee_endpoints.getAllEmployeeNamesWithId()

@app.route("/employee/<employeeId>/companies/add", methods = ['POST'])
def addCompaniesToEmployee(employeeId):
  return employee_endpoints.addCompaniesToEmployee(employeeId, request)

@app.route("/employee/<employeeId>/projects/add", methods = ['POST'])
def addProjectsToEmployee(employeeId):
  return employee_endpoints.addProjectsToEmployee(employeeId, request)

@app.route("/employee/<employeeId>/companies", methods = ['GET'])
def getCompaniesForEmployee(employeeId):
  return employee_endpoints.getCompaniesForEmployee(employeeId)

@app.route("/employee/<employeeId>/projects", methods = ['GET'])
def getProjectsForEmployee(employeeId):
  return employee_endpoints.getProjectsForEmployee(employeeId)

# PROJECT
@app.route("/project/create", methods = ['POST'])
def createProject():
  return project_endpoints.createProject(request)

@app.route("/project/list", methods = ['GET'])
def getAllProjectNamesWithId():
 return project_endpoints.getAllEmployeeNamesWithId()

@app.route("/project/id/<projectId>", methods = ['GET'])
def getProjectById(projectId):
  return project_endpoints.getProjectById(projectId)

@app.route("/project/<projectId>/employees/add", methods = ['POST'])
def addEmployeesToProject(projectId):
  return project_endpoints.addEmployeesToProject(projectId, request)

@app.route("/project/<projectId>/companies/add", methods = ['POST'])
def addCompaniesToProject(projectId):
  return project_endpoints.addCompaniesToProject(projectId, request)

@app.route("/project/<projectId>/employees", methods = ['GET'])
def getProjectEmployees(projectId):
  return project_endpoints.getEmployeesOnProject(projectId)

@app.route("/project/<projectId>/companies", methods = ['GET'])
def getProjectEmployees(projectId):
  return project_endpoints.getProjectCompanies(projectId)
