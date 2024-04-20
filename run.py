from flask import Flask, render_template, redirect, jsonify, request, url_for
import asyncio
import static.python.bluetooth as pybl
import static.python.rsacryptography as cryption

app = Flask(__name__, template_folder='templates', static_url_path='/static')

@app.route("/")
def index():
    return render_template('ActivateScripts.html')

@app.route("/activatescripts")
def home():
    return redirect('/')

@app.route("/heartbeats")
def hearts():
    return render_template('heartbeats.html')

@app.route("/caloriecounter")
def calories():
    return render_template('caloriescounter.html')

@app.route("/sleeprythm")
def sleep():
    return render_template('sleeprythm.html')

@app.route("/devicedetails", methods=['POST'])
def detailsDevice():
    if request.method == 'POST':
        device = request.json
        address = device["address"]
        name = device["name"]
        # return render_template("devicedetails.html", address=address, name=name)
        return render_template("devicedetails.html", address=address)
    
@app.route("/details", methods=['POST', 'GET'])
def details():
    if request.method == 'POST':
        name = request.values.get("name")
        address = request.values.get("address")
        print(name)
        print(address)
        return render_template("devicedetails.html", address=address, name=name)

@app.route("/activatescripts$getbl", methods=["GET"])
def findBl():
    devices = asyncio.run(pybl.BluetoothScan())
    devices = pybl.BluetoothToJSON(devices)
    return devices

@app.route("/activatescripts$delbl", methods=["DELETE"])
def delBl():
    pybl.deleteDevices()

if __name__ == "__main__":
    app.run(debug=True)