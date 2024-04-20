from flask import Flask, render_template, redirect, jsonify, request, url_for
import asyncio
import static.python.bluetooth as pybl
import static.python.rsacryptography as cryption

app = Flask(__name__, template_folder='templates', static_url_path='/static')

global thread

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
    
@app.route("/details", methods=['POST', 'GET'])
def details():
    if request.method == 'POST':
        name = request.values.get("name")
        address = request.values.get("address")
        return render_template("devicedetails.html", address=address, name=name)
    
@app.route("/details$forcedconnect", methods=["POST"])
def connected():
    if request.method == "POST":
        address = request.values.get('address')
        port = request.values.get('port')
        protocol = request.values.get('protocol')
        #socket = pybl.BluetoothForceConnectService(address, port, protocol)
        socket = "emptyness is life"
        return render_template('forcedconnect.html', address=address, port=port, protocol=protocol, socket=socket)

@app.route("/activatescripts$getbl", methods=["GET"])
def findBl():
    devices = asyncio.run(pybl.BluetoothScan())
    devices = pybl.BluetoothToJSON(devices)
    return devices

@app.route("/details$scanservices", methods=['GET'])
def scanServices():
    address = request.args.get('address')
    #services = pybl.BluetoothServiceScanner(address) # IS COMMENTED -> WORKS ONLY ON LINUX
    services = [{
        "name": "aaaa",
        "description": "bbbb",
        "host": "cccc",
        "provider": "dddd",
        "port": "eeee",
        "protocol": "ffff"
    }]
    services = jsonify(services)
    return services

@app.route("/activatescripts$delbl", methods=["DELETE"])
def delBl():
    pybl.deleteDevices()

@app.route("/details$dos-start")
def startDos():
    global thread
    address = request.args.get('address')
    #thread = startDos(address)
    return jsonify("started")

@app.route("/details$dos-stop")
def stopDos():
    global thread
    #stopDos(thread)
    return jsonify("stopped")

@app.route("/details$spoofmac")
def spoofMac():
    interface = "hci0"
    newMac = request.args.get('address')
    #pybl.SpoofingMacAddress(interface, newMac)
    return jsonify("spoofed")

@app.route("/details$forcedconnect-msgsend", methods=["POST"])
def sendMsg():
    socket = request.args.get("socket")
    msg = request.args.get("msg")
    print(msg)
    #pybl.blComsSend(Socket=socket, data=msg)
    return jsonify(socket)

@app.route("/details$forcedconnect-msgreceive", methods=["GET"])
def receiveMsg():
    socket = request.args.get("socket")
    msg = "HGAHAHAHA"
    #msg = pybl.blComsReceive(Socket=socket)
    return jsonify(msg)

if __name__ == "__main__":
    app.run(debug=True)