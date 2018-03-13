import requests
from  flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/") 
def hello():
    return render_template("hello.html")

@app.route("/sendmail", methods=["POST"])
def send_simple_message():
    form_data = request.form
    name = form_data["name"]
    email = form_data["email"]
    send_to = "{0} <{1}>".format(name, email)
    email_text = "Hello {0}, this is a mail from me".format(name)

    return "Mail sent - {0}".format(response.text)

app.run()