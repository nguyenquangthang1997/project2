import requests
from bs4 import BeautifulSoup


class HtmlData:

    def __init__(self, url):
        self.url = url
        self.distinctUrlOtherLink = []
        self.predicateValue = []

    def condition(self):
        req = requests.post(self.url)
        if (req.status_code / 100 >= 4):
            return 0
        else:
            return 1

    def getHtmlText(self):
        req = requests.post(self.url)
        return req.text

    # def getDistinctUrlOtherLink(self):
    #     htmlProcess = BeautifulSoup(self.getHtmlText(), "html.parser")
    #     for item in htmlProcess.find_all('a'):
    #         try:
    #             link = item.attrs['href']
    #         except:
    #             link = ''
    #         if(link[0:22]=='https://fptshop.com.vn'):
    #             link= link[22:len(link)]
    #             # and '-' in link[12:len(link) - 1]
    #         if (link[0:12] == "/dien-thoai/" ):
    #             if ((link in self.distinctUrlOtherLink) == False):
    #                 self.distinctUrlOtherLink.append(link)
    #     return self.distinctUrlOtherLink

    def getPredicate(self):
        htmlProcess = BeautifulSoup(self.getHtmlText(), "html.parser")
        html_info = ''
        for html in htmlProcess.find_all('div'):
            try:
                html.attrs['id']
            except:
                html.attrs['id'] = ''
            if (html.attrs['id'] == 'PopTSKT'):
                html_info = html
                break
        if (html_info != ''):
            a = html_info.find_all('li')
            for li in html_info.find_all('li'):
                if (li.label == None):
                    if (([li.text, 'sub'] in self.predicateValue) == False):
                        self.predicateValue.append([li.text, 'sub', 'sub'])
                        parentPredicate = li.text
                if (li.label != None):
                    if (([li.label.string, li.span.string, parentPredicate] in self.predicateValue) == False):
                        self.predicateValue.append([li.label.string, li.span.string, parentPredicate])
            return self.predicateValue
        else:
            return ''
