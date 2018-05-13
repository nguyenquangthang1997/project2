import requests

a = requests.post('https://fptshop.com.vn/dien-thoai/hang-khac')
c = a.status_code/100
c =1





















# htmlProcess = BeautifulSoup(r1.getHtmlText(), "html.parser")
# a = htmlProcess.find_all('a')
# for b in a:
#     try:
#         c = b.attrs['href']
#     except:
#         c = ''
    # if()
# b = a.attrs['href']
# a =
# b = a.find_all('a')
# print(a)

# import requests
# from bs4 import BeautifulSoup
#
# req = requests.post('https://fptshop.com.vn/dien-thoai/xiaomi-redmi-4x')
# b = req.text
# htmlReturn = BeautifulSoup(req.text, "html.parser")
# htmlInfo = ''
# for html in htmlReturn.find_all('div'):
#     try:
#         html.attrs['id']
#     except:
#         html.attrs['id'] = ''
#     if (html.attrs['id'] == 'PopTSKT'):
#         htmlInfo = html
#
# # return predicate, value
# for li in htmlInfo.find_all('li'):
#     if(li.label != None):
#         print(li.label.string)
#         print(li.span.string)
