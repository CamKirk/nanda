from flask import Flask, jsonify, render_template
import sqlalchemy
import flask_sqlalchemy
import pandas
import os

# print(os.environ)
if not os.environ['DYNO']:
    import config
    print(config.name)

if os.environ["JAWSDB_URL"]:
    dburl = os.environ["JAWSDB_URL"]
else:
    dburl = "sqlite://soemsqlitefilehere"

engine = sqlalchemy.create_engine(dburl)

df = pandas.read_sql("SELECT * FROM budget_data", engine)
print(df)
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify({"data":"is empty"})

if __name__ == "__main__":
    app.run()
