# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unpair.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
import sys
from test.train_def import train
from data.prepare_data import prepare_data_for_unpair_training

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(902, 688)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(17, 10, 221, 51))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(417, 10, 151, 51))
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(17, 90, 221, 61))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(420, 100, 121, 41))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 290, 91, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(610, -10, 251, 161))
        self.checkBox.setObjectName("checkBox")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 360, 91, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(40, 430, 91, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(40, 490, 91, 41))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_7.setGeometry(QtCore.QRect(370, 300, 91, 41))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_8.setGeometry(QtCore.QRect(370, 370, 91, 41))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_9.setGeometry(QtCore.QRect(370, 440, 91, 41))
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_10.setGeometry(QtCore.QRect(370, 500, 91, 41))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_11.setGeometry(QtCore.QRect(620, 300, 91, 41))
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_12.setGeometry(QtCore.QRect(620, 370, 91, 41))
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_13.setGeometry(QtCore.QRect(620, 440, 91, 41))
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_14.setGeometry(QtCore.QRect(620, 500, 91, 41))
        self.textEdit_14.setObjectName("textEdit_14")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 580, 191, 61))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(410, 230, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 290, 211, 51))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 370, 181, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(150, 440, 161, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(150, 500, 181, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(480, 310, 141, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(480, 380, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(490, 450, 54, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(490, 520, 54, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(750, 310, 54, 12))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(750, 380, 54, 12))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(750, 460, 54, 12))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(750, 520, 54, 12))
        self.label_15.setObjectName("label_15")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 110, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "非成对训练"))
        self.label.setText(_translate("Dialog", "输入数据路径(jpg|tif)"))
        self.label_2.setText(_translate("Dialog", "数据存放路径"))
        self.checkBox.setText(_translate("Dialog", "继续训练？"))
        self.pushButton.setText(_translate("Dialog", "开始训练"))
        self.label_3.setText(_translate("Dialog", "超参数"))
        self.label_4.setText(_translate("Dialog", "多久在显示屏上展示结果（默认100次）"))
        self.label_5.setText(_translate("Dialog", "多久更新网页(默认1000次)"))
        self.label_6.setText(_translate("Dialog", "多久打印结果（默认100次）"))
        self.label_7.setText(_translate("Dialog", "多久保存最新结果(默认1000次)"))
        self.label_8.setText(_translate("Dialog", "多少轮保存结果（默认5）"))
        self.label_9.setText(_translate("Dialog", "学习率（默认0.0002）"))
        self.label_10.setText(_translate("Dialog", "lambda_A"))
        self.label_11.setText(_translate("Dialog", "lambda_B"))
        self.label_12.setText(_translate("Dialog", "identity"))
        self.label_13.setText(_translate("Dialog", "TextLabel"))
        self.label_14.setText(_translate("Dialog", "TextLabel"))
        self.label_15.setText(_translate("Dialog", "TextLabel"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        
class Window1(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super(Window1, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_Clicked)
        self.pushButton_2.clicked.connect(self.set_input_data_dir)
        self.pushButton_3.clicked.connect(self.set_output_data_dir)
    
    
    def pushButton_Clicked(self):
        input_path=""
        output_path=""
        if self.textEdit.toPlainText()=="":
            print("please choose file input folder, in this folder, \n there should be sub-folder A and B, and in \n each  sub-folder, there should be images")
        else:
            input_path=self.textEdit.toPlainText()
        
        if self.textEdit_2.toPlainText()=="":
            print("please choose file input folder, in this folder, \n there should be sub-folder A and B, and in \n each  sub-folder, there should be images")
        else:
            output_path=self.textEdit_2.toPlainText()
        prepare_data_for_unpair_training(input_path, output_path, 512)
        continue_train=self.checkBox.isChecked()
        train(dataroot=output_path, continue_train=continue_train)
        
    def set_input_data_dir(self):
        dlg=QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        a=dlg.getExistingDirectory(self)
        self.textEdit.setPlainText(str(a))
        
    def set_output_data_dir(self):
        dlg=QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        a=dlg.getExistingDirectory(self)
        self.textEdit_2.setPlainText(str(a))
    


# if __name__=="__main__":
#         app=QApplication(sys.argv)
#         main_window=Window1()
#         main_window.show()
#         sys.exit(app.exec_())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

