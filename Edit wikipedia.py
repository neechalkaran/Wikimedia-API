#To edit test wikipedia page using BOT account

import string
import requests
from requests.auth import HTTPBasicAuth
import json
URL = "https://test.wikipedia.org/w/api.php"
mysession = requests.Session()

#get BOT credentials at https://www.mediawiki.org/wiki/Special:BotPasswords
user, passw ="YOUR_BOT_NAME","YOUR_BOT_PASSWORD"

options = {"action":"query","meta":"tokens","type":"login", "format":"json"}
r = mysession.get(URL, params=options)
r.encoding = 'utf-8'
data=r.json()
if(r.status_code==200):
  csrf=data['query']['tokens']['logintoken']
  print(csrf)
  options_1={"lgname":user, "lgpassword": passw, "lgtoken":csrf, "action":"login", "format":"json"}
  r = mysession.post(URL, data=options_1)
  r.encoding = 'utf-8'
  data1=r.json()
  cookie=json.dumps(r.cookies.get_dict())
  print(data1)
  #{'login': {'result': 'Success', 'lguserid': 3156, 'lgusername': 'NeechalBOT'}}
  logintoken=data['query']['tokens']['logintoken']

  option_2 = {"action": "query", "meta": "tokens","format": "json"}


  r = mysession.get(URL, params=option_2)
  r.encoding = 'utf-8'
  data2=r.json()
  CSRF_TOKEN=data2['query']['tokens']['csrftoken']
  print(data2)
#{'batchcomplete': '', 'query': {'tokens': {'csrftoken': '7309641d54840d37f45137e2474c676e65196f8b+\\'}}}


options={'action':'edit',
         'title':'User:Neechalkaran/sandbox',
         'summary':'test', 'text': result,'token':CSRF_TOKEN, 'format': 'json'}

r = mysession.post(URL, data=options)
print(r.status_code)
r.encoding = 'utf-8'
data3=r.json()
print(data3)

#{'edit': {'result': 'Success', 'pageid': 418813, 'title': 'பயனர்:Neechalkaran/sandbox', 'contentmodel': 'wikitext', 'nochange': ''}}


