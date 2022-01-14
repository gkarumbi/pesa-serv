from webob import Request,Response
from parse import parse

class API:

    #Create a dict where our framework will stores the paths as keys and the handle methods as values
    def __init__(self):
        self.routes={}

    #call instance of the API class
    def __call__(self,environ,start_response):
        request = Request(environ)
        response=self.handle_request(request)
        return response(environ,start_response)
    #Implement a decorator that wraps the route method
    def route(self,path):
        def wrapper(handler):
            self.routes[path]=handler
            return handler
        
        return wrapper
        
        
        
    #Where path is non-exist method returns a 404 error
    def default_response(self,response):
        response.status_code=404
        response.text = "Not found."

    
    def find_handler(self,request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path,request_path)
            if parse_result is not None:
                return handler,parse_result.named
        
        return None,None 
    #Handler to handle client requests
    def handle_request(self,request):
        response = Response()
        handler,kwargs  = self.find_handler(request_path=request.path)

        if handler is not None:
            handler(request,response,**kwargs)
        else:
            self.default_response(response)
        return response
