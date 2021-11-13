import time
import os
import sys
import wget 
import cv2
import requests
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from PyQt5.QtCore import *
import IG_crawler_ui



class IGcrawler():
    def __init__(self,account,password,keyword,quantity,path):
        self.account = account
        self.password = password
        self.src_list = []
        self.keyword = keyword
        self.quantity = quantity
        self.save_as = ""
        self.path = path
        self.img_cnt = 0
        self.link = "https://www.instagram.com/"
        self.driver_path =  "D:/Jhongfu/python/Tools/chromedriver.exe"
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.option.add_argument("--headless")
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

def Show_img(img_index):
    filename = str(img_index)
    img = QImage(filename)
    result = img.scaled(ui.preview_area_lab.width(),ui.preview_area_lab.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
    ui.preview_area_lab.setPixmap(QPixmap.fromImage(result))

def slot_btn_chooseDir():
    dir_choose = QtWidgets.QFileDialog.getExistingDirectory(MainWindow,'選擇資料夾',"C:\\")
    if dir_choose == "":
        ui.step2_input.setText("請點選路徑")
        return
    ui.step2_input.setText(dir_choose)


def message_pop(status_code):
    msg_acc = "請輸入帳號!"
    msg_pwd = "請輸入密碼!"
    msg_path = "請選擇儲存路徑!"

    if status_code == 1:
        QMessageBox.critical(MainWindow,"輸入錯誤",msg_acc)
    elif status_code == 2:
        QMessageBox.critical(MainWindow,"輸入錯誤",msg_pwd)
    elif status_code == 3:
        QMessageBox.critical(MainWindow,"輸入錯誤",msg_path)

def Is_path_chooson(path):
        if (path != False or path != None):
            return str(path)
        else:
            message_pop(3)

def Is_AccPwd(acc,pwd):
    if (acc != False or acc != None ):
        if (pwd != False or pwd != None):
            return str(acc),str(pwd)
        else:
            message_pop(2)
            return 1
    else:
        message_pop(1)
        return 1


def down_page():
    global img_path
    global img_index
    
    if  img_index < (int(len(img_path))-1):
        img_index += 1
        if img_path[img_index]:
            Show_img(img_path[img_index])    

def up_page():
    global img_path
    global img_index
    if img_index > 0:
        img_index -= 1
        if img_path[img_index]:
            Show_img(img_path[img_index])


def main_flow():
    global img_path
    global img_index
    img_cnt = 0
    acc_input,pwd_input = Is_AccPwd(ui.Acc_input.text(),ui.Pwd_input.text())
    ui.progressBar.setMaximum(int(ui.spinBox.text()))
    ui.progressBar.setMinimum(int(0))
    crawler = IGcrawler(acc_input,pwd_input,"#" + str(ui.step1_input.text()),int(ui.spinBox.text()),ui.step2_input.text())
    crawler.login_acc()
    crawler.query_keyword()
    crawler.get_data_list()
    crawler.path_check()
    # WorkThread = Thread()
    # crawler.start()
    print("共計 {:d} 筆資料,開始下載...".format(len(crawler.src_list)))
    for index in crawler.src_list:
        crawler.save_as = os.path.join(crawler.path,crawler.keyword,crawler.keyword + str(img_cnt) + '.jpg')
        with open(crawler.save_as,'wb') as f:
            f.write(requests.get(index).content)
        # wget.download(index,crawler.save_as)  
        if crawler.save_as:
            img_path.append(crawler.save_as)
        Show_img(img_path[img_cnt]) 
        img_index = img_cnt
        img_cnt += 1
     

class Thread(QThread):
    def __init__(self):
        super(Thread,self).__init__()

    def run(self):
        pass
        


if __name__ == "__main__":
    img_path = []
    img_index = 0
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = IG_crawler_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Path_btn.clicked.connect(slot_btn_chooseDir)
    ui.Start_btn.clicked.connect(main_flow)
    ui.Up_btn.clicked.connect(up_page)
    ui.Down_btn.clicked.connect(down_page)
    ui.Pwd_input.setEchoMode(QLineEdit.Password)
    MainWindow.setWindowFlags(QtCore.Qt.Window)
    ui.progressBar.setValue(0)
    MainWindow.show()
    
    sys.exit(app.exec_())
    
# self.ThreadRun.img_cnt_signal.connect(self.geted_index)
# self.ThreadRun.pic_path_signal.connect(self.geted_path)
# self.img_cnt_signal = pyqtSignal(int)
# self.pic_path_signal = pyqtSignal(list)

#     # self.img_cnt_signal.emit(self.img_cnt)
# self.img_index = self.img_cnt
# self.img_cnt += 1
# self.pic_path_signal.emit(self.img_path)
    