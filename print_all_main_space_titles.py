#List all Wikipedia article pages
import requests
from urllib.request import urlopen
from urllib.parse   import quote
import regex
import time
import json
continue_str=" "
while continue_str!="":
  url = "https://ta.wikipedia.org/w/api.php?action=query&list=allpages&aplimit=5000&format=json&apcontinue="+ continue_str
  page = requests.get(url)
  page.encoding = 'utf-8'
  data=page.json()
  titles=[]
  for i in data["query"]["allpages"]:
    titles.append(str(i["title"]))      
  try:
    continue_str= data["continue"]["apcontinue"]
  except:
    continue_str=""
  print("\n".join(titles))
  print(continue_str)
