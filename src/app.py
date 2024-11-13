from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.post('/reset')
def resetit():
    cnt.reset()
    return redirect('/')

@app.post('/set')
def setit():
    cnt.value = int(request.form['sv'])
    return redirect('/')
