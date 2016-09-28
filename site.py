import occupations, csv, random
from flask import Flask, render_template # Capital Flask is a subset of the module flask



fred = Flask(__name__)



# Home page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@fred.route("/") # decorator, goes directly above funtion header, the 
                 # "/" (route) for webpage will run this function
def welcome():
    return render_template('root.html', title = "Welcome to Homework #3")


# Occupations page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
@fred.route("/occupations")



def run():
    return render_template('occupations.html', title = "Behold the Occupations", head = "header", links = ['/'], table = occupations.getD(), randChoice = occupations.jobMe())
    


# For the winners page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@fred.route("/forthewinners")
def winners():
    return "we are da champions ma fwend"

if __name__ == '__main__':
    fred.debug = True
    fred.run()

