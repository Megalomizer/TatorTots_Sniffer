import asyncio
#import bluetooth
import json
import subprocess
from bleak import BleakScanner
from bleak import BleakClient

# SCAN FOR BLUETOOTH DEVICES
async def BluetoothScan():
    Devices = await BleakScanner.discover()
    return Devices
# # How to use
# Devices = asyncio.run(BluetoothScan())
# # Prints
# for Device in Devices:
#     print(f"{Device.name} - {Device.address}")

# SCAN FOR SERVICES ON BLUETOOTH DEVICE
# async def BluetoothServiceScanner(BluetoothAddress):
#   return bluetooth.find_service(address=BluetoothAddress)

# # How to use
# TargetAddress = input("[@] Enter target adddress: ")
# Services = BluetoothServiceScan(TargetAddress)
# for Service in Services:
#     print(f"Service Name: {Service['name']}")
#     print(f"    Host: {Service['host']}")
#     print(f"    Description: {Service['description']}")
#     print(f"    Provider: {Service['provider']}")
#     print(f"    Port: {Service['port']}")
#     print(f"    Protocol: {Service['protocol']}")

# CONVERT TO JSON
def BluetoothToJSON(devices):
  devicesJSON = []
  for device in devices:
    devicesJSON.append({
      "name": device.name,
      "address": device.address
    })

  print(devicesJSON)
  devicesJSON = json.dumps(devicesJSON)
  print(devicesJSON)

  return devicesJSON

# CHANGE MAC ADDRESS FOR SOME BLUETOOTH DEVICES ** LINUX ONLY
def SpoofingMacAddress(Interface, NewMac):
  try:
    Output = subprocess.check_output(['hciconfig', Interface])
    if b'No such device' in Output:
      print(f"[!] Error: Interface '{Interface}' not found")
      return
    PartList = NewMac.split(':')
    FinalMacAddress = ['0x' + PartList[5], '0x' + PartList[4], '0x' + PartList[3], '0x' + PartList[2], '0x' + PartList[1], '0x' + PartList[0]]
    print(FinalMacAddress)
    subprocess.call(['sudo', 'hcitool', 'cmd', '0x3f', '0x001', FinalMacAddress[0], FinalMacAddress[1], FinalMacAddress[2], FinalMacAddress[3], FinalMacAddress[4], FinalMacAddress[5]])
    subprocess.call(['sudo', 'service', 'bluetooth', 'restart'])
    print(f"[+] Successfully changed {Interface} MAC address to {NewMac}")
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
def BluetoothCommunicateWithDevice(Socket):
  Data = ""
  while Data != "q":
    Data = input("[@] Enter message to send:")
    Socket.send(Data.encrypt())
    RecvData = Socket.recv(1024)
    print(f"[#] Recv data: {RecvData}")
    Socket.close()

# TargetAddress = input("[@] Enter target address: ")
# TargetPort = input("[@] Enter target port: ")
# TargetProtocol = input("[@] Enter target protocol: ")

# ChosenProtocol = bluetooth.RFCOMM
# if TargetProtocol == "L2CAP":
#     ChosenProtocol = bluetooth.L2CAP

# Socket = BluetoothForceConnectService(TargetAddress, TargetPort, ChosenProtocol)
# BluetoothCommunicateWithDevice(Socket)