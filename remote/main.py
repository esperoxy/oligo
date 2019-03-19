import os
import subprocess
import time
import requests as r
import random
import json

ovpnFile = "remote.ovpn"
serverPvtIp = "10.8.0.1"
serverPvtPort = "8443"

vehicle_Number = 12345


def sendData(ip, port, data):
    tt = r.post(url = "http://"+ip+":"+port+"/handlers/vehicle_update", data = data) 
    #print(tt.text)
    return None


def getData():
    # Random Sensor Data for now
    w1 = random.randint(1,400)
    w2 = random.randint(1,400)
    w3 = random.randint(1,400)
    w4 = random.randint(1,400)
    w6 = random.randint(1,400)
    w7 = random.randint(1,400)
    data = { "data":json.dumps({'_id':str(vehicle_Number), 'milage':20, 'fuel':w7, 'total_distance':w6, 'vnum':12345, 'total_tires':4, 'tires':{'1':w1, '2':w2, '3':w3, '4':w4}})}
    return data

def doPing(ip):
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        return True 
    return False


def openVPN_Tunnel(file):
    os.system("nohup openvpn " + file+" &")
    while True:
        if doPing(serverPvtIp):
            break
        time.sleep(1)
    print("\nOpenVPN Tunnel Connection Established, Connected to Cloud servers...")
    return None


def initialCall():
    return None


if __name__ == '__main__':
    print("\nArlton Remote Base Station Initializing...")
    openVPN_Tunnel(ovpnFile)
    while True:
        data = getData()
        sendData(serverPvtIp, serverPvtPort, data)
        time.sleep(1)
