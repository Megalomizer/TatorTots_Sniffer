from flask import Flask, render_template, redirect

app = Flask(__name__, template_folder='templates', static_url_path='/static', )

global snifferActivityTracker;
global spooferActivityTracker;
snifferActivityTracker = "Inactive";
spooferActivityTracker = "Inactive";

@app.route("/")
def home(snifferbtntext=snifferActivityTracker, spooferbtntext=spooferActivityTracker):
    return render_template('activatescripts.html', snifferbtnactivity=snifferbtntext, spooferbtnactivity=spooferbtntext)

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

@app.route("/activatescripts/changeSnifferActivity")
def goScriptsBtn1():
    global snifferActivityTracker;
    global spooferActivityTracker;
    if snifferActivityTracker=="Active":
        snifferActivityTracker="Inactive"
    else:
        snifferActivityTracker="Active"
    return home(spooferbtntext=spooferActivityTracker, snifferbtntext=snifferActivityTracker)

@app.route("/activatescripts/changeSpooferActivity")
def goScriptsBtn2():
    global snifferActivityTracker;
    global spooferActivityTracker;
    if spooferActivityTracker=="Active":
        spooferActivityTracker="Inactive"
    else:
        spooferActivityTracker="Active"
    return home(spooferbtntext=spooferActivityTracker, snifferbtntext=snifferActivityTracker)

if __name__ == "__main__":
    app.run(debug=True)