thread_count = int(input("number of threds ? (850 is best)"))
import requests
import json
from random import randint
import threading
from lxml.html import fromstring
from itertools import cycle
import traceback
import time
from time import sleep



with open("proxy.txt", "r") as fs:
  proxies = [line.strip() for line in fs]
proxy_pool = cycle(proxies)

def Check():
  for x in range(10000):
      headers = {
      'Accept': 'application/json',
      }
      groupId = str(randint(0,700000))
        
      link = "https://groups.roblox.com/v1/groups/" + groupId
      proxy = next(proxy_pool)
      try :
          
          response = requests.get(link , headers=headers, proxies={"http": proxy, "https": proxy})
          response = response.json()
          print("testing " + groupId)
          try:
              if response['owner'] == None and response["publicEntryAllowed"] == True:
                print(groupId + "cool")
                with open("hit.txt", "a") as hit:
                    hit.write(groupId + " cool" + "\n")
              else:
                  print("no " + groupId + " bad ")
                  with open("log.txt", "a") as hit:
                      hit.write("no " + groupId + " bad ")
              time.sleep(1)

          except:
            print("Owned")
            with open("log.txt", "a") as hit:
                    hit.write(groupId + " Owned")
            time.sleep(1)
      except:
        print("proxy error")
for x in range(thread_count):
    threading.Thread(target=Check).start()





