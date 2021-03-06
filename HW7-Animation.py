import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class Example(QWidget):
    
    
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        
    def initUI(self):      
        self.d = 30; self.x = 0; self.y = 0;
        self.dx = 1; self. dy = 1;
        self.boxwidth = 600; self.boxheight = 400;
        
#        self.timeron = False
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(10)
#        self.qbtn = QPushButton('Start', self)
#        self.qbtn.clicked.connect(self.toggle)
#        self.qbtn.resize(self.qbtn.sizeHint())
#        self.qbtn.move(0, 401)   
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

        qp.setPen(QtGui.QColor(0, 0, 0, 255))
          
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(0, 0, self.boxwidth, self.boxheight)
        
        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawEllipse(self.x, self.y, self.d, self.d)
      
    def animate(self):
        self.x += self.dx
        self.y += self.dy
        self.checkCollision()
        self.update()
        
    def toggle(self):
        if self.timeron:
           # self.qbtn.setText("Play")
            self.timeron = False
            self.timer.stop()
        else:
            #self.qbtn.setText("Pause")
            self.timeron = True
            self.timer.start(10)
        
    def checkCollision(self):
        qr = self.frameGeometry()
        window_width, window_height = qr.width(), qr.height()
        
        if (self.x <= 0) or ((self.x + self.d)>= window_width):
            self.dx = -self.dx
        if (self.y <= 0) or ((self.y + self.d)>= window_height-22):
            self.dy = -self.dy
              
def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()