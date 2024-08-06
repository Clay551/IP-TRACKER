import time
import os
import colorama
import urllib.request
import json
from colorama import Fore, init
import pyfiglet

colorama.init()

banner = """
-----------------------------------|
                INFO               |
-----------------------------------|
"""

os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.RED)
pyfiglet.print_figlet("Asylum")
print(Fore.GREEN)
print("             IP-TRACKER")
print(Fore.RESET)

while True:
    ip = input("Enter IP ==> ")
    print(Fore.CYAN + "Please Wait...")
    time.sleep(2.3)
    print(Fore.RESET)

    url = "http://ip-api.com/json/"
    response = urllib.request.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print(banner)
    print(Fore.GREEN + f"Status: {values['status']}")
    print(Fore.RESET)
    print('')

    print(f"IP: {values['query']}")
    print('')
    print(f"City: {values['city']}")
    print('')
    print(f"ZIP Code: {values['zip']}")
    print('')
    print(f"ISP: {values['isp']}")
    print('')
    print(f"Country: {values['country']}")
    print('')
    print(f"Region: {values['region']}")
    print('')
    print(f"Time Zone: {values['timezone']}")
    print('')
    print(f"CountryCode: {values['countryCode']}")
    print('')
    print(f"Org: {values['org']}")
    print('')
    print(f"As: {values['as']}")
    break
