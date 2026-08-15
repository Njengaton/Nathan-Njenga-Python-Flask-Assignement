from flask import Flask, render_template
import pandas as pd
app=Flask(__name__)
df=pd.read_csv("accident_statisitics.csv")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/statistics")
def statistics():
    return render_template("statistics.html")
if __name__=="__main__":
    app.run(debug=True)