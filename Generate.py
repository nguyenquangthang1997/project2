from Url import *
from Predicate import *

for i in range(1, 14, 1):
    link = 'https://fptshop.com.vn/dien-thoai?sort=gia-cao-den-thap&trang=' + str(i)
    url = Url(link)
    html = HtmlData(link)
    if (html.condition() == 1):
        url.saveUrl()

# urlFile = open('/home/thang/Documents/Spider-master/venv/Url/data.txt', 'r')
# for line in urlFile:
#     url = Url(line[0:len(line)-1])
#     html = HtmlData(line[0:len(line)-1])
#     if(html.condition() == 1):
#         url.saveUrl()
