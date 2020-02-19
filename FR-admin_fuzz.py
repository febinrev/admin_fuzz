import sys
def febrev_fuzz():
	from urllib.request import urlopen
	import urllib as ulib
	print("""\033[1;36m
╔═╗╦═╗   ╔═╗┌┬┐┌┬┐┬┌┐┌    ╔═╗┬ ┬┌─┐┌─┐
╠╣ ╠╦╝───╠═╣ │││││││││    ╠╣ │ │┌─┘┌─┘
╚  ╩╚═   ╩ ╩─┴┘┴ ┴┴┘└┘────╚  └─┘└─┘└─┘ ---> coded by \033[0;39m FEBIN (https://github.com/febinrev)
	\033[1;38m""")
	feblist=open("febrev-fuzz.txt","r+")
	text=str(feblist.read())
	adminpages=list(text.split())
	url=input("\033[1;35mENTER THE URL TO FUZZ ADMIN PANEL :> \033[0;34m")
	print(f"""\033[1;33m
STARTED CRAWLING TO FIND ADMIN PANEL OF URL : \033[1;34m{url}
	""")
	if url.startswith("https://") or url.startswith("http://"):
		url=url
	else:
		print("Error : INVALID URL ! URL must start with 'http://' or 'https://'")
		exit()
	
	if url.endswith("/"):
		url=url
	else:
		url=f"{url}/"
	for i in range(len(adminpages)):
		try:
			urlopen(f"{url}/{adminpages[i]}")
			print(f"\033[1;39m FOUND  ==> {url}{adminpages[i]} \033[1;34m")
		except ulib.error.HTTPError:
			pass
	
	print("\033[1;37m ADMIN PANEL FOUND IS IN THE ABOVE.....IF NONE, BETTER LUCK NEXT TIME \033[1;34m")
try:
 febrev_fuzz()
except KeyboardInterrupt:
	print("\033[1;34m")
	print("\033[1;31m USER INTERRUPTION DETECTED.....EXITING")
	print("  ")
	print("\033[1;39m THANKS FOR USING FEBREV-ADMIN_FUZZ....You can give me a credit by providing a STAR in Github >> \033[4;34m \033[5;34m https://github.com/febinrev/febrev-admin_fuzz")
