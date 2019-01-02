# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:44:39 2018

@author: ptthai
"""


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
import socket 

class ChatApp(QMainWindow):
 
    def __init__(self):
        super(ChatApp, self).__init__()
        self.title = 'Chat App'
        self.left = 200
        self.top = 200
        self.width = 320
        self.height = 100
        
        self.data=None
        
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
        self.s.send(text)
    
    def incomingMsg(self):
        if self.data:
            self.setLabel(self.data)
        

    def run(self):
        host = "127.0.0.1"
        port = 12349
    
        self.s = socket.socket()
    #print "socket client created"
    
        try:
            self.s.connect((host, port))
        #print "client connects"
            self.setLabel("<connected>")
            
#            msg=self.sendMsg()
#        
#            if msg:
#                self.s.send(msg)
        
        except:
        
            self.s = socket.socket()
            self.s.bind(("", port))
    
            self.s.listen(5)
        
            c, addr = self.s.accept()
            self.setLabel("<connected>")
        
            self.s.settimeout(.25)
            
            self.data = c.recv(1024)
            

            #c.close()
            self.setLabel("<connection closed>")
            
        #self.s.close()        

        
        
 
def main():
    app = QApplication([])
    window = ChatApp()
    window.run()
    #server=Server(window)
    sys.exit(app.exec_())    



#    message = raw_input("--")
    
#    while message != "q":
#        s.send(message)
#        data = s.recv(1024)
#        print "Rec from server: "+str(data)
##        message = q.textbox.text()
#        message = raw_input("--")
        
    
#    sys.exit(app.exec_()) 
    
if __name__ == "__main__":
    main()