# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:44:39 2018

@author: ptthai
"""


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtCore
import socket 

class ChatApp(QMainWindow):
 
    def __init__(self):
        super(ChatApp, self).__init__()
        self.title = 'Chat App'
        self.left = 200
        self.top = 200
        self.width = 320
        self.height = 100
        
        self.initUI()
        #self.s=s
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,20)
        
        self.lbl = QLabel(self)
        self.lbl.setGeometry(20, 55,200,20)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.incomingMsg)
        self.timer.start(2000)
        
        self.show()
        
    def setLabel(self,n):
        self.lbl.setText(n)
        
    def getText(self):
        return self.textbox.text()
        
        #        self.textbox.setText("")
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            print "Return key pressed"
            self.sendMsg()
    
    def sendMsg(self):
        text=self.getText()
        print text
        #self.s.send(text)
        return text
    
    def incomingMsg(self):
        #msg=
        #self.setLabel(msg)
        pass
        
        
class Server():
    def __init__(self, window):
        host = "127.0.0.1"
        port = 12349
    
        s = socket.socket()
    #print "socket client created"
    
        try:
            s.connect((host, port))
        
            window.setLabel("<connected>")
            
            msg=window.sendMsg()
        
            if msg:
                s.send(msg)
        
        except:
        
            s = socket.socket()
            s.bind(("", port))
    
            s.listen(5)
        
            c, addr = s.accept()
            
            window.setLabel("<connected>")
            
            s.settimeout(.25)
                
            data = c.recv(1024)
            if data:
                window.setLabel(data)
                c.close()
            
                
        s.close()        
        
        
 
def main():
    app = QApplication([])
    window = ChatApp()
    server=Server(window)
    sys.exit(app.exec_())    

    
if __name__ == "__main__":
    main()