# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from gui.win1 import Window1
from gui.win2 import Window2
from gui.win3 import Window3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(605, 491)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 151, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 190, 151, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 300, 151, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 80, 241, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 241, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 200, 241, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 300, 241, 51))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "主界面"))
        self.pushButton.setText(_translate("Dialog", "非成对数据训练"))
        self.pushButton_2.setText(_translate("Dialog", "成对数据训练"))
        self.pushButton_3.setText(_translate("Dialog", "使用"))
        self.label.setText(_translate("Dialog", "步骤一：非成对训练阶段"))
        self.label_2.setText(_translate("Dialog", "说明"))
        self.label_3.setText(_translate("Dialog", "步骤二：成对训练阶段"))
        self.label_4.setText(_translate("Dialog", "步骤三：使用训练好的数据"))
        
class Main_Window(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super(Main_Window, self).__init__(parent)
        self.setupUi(self)
        
        self.win1=Window1()
        self.win2=Window2()
        self.win3=Window3()
        
        self.pushButton.clicked.connect(self.show_window1)
        self.pushButton_2.clicked.connect(self.show_window2)
        self.pushButton_3.clicked.connect(self.show_window3)

    
    def show_window1(self):
        self.win1.show()

    def show_window2(self):
        self.win2.show()

    def show_window3(self):
        self.win3.show()
    


if __name__=="__main__":
        app=QApplication(sys.argv)
        main_window=Main_Window()
        main_window.show()
        sys.exit(app.exec_())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

