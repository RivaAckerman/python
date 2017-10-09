"""
通用爬取豆瓣评论
"""

import requests
import re
import time

#cookie
cookies={
*****
}


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}

# Namelist=re.findall(r'<a href=.*? class="">(.*?)</a>',html) 评论用户ID
# #<span class="allstar10 rating" title="很差"></span>  
# Scorelist=re.findall(r'<span class="allstar\d.*? rating" title=(.*?)>',html) 评分
# #<span class="comment-time " title="2017-06-13 23:23:44">2017-06-13</span>  日期
# Timelist=re.findall(r'<span class="comment-time " title=.*?>(.*?)</span>',html,re.S)
# #<p class=""> 两星半吧 视觉高潮很爽 爽完脑子里也没留下些什么 犹如很有职业道德的性工作者</p> 内容
# Contentlist=re.findall(r'<p class="">(.*?)</p>',html,re.S)

#<a href="?start=27&amp;limit=20&amp;sort=new_score&amp;status=P" data-page="" class="next">后页 &gt;</a>下一页

url='https://movie.douban.com/subject/27038183/comments?start=0&limit=20&sort=new_score&status=P'
#
html=requests.get(url,headers=headers,cookies=cookies)
#
# list=re.findall(r'<a href="(.*?)" data-page="" class="next">',html)
#
# print(list[0])

while html.status_code==200:
    html=html.text
    Scorelist = re.findall(r'<span class="allstar\d.*? rating" title=(.*?)>', html)
    Timelist = re.findall(r'<span class="comment-time " title=.*?>(.*?)</span>', html, re.S)
    Contentlist = re.findall(r'<p class="">(.*?)</p>', html, re.S)
    for i,value in enumerate(Contentlist):
        with open('tiequan.txt','a+',encoding='utf-8') as f:
            data=Timelist[i].strip()+':'+value.strip()
            f.write(data)#json.dumps(data,ensure_ascii=False)
            f.write('\n')
    next = re.findall(r'<a href="(.*?)" data-page="" class="next">', html)
    url='https://movie.douban.com/subject/27038183/comments'+next[0]
    print(next[0])
    time.sleep(3)
    html=requests.get(url,headers=headers,cookies=cookies)






