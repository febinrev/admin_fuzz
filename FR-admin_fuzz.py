#!/usr/bin/python3
import sys
print("""\033[1;36m
╔═╗╦═╗   ╔═╗┌┬┐┌┬┐┬┌┐┌    ╔═╗┬ ┬┌─┐┌─┐
╠╣ ╠╦╝───╠═╣ │││││││││    ╠╣ │ │┌─┘┌─┘
╚  ╩╚═   ╩ ╩─┴┘┴ ┴┴┘└┘────╚  └─┘└─┘└─┘ ---> coded by \033[0;39m FEBIN (https://github.com/febinrev) \033[1;38m """)
def febrev_fuzz():
	import requests
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
			reqresp=requests.get(f"{url}/{dirs[i]}",timeout=10)
			if reqresp.status_code == 200:
				print(f"\033[1;39m FOUND DIRECTORY ==> {url}{dirs[i]}/ \033[1;34m")
			elif reqresp.status_code == 302:
				print("\033[1;39m May be moved  ==> {url}{dirs[i]}/ \033[1;34m")
			elif reqresp.status_code == 403:
				print(f"\033[1;39m FOUND FORBIDDEN DIRECTORY ==> {url}{dirs[i]}/ \033[1;34m")
					
			else:
				pass 

	except requests.exceptions.ConnectionError:
		print("Connection to the Server Failed, May be invalid URL or bad Internet connection. Check Your Internet connection,URL and try again\n ")
	except requests.exceptions.ReadTimeout:
		print("\033[1;31m Error : EXECUTION STOPPED DUE TO !TIMED OUT! ERROR, YOUR INTERNET MAY BE DISCONNECTED!!!....EXITTED")
	
	print("\033[1;37m FEBREV-Admin_Fuzz Execution Completed. \033[1;33m!HAPPY HACKING! \033[1;34m \n")


try:
	print("""
 [1]> Find the Admin panel(Admin_panel_fuzzer)

 [2]> DIRECTORY Bruteforce  

	""")
	try:
		choice=int(input("febrev-admin_fuzz(ENTER YOUR CHOICE) :>> "))
		print("")
		if choice == 1:
			febrev_fuzz()
		elif choice == 2:
			febrev_dirfuzz()
		else:
			print("\n \033[1;31m Error : YOUR CHOICE IS INVALID!!.....Exiting!\n")
	except ValueError:
		print("\n \033[1;31m Error :YOU ENTERED AN INVALID CHOICE INPUT,,,PLEASE ENTER 1 or 2....Please Rerun the tool with correct input.\n")
		print("\033[1;39m THANKS FOR USING FEBREV-ADMIN_FUZZ....You can give me a credit by providing a STAR in Github >> \033[4;34m \033[5;34m https://github.com/febinrev/febrev-admin_fuzz")
except KeyboardInterrupt:
	print("\033[1;34m")
	print("\033[1;31m USER INTERRUPTION DETECTED.....EXITING")
	print("  ")
	print("\033[1;39m THANKS FOR USING FEBREV-ADMIN_FUZZ....You can give me a credit by providing a STAR in Github >> \033[4;34m \033[5;34m https://github.com/febinrev/febrev-admin_fuzz")
	sys.exit(0)
