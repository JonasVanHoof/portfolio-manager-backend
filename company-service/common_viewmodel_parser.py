import exceptions

def sparqlResultToJsonFormat(sparqlResult):
    bindings = sparqlResult["results"]["bindings"]
    properties = sparqlResult["head"]["vars"]
    viewmodel = []

    if properties == []:
        return viewmodel


    for binding in bindings:
        companyWithProperties = {}
        for propertyWithValue in properties:
            if propertyWithValue in binding:
                companyWithProperties[propertyWithValue] =  binding[propertyWithValue]["value"]     
        viewmodel.append(companyWithProperties)

    return viewmodel

def sparqlResultToValueOfSingleProperty(sparqlResult, property):
    bindings = sparqlResult["results"]["bindings"]
    properties = sparqlResult["head"]["vars"]

    if len(bindings) == 0:
        return exceptions.createNotFoundException("The sparql query resulted in zero bindings. Cannot get propery of empty list")
    
    if len(bindings) > 1:
        return exceptions.createBadRequestException("Result gave more than one result maybe you should use a differten viewmodel parser")

    if property not in properties:
        return exceptions.createNotFoundException(f"Could not get the value for property `{property}` from sparqlResult")
    
    return bindings[0][property]["value"]
