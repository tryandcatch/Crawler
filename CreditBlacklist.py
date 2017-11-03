#coding=utf-8
#执行：
# pip2 install pandas
# pip2 install --upgrade numpy
# pip2 install openpyxl

# pandas、openpyxl、使用pandas前记得升级numpy（若安装了numpy） 》pip2 install --upgrade numpy
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd



def f(x):
    return str(x).lstrip('<td>').rstrip('</td>')


def xyhmd(x= 1,y= 131):
    name = []
    id = []
    ph = []
    amounts = []
    status = []
    for i in range(x,y + 1):
        print '页码：%d' % (i)
        # 数据来源网址
        url= '数据网址'.format(i)
        res= requests.get(url).content
        html= bs(res,'html.parser')
        tr= html.find_all(name= 'tr', attrs= {'class':'pointer'})
        for i in tr:
            x= i.find_all(name= 'td')
            name.append(x[0])
            id.append(x[1])
            ph.append(x[2])
            amounts.append(x[3])
            status.append(x[4])
    df= pd.DataFrame({'name':name,'idcard':id,'tel':ph,'amounts':amounts,'status':status})
    df= df.applymap(f)
    df.to_excel('xyhmdd.xlsx')
    return 'cool'

xyhmd();