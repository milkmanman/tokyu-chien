#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib.request
from bs4 import BeautifulSoup
import datetime
import configparser

config = configparser.ConfigParser()
config.read('setting.ini')

section1 = 'train_info'
isnobori = config[section1]['isnobori']
linetype = config[section1]['line']

today = datetime.date.today()
iso = today.isoformat()
dataforurl =  iso.replace('-', '')

def trainurl():
    retnum = 0
    if (isnobori == "true" and linetype == "touyoko"):
        retnum = 1
    elif (isnobori == "false" and linetype == "touyoko"):
        retnum = 11
    elif (isnobori == "true" and linetype == "meguro"):
        retnum = 2
    elif (isnobori == "false" and linetype == "meguro"):
        retnum = 12
    elif (isnobori == "true" and linetype == "dento"):
        retnum = 3
    elif (isnobori == "false" and linetype == "dento"):
        retnum = 13
    elif (isnobori == "true" and linetype == "oimachi"):
        retnum = 4
    elif (isnobori == "false" and linetype == "oimachi"):
        retnum = 14
    elif (isnobori == "true" and linetype == "ikegami"):
        retnum = 5
    elif (isnobori == "false" and linetype == "ikegami"):
        retnum = 15
    elif (isnobori == "true" and linetype == "tamagawa"):
        retnum = 6
    elif (isnobori == "false" and linetype == "tamagawa"):
        retnum = 16
    elif (isnobori == "true" and linetype == "setagaya"):
        retnum = 7
    elif (isnobori == "false" and linetype == "setagaya"):
        retnum = 17

    return retnum


def getTrainInfo(numberstr):
    url = 'https://www.tokyu.co.jp/railway/delay/print.php?line=' + numberstr + '&d='+ dataforurl +'_1'
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
    return mailbody


def getInfoURL(numberstr):
    url = 'https://www.tokyu.co.jp/railway/delay/print.php?line=' + str(trainurl()) + '&d='+ numberstr  +'_1'
    return mailbody


num = str(trainurl())
mailbody = getTrainInfo(num)
url = getInfoURL(num)

line_notify_token = config['line_notify']['token']
line_notify_api = 'https://notify-api.line.me/api/notify'
message = "遅延情報"
message += mailbody
message += "\n" + url

payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token} 
line_notify = requests.post(line_notify_api, data=payload, headers=headers)
