
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from sqlalchemy import create_engine
import json

app = Flask(__name__)
app.config["DEBUG"] = True

recipe_data = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="c2c_login",
    password="38Ua2ZrCuXws",
    hostname="c2c-db.coos5kthp77n.us-west-2.rds.amazonaws.com",
    databasename="flask_app")

@app.route('/', methods=["GET"])
def index():
    return render_template("main_page.html")
        
@app.route('/recipes', methods=["GET"])
def get_recipes():
    title = request.args.get("name")
    category = request.args.get("category")
    url= request.args.get("url")

    engine = create_engine(recipe_data)
    sql_query_string = "select * from RecipeData where name LIKE '%{0}%' OR url = '{1}' OR category = '{2}';".format(title, url, category)
    print(sql_query_string)
    results = engine.execute(sql_query_string)
    return json.dumps([(dict(row.items())) for row in results])