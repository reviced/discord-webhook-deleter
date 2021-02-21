import requests
import colorama
import asyncio
import time
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')



print(f"""

{b+Fore.GREEN}


██████╗ ███████╗██╗   ██╗██╗ ██████╗███████╗██████╗ 
██╔══██╗██╔════╝██║   ██║██║██╔════╝██╔════╝██╔══██╗
██████╔╝█████╗  ██║   ██║██║██║     █████╗  ██║  ██║
██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██║     ██╔══╝  ██║  ██║
██║  ██║███████╗ ╚████╔╝ ██║╚██████╗███████╗██████╔╝
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝╚═════╝ 

                                                             
{b+Fore.BLUE} > {Fore.RESET}Webhook deleter
{b+Fore.BLUE} > {Fore.RESET}Creator: isaiah#6969
""")

print(f"[{Fore.GREEN}>{Fore.RESET}] Webhook link ")
webhook = input("#root~reviced~ ")
delhook = requests.delete(webhook)
lmao = requests.get(webhook)
if lmao.status_code == 404:
  print(f"[{Fore.GREEN}>{Fore.RESET}] Webhook Deleted")

