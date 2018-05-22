import requests
from bs4 import BeautifulSoup
import os

file = open('/home/thang/Documents/Spider-master/venv/Url/Link.txt', 'w')
file.write('https://fptshop.com.vn/dien-thoai/oppo-f7\n')
list = ['/dien-thoai/oppo-f7']
for index in list:
    a = requests.post('https://fptshop.com.vn' + index)
    htmlProcess = BeautifulSoup(a.text, "html.parser")
    for item in htmlProcess.find_all('a'):
        try:
            link = item.attrs['href']
        except:
            link = ''
        if (link[0:22] == 'https://fptshop.com.vn'):
            link = link[22:len(link)]
        if (link[0:12] == "/dien-thoai/" and '-' in link[12:len(link) - 1] and link[12:15] != 'tu-' and link[12:15]!= 'tre' and link[12:15]!='app'):
            if ((link in list) == False):
                list.append(link)
                file.write('https://fptshop.com.vn' + link + '\n')
file.close()