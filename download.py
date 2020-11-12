from bs4 import BeautifulSoup as bs
import requests as rq
import wget
r=rq.get('https://gpldl.com/repository/premium-woocommerce-extensions/')
data=r.text
soup=bs(data)
for link in soup.find_all('a'):
    print(link.get('href'))
'''f=open('c:/users/sarthak/links.txt','r')
url1=f.readlines()
url=[]
for i in url1:
    url.append(i[:-1])
for i in range(len(url)):
    wget.download(url[i],'/'+str(i+1)+'.jpg')
'''
