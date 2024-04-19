import asyncio
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
async def BluetoothServiceScanner(BluetoothAddress):
  async with BleakClient(BluetoothAddress) as Client:
    return Client.services
# # How to use
# Address = input("[@] Enter bluetooth address: ")
# Services = asyncio.run(BluetoothServiceScanner(Address))
# # prints
# for Service in Services:
#     print(f"Service UUID: {Service.uuid}")
#     Characteristics = Service.characteristics
#     if Characteristics:
#         print("    Characteristics:")
#         for Characteristic in Characteristics:
#             Readable = "Read" in Characteristic.properties
#             Writable = "Write" in Characteristic.properties or "WriteWithoutResponse" in Characteristic.properties
#             print(f"        - UUID: {Characteristic.uuid}")
#             print(f"          Readable: {Readable}")
#             print(f"          Writable: {Writable}")

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