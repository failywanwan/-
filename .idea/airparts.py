from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup
import time
import re
import pandas as pd
from openpyxl import Workbook
Lable = ['type','title','model','classify','name','amount','state','aircraftype','time']
#driver=webdriver.PhantomJS()
driver=webdriver.Chrome()

def aripartspage():
    alist=[]#存放链接
    blist=[]#存放对应连接的名字
    airparts=[]
    #获得页面页数
    for i in range(1,110):
        baseurl="http://www.airparts.cn/Hk_Function/Hk_Buy.aspx?lm=17"
        pageurl="&pageid="+str(i)
        url=baseurl+pageurl
        driver.get(url)
        for link in driver.find_elements_by_class_name('product_list'):
            href = link.get_attribute('href')
            title=link.get_attribute('title')
            if href not in  alist:
                alist.append(href)
            if title not in blist:
                blist.append(title)
    print(alist)
    print(blist)
    artpartclassification(alist)

def test():
    airparturl='http://www.airparts.cn/Details/Hk_Buy_Details.aspx?Sell_Id=2276&page_id=2&lm=17'
    driver=webdriver.Chrome()
    driver.get(airparturl)
    airparts=[]
    temp=dict( type=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblType").text,
    title=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblTitle").text,
    model=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblModel").text,
    classify=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblClass").text,
    name=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblName").text,
    amount=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblAmount").text,
    state=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblState").text,
    aircraftype=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblAircraftType").text,
    time=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblTime").text,
               )
    airparts.append(temp)
    print(airparts)



def artpartclassification(alist):
    airparts=[]
    print(alist)
    for airparturl in alist:
        try:
            driver.get(airparturl)
            temp=dict( type=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblType").text,
                   title=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblTitle").text,
                   model=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblModel").text,
                   classify=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblClass").text,
                   name=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblName").text,
                   amount=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblAmount").text,
                   state=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblState").text,
                   aircraftype=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblAircraftType").text,
                   time=driver.find_element_by_id("ctl00_ContentPlaceHolder1_lblTime").text,
                       )
            airparts.append(temp)
            time.sleep(3)
        except:
            print("写入失败")
    for item in airparts:
        print(item)
    export_excel(airparts)
    #writeDataToExcleFile(airparts,'data.xlsx')
    #write_airpart(airparts)

def export_excel(dic_data):
    # 将字典列表转换为DataFrame
    pf=pd.DataFrame(list(dic_data))
    # 指定字段顺序
    order=['type', 'title', 'model','classify', 'name','amount','state','aircraftype','time']
    pf=pf[order]
    # 将列名替换为中文
    columns_map={
        'type': '类别',
        'title': '标题',
        'model': '件号',
        'classify': '分类',
        'name': '名称',
        'amount': '数量',
        'state':'状态',
        'aircraftype':'飞机型号',
        'time':'时间',
    }
    pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    file_path=pd.ExcelWriter('airparts.xlsx')
    # file_csv_path = pd.read_csv("compound.csv")
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # pf.to_csv(file_csv_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


if __name__=='__main__':
    aripartspage()




