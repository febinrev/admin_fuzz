import sys
def febrev_fuzz():
	import requests
	print("""\033[1;36m
╔═╗╦═╗   ╔═╗┌┬┐┌┬┐┬┌┐┌    ╔═╗┬ ┬┌─┐┌─┐
╠╣ ╠╦╝───╠═╣ │││││││││    ╠╣ │ │┌─┘┌─┘
╚  ╩╚═   ╩ ╩─┴┘┴ ┴┴┘└┘────╚  └─┘└─┘└─┘ ---> coded by \033[0;39m FEBIN (https://github.com/febinrev)
	\033[1;38m""")
	feblist=open("febrev-fuzzlist.txt","r+")
	text=str(feblist.read())
	adminpages=list(text.split())
	feblist.close()
	url=input("\033[1;35mENTER THE URL TO FUZZ ADMIN PANEL :> \033[0;34m")
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
			print(f"\033[1;37mSERVER Type >> {server}")
			print("<----------------------------------------------------------------------------------->")
			print(" ")
		else:
			url=f"{url}/"
			server=requests.get(url).headers.get('Server')
			print(f"\033[1;37mSERVER Type >> {server}")
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
	
	print("\033[1;37m FEBREV-Admin_Fuzz Execution Completed. \033[1;33m!HAPPY HACKING! \033[1;34m \n")
try:
 febrev_fuzz()
except KeyboardInterrupt:
	print("\033[1;34m")
	print("\033[1;31m USER INTERRUPTION DETECTED.....EXITING")
	print("  ")
	print("\033[1;39m THANKS FOR USING FEBREV-ADMIN_FUZZ....You can give me a credit by providing a STAR in Github >> \033[4;34m \033[5;34m https://github.com/febinrev/febrev-admin_fuzz")
	sys.exit(0)
