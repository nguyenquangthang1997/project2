import requests
from bs4 import BeautifulSoup


class HtmlData:

    def __init__(self, url):
        self.url = url
        self.distinctUrlOtherLink = []
        self.predicateValue = []
    def condition(self):
        req = requests.post(self.url)
        if(req.status_code/100 >= 4):
            return 0
        else:
            return 1
    def getHtmlText(self):
        req = requests.post(self.url)
        # tempFile = open('tempFile.html', 'w')
        # tempFile.write(req.text)
        # tempFile.close()
        return req.text

    def getDistinctUrlOtherLink(self):
        htmlProcess = BeautifulSoup(self.getHtmlText(), "html.parser")
        for item in htmlProcess.find_all('a'):
            try:
                link = item.attrs['href']
            except:
                link = ''
            if (link[0:12] == "/dien-thoai/" and '-' in link[12:len(link) - 1]):
                if ((link in self.distinctUrlOtherLink) == False):
                    self.distinctUrlOtherLink.append(link)
        return self.distinctUrlOtherLink

    def getPredicate(self):
        htmlProcess = BeautifulSoup(self.getHtmlText(), "html.parser")
        for html in htmlProcess.find_all('div'):
            try:
                html.attrs['id']
            except:
                html.attrs['id'] = ''
            if (html.attrs['id'] == 'PopTSKT'):
                htmlInfo = html
                break
            else:
                htmlInfo = ''
        if(htmlInfo != ''):
            for li in htmlInfo.find_all('li'):
                if (li.label != None):
                    # a = self.predicateValue
                    # b = [li.label.string, li.span.string]
                    # c = b in a
                    # e = [li.label.string, li.span.string] in self.predicateValue
                    # d = ([li.label.string, li.span.string] in self.predicateValue) ==False
                    if(([li.label.string, li.span.string] in self.predicateValue) == False):
                        self.predicateValue.append([li.label.string, li.span.string])
            return self.predicateValue
        else:
            return ''
