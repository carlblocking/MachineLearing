#coding=utf-8
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
# from PyQt5.QtCore import QObject, pyqtSignal
# # 
# # app=QApplication([])
# # widget=QWidget()
# # 
# # 
# # def show_message():
# #     QMessageBox.information(widget, "信息框", "ok,弹出测试信息")
# # 
# # btn=QPushButton("点击测试按钮", widget)
# # 
# # btn.clicked.connect(show_message)
# # 
# # widget.show()
# # sys.exit(app.exec_())
# 
# class Send_Signal(QObject):
#     send_message=pyqtSignal(object, object)
#     
#     def __init__(self):
#         super(Send_Signal, self).__init__()
#         
#     def run(self):
#         self.send_message.emit("param1","param2")
#         
# class Receive_Signal(QObject):
#     def __init__(self):
#         super(Receive_Signal, self).__init__()
#     
#     def show_message(self, message1, message2):
#         print(message1, '\t', message2)
#         
# class WinForm(QWidget):
#     button_click_signal=pyqtSignal()
#     def __init__(self):
#         super(WinForm, self).__init__()
#         self.setWindowTitle("内置信号示例")
#         self.resize(100,100)
#         btn=QPushButton("close", self)
#         
#         btn.clicked.connect(self.btn_clicked)
#         self.button_click_signal.connect(self.close)
#     
#     def btn_close(self):
#         self.close()
#         
#     def btn_clicked(self):
#         self.button_click_signal.emit()
#         
# 
#         
# if __name__=="__main__":
# #     sender=Send_Signal()
# #     receiver=Receive_Signal()
# #     
# #     sender.send_message.connect(receiver.show_message)
# #     sender.run()
# #     
# #     sender.send_message.disconnect(receiver.show_message)
# #     sender.run()
#     app=QApplication(sys.argv)
#     win=WinForm()
#     win.show()
#     sys.exit(app.exec_())
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 


