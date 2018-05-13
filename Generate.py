from Url import *
from Predicate import *

link  = 'https://fptshop.com.vn/dien-thoai/samsung-new-gear-vr'
url = Url(link)
html = HtmlData(link)
predicate = Predicate(link)
if(html.condition() == 1):
    url.saveUrl()
    predicate.savePredicate()


urlFile = open('/home/thang/Documents/Spider-master/venv/Url/data.txt', 'r')
for line in urlFile:
    url = Url(line[0:len(line)-1])
    html = HtmlData(line[0:len(line)-1])
    predicate = Predicate(line[0:len(line)-1])
    if(html.condition() == 1):
        url.saveUrl()
        predicate.savePredicate()