from flask import Flask

app = Flask(__name__) #Flask is a class from the flask module/package.
#the variable __name__ is automatically defined by python language. 
# special built-in "dunder variable" (recall cs1301) keyword
#there to act as filename if another file imports this file/module.
#ex: in script.py, if we did import bruh and bruh has __name__, it replaces 
#  __name__ with bruh. most common use is to have something run 
# (ex: method or print statement) if run within and have them not run automatically
# if they're imported. ex: 
# my_module.py

#def greet():
    #return "Hello from the module!"

# This block only runs if you execute this file directly
#if __name__ == "__main__":
    #print("Running script directly...")
    #print(greet())

#if run as a script, python replaces variable with __main__ as starting point
from . import routes #routes module needs to be imported after the app
#(not the local, Flask instance, but the directory/package we're making/in). 
# at the beginning, routes module doesn't exist. but when it's made, routes module
#imports the app VARIABLE that we defined as flask instance. to avoid this circular
#import error (where init imports routes and routes imports app variable from init)
#we make sure to import after app variable defined, instead of importing at the very
# top like usual.

#routes handle different URLs for the web app