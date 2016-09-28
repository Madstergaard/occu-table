from flask import Flask # Capital Flask is a subset of the module flask
from utils import occupations


fred = Flask(__name__)



# Home page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@fred.route("/") # decorator, goes directly above funtion header, the 
                 # "/" (route) for webpage will run this function
def welcome():
    return render_template("root.html")


# Occupations page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
@fred.route("/occupations")


def run():
    return render_template('occuaptions.html' , occu=occupations.jobme())


# For the winners page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@fred.route("/forthewinners")
def winners():
    return "we are da champions"

if __name__ == '__main__':
    fred.run()

