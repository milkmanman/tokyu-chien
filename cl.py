#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib.request
from bs4 import BeautifulSoup
import datetime

isNobori = false

today = datetime.date.today()
iso = today.isoformat()
dataforurl =  iso.replace('-', '')

url = 'https://www.tokyu.co.jp/railway/delay/print.php?line=17&d='+ dataforurl  +'_1'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/55.0.2883.95 Safari/537.36 '

req = urllib.request.Request(url, headers={'User-Agent': ua})
html = urllib.request.urlopen(req)
mailbody = "train delay : "
soup = BeautifulSoup(html, "html.parser")
topicsindex = soup.find('div', attrs={'id' : 'print4'})
topics = topicsindex.find('table').find_all('tr')
for topic in topics:
    tds = topic.find_all('td')
    for td in tds:
        print(td.text)
        mailbody += td.text 

print(soup.find('head').find('title').text)

line_notify_token = ''
line_notify_api = 'https://notify-api.line.me/api/notify'
message = "遅延情報"
message += mailbody
message += "\n" + url


payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token} 
line_notify = requests.post(line_notify_api, data=payload, headers=headers)