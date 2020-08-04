"""
Jiofi-cli is a CLI for fetching data from your Jiofi network without going to Jiofi Web DashBoard.

:authors: Athul Cyriac Ajay <athul8720@gmail.com>
"""
import requests
import sys
import fire
import socket
from urllib3.exceptions import NewConnectionError,MaxRetryError
from rich import print, text
from rich.table import Table
from rich.console import Console

URL = "http://jiofi.local.html/cgi-bin/qcmap_web_cgi"


def getDevices(log:bool = True):
    """Prints a tabular view of all the connected devices in the network
    """
    form = {'Page':'GetLANInfo'}
    try:
        res = requests.post(URL,form)
    except requests.ConnectionError or NewConnectionError or MaxRetryError or socket.gaierror as err:
        print("Connect to a Jiofi Network to get the details")
        exit(1)
    data = res.json()
    no_devices = data['client_count']
    devices = data['entries']
    if log is False:
        return no_devices
    else:
        table = Table(title=f"Devices Connected: {no_devices}")
        table.add_column("Name", justify="center", style="cyan", no_wrap=True)
        table.add_column("IPV4", justify="center", style="green",  no_wrap=True)
        table.add_column("IPV6", justify="center", style="magenta",    no_wrap=True)
        table.add_column("MAC", justify="center", style="pale_green1", no_wrap=True)
        table.add_column("Time", justify="center", style="orange3",    no_wrap=True)
        table.add_column("Status", justify="center", style="purple",   no_wrap=True)
        for i,l in enumerate(devices):
            table.add_row(devices[i]['name'],devices[i]['ipv4'],devices[i]['ipv6'],devices[i]['mac'],devices[i]['time'],devices[i]['status'])
        console = Console()
        console.print(table)

def getBandwidth():
    """Prints the Current upload and download speed
    """
    form = {'Page':'GetSystemPerformance'}
    try:
        res = requests.post(URL,form)
    except requests.ConnectionError:
        print("Connect to a Jiofi Network to get the details")
        sys.exit(1)
    data = res.json()
    curr_up = data['uplink_cur_usg']
    curr_down = data['dwlink_cur_usg']
    print(f"Current Upload Speed:\t[bold magenta]{curr_up} ↑[/bold magenta]\nCurrent Download Speed:\t[bold cyan]{curr_down} ↓[/bold cyan]")


def getLteStats():
    form = {'Page':'GetLTEStatus'}
    try:
        res = requests.post(URL,form)
    except requests.ConnectionError:
        print("Connect to a Jiofi Network to get the details")
        sys.exit(1)
    data = res.json()
    return (data['connection_time'],data['signal_strength'])


def deviceDetails(log:bool = True):
    """Get Details of the device, Battery Charge, Battery State, Phone number or MSISDN
    """
    form = {'Page':'GetDeviceDetails'}
    try:
        res = requests.post(URL,form)
    except requests.ConnectionError:
        print("Connect to a Jiofi Network to get the details")
        sys.exit(1)
    data = res.json()
    battery = data['battery_level']
    status = data['battery_status']
    if status == "Discharging":
        battery_status = f"[bold red]{status}[/bold red]"
    else:
        battery_status = f"[green]{status}[/green]"
    phone = data['msisdn']
    if int(battery) >= 50:
        battery = f"[sea_green2]{battery}%[/sea_green2]"
    else:
        battery = f"[turquoise2]{battery}%[/turquoise2]"
    if log is False:
        return battery,battery_status
    else:
        print(f"Battery:zap: :\t {battery}\nBattery Status:\t {battery_status}\nJio Number:\t{phone}\nConnection\t[yellow1]{getLteStats()[1]}[/yellow1]")

def getWanInfo(log:bool = True):
    """Get Data usage in Upload and Download data in <time>
    """
    form = {'Page':'GetWANInfo'}
    try:
        res = requests.post(URL,form)
    except requests.ConnectionError:
        print("Connect to a Jiofi Network to get the details")
        sys.exit(1)
    data = res.json()
    data_upl = data['total_data_used_ulink']
    data_dwl = data['total_data_used_dlink']
    usage = data['total_data_used']
    total_data = f"[spring_green2]{float(usage)/1000000}[/spring_green2]"
    if log is False:
        return total_data
    else:
        print(f'Upload Data Usage:\t{data_upl}\nDownload Data Usage:\t{data_dwl}\nTotal Data Usage:\t{total_data} MB in [orange3]{getLteStats()[0]} Hours[/orange3]')

def getBasicDetails():
    """Get basic Details like Battery charge and state, no of connected devices and data used in <time>
    """
    bats = deviceDetails(False)
    devc = getDevices(False)
    usg = getWanInfo(False)
    time = getLteStats()
    print(f'Battery:\t{bats[0]}%\nBattery Status:\t{bats[1]}\nNo of Users:\t{devc}\nData usage\t{usg} MB in {time[0]} \nSignal Strength: [bold yellow]{time[1]}[/bold yellow]')

def main():
    fire.Fire({
      'devices': getDevices,
      'speed': getBandwidth,
      'basic':getBasicDetails,
      'usage':getWanInfo,
      'device':deviceDetails
  })
    # getBandwidth()
    # getBasicDetails()
    # getDevices()
    # getWanInfo()
    # deviceDetails()
if __name__ == '__main__':
    main()
