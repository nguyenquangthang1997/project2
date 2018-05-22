# from Url import *
from Predicate import *
import requests
import os

link = open('/home/thang/Documents/Spider-master/venv/Url/Link.txt', 'r')
for line in link:
    html = HtmlData(line[0:len(line)-1])
    b = html.condition()
    if(html.condition() == 0):
        html = HtmlData(line[0:len(line) - 1])
    if(html.condition() == 1):
        predicate = Predicate(line[0:len(line)-1])
        predicate.savePredicate()

# link = 'https://fptshop.com.vn/dien-thoai'
# a = requests.post('https://fptshop.com.vn/dien-thoai')
# url = Url(link)
# html = HtmlData(link)
#
# if (html.condition() == 1):
#     url.saveUrl()
#
# urlFile = open('/home/thang/Documents/Spider-master/venv/Url/data.txt', 'r')
# for line in urlFile:
#     url = Url(line[0:len(line) - 1])
#     html = HtmlData(line[0:len(line) - 1])
#     if (html.condition() == 1):
#         url.saveUrl()
