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

def getBandwidth():
    form = {'Page':'GetSystemPerformance'}
    res = requests.post(URL,form)
    if res.status_code == 404:
        print("Please connect to a Jiofi Network")
        sys.exit(1)
    data = res.json()
    curr_up = data['uplink_cur_usg']
    curr_down = data['dwlink_cur_usg']
    print(f"Current Upload Speed:\t{curr_up} ↑\nCurrent Download Speed:\t {curr_down} ↓")
def getLteStats():
    form = {'Page':'GetLTEStatus'}
    res = requests.post(URL,form)
    if res.status_code == 404:
        print("Please connect to a Jiofi Network")
        sys.exit(1)
    data = res.json()
    return (data['connection_time'])

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

def getWanInfo(log:bool = True):
    form = {'Page':'GetWANInfo'}
    res = requests.post(URL,form)
    if res.status_code == 404:
        print("Please connect to a Jiofi Network")
        sys.exit(1)
    data = res.json()
    data_upl = data['total_data_used_ulink']
    data_dwl = data['total_data_used_dlink']
    if 'KB' in data_upl:
        data_upl_mb = float(data_upl[:-3])/1000
    if 'KB' in data_dwl:
        data_dwl_mb =  float(data_upl[:-3])/1000
    try:
        total_data = data_upl_mb + data_dwl_mb
    except NameError:
        total_data = float(data_dwl[:-3])+float(data_upl[:-3])
    if log is False:
        return total_data
    else:
        print(f'Upload Data Usage:\t{data_upl}\nDownload Data Usage:\t{data_dwl}\nTotal Data Usage:\t{total_data} MB')
    
def getBasicDetails():
    bats = deviceDetails(False)
    devc = getDevices(False)
    usg = getWanInfo(False)
    time = getLteStats()
    print(f'Battery:\t{bats[0]}%\nBattery Status:\t{bats[1]}\nNo of Users:\t{devc}\nData usage\t{usg} MB in {time}')

def getusage():
    form = {'Page':'GetLTEStatus'}
    res = requests.post(url,form)
    data = res.json()
    up_time = data['connection_time']



if __name__ == '__main__':
    getBasicDetails()