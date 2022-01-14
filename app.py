from api import API
#create our entrypoint for Gunicorn
app =API()

@app.route("/home")
def home(request,response):
    response.text = "<h1>Hello from the HOME page</h1>"

@app.route("/about")
def about(request,response):
    response.text = "<h1>Hellow from the about page</h1>"

@app.route("/hello/{name}")
def greeting(request,response,name):
    response.text = f'<h1>Hello,{name}</h1>'
