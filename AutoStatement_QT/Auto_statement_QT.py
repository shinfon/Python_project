from os import sep
import sys
import re
import time
import tkinter as tk
from tkinter import messagebox   
from tkinter import *
from tkinter.constants import DISABLED, FALSE, LEFT, TRUE, W
from apscheduler import schedulers
import apscheduler.schedulers.background
from pkg_resources import *
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from apscheduler import schedulers
from apscheduler.schedulers.background import *
from apscheduler.schedulers.qt import QtScheduler
from PyQt5.QtWidgets import QApplication,QMainWindow, QMessageBox
from PyQt5 import QtCore , QtGui , QtWidgets
import Asist_UI

div_btn = True

def main_flow():
    
    driver_path = "chromedriver/chromedriver.exe"
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    option.add_argument("--headless")
    driver = webdriver.Chrome(driver_path, chrome_options=option)
    acc_input=Ui.acc_input.text()
    pwd_input=Ui.pwd_input.text()
    result = ""


    driver.get("https://www.spil.com.tw/Questionnaire/Login.aspx")
    acc_point = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cphMain_cpContent_tbEmpno"))
    )
    pwd_point = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cphMain_cpContent_tbIDdigits"))
    )

    acc_point.clear()
    pwd_point.clear()
    acc_point.send_keys(str(acc_input))
    pwd_point.send_keys(str(pwd_input))
    time.sleep(2)
    login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cphMain_cpContent_btnLogin"]'))
    )

    login.click()

    agreed = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphMain_cpContent_btnAgree"))
    )
    agreed.click()

    radio_1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphMain_cpContent_rbSymptonN"))
    )
    radio_2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphMain_cpContent_rbSituationN"))
    )
    radio_3 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cphMain_cpContent_rbContactN"))
    )


    radio_1.click()
    radio_2.click()
    radio_3.click()

    rad1_sta = radio_1.is_selected()
    rad2_sta = radio_2.is_selected()
    rad3_sta = radio_3.is_selected()


    if (rad1_sta and rad2_sta):
        if rad3_sta:
            time.sleep(1)
            confirm = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "cphMain_cpContent_confirm"))
            )
            #confirm = driver.find_element_by_id("cphMain_cpContent_confirm")
            confirm.click()
            time.sleep(1)
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, "cphMain_cpContent_lblDialogContent"))
            )
            Ui.msg_box.append("============執行結果============\n")
            Ui.msg_box.append(result.text + "\n")
            driver.quit()

        else:
            print("not selected!!")
    else:
        print("not selected!!")

def btn_action():
    global div_btn
    hour_input = int(Ui.hr_spin.value())
    minute_input = int(Ui.minute_spin.value())
    sche = apscheduler.schedulers.qt.QtScheduler()
    sche.add_job(main_flow,"cron",hour=hour_input,minute=minute_input,id='jobid')
    def Run_inschedul():
        Ui.msg_box.append("運行中.....\n")
        Ui.msg_box.append("預計自動聲明時間為每日 :"+str(hour_input) + "時" + str(minute_input) + "分\n")
        Ui.msg_box.append("等待任務觸發...\n")
        Ui.acc_input.setReadOnly(TRUE)
        Ui.pwd_input.setReadOnly(TRUE)
        Ui.hr_spin.setReadOnly(TRUE)
        Ui.minute_spin.setReadOnly(TRUE)
        sche.start()


    def stop_schedul():
        sche.remove_job('jobid')
        Ui.msg_box.append(".........終止運行!\n")
        Ui.acc_input.setReadOnly(FALSE)
        Ui.pwd_input.setReadOnly(FALSE)
        Ui.hr_spin.setReadOnly(FALSE)
        Ui.minute_spin.setReadOnly(FALSE)

    if div_btn:
        if input_check() == 0:
            Run_inschedul()
            div_btn = FALSE 
            Ui.Act_btn.setText("Stop!!")
    else:
        stop_schedul()
        div_btn = TRUE
        Ui.Act_btn.setText("Start!!")
    
def message_pop(stat):
    msg_acc="請輸入正確工號格式!(6碼數字)"
    msg_pwd="請輸入正確身分證後5碼格式!"
    if stat == 1:
        QMessageBox.critical(MainWindow,"輸入錯誤",msg_acc)

    elif stat == 2:
        QMessageBox.critical(MainWindow,"輸入錯誤",msg_pwd)

    
        

def msg_info():
    msg = '''請輸入工號與身分證後5碼,依選單設定時間後按下Start鍵開始定時聲明
        此工具僅使用在個人認知狀況與聲明內容無異時使用
        若自身情形與申明內容不符,請手動至網站聲明。
        有任何問題請聯繫作者:JhongfuChen'''
    QMessageBox.about(MainWindow,"關於本程式",msg)

def end_pro():
    sys.exit(0)

def input_check():
    acc_check=Ui.acc_input.text()
    pwd_check=Ui.pwd_input.text()
    acc_stander = r'\d{6}'
    pwd_stander = r'\d{5}'
    acc_feedbk = re.match(acc_stander,acc_check)
    pwd_feedbk = re.match(pwd_stander,pwd_check)
    if ( acc_feedbk == None or pwd_feedbk == None):
        if acc_feedbk == None:
            message_pop(1)
            return 1
        elif pwd_feedbk == None:
            message_pop(2)
            return 1
    else:
        return 0




class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self,MainWindow,parent=None):
        super(TrayIcon, self).__init__(parent)
        self.ui = MainWindow
        self.createMenu()
    
    def createMenu(self):
        self.menu = QtWidgets.QMenu()
        self.showAction1 = QtWidgets.QAction("開啟", self, triggered=self.show_window)
        # self.showAction2 = QtWidgets.QAction("顯示資訊", self,triggered=self.showMsg)
        self.quitAction = QtWidgets.QAction("退出", self, triggered=self.quit)
        self.menu.addAction(self.showAction1)
        # self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

        #設定圖案
        self.setIcon(QtGui.QIcon("img/dog_tray.ico"))
        self.icon = self.MessageIcon()

        #連結滑鼠點擊訊號
        self.activated.connect(self.onIconClicked)

    def showMsg(self):
        self.showMessage("Message", "skr at here", self.icon)

    def show_window(self):
        self.ui.showNormal()
        self.ui.activateWindow()
        
 
    def quit(self):
        self.setVisible(False)  #關閉殘留圖案
        QtWidgets.qApp.quit()

    #鼠标点击icon传递的信号会带有一个整形的值,1是表示单击右键,2是双击,3是单击左键,4是用鼠标中键点击
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3:
            # self.showMessage("Message", "skr at here", self.icon)
            if self.ui.isMinimized() or not self.ui.isVisible():

                self.ui.showNormal()
                self.ui.activateWindow()
                self.ui.setWindowFlags(QtCore.Qt.Window)
                self.ui.show()
            else:
                #若不是最小化,则最小化
                self.ui.close()
                # self.ui.showMinimized()
                # self.ui.setWindowFlags(QtCore.Qt.SplashScreen)
                # self.ui.show()


class Dialog(QtWidgets.QMainWindow):
    def __init__(self,MainWindow,parent=None):
        super(Dialog, self).__init__(parent)
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, self.tr("提示"), self.tr("是否確定退出"), QtWidgets.QMessageBox.NoButton, self)
        yr_btn = reply.addButton(self.tr("退出程式"), QtWidgets.QMessageBox.YesRole)
        reply.addButton(self.tr("最小化至系統背景"), QtWidgets.QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yr_btn:
            event.accept()
            # QtWidgets.qApp.quit()
            sys.exit(app.exec_())
        else:
            event.ignore()
            # 最小化到托盘
            MainWindow.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
            MainWindow.showMinimized()
            
        
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
Ui = Asist_UI.Ui_MainWindow
MainWindow = Dialog(MainWindow)
Ui.setupUi(Ui,MainWindow)

MainWindow.setWindowFlags(QtCore.Qt.Window)

Ui.hr_spin.setMaximum(23)
Ui.hr_spin.setMinimum(0)
Ui.minute_spin.setMaximum(59)
Ui.minute_spin.setMinimum(0)
Ui.Act_btn.clicked.connect(btn_action)
Ui.action.triggered.connect(btn_action)
Ui.action_2.triggered.connect(end_pro)
Ui.action_3.triggered.connect(msg_info)
MainWindow.show()

ti = TrayIcon(MainWindow)
ti.show()

sys.exit(app.exec_())