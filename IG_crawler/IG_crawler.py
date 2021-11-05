import time
import os
import sys
import wget 
import cv2
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class IGcrawler():
    def __init__(self,account,password,keyword,quantity,path):
        self.account = account
        self.password = password
        self.src_list = []
        self.keyword = keyword
        self.quantity = quantity
        self.path = path
        self.link = "https://www.instagram.com/"
        self.driver_path =  "D:/Jhongfu/python/Tools/chromedriver.exe"
        self.option = webdriver.ChromeOptions().add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.driver = webdriver.Chrome(self.driver_path,chrome_options=self.option)

    def login_acc(self):
        self.driver.get(self.link)
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.NAME,"username"))
        )
        self.acc = self.driver.find_element_by_name("username")
        self.pwd = self.driver.find_element_by_name("password")
        self.acc.clear()
        self.pwd.clear()
        self.acc.send_keys(self.account)
        self.pwd.send_keys(self.password)
        self.login = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button'))
        )
        self.login.click()

    def query_keyword(self):
        self.query = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
        )
        self.query.clear()
        self.query.send_keys(self.keyword)
        self.query.send_keys(Keys.RETURN)
        
        self.sel_1 = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[1]/div'))
        )
        self.move_action = ActionChains(self.driver)
        self.move_action.move_to_element(self.sel_1)
        self.move_action.click()
        self.move_action.perform()
    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight-20);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def path_check(self):
        if not os.path.isdir(os.path.join(self.path,self.keyword)):
            os.mkdir(os.path.join(self.path,self.keyword))

    def download_list_data(self):
        self.cnt = 0
        self.path_check()
        print("共計 {:d} 筆資料,開始下載...".format(len(self.src_list)))
        for index in self.src_list:
            self.save_as = os.path.join(self.path,self.keyword,self.keyword + str(self.cnt) + '.jpg')
            wget.download(index,self.save_as)
            # time.sleep(1)
            self.cnt += 1

    def get_data_list(self):
        self.lis_quan =0
        self.imgs = []
        #video class="tWeCl"
        
        print("開始獲取資料列表....\n")

        while(self.lis_quan < self.quantity):
            time.sleep(4)
            self.imgs.extend(self.driver.find_elements_by_class_name("FFVAD"))

            # imgs = WebDriverWait(driver.current_url,10).until(
            #     EC.presence_of_all_elements_located((By.CLASS_NAME,"FFVAD"))
            # )
            print("預計獲取:{:s} 筆...目前共獲取:{:s} 筆 \n".format(str(self.quantity),str(self.lis_quan)))
            for index in range(len(self.imgs)):
                img_url = self.imgs.pop().get_attribute("src")
                if (img_url != None) & (img_url not in self.src_list):
                    if len(self.src_list) < self.quantity:
                        self.src_list.append(img_url)
                    else:
                        break
    
            self.scroll_page()
            self.lis_quan = len(self.src_list)


def main_flow():
    crawler = IGcrawler("yourAccount","yourPassword","#yourKeyword",100,"yourSavePath")
    crawler.login_acc()
    crawler.query_keyword()
    crawler.get_data_list()
    crawler.download_list_data()

if __name__ == "__main__":
     main_flow()




    