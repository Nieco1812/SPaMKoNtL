# SpamKtL

import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
                     
          def loginSC():
	os.system('clear')
	print"\033[1;97mSilahkan login SC nya dulu bosque\n"
	username = raw_input("\033[1;96m[*] \033[1;97mUsername \033[1;91m: \033[1;92m")
	password = raw_input("\033[1;96m[*] \033[1;97mPassword \033[1;91m: \033[1;92m")
	if username =="D34TOR" and password =="Ganteng":
		print"\033[1;96m[✓] \033[1;92mLogin success"
		time.sleep(1)
		login()
	else:
		print"\033[1;96m[!] \033[1;91mSalah!!"
		time.sleep(1)
                LoginSC()
           

		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;       S P A M  S M S      ;
		;---------------------------;
		;       Author : D34TOR     ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
NOTE: This tool's only work for Indonesia number phone.
1. SMS Gratis
2. OTP Matahari
3. OTP Hallodok
4. OTP Olx.co.id
5. OTP Sociolla.com
""")
		pilih=int(input('D34TOR/> '))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.matahari
		elif pilih == 3:
			import src.alodok
		elif pilih == 4:
			import src.olx
		elif pilih == 5:
			import src.socil
		else: print("[!] TENGOK MENU NYA KONTOL(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
