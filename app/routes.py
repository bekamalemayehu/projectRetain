#homepage route
from . import app
@app.route('/') # a "decorator" (unique to python). modifies the function after it
@app.route('/index')
def index():
    return "Hello world!"
#basically, anytime someone requests / or /index, 
# the index() function will be called and return "Hello world!" to the user.
#can have multiple URLs for the same function/handler, as shown above.
#can't have multiple functions/handlers for the same URL, though. only 1