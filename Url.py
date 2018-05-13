from HtmlData import *
from Predicate import *
import os


class Url:
    def __init__(self, url):
        self.url = url

    def saveUrl(self):
        htmlData = HtmlData(self.url)
        flag = 1
        distinctUrlOtherLink = htmlData.getDistinctUrlOtherLink()
        urlFile = open('/home/thang/Documents/Spider-master/venv/Url/data.txt', 'a')
        for item in distinctUrlOtherLink:
            urlFileTemp = open('/home/thang/Documents/Spider-master/venv/Url/data.txt', 'r')
            for line in urlFileTemp:
                item1 = 'https://fptshop.com.vn' + item + '\n'
                if (line == 'https://fptshop.com.vn' + item + '\n'):
                    flag = 0
                    break
            urlFileTemp.close()
            if (flag == 1):
                urlFile.write('https://fptshop.com.vn' + item + '\n')
        urlFile.close()
