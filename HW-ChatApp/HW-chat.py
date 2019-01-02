

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class ChatApp(QMainWindow):
 
    def __init__(self):
        super(ChatApp, self).__init__()
        self.title = 'Chat App'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 100
        
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,20)
        
        self.lbl = QLabel(self)
        self.lbl.setGeometry(20, 55,200,20)
        self.lbl.setText("Type Something and Press Ok!")
        self.show()
        
        #        self.textbox.setText("")

 

    
def main():
    app = QApplication([])
    q = ChatApp()
    q.show()
    sys.exit(app.exec_())    

    
if __name__ == "__main__":
    main()