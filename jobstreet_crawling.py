#Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
import os
import time
from  datetime import date


driver_path = Service('C:/WebDriver/chromedriver')
driver = webdriver.Chrome(service=driver_path)
driver2 = webdriver.Chrome(service=driver_path)

# Preparing pandas dataframe
col_name = ['company','position', 'qualificatiion']
dataset = pd.DataFrame(columns=col_name)

for i in range(1,68):
    url = "https://www.jobstreet.com.my/en/job-search/data-scientist-jobs/"
    driver.get(url+str(i))

    posts = driver.find_elements(By.CLASS_NAME,"sx2jih0.zcydq89e.zcydq88e.zcydq872.zcydq87e")
    for post in posts:
        title = post.find_element(By.CLASS_NAME,'sx2jih0.l3gun70.l3gun74.l3gun72').text
        print(title)
        link = post.find_element(By.CLASS_NAME,"sx2jih0.zcydq84u._18qlyvc0._18qlyvc1x._18qlyvc3._18qlyvca").find_element(By.TAG_NAME,'a').get_attribute('href')
        print(link)
        company = post.find_element(By.CLASS_NAME,"sx2jih0.zcydq84u.zcydq80.iwjz4h0").text
        print("Company: ", company)

        driver2.get(link)
        desc = driver2.find_element(By.CLASS_NAME,"sx2jih0._17fduda0._17fduda7._17fdudah").text
        print(desc)

        # Appending data to dataframe
        data = [company, title, desc]
        data_series = pd.Series(data, index=dataset.columns)
        dataset = dataset.append(data_series, ignore_index=True)

        time.sleep(1)

dataset = dataset.applymap(lambda x: x.encode('unicode_escape').
                     decode('utf-8') if isinstance(x, str) else x)

file_path = os.getcwd()
file_name = 'jobstreet_data_scientist28sept.xlsx'
save_file = os.path.join(file_path, file_name)
dataset.to_excel(save_file,
                 engine='openpyxl',
                 startrow=0,
                 startcol=0,
                 header=True,
                 na_rep='NaN',
                 float_format='%.2f',
                 sheet_name='Sheet1'
                 )


driver.close()
driver2.close()