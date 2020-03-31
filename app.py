from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def theme():
    return "<h1> Furniture </h1>"



@app.route("/furlist")
def furlist():
    return render_template("furlist.html")



@app.route("/kitfur")
def kitfur():
    return render_template("kitfur.html")



@app.route("/<name>/my congratulations!")
def lot(name):
    name = name.capitalize()
    return render_template("lot.html", name = name)




    