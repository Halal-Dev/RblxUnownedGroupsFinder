
import requests
import json
from random import randint

for x in range(1000):

      headers = {
      'Accept': 'application/json',
      }
      groupId = ""
      for a in range(randint(1,6)):
        groupId = groupId + str(randint(1,7))
      groupId = groupId + str(randint(4,7))

      link = "https://groups.roblox.com/v1/groups/" + groupId
      response = requests.get(link , headers=headers)
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

      except:
        print("Owned")
        with open("log.txt", "a") as hit:
                hit.write(groupId + " Owned")





