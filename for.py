#KACANG
import requests as req
import os, json, hashlib, sys
from bs4 import BeautifulSoup as bs
import requests.packages.urllib3
import time
requests.packages.urllib3.disable_warnings()

grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[41;39m'
bold = '\033[1m'
normal = '\033[0m'
off = '\x1b[m'

bn = f"""
  {blue}o888o                    o888    {flag}Sakarep{off}                 
{purple}o888oo ooooooo  oo oooooo   888   ooooooo  ooooooooo   
 {cyan}888 888     888 888    888 888   ooooo888  888    888 
 {white}888 888     888 888        888 888    888  888    888 
{white}o888o  88ooo88  o888o      o888o 88ooo88 8o 888ooo88   
                                           {off}o888       
                                           """

'''
 
 DO NOT RESELL FOR RESPECT
 MAKING THIS TOOL IS VERY DIFFICULT
 
'''

def main():
	os.system('clear')
	a = "1"
	b = "1"
	print(f"{red}Harap login dulu!!{off}\n")
	cok = input(f"{flag}>{off} Masukan username > ")
	if cok == b:
		cus = input(f"{flag}>{off} Masukan password > ")
		if cus == a:
			print(f"{green}Akses diterima.{off}")
			time.sleep(1)
			asu()
		else:
			print(f"{red}Sandi salah{off}")
			time.sleep(1)
			main()
	else:
		print(f"{red}Username salah!{off}")
		time.sleep(1)
		main()
		
yxc = []
def asu():
	os.system('clear')
	print(bn)
	print(f"{purple}[{yellow}1{purple}]{off}nim:xxx\n{purple}[{yellow}2{purple}]{off}binus pilih ini(i)\n{purple}[{yellow}3{purple}]{off}nim:nim\n{purple}[{yellow}4{purple}]{off}nama:nama uns\n{purple}[{yellow}5{purple}]{off}nim:Nama (upi)(i+i)\n{purple}[{yellow}6{purple}]{off}ipb\n{purple}[{yellow}7{purple}]{off}nama:Nama(i)\n{purple}[{yellow}8{purple}]{off}Email:nim{yellow}[{cyan}nim@xx:nim{yellow}]{off}\n")
	_0 = input(f"{green}[{red}?{green}]{white}Pilih > ")
	_1 = cut(input(f"\n{red}[{yellow}!{red}]{off}Ambil link dari tahun Smester\n\n{off}[{green}+{off}]{green}Input Link {off}> "))
	print(f"{yellow}NEW!!!{off}")
	cok = input("ekor 1 : ")
	_2 = input(f"{off}[{green}+{off}]{green}Nama Output (nama + .txt) {off}> ")
	_3 = stat(_1)
	if _0 == '1':
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].title()+'111\n')
					o_.write(__+':'+x[0].title()+'1111\n')
					o_.write(__+':'+x[0].title()+'11111\n')
					o_.write(__+':'+x[0].title()+'1212\n')
					o_.write(__+':'+x[0].title()+'21\n')
					o_.write(__+':'+x[0].title()+'321\n')
					o_.write(__+':'+x[0].title()+'4321\n')
					o_.write(__+':'+x[0].title()+'54321\n')
					o_.write(__+':'+x[0].title()+'23\n')
					o_.write(__+':'+x[0].title()+'234\n')
					o_.write(__+':'+x[0].title()+'2345\n')
					o_.write(__+':'+x[0].title()+'34\n')
					o_.write(__+':'+x[0].title()+'32\n')
					o_.write(__+':'+x[0].title()+'3232\n')
					o_.write(__+':'+x[0].title()+'345\n')
					o_.write(__+':'+x[0].title()+'4545\n')
					o_.write(__+':'+x[0].title()+'45\n')
					o_.write(__+':'+x[0].title()+'55\n')
					o_.write(__+':'+x[0].title()+'00\n')
					o_.write(__+':'+x[0].title()+'000\n')
					o_.write(__+':'+x[0].title()+'0101\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == '2':
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1995\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1996\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1997\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1998\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1999\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'2000\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'2001\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'2002\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'2020\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'2019\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'11\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'12\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'2021\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1945\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'123\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'1234\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'12345\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'321\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'4321\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'54321\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'00\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'22\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'33\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'44\n')
			except:
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+':'+x[0].title()+'25\n')
		done(_2)
	elif _0 == '3':
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	if _0 == '4':
		print()
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+':'+x[0].lower()+'12\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'123\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'1234\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'12345\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'321\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'21\n')
					o_.write(x[0].lower()+':'+x[1].lower()+'12\n')
					o_.write(x[0].lower()+':'+x[1].lower()+'123\n')
					o_.write(x[0].lower()+':'+x[1].lower()+'1234\n')
					o_.write(x[0].lower()+':'+x[1].lower()+'12345\n')
					o_.write(x[0].lower()+':'+x[1].lower()+'321\n')
					o_.write(x[0].lower()+':'+x[1].lower()+'21\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].lower()+'1\n')
		done(_2)
	if _0 == '5':
		print()
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+'@'+x[0].title()+'123\n')
					o_.write(__+':'+'@'+x[0].title()+'1234\n')
					o_.write(__+':'+'@'+x[0].title()+'12345\n')
					o_.write(__+':'+'@'+x[0].title()+'1999\n')
					o_.write(__+':'+'@'+x[0].title()+'2000\n')
					o_.write(__+':'+'@'+x[0].title()+'2001\n')
					o_.write(__+':'+x[0].title()+'_'+'123\n')
					o_.write(__+':'+x[0].title()+'_'+'1234\n')
					o_.write(__+':'+x[0].title()+'_'+'12345\n')
					o_.write(__+':'+x[0].title()+'_'+'1999\n')
					o_.write(__+':'+x[0].title()+'_'+'2000\n')
					o_.write(__+':'+x[0].title()+'_'+'2001\n')
					o_.write(__+':'+x[0].title()+'123\n')
					o_.write(__+':'+x[0].title()+'1234\n')
					o_.write(__+':'+x[0].title()+'12345\n')
					o_.write(__+':'+x[0].title()+'1999\n')
					o_.write(__+':'+x[0].title()+'2000\n')
					o_.write(__+':'+x[0].title()+'2001\n')
					o_.write(__+':'+x[0].lower()+'123\n')
					o_.write(__+':'+x[0].lower()+'1234\n')
					o_.write(__+':'+x[0].lower()+'12345\n')
					o_.write(__+':'+x[0].lower()+'1999\n')
					o_.write(__+':'+x[0].lower()+'2000\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == '6':
		print()
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+':'+__+'\n')
					o_.write(x[0].lower()+':'+x[0].title()+'123\n')
					o_.write(x[0].lower()+'_'+x[1].lower()+':'+__+'\n')
					o_.write(x[0].lower()+'_'+x[1].lower()+':'+x[0].title()+'123\n')
					o_.write(x[0].lower()+x[1].lower()+x[2].lower()+':'+x[0].title()+'123\n')
					o_.write(x[0].lower()+x[1].lower()+x[2].lower()+':'+__+'\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+'123\n')
			except:
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+'_'+__+':'+x[0].title()+'\n')
		done(_2)
	elif _0 == '7':
		print()
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+'.'+x[1].lower()+'.'+x[2].lower()+':'+x[0].title()+cok+'\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+'.'+x[2].lower()+':'+x[1].title()+cok+'\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+':'+x[0].title()+cok+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+':'+x[0].title()+cok+'\n')
		done(_2)
	elif _0 == '8':
		mail = input(f"{off}[{red}!{off}]{off}Tulis jenis mail {red}contoh : {yellow}[{off}student.uny{yellow}]{off}\n{green}[{cyan}+{green}]{off}Masukan disini : ")
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}[{green}{_+1}{cyan}]{blue}Harap menunggu sayang. . . . {off}:v")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+'.'+x[1].lower()+'@'+mail+'.'+'ac.id'+':'+__+'\n')
					o_.write(x[0].lower()+'@'+mail+'.'+'ac.id'+':'+__+'\n')
					o_.write(__+'@'+mail+'.'+'ac.id'+__+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == '9':
		print()
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+'.'+x[1].lower()+'10'+':'+x[0].title()+cok+'\n')
					o_.write(x[0].lower()+'.'+x[1].lower()+'123'+':'+x[1].title()+cok+'\n')
					o_.write(x[0].lower()+'10'+':'+x[0].title()+cok+'\n')
					o_.write(x[0].lower()+'123'+':'+x[0].title()+cok+'\n')
			except:
				with open(_2,'a') as o_:
					o_.write(x[0].lower()+'1'+':'+x[0].title()+cok+'\n')
		done(_2)
	else:
		exit()

def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		yxc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _

def done(_2):
	print(f"\n{green}[{purple}✓{green}]{cyan}{len(yxc)} {off}Hasil tersimpan di{green} '{_2}'{off}")

if __name__=='__main__':
	main()