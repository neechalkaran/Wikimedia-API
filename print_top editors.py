#Collect All User whith More than 9000 edits
import string
import requests
project="wikipedia"
limit=9000
URL = "https://ta."+project+".org/w/api.php?action=query&list=allusers&auprop=editcount&format=json&aulimit=500&aufrom="
cont_string=""

while cont_string != "Nil":
  r = requests.get(url = URL+cont_string)
  r.encoding = 'utf-8'
  data=r.json()
  if("continue" in data):
    cont_string = data["continue"]["aufrom"]
  else:
    cont_string="Nil"
  for i in data["query"]["allusers"]:
    if(i["editcount"]>limit):
      print(i["name"] +" "+str(i["editcount"]))
