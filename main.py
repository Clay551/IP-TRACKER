import time 
from colorama import Fore, init
import pyfiglet
import os
import colorama
import urllib.request
import json
banner = """

-----------------------------------|
                INFO               |
-----------------------------------|
"""
os.system('cls' if os.name == 'nt' else 'clear')
print(colorama.Fore.RED)
pyfiglet.print_figlet("Asylum")
print(colorama.Fore.GREEN)
print("             IP-TRACKER")
print(colorama.Fore.RESET)
while True:
    ip = input("Enter IP==>")
    print(colorama.Fore.CYAN+"Please Wait...")
    time.sleep(2.3)
    print(colorama.Fore.RESET)
    url = "http://ip-api.com/json/"
    response = urllib.request.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    print(banner)
    print(colorama.Fore.GREEN + "Status: " + values['status'])
    print(colorama.Fore.RESET)
    print('')
    print("IP: " + values['query'])
    print('')
    print("City: " + values['city'])
    print('')
    print("ZIP Code: " + values['zip'])
    print('')
    print("ISP: " + values['isp'])
    print('')
    print("Country: " + values['country'])
    print('')
    print("Region: " + values['region'])
    print('')
    print("Time Zone: " + values['timezone'])
    print('')
    print("CountryCode: " + values['countryCode'])
    print('')
    print("Org: " + values['org'])
    print('')
    print("As: " + values['as'])  
    break
