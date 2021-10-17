# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Asist_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/dog_tray.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Act_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Act_btn.setGeometry(QtCore.QRect(10, 10, 121, 101))
        self.Act_btn.setStyleSheet("font: 10pt \"AcmeFont\";\n"
"border-color: rgb(104, 104, 104);\n"
"background-color: rgb(204, 204, 204);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Img/dog_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Act_btn.setIcon(icon1)
        self.Act_btn.setIconSize(QtCore.QSize(60, 60))
        self.Act_btn.setAutoDefault(False)
        self.Act_btn.setObjectName("Act_btn")
        self.acc_lab = QtWidgets.QLabel(self.centralwidget)
        self.acc_lab.setGeometry(QtCore.QRect(160, 20, 91, 21))
        self.acc_lab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.acc_lab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acc_lab.setStyleSheet("font: 75 9pt \"微軟正黑體\";")
        self.acc_lab.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.acc_lab.setObjectName("acc_lab")
        self.pwd_lab = QtWidgets.QLabel(self.centralwidget)
        self.pwd_lab.setGeometry(QtCore.QRect(160, 50, 101, 21))
        self.pwd_lab.setAutoFillBackground(True)
        self.pwd_lab.setStyleSheet("font: 75 9pt \"微軟正黑體\";")
        self.pwd_lab.setObjectName("pwd_lab")
        self.time_lab = QtWidgets.QLabel(self.centralwidget)
        self.time_lab.setGeometry(QtCore.QRect(160, 80, 81, 20))
        self.time_lab.setTabletTracking(True)
        self.time_lab.setAutoFillBackground(True)
        self.time_lab.setStyleSheet("font: 75 9pt \"微軟正黑體\";")
        self.time_lab.setObjectName("time_lab")
        self.hr_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.hr_spin.setGeometry(QtCore.QRect(250, 80, 42, 20))
        self.hr_spin.setStyleSheet("font: 9pt \"細明體\";")
        self.hr_spin.setObjectName("hr_spin")
        self.minute_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.minute_spin.setGeometry(QtCore.QRect(320, 80, 42, 22))
        self.minute_spin.setStyleSheet("font: 9pt \"新細明體\";")
        self.minute_spin.setObjectName("minute_spin")
        self.acc_input = QtWidgets.QLineEdit(self.centralwidget)
        self.acc_input.setGeometry(QtCore.QRect(270, 20, 111, 20))
        self.acc_input.setObjectName("acc_input")
        self.pwd_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd_input.setGeometry(QtCore.QRect(270, 50, 111, 20))
        self.pwd_input.setObjectName("pwd_input")
        self.hr_lab = QtWidgets.QLabel(self.centralwidget)
        self.hr_lab.setGeometry(QtCore.QRect(300, 80, 16, 21))
        self.hr_lab.setObjectName("hr_lab")
        self.minute_lab = QtWidgets.QLabel(self.centralwidget)
        self.minute_lab.setGeometry(QtCore.QRect(370, 80, 16, 21))
        self.minute_lab.setObjectName("minute_lab")
        self.msg_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.msg_box.setGeometry(QtCore.QRect(20, 130, 361, 221))
        self.msg_box.setObjectName("msg_box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPIL-防疫聲明助手"))
        self.Act_btn.setText(_translate("MainWindow", "Start!!"))
        self.acc_lab.setText(_translate("MainWindow", "使用者工號:"))
        self.pwd_lab.setText(_translate("MainWindow", "身分末五碼:"))
        self.time_lab.setText(_translate("MainWindow", "選擇時間"))
        self.hr_lab.setText(_translate("MainWindow", "時"))
        self.minute_lab.setText(_translate("MainWindow", "分"))
        self.menu.setTitle(_translate("MainWindow", "功能選單"))
        self.menu_2.setTitle(_translate("MainWindow", "說明"))
        self.action.setText(_translate("MainWindow", "開始/停止"))
        self.action_2.setText(_translate("MainWindow", "退出"))
        self.action_3.setText(_translate("MainWindow", "關於"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())