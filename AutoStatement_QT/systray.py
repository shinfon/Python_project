from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self,MainWindow,parent=None):
        super(TrayIcon, self).__init__(parent)
        self.ui = MainWindow
        self.createMenu()
    
    def createMenu(self):
        self.menu = QtWidgets.QMenu()
        self.showAction1 = QtWidgets.QAction("启动", self, triggered=self.show_window)
        self.showAction2 = QtWidgets.QAction("显示通知", self,triggered=self.showMsg)
        self.quitAction = QtWidgets.QAction("退出", self, triggered=self.quit)
        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

        #设置图标
        self.setIcon(QtGui.QIcon("c:\\My_World\\gitee_code\\qt_toolkit\\hello_world\\sys-user.png"))
        self.icon = self.MessageIcon()

        #把鼠标点击图标的信号和槽连接
        self.activated.connect(self.onIconClicked)

    def showMsg(self):
        self.showMessage("Message", "skr at here", self.icon)

    def show_window(self):
        #若是最小化&#xff0c;则先正常显示窗口&#xff0c;再变为活动窗口&#xff08;暂时显示在最前面&#xff09;
        self.ui.showNormal()
        self.ui.activateWindow()
        
 
    def quit(self):
        QtWidgets.qApp.quit()

    #鼠标点击icon传递的信号会带有一个整形的值&#xff0c;1是表示单击右键&#xff0c;2是双击&#xff0c;3是单击左键&#xff0c;4是用鼠标中键点击
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3:
            # self.showMessage("Message", "skr at here", self.icon)
            if self.ui.isMinimized() or not self.ui.isVisible():
                #若是最小化&#xff0c;则先正常显示窗口&#xff0c;再变为活动窗口&#xff08;暂时显示在最前面&#xff09;
                self.ui.showNormal()
                self.ui.activateWindow()
                self.ui.setWindowFlags(QtCore.Qt.Window)
                self.ui.show()
            else:
                #若不是最小化&#xff0c;则最小化
                self.ui.showMinimized()
                self.ui.setWindowFlags(QtCore.Qt.SplashScreen)
                self.ui.show()
                # self.ui.show()

class Dialog(QtWidgets.QMainWindow):
    def __init__(self,MainWindow,parent=None):
        super(Dialog, self).__init__(parent)
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, self.tr("提示"), self.tr("汝妻子我养之&#xff0c;汝勿虑之。\n 汝特么确定要退出吗&#xff1f;"), QtWidgets.QMessageBox.NoButton, self)
        yr_btn = reply.addButton(self.tr("是的我要退出"), QtWidgets.QMessageBox.YesRole)
        reply.addButton(self.tr("最小化到托盘"), QtWidgets.QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yr_btn:
            event.accept()
            QtWidgets.qApp.quit()
            # sys.exit(app.exec_())
        else:
            event.ignore()
            # 最小化到托盘
            MainWindow.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
            MainWindow.showMinimized()

        # 默认直接调用QMessageBox.question 弹出询问的方法
        # reply = QtWidgets.QMessageBox.question(self,
        #                                        &#39;本程序&#39;,
        #                                        "是否要退出程序&#xff1f;",
        #                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        # if reply = QtWidgets.QMessageBox.Yes:
        #     event.accept()
        # elif reply = QtWidgets.QMessageBox.No:
        #     event.ignore()
        #     MainWindow.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
        #     MainWindow.showMinimized()
        # else:
        #     # 最小化到托盘
        #     MainWindow.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint)
        #     MainWindow.showMinimized()