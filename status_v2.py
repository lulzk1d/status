# -*- coding: utf-8 -*-
# :D
import sys,os,random
if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
elif sys.platform == "darwin":
    os.system("clear")
else:
    print("Unknown System Detected")
try: 
 import cfscrape
except:
 print("===================================")
 print("[-] pip install cfscrape")
 print("    [+] You need install: cfscrape")
 print("===================================") 
 sys.exit()
try:
 import requests
except:
 print("===================================")
 print("[-] pip install requests")
 print("    [+] You need install: requests")
 print("===================================") 
 sys.exit() 
print """
                   .-"      "-.  
                  /            \ 
                 |    LuLZK1D   | 
                 |,  .-.  .-.  ,| 
                 | )(__/  \__)( | 
                 |/     /\     \| 
       (@_       (_     ^^     _) 
  _     ) \_______\__|IIIIII|__/__________________________ 
 (_)@8@8{}<________|-\IIIIII/-|_S_O_S_S_O_S_S_O_S_S_O_S_P_> 
        )_/        \          / 
       (@           `--------` Welcome! 
       
	./Beta Checking HTTP-Status Code BYPASS Cloudflare UAM
	./Author: lulzkid
	./Github.com/lulzkid
"""
print("================================================")
u = raw_input("[*] Target [URL]: ")
s2 = cfscrape.create_scraper()
code3 = s2.get(u).status_code
if s2.get(u).status_code == 200:
    print "[!] HTTP " + str(code3) + " [OK]"
elif s2.get(u).status_code == 404:
    print "[!] HTTP " + str(code3) + " [Not Found]"
elif s2.get(u).status_code == 403:
    print "[!] HTTP " + str(code3) + " [Forbidden]"
elif s2.get(u).status_code == 500:
    print "[!] HTTP " + str(code3) + " [Internal Server Error]"
elif s2.get(u).status_code == 502:
    print "[!] HTTP " + str(code3) + " [Bad Gateway]"
elif s2.get(u).status_code == 503:
    print "[!] HTTP " + str(code3) + " [Service Unavailable]"
elif s2.get(u).status_code == 504:
    print "[!] HTTP " + str(code3) + " [Gateway Timeout]"
elif s2.get(u).status_code == 520:
    print "[!] HTTP " + str(code3) + " [Unknown Error]"
elif s2.get(u).status_code == 521:
    print "[!] HTTP " + str(code3) + " [Web Server is Down]"
elif s2.get(u).status_code == 522:
    print "[!] HTTP " + str(code3) + " [Connected Time out]"
elif s2.get(u).status_code == 523:
    print "[!] HTTP " + str(code3) + " [Origin Is Unreachable]"
elif s2.get(u).status_code == 524:
    print "[!] HTTP " + str(code3) + " [A Timeout Occurred]"
elif s2.get(u).status_code == 525:
    print "[!] HTTP " + str(code3) + " [SSL Handshake Failed]"
elif s2.get(u).status_code == 530:
    print "[!] HTTP " + str(code3) + " [Origin DNS Error]"
else:
    print "[!] HTTP " + str(code3) + " [Error or Down]"
print("================================================")
print("[*] 1. Normal")
print("[*] 2. Bypass" + " (only work on cloudflare uam)")
mode = raw_input("[*] Select Mode: ")
print("================================================")
if mode == '1':
	print("- [1] Checking Target: "+"["+u+"]"+ " HTTP Status Code Normal:")
	print("                          Ctrl + C to stop                     ")
	while True:
            try:
                i = random.choice(("[!]", "[@]", "[~]", "[+]", "[-]"))
                r = requests.get(u).status_code
                print i,"Sending HTTP-Requests to " + "[" + u + "]" + " => " + "Status: ["+str(r)+"]"
            except KeyboardInterrupt:
                print('./Exiting, Have fun day ;)')
                sys.exit(0)  
            except requests.exceptions.ConnectionError as e:
                print("[!]"+" Please Check Your Internet Connection!")
                sys.exit(1)  
elif mode == '2':
    print("+ [2] Checking Target: "+"["+u+"]"+ " HTTP Status Code Bypass Cloudflare UAM:") 
    print("                          Ctrl + C to stop                     ")
    while True:
        try:
            i = random.choice(("[!]", "[@]", "[~]", "[+]", "[-]"))
            s = cfscrape.create_scraper()
            code2 = s.get(u).status_code
            print i,"Sending HTTP-Requests to " + "[" + u + "]" + " => " + "Status: ["+str(code2)+"]"
        except KeyboardInterrupt:
            print('./Exiting, Have fun day ;)')
            sys.exit(0)
        except requests.exceptions.ConnectionError as e:
            print("[!]"+" Please Check Your Internet Connection!")
            sys.exit(1) 
else:
  sys.exit(0)
