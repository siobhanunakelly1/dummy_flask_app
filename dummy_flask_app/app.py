import requests
from  flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/") 
def hello():
    return render_template("hello.html")

@app.route("/about") 
def about():
    return render_template("dummy_file.html")

@app.route("/search") 
def search():
    text_box_value = request.GET['text_box']
    if text_box_value == "London":
        return render_template("london.html")
    if text_box_value == "Thailand":
        return render_template("thailand.html")
    if text_box_value == "Sydney":
        return render_template("sydney.html")
    if text_box_value == "NYC":
        return render_template("nyc.html")
    if text_box_value == "Rome":
        return render_template("rome.html")
    if text_box_value == "Toronto":
        return render_template("toronto.html")

if __name__ == "__main__":
    app.run()
