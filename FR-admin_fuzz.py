#!/usr/bin/python3
import sys
import os
os.system("clear")
print("""\033[1;36m
╔═╗╦═╗   ╔═╗┌┬┐┌┬┐┬┌┐┌    ╔═╗┬ ┬┌─┐┌─┐
╠╣ ╠╦╝───╠═╣ │││││││││    ╠╣ │ │┌─┘┌─┘
╚  ╩╚═   ╩ ╩─┴┘┴ ┴┴┘└┘────╚  └─┘└─┘└─┘ ---> coded by \033[0;39m FEBIN (https://github.com/febinrev) \033[1;38m """)
def febrev_fuzz():
	import requests
	os.system("clear")
	feblist=open("febrev-fuzzlist.txt","r+")
	text=str(feblist.read())
	adminpages=list(text.split())
	feblist.close()
	url=input("\n \033[1;35mENTER THE URL TO FUZZ ADMIN PANEL :> \033[0;34m")
	print(f"""\033[1;33m
STARTED CRAWLING TO FIND ADMIN PANEL OF URL : \033[1;34m{url}
	""")
	try:
		if url.startswith("https://") or url.startswith("http://"):
			url=url
		else:
			print("Error : INVALID URL ! URL must start with 'http://' or 'https://'")
			exit()
		
		if url.endswith("/"):
			url=url
			server=requests.get(url).headers.get('Server')
			print(f"\033[1;37m SERVER Type >> {server}")
			print("\n<----------------------------------------------------------------------------------->")
			print(" ")
		else:
			url=f"{url}/"
			server=requests.get(url).headers.get('Server')
			print(f"\033[1;37mSERVER Type >> {server}")
			print("\n<----------------------------------------------------------------------------------->")
			print(" ")
		for i in range(len(adminpages)):
			reqresp=requests.get(f"{url}/{adminpages[i]}",timeout=10)
			if reqresp.status_code == 200:
				print(f"\033[1;39m FOUND  ==> {url}{adminpages[i]} \033[1;34m")
			elif reqresp.status_code == 302:
				print("\033[1;39m May be moved  ==> {url}{adminpages[i]} \033[1;34m")
			elif reqresp.status_code == 403:
				print(f"\033[1;39m FOUND FORBIDDEN PAGE ==> {url}{adminpages[i]} \033[1;34m")
					
			else:
				pass
	except requests.exceptions.ConnectionError:
		print("Connection to the Server Failed, May be invalid URL or bad Internet connection. Check Your Internet connection,URL and try again\n ")
	except requests.exceptions.ReadTimeout:
		print("\033[1;31m Error : EXECUTION STOPPED DUE TO !TIMED OUT! ERROR, YOUR INTERNET MAY BE DISCONNECTED!!!....EXITTED")
	
	print("\033[1;37m FEBREV-Admin_Fuzz Execution Completed. \033[1;33m!HAPPY HACKING! \033[1;34m \n")

def febrev_dirfuzz():
	import requests
	os.system("clear")
	feblist=open("dirfuzz.txt","r+")
	text=str(feblist.read())
	dirs=list(text.split())
	feblist.close()
	url=input("\n \033[1;35mENTER THE URL TO FUZZ/BRUTE :> \033[0;34m")
	print(f"""\033[1;33m
STARTED CRAWLING TO FIND DIRECTORIES THE URL : \033[1;34m{url}
	""")
	try:
		if url.startswith("https://") or url.startswith("http://"):
			url=url
		else:
			print("Error : INVALID URL ! URL must start with 'http://' or 'https://'")
			exit()
		
		if url.endswith("/"):
			url=url
			server=requests.get(url).headers.get('Server')
			print(f"\033[1;37m SERVER Type >> {server}")
			print("\n<----------------------------------------------------------------------------------->")
			print(" ")
		else:
			url=f"{url}/"
			server=requests.get(url).headers.get('Server')
			print(f"\033[1;37mSERVER Type >> {server}")
			print("\n<----------------------------------------------------------------------------------->")
			print(" ")
		for i in range(len(dirs)):
			reqresp=requests.get(f"{url}/{dirs[i]}/",timeout=10)
			reqrespage=requests.get(f"{url}/{dirs[i]}",timeout=10)
			if reqresp.status_code == 200:
				print(f"\033[1;39m FOUND DIRECTORY ==> {url}{dirs[i]}/ \033[1;34m")
			elif reqresp.status_code == 302:
				print("\033[1;39m May be moved  ==> {url}{dirs[i]}/ \033[1;34m")
			elif reqresp.status_code == 403:
				print(f"\033[1;39m FOUND FORBIDDEN DIRECTORY ==> {url}{dirs[i]}/ \033[1;34m")
					
			else:
				pass 
			if reqrespage.status_code == 200 and reqresp.status_code == 404:
				print(f"\033[1;39m FOUND Page ==> {url}{dirs[i]} \033[1;34m")
			else:
				pass

	except requests.exceptions.ConnectionError:
		print("Connection to the Server Failed, May be invalid URL or bad Internet connection. Check Your Internet connection,URL and try again\n ")
	except requests.exceptions.ReadTimeout:
		print("\033[1;31m Error : EXECUTION STOPPED DUE TO !TIMED OUT! ERROR, YOUR INTERNET MAY BE DISCONNECTED!!!....EXITTED")
	
	print("\033[1;37m FEBREV-Admin_Fuzz Execution Completed. \033[1;33m!HAPPY HACKING! \033[1;34m \n")
def wordlistgen():
	import requests
	from bs4 import BeautifulSoup
	url=input("\033[1;34mENTER THE WEBSITE or WEBPAGE URL TO CREATE A WORDLIST :> ")
	print("")
	filepath=input("\033[1;33mEnter the path/name of the output file to be written :> ")
	try:
		webpage=requests.get(url)
		pagedata=webpage.text
		soup=BeautifulSoup(pagedata,"html.parser")
	except requests.exceptions.ConnectionError:
		print("\033[1;31mSOME ERRORS ARE FACED WHILE CONNECTING THE SERVER...")
	for script in soup(["script","style"]):
		script.extract()
	text1=soup.get_text()
	text=str(text1.strip())
	feb=text.split()
	iscount=feb.count('is')
	wascount=feb.count('was')
	arecount=feb.count('are')
	forcount=feb.count('for')
	thecount=feb.count('the')
	ofcount=feb.count('of')
	tocount=feb.count('to')
	try:
		isinit=0
		while isinit<=iscount:
			feb.remove('is')
			isinit=isinit+1
		wasinit=0
		while wasinit<=wascount:
			feb.remove('was')
			wasinit=wasinit+1
		areinit=0
		while areinit<=arecount:
			feb.remove('are')
			areinit=areinit+1
		forinit=0
		while forinit<=forcount:
			feb.remove('for')
			forinit=forinit+1
		theinit=0
		while theinit<=thecount:
			feb.remove('the')
			theinit=theinit+1
		ofinit=0
		while ofinit<=ofcount:
			feb.remove('of')
			ofinit=ofinit+1
		toinit=0
		while toinit<=tocount:
			feb.remove('to')
			toinit=toinit+1
	except ValueError:
		pass
	feb.sort()
	for string in feb:
		count=feb.count(string)
		strinit=0
		while strinit < count:
			feb.remove(string)
			strinit=strinit+1
	feb.sort()
	for i in range(len(feb)):
		try:
			file=open(filepath,"a+")
			file.write("\n"+feb[i])
			file.close()
		except FileNotFoundError:
			homedir=os.environ.get('HOME')
			file=open(f"{homedir}/fr-wordlist.txt","a+")
			file.write("\n"+feb[i])
			file.close()
	if os.path.isfile(filepath):
		print("")
		print(f"\033[1;35mWordlist {filepath} successfully witten")
	else:
		print("\033[1;31mSorry:Path not Found!! The Path You Specified Doesn't Exist")
		print("So Saved the wordlist as fr-wordlist.txt in the HOME Directory of the current User.....")
	print("\033[1;37m FEBREV-Admin_Fuzz Execution Completed. \033[1;33m!HAPPY HACKING! \033[1;34m \n")



def word_analyze():
	import requests
	from bs4 import BeautifulSoup
	url=input("\033[1;34mENTER THE WEBSITE or WEBPAGE TO ANALYZE :> ")
	print("")
	try:
		webpage=requests.get(url)
		pagedata=webpage.text
		soup=BeautifulSoup(pagedata,"html.parser")
	except requests.exceptions.ConnectionError:
		print("\033[1;31mSOME ERRORS ARE FACED WHILE CONNECTING THE SERVER...")
	for script in soup(["script","style"]):
		script.extract()
	text1=soup.get_text()
	text=str(text1.strip())
	feb=text.split()
	iscount=feb.count('is')
	wascount=feb.count('was')
	arecount=feb.count('are')
	forcount=feb.count('for')
	thecount=feb.count('the')
	ofcount=feb.count('of')
	tocount=feb.count('to')
	try:
		isinit=0
		while isinit<=iscount:
			feb.remove('is')
			isinit=isinit+1
		wasinit=0
		while wasinit<=wascount:
			feb.remove('was')
			wasinit=wasinit+1
		areinit=0
		while areinit<=arecount:
			feb.remove('are')
			areinit=areinit+1
		forinit=0
		while forinit<=forcount:
			feb.remove('for')
			forinit=forinit+1
		theinit=0
		while theinit<=thecount:
			feb.remove('the')
			theinit=theinit+1
		ofinit=0
		while ofinit<=ofcount:
			feb.remove('of')
			ofinit=ofinit+1
		toinit=0
		while toinit<=tocount:
			feb.remove('to')
			toinit=toinit+1
	except ValueError:
		pass
	feb.sort()
	print("\033[1;32m-"*74)
	print("\033[1;32m|           Words    |     count/frequency    |        Graph              |  ")
	print("\033[1;32m-"*74)
	for string in feb:
		count=feb.count(string)
		for i in range(count):
			feb.remove(string)
		print(f"\033[1;34m| {string + ' ' * (22 - len(string)) + '| '}{str(count) +' ' * (22 - len(str(count)))}|    \033[1;32m{'█' * count}  " )
		print("\033[1;33m-"*74)






try:
	print("""\033[1;37m
 [1]> Find the Admin panel(Admin_panel_fuzzer)

 \033[1;32m[2]> DIRECTORY Bruteforce  

 \033[1;33m[3]> Create WORDLIST from a WEBSITE/WEBPAGE

 \033[1;32m[4]> Website's Words frequency analysis

	""")
	try:
		choice=int(input("\033[1;39mfebrev-admin_fuzz(ENTER YOUR CHOICE) :>> "))
		print("")
		if choice == 1:
			febrev_fuzz()
		elif choice == 2:
			febrev_dirfuzz()
		elif choice == 3:
			wordlistgen()
		elif choice == 4:
			word_analyze()
		else:
			print("\n \033[1;31m Error : YOUR CHOICE IS INVALID!!.....Exiting!\n")
	except ValueError:  #ValueError
		print("\n \033[1;31m Error :YOU ENTERED AN INVALID CHOICE INPUT,,,PLEASE ENTER 1 or 2....Please Rerun the tool with correct input.\n")
		print("\033[1;39m THANKS FOR USING FEBREV-ADMIN_FUZZ....You can give me a credit by providing a STAR in Github >> \033[4;34m \033[5;34m https://github.com/febinrev/febrev-admin_fuzz")
except KeyboardInterrupt:
	print("\033[1;34m")
	print("\033[1;31m USER INTERRUPTION DETECTED.....EXITING")
	print("  ")
	print("\033[1;39m THANKS FOR USING FEBREV-ADMIN_FUZZ....You can give me a credit by providing a STAR in Github >> \033[4;34m \033[5;34m https://github.com/febinrev/febrev-admin_fuzz")
	sys.exit(0)
except UnboundLocalError:
	print("Error : Due to Connection error , webpage data can't be retrieved.......")
	print("\033[1;39m THANKS FOR USING FEBREV-ADMIN_FUZZ....You can give me a credit by providing a STAR in Github >> \033[4;34m \033[5;34m https://github.com/febinrev/febrev-admin_fuzz")
	sys.exit(0)

