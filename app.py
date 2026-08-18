from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# opening the csv data which is the home screen
@app.route("/")
def home():
    data=pd.read_csv("accident_statistics.csv")
    records=data.to_dict(orient="records")
    return render_template("index.html",data=records)

# opening the statistics page (the charts)
@app.route("/statistics")
def statistics():
    return render_template("statistics.html")


if __name__ == "__main__":
    app.run(debug=True)

