from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup
import time
import re
import pandas as pd
from openpyxl import Workbook
Label=['product_attribute_sku', 'product_attribute_product', 'product_condition','product_serial_number', 'Warranty','Location','Compatible_Aircraft','Manufacturer','ATA_Chapter']
driver=webdriver.Chrome()
def aripartspage():
    alist=[]#存放链接
    blist=[]#存放对应连接的名字
    clist=[]
    dlist=[]
    elist=[]
    airparts=[]
    #获得页面页数
    for i in range(1,7):
        baseurl="https://www.godirecttrade.com/apu.html"
        pageurl="?p="+str(i)
        url=baseurl+pageurl
        driver.get(url)
        for item in driver.find_elements_by_class_name("product-page-anchor"):
            title1=item.get_attribute('href')
            alist.append(title1)
        '''
        for item in driver.find_elements_by_class_name("serial-number-searchlist-td"):
            title2=item.get_attribute("title")
            blist.append(title2)
        for item in driver.find_elements_by_class_name("product-name-searchlist-td"):
            title3=item.get_attribute('title')
            clist.append(title3)
        for item in driver.find_elements_by_class_name("warranty-searchlist-td"):
            for sub_item in driver.find_elements_by_class_name("label"):
                title4=sub_item.get_attribute("title")
                dlist.append(title4)
            for sub_item in driver.find_elements_by_class_name("value"):
                title5=sub_item.get_attribute("title")
                elist.append(title5)
            #if href not in  alist:
                #alist.append(href)
            #if title not in blist:
                #blist.append(title)
                '''
    print(alist)
    print(len(alist))
    #print(blist)
    #print(clist)
    #print(dlist)
    artpartclassification(alist)

def artpartclassification(alist):
    airparts=[]
    print(alist)
    for airparturl in alist:
        try:
            driver.get(airparturl)
            #1
            try:
                sku=driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/h1').text
            except:
                sku=''
             #2
            try:
                product=driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/h2').text
            except:
                product=''
            #3
            try:
                condition=driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/span[2]/h2').text
            except:
                condition=''
            #4
            try:
                number=driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div[3]/div[2]/span[2]/h2').text
            except:
                number=''
            #5
            try:
                warranty=driver.find_element_by_xpath('//*[@id="product-attribute-specs-table-1"]/tbody/tr[1]/td').text
            except:
                warranty=''
            #6
            try:
                location=driver.find_element_by_xpath('//*[@id="product-attribute-specs-table-1"]/tbody/tr[2]/td').text
            except:
                location=''
            #7
            try:
                compatible_aircraft=driver.find_element_by_xpath('//*[@id="compatible_aircraft"]/td').text
            except:
                compatible_aircraft=''
            #8
            try:
                manufacturer=driver.find_element_by_xpath('//*[@id="product-attribute-specs-table-2"]/tbody/tr[2]/td/span').text
            except:
                manufacturer=''
            #9
            try:
                Chapter=driver.find_element_by_xpath('//*[@id="product-attribute-specs-table-2"]/tbody/tr[3]/td/span').text
            except:
                Chapter=''
            temp=dict(product_attribute_sku=sku,
                        product_attribute_product=product,
                        product_condition=condition,
                        product_serial_number=number,
                        Warranty=warranty,
                        Location=location,
                        Compatible_Aircraft=compatible_aircraft,
                        Manufacturer=manufacturer,
                        ATA_Chapter=Chapter)
            airparts.append(temp)
            time.sleep(3)
        except:
            print("写入失败")
    for item in airparts:
        print(item)
    export_excel(airparts)

def export_excel(dic_data):
    # 将字典列表转换为DataFrame
    pf=pd.DataFrame(list(dic_data))
    # 指定字段顺序
    order=['product_attribute_sku', 'product_attribute_product', 'product_condition','product_serial_number', 'Warranty','Location','Compatible_Aircraft','Manufacturer','ATA_Chapter']
    pf=pf[order]
    # 将列名替换为中文
    '''
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
    '''
    #pf.rename(columns=columns_map, inplace=True)
    # 指定生成的Excel表格名称
    file_path=pd.ExcelWriter('APU.xlsx')
    # file_csv_path = pd.read_csv("compound.csv")
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # pf.to_csv(file_csv_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()

def test():
    airparts=[]
    url="https://www.godirecttrade.com/turbineaero-repair-pn-3800396-1-sn-p-263.html"
    driver.get(url)
    #1
    try:
        sku=driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/h1').text
    except:
        sku=''
    #2
    try:
        product=driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/h2').text
    except:
        product=''
    #3
    try:
        condition=driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/span[2]/h2').text
    except:
        condition=''
    #4
    try:
        number=driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div[3]/div[2]/span[2]/h2').text
    except:
        number=''
    #5
    try:
        warranty=driver.find_element_by_xpath('//*[@id="product-attribute-specs-table-1"]/tbody/tr[1]/td').text
    except:
        warranty=''
    #6
    try:
        location=driver.find_element_by_xpath('//*[@id="product-attribute-specs-table-1"]/tbody/tr[2]/td').text
    except:
        location=''
     #7
    try:
        compatible_aircraft=driver.find_element_by_xpath('//*[@id="compatible_aircraft"]/td').text
    except:
        compatible_aircraft=''
    #8
    try:
        manufacturer=driver.find_element_by_xpath('//*[@id="product-attribute-specs-table-2"]/tbody/tr[2]/td/span').text
    except:
        manufacturer=''
    #9
    try:
        Chapter=driver.find_element_by_xpath('//*[@id="product-attribute-specs-table-2"]/tbody/tr[3]/td/span').text
    except:
        Chapter=''
    temp=dict(     product_attribute_sku=sku,
    product_attribute_product=product,
    product_condition=condition,
    product_serial_number=number,
    Warranty=warranty,
    Location=location,
    Compatible_Aircraft=compatible_aircraft,
    Manufacturer=manufacturer,
    ATA_Chapter=Chapter)
    airparts.append(temp)
    print(airparts)
    export_excel(airparts)


if __name__=='__main__':
    aripartspage()
    #test()
