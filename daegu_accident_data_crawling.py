from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import openpyxl
import os
import time
from  datetime import date

path="C:/WebDriver/chromedriver"
service = Service(executable_path=path)
driver=webdriver.Chrome(path)
col_name=['daegu']
dataset=pd.DataFrame(columns=col_name)

for i in range (1,503):
    url="http://car.daegu.go.kr/metro/outbreak?incidentcode=1&pageIndex=%d&searchFromDate=2020-01-01&searchToDate=2022-11-21"%i
    driver.get(url)
    daegu = driver.find_element(By.XPATH, '//*[@id="board"]/div[2]/table').text
    data = daegu.split("\n")
    data_series = pd.Series(data)
    dataset = dataset.append(data_series, ignore_index=True)
    time.sleep(1)

dataset=dataset.drop(['daegu'],axis=1)
dataset=dataset.transpose()
dataset=pd.Series(dataset.values.ravel("F"))
file_path = os.getcwd()
file_name = 'daegufulldata1.xlsx'
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

driver.quit()