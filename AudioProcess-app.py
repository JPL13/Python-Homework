#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:20:57 2018

@author: AppleMoony
"""
from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import QTimer

from PyQt5.uic import loadUi

import csv
import re

class canvas(QWidget):
    def __init__(self, parent=None):
        super(canvas, self).__init__(parent)
        self.x=0
        self.y=0
        
        
    def paintEvent(self, event):
        p=QPainter()
        p.begin(self)
        self.draw(p)       
        p.end()
    
    def draw(self, p):
        white = QColor(255,255,255)
        p.setBrush(white)
        p.setPen(QColor(0, 0, 0))
        
        p.drawRect(0,0,self.geometry().width(), self.geometry().height())
        
        p.setBrush(QColor(255, 0, 0))
        p.setPen(QColor(0, 0, 255))
        p.drawEllipse(self.x, self.y, 10, 10)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        loadUi("form.ui", self)
        
        self.setWindowTitle("Point Animation") 

        self.li=[]
        self.clicked=False
        self.fileloaded=False
        
        if not self.fileloaded:
            self.pushButton_2.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            
        
        #left button
        self.pushButton_2.clicked.connect(self.changeName)
        
        #right button
        self.pushButton.clicked.connect(self.stopbuttonclick)
        
        #slider
        self.horizontalSlider.valueChanged.connect(self.f)
        self.horizontalSlider.sliderMoved.connect(self.sliderdrag)
        
        #menubar
        self.menubar.setNativeMenuBar(False)


        #fileselector
        bar = self.menuBar()
        
        openAction = QAction('&Open', self)        
        openAction.triggered.connect(self.file_open)
        
        file = bar.addMenu("File")
        file.addAction(openAction)

        self.show()
        
        #timer
        self.t = QTimer(self)
        self.t.timeout.connect(self.slidermove)
        self.t.start(5)
        
        self.sliderpos=0
        self.dx=0
        
        self.sliderMax=100
        self.step=.5
        
        self.horizontalSlider.setMaximum(self.sliderMax)
        

    def f(self, value):
        print value 
        self.widget.x=value
        self.widget.y=value
        self.widget.repaint()
        

        
    def sliderdrag(self, value):
        print "Move", value
        #self.dx=0
        self.sliderpos=value
        self.horizontalSlider.setValue(self.sliderpos)
        
        
    def changeName(self):
        #print self.clicked
#        if self.clicked==False:
#            self.clicked=True
#        else:
#            self.clicked=False
        
        self.clicked=not self.clicked
        
        if self.sliderpos==self.sliderMax:
            self.sliderpos=0
        
        if self.clicked or (self.sliderpos==self.sliderMax):
            
            self.pushButton_2.setText("Pause")
            self.dx=self.step
            #self.slidermove()

        if not self.clicked:
            self.pushButton_2.setText("Play")
            self.dx=0

#the  “Stop”  button  should  
#1)  cause  the  leftmostbutton  to  become  a“Play”  button,  if  it  is  not  already, 
# 2)  return  the  slider  to  its  leftmost  position,  and 
# 3)  stop  the  slider  movement
    def stopbuttonclick(self):
        
        if self.dx>0 or (self.dx==0 and self.sliderpos>0) :
            self.pushButton_2.setText("Play")
            self.clicked=False
            self.sliderpos=0
            self.horizontalSlider.setValue(self.sliderpos)
            self.dx=0

  
    
    def slidermove(self):
        
        if self.sliderpos<=self.sliderMax:
            self.sliderpos+=self.dx
            self.horizontalSlider.setValue(self.sliderpos)
        #When  the  slider  reaches  its  rightmost  position,  
        # 1)  make  the  leftmost  button  a  “Play”  button,  if  it  is  not  already 
        #2)  stop  the  slider  movement
        if self.sliderpos>=self.sliderMax:
            #print "Max"
            self.pushButton_2.setText("Play")
            self.dx=0
            self.clicked=False

    def file_open(self):
        print "file open"
        name=QFileDialog.getOpenFileName(self, 'Open', "", "csv(*.csv)")
        
        print "filename" + str(name)
        
        filename=name[0] 
        print filename
       
        try:
            with open(filename, "r") as f:
                r=csv.reader(f)
                
                for row in r:
                    if len(row)==2 and row[0].isdigit() and row[1].isdigit():
                        self.li.append(row)
#                        print self.t
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Invalid data")
                        msg.exec_()
                        print "Invalid data"
                        self.li=[]
                        break
                    
            
        except:
            print "Error with Opening file"
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error with Opening file")
            msg.exec_()
        
        if len(self.li)>0:       
            self.fileloaded=True        
            #print self.li
            self.pushButton_2.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.horizontalSlider.setEnabled(True)                   

def main():
    app = QApplication([])
    q = MainWindow()
    q.show()
    app.exec_()    
    

    
if __name__ == "__main__":
    main()