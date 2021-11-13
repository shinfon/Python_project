import time
import os
import sys
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
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from PyQt5.QtCore import *
from IG_crawler_ui import Ui_MainWindow



class IGcrawler(Ui_MainWindow):

    def __init__(self):
        # super(IGcrawler,self).__init__() 
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.setWindowFlags(QtCore.Qt.Window)
        self.Start_btn.clicked.connect(self.Thread_Run)
        self.Up_btn.clicked.connect(self.up_page)
        self.Down_btn.clicked.connect(self.down_page)
        self.Path_btn.clicked.connect(self.slot_btn_chooseDir)
        self.action.triggered.connect(self.msg_info)
        self.actionStart_Stop.triggered.connect(self.Thread_Run)
        self.actionExit.triggered.connect(self.end_pro)
        self.Pwd_input.setEchoMode(QLineEdit.Password)
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        self.dir_choose = ""
        self.geted_index = 0
        self.geted_path = []

    def slot_btn_chooseDir(self):
        self.dir_choose = QtWidgets.QFileDialog.getExistingDirectory(self.MainWindow,'選擇資料夾',"C:\\")
        if self.dir_choose == "":
            self.step2_input.setText("請點選路徑")
            return
        self.step2_input.setText(self.dir_choose)
    

    def msg_info(self):
        msg = '''
            本程式自動抓取Instagram HashTage關鍵字圖片,
            輸入資訊後,點擊"Star"鈕開始。
            隨設定抓取照片張數影響執行時間...
            -------沒有任何帳號密碼會被記住-------
            有任何問題請聯繫作者:John'''
        QMessageBox.about(self.MainWindow,"關於本程式",msg)
    
    def end_pro(self):
        sys.exit(0)

    def get_index(self,nIndex):
        self.geted_index = nIndex

    def get_path(self,lisIndex):
        self.geted_path = lisIndex
    
    def Status_show(self,string):
        self.textBrowser.append(string)

    def set_ProcessTotal(self,process_total):
        self.progressBar.setMaximum(process_total)

    def Download_peocess(self,process):
        self.progressBar.setValue(process)


    def down_page(self):
        if  self.geted_index < (int(len(self.geted_path))-1):
            self.geted_index += 1
            if self.geted_path[self.geted_index]:
                self.Show_img(self.geted_path[self.geted_index])    

    def up_page(self):
        if self.geted_index > 0:
            self.geted_index -= 1
            if self.geted_path[self.geted_index]:
                self.Show_img(self.geted_path[self.geted_index])
    
    def Show_img(self,img_index):
        filename = str(img_index)
        img = QImage(filename)
        result = img.scaled(ui.preview_area_lab.width(),ui.preview_area_lab.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        ui.preview_area_lab.setPixmap(QPixmap.fromImage(result))

    def Thread_Run(self):
        self.Acc_input.setReadOnly(TRUE)
        self.Pwd_input.setReadOnly(TRUE)
        self.step1_input.setReadOnly(TRUE)
        self.spinBox.setReadOnly(TRUE)
        self.step2_input.setReadOnly(TRUE)
        self.ThreadRun = Thread()
        self.ThreadRun.img_cnt_signal.connect(self.get_index)
        self.ThreadRun.pic_path_signal.connect(self.get_path)
        self.ThreadRun.getdata_Info_signal.connect(self.Status_show)
        self.ThreadRun.process_total_signal.connect(self.set_ProcessTotal)
        self.ThreadRun.download_progress_signal.connect(self.Download_peocess)

        self.ThreadRun.start()
        self.Acc_input.setReadOnly(FALSE)
        self.Pwd_input.setReadOnly(FALSE)
        self.step1_input.setReadOnly(FALSE)
        self.spinBox.setReadOnly(FALSE)
        self.step2_input.setReadOnly(FALSE)



     

class Thread(QThread):
    img_cnt_signal = pyqtSignal(int)
    pic_path_signal = pyqtSignal(list)
    getdata_Info_signal = pyqtSignal(str)
    download_progress_signal = pyqtSignal(int)
    process_total_signal = pyqtSignal(int)
    def __init__(self):
        super(Thread,self).__init__()
        self.account = ui.Acc_input.text()
        self.password = ui.Pwd_input.text()
        self.src_list = []
        self.keyword = "#" + str(ui.step1_input.text())
        self.quantity = int(ui.spinBox.text())
        self.save_as = ""
        self.path = ui.step2_input.text()
        self.img_path = []
        self.img_cnt = 0
        self.img_index = 0
        
        
        self.link = "https://www.instagram.com/"
        self.driver_path =  "D:/Jhongfu/python/Tools/chromedriver.exe"
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.option.add_argument("--headless")
        self.driver = webdriver.Chrome(self.driver_path,chrome_options=self.option)

    def login_acc(self):
        self.getdata_Info_signal.emit("取得頁面資訊中....\n")
        self.process_total_signal.emit(self.quantity)
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
        self.getdata_Info_signal.emit("登入成功..取得關鍵字資訊....\n")
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
        # print("開始獲取資料列表....\n")
        self.getdata_Info_signal.emit("開始獲取資料列表....\n")
        while(self.lis_quan < self.quantity):
            time.sleep(4)
            self.imgs.extend(self.driver.find_elements_by_class_name("FFVAD"))

            # imgs = WebDriverWait(driver.current_url,10).until(
            #     EC.presence_of_all_elements_located((By.CLASS_NAME,"FFVAD"))
            # )
            # print("預計獲取:{:s} 筆...目前共獲取:{:s} 筆 \n".format(str(self.quantity),str(self.lis_quan)))
            self.getdata_Info_signal.emit("預計獲取:{:s} 筆...目前共獲取:{:s} 筆 \n".format(str(self.quantity),str(self.lis_quan)))
            for self.index in range(len(self.imgs)):
                self.img_url = self.imgs.pop().get_attribute("src")
                if (self.img_url != None) & (self.img_url not in self.src_list):
                    if len(self.src_list) < self.quantity:
                        self.src_list.append(self.img_url)
                    else:
                        break
    
            self.scroll_page()
            self.lis_quan = len(self.src_list)

    def Download_data(self):
        # print("共計 {:d} 筆資料,開始下載...".format(len(self.src_list)))
        self.getdata_Info_signal.emit("共計 {:d} 筆資料,開始下載...".format(len(self.src_list)))
        for index in self.src_list:
            self.save_as = os.path.join(self.path,self.keyword,self.keyword + str(self.img_cnt) + '.jpg')
            with open(self.save_as,'wb') as f:
                f.write(requests.get(index).content)
            # wget.download(index,self.save_as)  
            if self.save_as:
                self.img_path.append(self.save_as)
            self.Show_img(self.img_path[self.img_cnt]) 
            self.img_index = self.img_cnt
            self.img_cnt += 1
            self.download_progress_signal.emit(self.img_cnt)
        self.img_cnt_signal.emit(self.img_cnt)
        self.pic_path_signal.emit(self.img_path)
        self.getdata_Info_signal.emit("圖片抓取完成!")

    def down_page(self):
        if  self.img_index < (int(len(self.img_path))-1):
            self.img_index += 1
            if self.img_path[self.img_index]:
                self.Show_img(self.img_path[self.img_index])    

    def up_page(self):
        if self.img_index > 0:
            self.img_index -= 1
            if self.img_path[self.img_index]:
                self.Show_img(self.img_path[self.img_index])
    
    def Show_img(self,img_index):
        filename = str(img_index)
        img = QImage(filename)
        result = img.scaled(ui.preview_area_lab.width(),ui.preview_area_lab.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        ui.preview_area_lab.setPixmap(QPixmap.fromImage(result))




    def run(self):
        self.login_acc()
        self.query_keyword()
        self.get_data_list()
        self.path_check()
        self.Download_data()
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = IGcrawler()
    ui.MainWindow.show()
    sys.exit(app.exec_())
    




    