# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 15:35:57 2018

@author: ptthai
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
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
        
    def setLabel(self,n):
        self.lbl.setText(n)
        
    def getText(self):
        return self.textbox.text()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,20)
        
        self.lbl = QLabel(self)
        self.lbl.setGeometry(20, 55,200,20)
        #self.setLabel("Hello")
        self.show()
        
        #        self.textbox.setText("")
 
def main():
    
    app = QApplication(sys.argv)
    q = ChatApp()    
    
    host = "127.0.0.1"
    port = 12349
    
    s = socket.socket()
    
    try:
        s.connect((host, port))
        #print "client connects"
        q.setLabel("<connected>")
  
        
        
    except:
        s = socket.socket()
        s.bind(("", port))
    
        s.listen(5)
        
        c, addr = s.accept()
        #print "server connects"
        
        q.setLabel("<connected>")
        
        
     #message = q.textbox.text()   

    
#    while True:
#        data = c.recv(1024)
#        q.setLabel("it worked!")
#    #sys.exit(app.exec_())
#        if not data:
#            break
#        print "From connected user: "+str(data)
#        data = str(data).upper()
#        print "Sending: "+str(data)
#        c.send(data)
    
    
    
    #q.setLabel("it worked!")
    
    
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    main()