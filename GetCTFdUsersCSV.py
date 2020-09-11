#!/usr/bin/env python
'''
Script to download user CSV from CTFd Server for python 3.8.5 (Built on Windows 10)

You will need to change the variables:
    - url - specify in one of these formats:
        http://www.domain.com:8000/
        http://www.domain.com/
        https://www.domain.com/
    - uname - username with admin rights to CTFd
    - passwd - password for user with admin rights to CTFd
Then simply run the script under regular user rights.


__author__ = "James Rodewald"
__copyright__ = "Copyright 2020, Akblarb"
__credits__ = ["Wireshark for showing me headers and request info"]
__license__ = "GPL"
__version__ = "1.0.0.0"
__maintainer__ = "James Rodewald"
__email__ = "<snip>"
__status__ = "Beta PoC"

***Currently does not save CSV to disk.  Only displays on screen.

'''
import requests 

'''
Modify these vars to match your environment
'''
url = 'https://www.domain.com/'
uname = "MyAdminUName"
passwd = "abc123"


nonce = ""
s = requests.Session()
print(url)
r = s.get(url+"login")

print("---headers:PreAuth---")
print(r.headers)
print("\n\n")
print("---cookies:PreAuth---")
print(s.cookies)
print("\n\n")
#no need to manually set cookies.
#s.headers.update({"Cookie": f"{r.headers['Set-Cookie']}"})
#print(r.text)

#Get "nonce" from server
for line in r.text.split("\n"):
    if "nonce" in line:
        #print(line.strip().split(" "))
        for item in line.strip().split(" "):
            #print(item)
            if "value" in item:
                #print(item)
                #print(item.split("=")[1].split("\"")[1])
                nonce = item.split("=")[1].split("\"")[1]
                break
        break

#nonce
print(nonce)

data = {"name":f"{uname}", "password":f"{passwd}", "_submit":"Submit", "nonce":f"{nonce}"}

#statuscode
print(r)

r = s.post(url+"login", data=data)
print("---headers:PostAuth---")
print(r.headers)
print("\n\n")
print("---cookies:PostAuth---")
print(s.cookies)
print("\n\n")
#statuscode - If not 200, authenticaiton failed.
print(r)
print("\n\n")
s.headers.update({"Referer": f"{url}/admin/config"})
r = s.get(url+"admin/export/csv?table=users")
print(r.headers)
print("\n\n")
print(r.text)
#statuscode - If not 200, download of users.csv failed.
print(r)
