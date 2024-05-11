"""
The Chain of Responsibility design pattern is a "behavioral design pattern" that allows an object to pass 
a request along a chain of handlers. Each handler in the chain decides either to process the request or 
to pass it along the chain to the next handler
"""

"""
The Chain of Responsibility Design Pattern comprises the following key components:

Handler: This is an interface or abstract class that declares a method for handling requests
         and a reference to the next handler in the chain.

Concrete Handler: The concrete class that implements the Handler interface. It decides whether to process
                     a request or pass it to the next handler.

Client: The class that initiates the request and sends it to the first handler in the chain.
"""

class Request:
    def __init__(self, data):
        self.data = data
        self.valid = True

class RequestHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class AuthenticationHandler(RequestHandler):
    def handle_request(self, request):
        if "token" not in request.data:
            request.valid = False
            print("Authentication failed")
        print("AuthenticationHandler Done.....")    
        super().handle_request(request)

class DataValidationHandler(RequestHandler):
    def handle_request(self, request):
        if not request.valid:
            return
        if "data" not in request.data:
            request.valid = False
            print("Data validation failed")
        print("DataValidationHandler Done.....")      
        super().handle_request(request)

class LoggingHandler(RequestHandler):
    def handle_request(self, request):
        if not request.valid:
            return
        print("Logging request")
        super().handle_request(request)

# Client code
if __name__ == "__main__":
    request = Request({"token": "abc123", "data": "some_data"})

    authentication_handler = AuthenticationHandler()
    validation_handler = DataValidationHandler(authentication_handler)
    logging_handler = LoggingHandler(validation_handler)

    logging_handler.handle_request(request)

    if request.valid:
        print("Request processing successful")
    else:
        print("Request processing failed")