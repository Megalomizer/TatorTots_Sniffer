from flask import Flask, render_template, redirect
import py_files.activatescripts as activatescripts

app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.route("/")
def index():
    return render_template()

@app.route("/activatescripts")
def goScripts():
    return redirect('/')

@app.route("/heartbeats")
def goHearts():
    return render_template('heartbeats.html')

@app.route("/caloriecounter")
def goCalories():
    return render_template('caloriescounter.html')

@app.route("/sleeprythm")
def goSleep():
    return render_template('sleeprythm.html')

if __name__ == "__main__":
    app.run(debug=True)