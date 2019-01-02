#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:25:08 2018

@author: AppleMoony
"""

import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog

class Example(QWidget):
    
    
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        
    def initUI(self):      
        self.d = 50; self.x = 0; self.y = 0;
        self.dx = 0; self. dy = 0;
        self.boxwidth = 600; self.boxheight = 400;
        
        self.selected_color=QtGui.QColor(200, 0, 0)
#        self.timeron = False
#        self.timer = QtCore.QTimer()
#        self.timer.timeout.connect(self.animate)
#        self.timer.start(10)
#        self.qbtn = QPushButton('Start', self)
#        self.qbtn.clicked.connect(self.toggle)
#        self.qbtn.resize(self.qbtn.sizeHint())
#        self.qbtn.move(0, 401)  
        
        self.dragging=False
#        
        self.setGeometry(300, 300, 600, 400)
        

        self.setWindowTitle('Animation')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):

        qp.setPen(QtGui.QColor(255, 255, 255))
        
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(0, 0, self.boxwidth, self.boxheight)
        
        qp.setBrush(self.selected_color)
        qp.drawRect(self.x, self.y, self.d, self.d)

       # qp.drawEllipse(self.x, self.y, self.d, self.d)
    
    def mousePressEvent(self, e):
#        print e.x()
#        print e.y()
        if e.x()>self.x and e.x()<self.x+50 and e.y()>self.y and e.y()<self.y+50:
            self.dragging=True
            self.currentx=e.x()
            self.currenty=e.y()
    
    def mouseReleaseEvent(self, e):
        self.dragging=False
        self.dx=0
        self.dy=0
    
    def mouseMoveEvent(self, e):
        if self.dragging:
            newx=e.x()
            newy=e.y()
            self.dx=newx-self.currentx
            self.dy=newy-self.currenty
            self.currentx=newx
            self.currenty=newy
            self.animate()
    
    def mouseDoubleClickEvent(self, e):
        self.selected_color=QColorDialog.getColor()
        #print self.selected_color.name()
        self.update()

        
    def animate(self):
        self.x += self.dx
        self.y += self.dy
#        self.checkCollision()
        self.update()
        
#    def setSquareColor(self):
#        pass
        
#    def toggle(self):
#        if self.timeron:
#           # self.qbtn.setText("Play")
#            self.timeron = False
#            self.timer.stop()
#        else:
#            #self.qbtn.setText("Pause")
#            self.timeron = True
#            self.timer.start(10)
        
#    def checkCollision(self):
#        qr = self.frameGeometry()
#        window_width, window_height = qr.width(), qr.height()
#        
#        if (self.x <= 0) or ((self.x + self.d)>= window_width):
#            self.dx = -self.dx
#        if (self.y <= 0) or ((self.y + self.d)>= window_height-22):
#            self.dy = -self.dy
              
def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()