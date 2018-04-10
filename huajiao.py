#爬花椒主播信息
from bs4 import BeautifulSoup
import requests
import re

__author__='cs'

def getlinks(url):
    InformationList=[]

    html=requests.get(url).text

    soup=BeautifulSoup(html,'html.parser')

    result=re.findall(r'<a href="(/l/\d.*?)" class="figure" target="_blank">',html)
    name=soup.find_all('p','name fl')
    title=soup.find_all('p','feed-title')
    # for n in name:
    #     print(n.string.strip())
    # for id in result:
    #      print(id)
    #
    for i,value in enumerate(name):
        s=value.string.strip(),result[i]
        InformationList.append(s)
    getinformation(InformationList)

def getinformation(list):
    for i in list:
        url = 'http://www.huajiao.com{x}'
        url = url.format(x=i[1])
        html = requests.get(url).text
        soup=BeautifulSoup(html,'html.parser')
        follower=soup.find_all('span',attrs={'class':"number js-fans"})
        praises = soup.find_all('span', attrs={'class': "number js-praises"})
        currency = soup.find_all('span', attrs={'class': "number js-currency"})
        print(i[0],'  ','粉丝数:',follower[0].string,'  ','赞数:',praises[0].string,'  ','礼物数:',currency[0].string)

if __name__=='__main__':
    num = 999
    while num < 1001:
        Furl = 'http://www.huajiao.com/category/%d'%(num)
        print(num)
        print(Furl)
        getlinks(Furl)
        num=num+1
