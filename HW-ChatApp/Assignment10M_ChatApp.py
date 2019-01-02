# -*- coding: utf-8 -*-

"""

Created on Mon Aug 13 15:44:39 2018



@author: ptthai

"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel
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
        self.run()
        """
            timer will initiated after socket is created from run()
        """
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.incomingMsg)
        self.timer.start(2000)

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,20)
     
        self.lbl = QLabel(self)
        self.lbl.setGeometry(20, 55,200,20)        

        self.show()
        
    def setLabel(self,n):

        self.lbl.setText(n)  

    def getText(self):

        return self.textbox.text()       

    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_Return:
            print "Return key pressed"
            self.sendMsg() 

    def sendMsg(self):

        text=self.getText()
        print "sendMsg:", text
        self.s.send(text)   
            
    def incomingMsg(self):

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

        try:
            print "client in run"
            self.s = socket.socket()
            self.s.connect((host, port))
            self.setLabel("<connected>")
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

            self.ss.close()
            print "run: closed"

        self.s.settimeout(.25)

def main():    

    app = QApplication([])
    window = ChatApp()
    app.exec_() 

if __name__ == "__main__":

    main()