
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from sqlalchemy import create_engine
import json

app = Flask(__name__)
app.config["DEBUG"] = True


recipe_data = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="c2c_login",
    password="38Ua2ZrCuXws",
    hostname="c2c-dev-db.coos5kthp77n.us-west-2.rds.amazonaws.com",
    databasename="flask_app")

engine = create_engine(recipe_data, convert_unicode=True)
comments = []
results = []

@app.route('/', methods=["GET"])
def index():
    return render_template("main_page.html")
        
@app.route('/recipes/', methods=["GET"])
def get_recipes():
    zip_code = request.args.get["zip_code"]
    cuisine_pref = request.args.get["cuisine_pref"]
    results = engine.execute('select * from RecipeData where zip_code = %s OR cuisine_pref = %s;'.format(zip_code, cuisine_pref))
    return json.dumps(results)