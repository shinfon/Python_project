from os import sep
import sys
import re
import time
import tkinter as tk
from tkinter import messagebox   
from tkinter import *
from tkinter.constants import DISABLED, FALSE, LEFT, TRUE, W
import apscheduler.schedulers.background
from pkg_resources import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from apscheduler.schedulers.background import *

div_btn = True

def main_flow():
    driver_path = "chromedriver/chromedriver.exe"
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(driver_path, chrome_options=option)
    acc_input=acc.get()
    pwd_input=pwd.get()
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
            tb.config(state=tk.NORMAL)
            tb.insert(tk.INSERT,"==============執行結果=============\n")
            tb.insert(tk.END, result.text + "\n" )
            tb.config(state=tk.DISABLED)
            driver.quit()

        else:
            print("not selected!!")
    else:
        print("not selected!!")

def btn_action():
    global div_btn
    hour_input = int(spinbox_1.get())
    minute_input = int(spinbox_2.get())
    sche = apscheduler.schedulers.background.BackgroundScheduler()
    sche.add_job(main_flow,"cron",hour=hour_input,minute=minute_input,id='jobid')
    
    def Run_inschedul():
        tb.config(state=tk.NORMAL)
        tb.insert(tk.INSERT,"==============運行中==============\n")
        tb.insert(tk.INSERT,"預計自動聲明時間為每日 :"+str(hour_input) + "時" + str(minute_input) + "分\n")
        tb.insert(tk.INSERT,"==================================\n")
        tb.config(state=tk.DISABLED)
        acc.config(state="readonly")
        pwd.config(state="readonly")
        sche.start()

    def stop_schedul():
        sche.remove_job('jobid')
        tb.config(state=tk.NORMAL)
        tb.insert(tk.INSERT,"==============終止運行============\n")
        tb.config(state=tk.DISABLED)
        acc.config(state="normal")
        pwd.config(state="normal")        

    if div_btn:
        if input_check() == 0:
            Run_inschedul()
            div_btn = FALSE 
            btn_sta.set("Stop!!")
    else:
        stop_schedul()
        div_btn = TRUE
        btn_sta.set("Start!!")
    
def message_pop(stat):
    msg_acc="請輸入正確工號格式!(6碼數字)"
    msg_pwd="請輸入正確身分證後5碼格式!"
    if stat == 1:
        messagebox.showerror(title="輸入錯誤",message=msg_acc)
    elif stat == 2:
        messagebox.showerror(title="輸入錯誤",message=msg_pwd)
    
        

def msg_info():
    msg = '''請輸入工號與身分證後5碼,依選單設定時間後按下Start鍵開始定時聲明
        此工具僅使用在個人認知狀況與聲明內容無異時使用
        若自身情形與申明內容不符,請手動至網站聲明。
        有任何問題請聯繫作者:JhongfuChen'''
    messagebox.showinfo(title="關於本程式",message=msg)

def end_pro():
    sys.exit(0)

def input_check():
    acc_check = acc.get()
    pwd_check = pwd.get()
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



#建立主視窗
win = tk.Tk()
win.iconbitmap("img/dog_tray.ico")
win.geometry("270x330")
win.title("SPIL-防疫聲明助手")
#程式區塊1
frame1=tk.Frame(win)
frame1.pack(side="top",pady=2)
#選單1
menubtn1 = tk.Menubutton(frame1,text="功能選單")
menubtn1_menu = tk.Menu(menubtn1,tearoff=0)
menubtn1.config(menu=menubtn1_menu)
menubtn1_menu.add_command(label="開始/停止",command=btn_action)
menubtn1_menu.add_command(label="結束程式",command=end_pro)
# menubtn1_menu.add_command(label="縮小視窗",command=)
menubtn1.grid(row=0,column=0,columnspan=1,sticky="w")
#選單2
menubtn2 = tk.Menubutton(frame1,text="說明")
menubtn2_menu = tk.Menu(menubtn2,tearoff=0)
menubtn2.config(menu=menubtn2_menu)
menubtn2_menu.add_command(label="關於",command=msg_info)
menubtn2.grid(row=0,column=1,sticky="w")
#程式區塊2
frame2 = tk.Frame(win)
frame2.pack(side="top")
#標籤、輸入文字區塊
acc_value = tk.StringVar
pwd_value = tk.StringVar
label_1 = tk.Label(frame2,text="使用者工號 :")
label_2 = tk.Label(frame2,text="身分證末5碼:")
label_3 = tk.Label(frame2,text="選擇時間(時/分):")
label_1.grid(row=0,column=0)
label_2.grid(row=1,column=0)
label_3.grid(row=2,column=0)
acc = tk.Entry(frame2,textvariable=acc_value)
pwd = tk.Entry(frame2,textvariable=pwd_value)
acc.grid(row=0,column=1)
pwd.grid(row=1,column=1)
spinbox_1 = tk.Spinbox(frame2,from_=00,to=23,state="readonly",width=8,)
spinbox_2 = tk.Spinbox(frame2,from_=00,to=59,state="readonly",width=8)
spinbox_1.grid(row=2,column=1,columnspan=2,sticky="w")
spinbox_2.grid(row=2,column=1,sticky="e")
#程式區塊3
frame3 = tk.Frame(win)
frame3.pack()
#按鈕
btn_sta = tk.StringVar()
img = tk.PhotoImage(file="img/dog_btn.png")
btnimg = img.subsample(2,2)
Start_btn = tk.Button(frame3,textvariable=btn_sta,image=btnimg,command=btn_action,compound=LEFT,width="260")
btn_sta.set("Start!!")
Start_btn.configure(font=("Courier", 16, "italic"),bg="#E0E0E0")
Start_btn.grid(row=1,column=0,rowspan=2,sticky="s")
#程式區塊4
frame4 = tk.Frame(win)
frame4.pack()
#底部文字區、滾動條
sb = tk.Scrollbar(frame4)
tb = tk.Text(frame4,yscrollcommand=sb.set,width="35",height="10")
tb.pack(side="left",fill="y")
sb.pack(side="right",fill="both")
sb.config(command=tb.yview())
win.mainloop()
