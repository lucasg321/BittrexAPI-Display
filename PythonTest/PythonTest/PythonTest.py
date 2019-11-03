import urllib.request
import json
import collections
import time
import hashlib
import hmac
import tkinter as tk

nonce1 = str(time.time())
apikey = ''
apisecret = ''
currency = 'USD'
url = 'https://bittrex.com/api/v1.1/account/getbalances?apikey='+apikey+'&nonce='+nonce1#+'&currency='+currency
sign=hmac.new(bytes(apisecret,encoding='utf-8'),bytes(url,encoding='utf-8'),hashlib.sha512).hexdigest()

req = urllib.request.Request(url, headers={"apisign" : sign})
accountreq=urllib.request.urlopen(req).read()
accountreqjson=json.loads(accountreq)

#print(accountreqjson)

url = 'https://bittrex.com/api/v1.1/account/getbalance?apikey='+apikey+'&nonce='+nonce1+'&currency='+currency
sign=hmac.new(bytes(apisecret,encoding='utf-8'),bytes(url,encoding='utf-8'),hashlib.sha512).hexdigest()

req = urllib.request.Request(url, headers={"apisign" : sign})
accountreq1=urllib.request.urlopen(req).read()
accountreqjson1=json.loads(accountreq1)

#print(accountreqjson1)

win = tk.Tk()
win.title("Bittrex Account Holdings")
win.geometry("900x600")
frame1 = tk.Frame(win)


frame1.grid(column = 0, row = 0)
with open('data.txt', 'w') as outfile:
    json.dump(accountreqjson, outfile)


with open('data.txt') as json_file:
    data = json.load(json_file)
#print(data["result"][0]["Currency"])

for i in data["result"]:
 currency = i["Currency"]
 #print(i["Currency"])
 label1 = tk.Label(frame1, text = currency, font=("Times New Roman", 20))
 label1.pack()

frame2 = tk.Frame(win)
frame2.grid(column = 1, row = 0)

for i in data["result"]:
 balance = i['Balance']
 #print(i["Balance"])
 label2 = tk.Label(frame2, text = balance, font=("Times New Roman", 20))
 label2.pack()

win.mainloop()
