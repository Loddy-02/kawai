#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('rich is not installed yet')
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich import pretty
from rich.text import Text as tekz
os.system("clear")

def banner():
	ban='''
•   ███████ ████████ ██    ██ ██      ███████   •
•   ██         ██     ██  ██  ██      ██        •
•   ███████    ██      ████   ██      █████     •
•        ██    ██       ██    ██      ██        •
•   ███████    ██       ██    ███████ ███████   •

•   GITHUB : https://github.com/Loddy-02/nero   •
'''
	oi = nel(tekz(ban,justify='center',style='bold'),style='yellow')
	cetak(nel(oi,title='',style='bold white'))

banner()
