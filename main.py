from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify, escape, send_from_directory
#import pandas as pd
from flask_cors import CORS
import mysql.connector
#from dao import FeuilleDao
#from dao import FeuilleDao
#from models import Usager, Feuille_de_temps, Projet, User
from types import SimpleNamespace
import json
#import pdfkit
from operator import attrgetter
from datetime import date, timedelta
#from ConfigParser import ConfigParser
import os
#from BDEclipseController import BDEclipseController
#from BDEclipseHelper import sunday


app = Flask(__name__)
app.secret_key = "Electrique"
cors = CORS(app)

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     port = 3306,
#     password="LG2000",
#     auth_plugin='mysql_native_password',
#     database='Electrique'
# )

@app.route("/")
def index():

    return render_template('accueuil.html', titulo='accueuil')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)