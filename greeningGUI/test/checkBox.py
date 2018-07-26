# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(150, 70, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))

class Main_Window(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(Main_Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_state)
        
    
    def show_state(self):
        state=self.checkBox.isChecked()
        print(state)
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Main_Window()
    window.show()
    sys.exit(app.exec_())
    
    
    
    
    
