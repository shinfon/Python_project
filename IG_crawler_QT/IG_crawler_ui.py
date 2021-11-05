# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IG_crawler.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(260, 30, 411, 351))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 221, 91))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Acc_lab = QtWidgets.QLabel(self.frame)
        self.Acc_lab.setGeometry(QtCore.QRect(20, 10, 71, 41))
        self.Acc_lab.setStyleSheet("font: 75 10pt \"微軟正黑體\";")
        self.Acc_lab.setObjectName("Acc_lab")
        self.Pwd_lab = QtWidgets.QLabel(self.frame)
        self.Pwd_lab.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.Pwd_lab.setStyleSheet("font: 75 10pt \"微軟正黑體\";")
        self.Pwd_lab.setObjectName("Pwd_lab")
        self.Acc_input = QtWidgets.QLineEdit(self.frame)
        self.Acc_input.setGeometry(QtCore.QRect(82, 20, 121, 20))
        self.Acc_input.setObjectName("Acc_input")
        self.Pwd_input = QtWidgets.QLineEdit(self.frame)
        self.Pwd_input.setGeometry(QtCore.QRect(82, 50, 121, 20))
        self.Pwd_input.setObjectName("Pwd_input")
        self.Up_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Up_btn.setGeometry(QtCore.QRect(270, 390, 75, 23))
        self.Up_btn.setStyleSheet("font: 11pt \"Hand Me Down S (BRK)\";")
        self.Up_btn.setObjectName("Up_btn")
        self.Down_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Down_btn.setGeometry(QtCore.QRect(590, 390, 75, 23))
        self.Down_btn.setStyleSheet("font: 11pt \"Hand Me Down S (BRK)\";")
        self.Down_btn.setObjectName("Down_btn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 10, 20, 401))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Preview_lab = QtWidgets.QLabel(self.centralwidget)
        self.Preview_lab.setGeometry(QtCore.QRect(260, 10, 411, 20))
        self.Preview_lab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Preview_lab.setAutoFillBackground(False)
        self.Preview_lab.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(128, 221, 237, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 11pt \"Hand Me Down S (BRK)\";")
        self.Preview_lab.setObjectName("Preview_lab")
        self.Logo_title_lab = QtWidgets.QLabel(self.centralwidget)
        self.Logo_title_lab.setGeometry(QtCore.QRect(40, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Vivian")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.Logo_title_lab.setFont(font)
        self.Logo_title_lab.setStyleSheet("font: 20pt \"Vivian\";\n"
"text-decoration: underline;")
        self.Logo_title_lab.setObjectName("Logo_title_lab")
        self.step1_lab = QtWidgets.QLabel(self.centralwidget)
        self.step1_lab.setGeometry(QtCore.QRect(20, 150, 211, 21))
        self.step1_lab.setStyleSheet("font: 75 10pt \"微軟正黑體\";")
        self.step1_lab.setObjectName("step1_lab")
        self.step1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.step1_input.setGeometry(QtCore.QRect(20, 180, 111, 21))
        self.step1_input.setObjectName("step1_input")
        self.step3_lab = QtWidgets.QLabel(self.centralwidget)
        self.step3_lab.setGeometry(QtCore.QRect(20, 260, 191, 21))
        self.step3_lab.setStyleSheet("font: 75 10pt \"微軟正黑體\";")
        self.step3_lab.setObjectName("step3_lab")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(370, 390, 201, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(180, 260, 51, 21))
        self.spinBox.setObjectName("spinBox")
        self.step2_lab = QtWidgets.QLabel(self.centralwidget)
        self.step2_lab.setGeometry(QtCore.QRect(20, 200, 91, 41))
        self.step2_lab.setStyleSheet("font: 75 10pt \"微軟正黑體\";")
        self.step2_lab.setObjectName("step2_lab")
        self.Path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Path_btn.setGeometry(QtCore.QRect(180, 230, 51, 21))
        self.Path_btn.setObjectName("Path_btn")
        self.step2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.step2_input.setGeometry(QtCore.QRect(20, 230, 151, 21))
        self.step2_input.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.step2_input.setObjectName("step2_input")
        self.step2_input.setReadOnly(True)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 350, 221, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.Start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Start_btn.setGeometry(QtCore.QRect(20, 290, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Start_btn.setFont(font)
        self.Start_btn.setStyleSheet("font: 75 20pt \"微軟正黑體\";")
        self.Start_btn.setObjectName("Start_btn")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 130, 211, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart_Stop = QtWidgets.QAction(MainWindow)
        self.actionStart_Stop.setObjectName("actionStart_Stop")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.actionStart_Stop)
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        #設定選擇資料夾按鈕

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IG_Crawler"))
        self.Acc_lab.setText(_translate("MainWindow", "登入帳號 :"))
        self.Pwd_lab.setText(_translate("MainWindow", "登入密碼 :"))
        self.Up_btn.setText(_translate("MainWindow", "Up Page"))
        self.Down_btn.setText(_translate("MainWindow", "Down Page"))
        self.Preview_lab.setText(_translate("MainWindow", "                               Preview"))
        self.Logo_title_lab.setText(_translate("MainWindow", "IG Crawler"))
        self.step1_lab.setText(_translate("MainWindow", "1.輸入關鍵字(不須加上Hashtag)"))
        self.step3_lab.setText(_translate("MainWindow", "3.設定抓取張數"))
        self.step2_lab.setText(_translate("MainWindow", "2.選擇存檔路徑"))
        self.Path_btn.setText(_translate("MainWindow", "存至..."))
        self.Start_btn.setText(_translate("MainWindow", "Start"))
        self.menu.setTitle(_translate("MainWindow", "檔案"))
        self.menu_2.setTitle(_translate("MainWindow", "關於"))
        self.actionStart_Stop.setText(_translate("MainWindow", "Start/Stop"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.action.setText(_translate("MainWindow", "說明"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
