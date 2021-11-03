import time
import os
import wget 
import requests
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import json


keyword = "#ahegao"
data_path = "D:/Jhongfu/python/data"
# roll_cnt = 10
pic_quantity = 80
src_list = []
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# option.add_argument("--headless")
Driver_Path = "D:/Jhongfu/python/Tools/chromedriver.exe"

driver = webdriver.Chrome(Driver_Path,chrome_options=option)
driver.get("https://www.instagram.com/")

def login_acc():
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME,"username"))
    )
    acc = driver.find_element_by_name("username")
    pwd = driver.find_element_by_name("password")
    acc.clear()
    pwd.clear()
    acc.send_keys("bboyjhongfu")
    pwd.send_keys("blue337home")
    # pwd.send_keys(Keys.RETURN)
    # WebDriverWait(driver,10).until(
    #     EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button'))
    # )
    login = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button'))
    )
    login.click()
    # action_login_btn = ActionChains(driver)
    # action_login_btn.move_to_element(login)
    # action_login_btn.click()

def query_keyword():
    query = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
    )
    query.clear()
    query.send_keys(keyword)
    query.send_keys(Keys.RETURN)
    sel_1 = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[1]/div'))
    )
    move_action = ActionChains(driver)
    move_action.move_to_element(sel_1)
    move_action.click()
    move_action.perform()

def scroll_page():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-20);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def path_check():
    if not os.path.isdir(os.path.join(data_path,keyword)):
       os.mkdir(os.path.join(data_path,keyword))


def download_list_data():
    global src_list
    cnt = 0
    path_check()
    print("共計 {:d} 筆資料,開始下載...".format(len(src_list)))
    for index in src_list:
        save_as = os.path.join(data_path,keyword,keyword + str(cnt) + '.jpg')
        wget.download(index,save_as)
        time.sleep(1)
        cnt += 1


def get_data_list():
    global src_list
    lis_quan =0
    cnt = 0
    imgs = []
    #video class="tWeCl"
    
    print("開始獲取資料列表....\n")

    while(lis_quan < pic_quantity):
        time.sleep(4)
        imgs.extend(driver.find_elements_by_class_name("FFVAD"))

        # imgs = WebDriverWait(driver.current_url,10).until(
        #     EC.presence_of_all_elements_located((By.CLASS_NAME,"FFVAD"))
        # )
        print("預計獲取:{:s} 筆...目前共獲取:{:s} 筆 \n".format(str(pic_quantity),str(lis_quan)))
        for index in range(len(imgs)):
            img_url = imgs.pop().get_attribute("src")
            if (img_url != None) & (img_url not in src_list):
                if len(src_list) < pic_quantity:
                    src_list.append(img_url)
                else:
                    break
  
        scroll_page()
        lis_quan = len(src_list)
        cnt += 1
    
    

login_acc()
query_keyword()
get_data_list()
download_list_data()




    