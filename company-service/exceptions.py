import httpStatusCode
import json

def createBadRequestException(message):
  errorBody = json.dumps({
    "message": message
    }
  )
  return json.loads(errorBody), httpStatusCode.HTTP_BAD_REQUEST

def createNotFoundException(message):
  errorBody = json.dumps({
    "message": message
    }
  )
  return json.loads(errorBody), httpStatusCode.HTTP_NOT_FOUND