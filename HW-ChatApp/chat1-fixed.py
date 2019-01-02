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

        """
            run() is included here instead of inside of main() function
        """
        self.run()

        """
            timer will initiated after socket is created from run()
        """
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.incomingMsg)
        self.timer.start(2000)
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
        
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.incomingMsg)
        # self.timer.start(2000)
        
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
        print "sendMsg:", text
        """
            it will only send text if text is nonempty
        """
        if text != "":
            self.s.send(text)
    
    def incomingMsg(self):

        """
            used try and except for conveinience

            put s.rev(1024) here instead of inside the run() function
        """
        try:
            self.data = self.s.recv(1024)
            if self.data:
                self.setLabel(self.data)
        except:
            pass
            
            
    def closeEvent(self, event):
        self.s.send("<connection closed>")
            

    def run(self):
        host = "127.0.0.1"
        port = 12312

    
        
    #print "socket client created"
    
        try:
            print "client in run"
            """
                moved the self.s = socket.socket inside try
            """
            self.s = socket.socket()
            self.s.connect((host, port))
        #print "client connects"
            self.setLabel("<connected>")
            
#            msg=self.sendMsg()
#        
#            if msg:
#                self.s.send(msg)
        
        except:
            """
                used different variable name for the server socket. This will allow you 
                  to have 2 sockets for client and server separately.
                
                the server will wait until you run this .py again in other terminal.

                When a client socket is created from other terminal,
                  accept() will create a new socket. It will be assigned to self.s

                Then self.ss socket object will be closed and two terminals
                  are connected by self.s sockets

            """
            print "server in run"
            self.ss = socket.socket()
            self.ss.bind((host, port))
    
            self.ss.listen(5)

            print "run: listening"
        
            self.s, addr = self.ss.accept()
            self.setLabel("<connected>")

            print "run: accepted"
        
            
            
            # self.data = c.recv(1024)
            

            self.ss.close()
            print "run: closed"
            #self.setLabel("<connection closed>")
            
        self.s.settimeout(.25)
        # self.s.close()        

        
        
 
def main():
    
    app = QApplication([])
    window = ChatApp()

    """
        I included this in __init function
    """
    # window.run() 

    #server=Server(window)
    app.exec_() 
    #self.setLabel("<connection closed>")
    #self.s.close() 



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