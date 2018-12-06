import requests
from  flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/") 
def hello():
    return render_template("hello.html")

@app.route("/about") 
def about():
    return render_template("dummy_file.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route('/', methods=['POST']) 
def search():
    text_box_value = request.form['text']
    if text_box_value == "london":
        return render_template("london.html")
    if text_box_value == "thailand":
        return render_template("thailand.html")
    if text_box_value == "sydney":
        return render_template("sydney.html")
    if text_box_value == "new york":
        return render_template("nyc.html")
    if text_box_value == "rome":
        return render_template("rome.html")
    if text_box_value == "toronto":
        return render_template("toronto.html")
    else:
        return render_template("no_page.html")

@app.route("/", methods=['SUBMIT'])
def signup():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return render_template("success.html", first_name, last_name)


if __name__ == "__main__":
    app.run()
