from flask import Flask, render_template, redirect
# from py_files.activatescripts import goScriptsBtn1
# from py_files.activatescripts import goScriptsBtn2
import py_files.activatescripts as activatescripts
#import activatescripts as activatescripts

app = Flask(__name__, template_folder='templates', static_url_path='/static')

global snifferActivityTracker;
global spooferActivityTracker;
snifferActivityTracker = "Inactive";
spooferActivityTracker = "Inactive";

@app.route("/")
def index(snifferbtntext=snifferActivityTracker, spooferbtntext=spooferActivityTracker):
    return render_template('activatescripts.html', snifferbtnactivity=snifferbtntext, spooferbtnactivity=spooferbtntext)

@app.route("/activatescripts")
def goScripts():
    return redirect('/')

@app.route("/activatescripts/changeSnifferActivity")
def goScriptsRunSniffer():
    return activatescripts.changeSnifferActivity()

@app.route("/activatescripts/changeSpooferActivity")
def goScriptsRunSpoofer():
    return activatescripts.changeSpooferActivity()

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