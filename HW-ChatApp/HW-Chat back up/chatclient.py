# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:44:39 2018

@author: ptthai
"""


#import sys
#from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot
import socket 
#
#class ChatApp(QMainWindow):
# 
#    def __init__(self):
#        super(ChatApp, self).__init__()
#        self.title = 'Chat App'
#        self.left = 200
#        self.top = 200
#        self.width = 320
#        self.height = 100
#        
#        self.initUI()
# 
#    def initUI(self):
#        self.setWindowTitle(self.title)
#        self.setGeometry(self.left, self.top, self.width, self.height)
# 
#        # Create textbox
#        self.textbox = QLineEdit(self)
#        self.textbox.move(20, 20)
#        self.textbox.resize(280,20)
#        
#        self.lbl = QLabel(self)
#        self.lbl.setGeometry(20, 55,200,20)
#        self.show()
#        
#    def setLabel(self,n):
#        self.lbl.setText(n)
#        
#    def getText(self):
#        return self.textbox.text()
#        
#        #        self.textbox.setText("")

 
def main():
#    app = QApplication([])
#    q = ChatApp()
#    q.show()
#    sys.exit(app.exec_())    

    host = "76.91.16.49"
    port = 12347
    
    s = socket.socket()
    print "socket client created"
    
    s.connect((host, port))
    print "client connects"
    
#    q.setLabel("<connected>")
#    message = q.textbox.text()
    message = raw_input("--")
    
    while message != "q":
        s.send(message)
        data = s.recv(1024)
        print "Rec from server: "+str(data)

        message = raw_input("--")
        
    s.close()
    
if __name__ == "__main__":
    main()