# improve with adding 대, 중, 소 category
# improve with 90개씩 나온다
# improve with end page, end product name and stop there
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import openpyxl
import os
import time
from  datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

path="C:/WebDriver/chromedriver"
service = Service(executable_path=path)
driver=webdriver.Chrome(path)



product_name_list = []
product_big_cat_list = []
product_middle_cat_list = []
product_cat_list = []

# for element in non_home_crawl_list :
  # 10??
# driver.find_element(By.XPATH,'//*[@id="e_gnb"]/div/div[1]/div[2]/ul[1]/li[11]/a').click()

# driver.implicitly_wait(10)


for i in range(1, 6):  # 1 pages, 00 items
    try:
        for catid in myfile:
        url='https://www.ygoon.com/mall/product/list?categoryId=1439&level=C&pageSize=30&listType=1&pageNo=%d&searchFilterCodeIds='%i
        driver.get(url)
        time.sleep(5)
        for j in range (1,91):
            try:
                # "//*[@id="contents"]/div[2]/div/span/div/div[3]/ul/li[54]/div/div[2]/a/div[1]/div[1]"
                product_name = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div/span/div/div[3]/ul/li[' + str(
                    j) + ']/div/div[2]/a/div[1]/div[1]').text
                product_big_cat = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/ul/li[2]/a/span').text
                product_middle_cat = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div/ul/li[3]/a/span').text
                product_cat = driver.find_element(By.XPATH, '*//*[@id="contents"]/div[2]/div/div/h1').text

                product_name_list.append(product_name)
                product_big_cat_list.append(product_big_cat)
                product_middle_cat_list.append(product_middle_cat)
                product_cat_list.append(product_cat)

            except NoSuchElementException:
                break

            print(product_cat, ' done')
    except NoSuchElementException:
        break

driver.close()

df_non_home = pd.DataFrame(
    {'카데고리(대)': product_big_cat_list, '카데고리(중)': product_middle_cat_list, '카데고리(소)': product_cat_list,
     '상품명': product_name_list})
print(df_non_home.shape)
df_non_home.head()

# 처음이전12345678910다음마지막 -> will take 0 only.... be cause this cause many data loss, check item behind 커피머신/커피메이커, for example