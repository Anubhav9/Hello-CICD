"""
This is the base module of the flask app

Author: Anubhav Sanyal
Date Modified: 12/12/23
"""
from flask import Flask,render_template
import constants

app=Flask(__name__)

@app.route("/",methods=["GET"])
def open_home_page():
    """The function opens the base page of the Flask App"""
    return render_template("index.html",itr_count=constants.ITERATION_COUNT)

if(__name__=="__main__"):
    app.run(port=1212,debug=True)
