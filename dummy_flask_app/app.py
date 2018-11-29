import requests
from  flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") 
def hello():
    return render_template("hello.html")

@app.route("/about") 
def about():
    return render_template("dummy.html")
 


if __name__ == "__main__":
    app.run()
