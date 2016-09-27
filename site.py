from flask import Flask # Capital Flask is a subset of the module flask
from utils import occupations

fred = Flask(__name__)



# Home page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@fred.route("/") # decorator, goes directly above funtion header, the 
                 # "/" (route) for webpage will run this function
def welcome():
    return "Welcome to the site"


# Occupations page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
@fred.route("/occupations")

import csv
import random

oc = open("occupations.csv","r").readlines()[1:-1]
oc = csv.reader(oc)
dictionary = {}

for job in oc:
    dictionary[job[0]] = float(job[1])


def jobme():
    counter = 0
    choose = random.uniform(0,99.8)
    for i in dictionary:
        counter += dictionary[i]
        if choose <= counter:
            return i


def run():
    return render_template('model-occuaptions.html' , occu=jobme())


# For the winners page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@fred.route("/forthewinners")
def winners():
    return "we are da champions"

if __name__ == '__main__':
    fred.run()

