import requests
import sys
from tabulate import tabulate

URL = "http://jiofi.local.html/cgi-bin/qcmap_web_cgi"

def getDevices(log:bool = True):
    form = {'Page':'GetLANInfo'}
    res = requests.post(URL,form)
    if res.status_code == 404:
        print("Please connect to a Jiofi Network")
        sys.exit(1)
    data = res.json()
    no_devices = data['client_count']
    devices = data['entries']
    if log is False:
        return no_devices
    else:
        print(tabulate(devices,headers="keys"))

def getBandwidth(log:bool = True):
    form = {'Page':'GetSystemPerformance'}
    res = requests.post(URL,form)
    if res.status_code == 404:
        print("Please connect to a Jiofi Network")
        sys.exit(1)
    data = res.json()
    curr_up = data['uplink_cur_usg']
    curr_down = data['dwlink_cur_usg']
    print(f"Current Upload Speed:\t{curr_up} ↑\nCurrent Download Speed:\t {curr_down} ↓")

def deviceDetails(log:bool = True):
    form = {'Page':'GetDeviceDetails'}
    res = requests.post(URL,form)
    if res.status_code == 404:
        print("Please connect to a Jiofi Network")
        sys.exit(1)
    data = res.json()
    battery = data['battery_level']
    status = data['battery_status']
    phone = data['msisdn']
    if log is False:
        return battery,status
    else:
        print(f"Battery 🔋:\t {battery}%\nBattery Status:\t {status}\nJio Number:\t{phone}")

def getBasicdeets():
    bats = deviceDetails(False)
    devc = getDevices(False)
    print(f'Battery:\t{bats[0]}%\nBattery Stats:\t{bats[1]}\nNo of Users:\t{devc}')



if __name__ == '__main__':
    getBasicdeets()