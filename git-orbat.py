#!/usr/bin/env python3

import requests
import re
import colorama
from colorama import Fore, Back, Style, init
import pyfiglet

banner = pyfiglet.figlet_format("Git Orbat") #banner
print(banner)
print(" ")
init()

username=input(Fore.RED+"Send me the target username: "+Style.RESET_ALL)
repo=input(Fore.RED+"Do you have a repo name?: "+Style.RESET_ALL)

requestFollowers=requests.get("https://api.github.com/users/{0}/followers".format(str(username)))
findLogin = re.findall(r"\"login\":\"(.*?)\"", requestFollowers.text)
followers=[]
print(" ")
followers.append(findLogin)
print(" ")
print(Fore.RED+"<+> -- Followers: -- <+> "+Style.RESET_ALL)
y=0
for x in findLogin:
	print(Fore.GREEN+"- "+findLogin[y]+Style.RESET_ALL)
	y=y+1

requestFollowing=requests.get("https://api.github.com/users/{0}/following".format(str(username)))
findLogin_f = re.findall(r"\"login\":\"(.*?)\"", requestFollowing.text)
following=[]
following.append(findLogin_f)
print(" ")
print(Fore.RED+"<+> -- Following: -- <+> "+Style.RESET_ALL)
y=0
for x in findLogin_f:
	print(Fore.GREEN+"- "+findLogin_f[y]+Style.RESET_ALL)
	y=y+1

requestGit=requests.get("https://api.github.com/users/{0}/events/public".format(str(username)))	
findEmailField = re.findall(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)", requestGit.text)
findRepo = re.findall(r"\"html_url\":\"(.*?)\"", requestGit.text)
reponame=[]
reponame.append(findRepo)

requestComits=requests.get(f"https://api.github.com/repos/{username}/{repo}/commits")
findEmailField_2 = re.findall(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)", requestComits.text)

# Deleting repeated emails
findEmailField = list(dict.fromkeys(findEmailField))
findEmailField_2 = list(dict.fromkeys(findEmailField_2))

print(Fore.RED+"-- <+> EMAILS FOUND <x>---"+Style.RESET_ALL)
print(" ")
y = 0
for findEmail in findEmailField:
	print("<-> "+Fore.GREEN+str(findEmailField[y])+Style.RESET_ALL)
	y=y+1
y = 0
for findE in findEmailField_2:
	print("<-> "+Fore.GREEN+str(findEmailField_2[y])+Style.RESET_ALL)
	y=y+1
print("---------------------------------------------------")


