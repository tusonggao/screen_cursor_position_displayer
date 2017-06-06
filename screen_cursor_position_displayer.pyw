from PyQt4 import QtGui  
from PyQt4 import QtCore  
#from PyQt4.QtWebKit import*  
#from PyQt4 import QtCore, QtGui  
#from PyQt4 import uic  
from PyQt4.QtCore import *  
from PyQt4.QtGui import *  
#from PyQt4.QtWebKit import *  
#from PyQt4.QtNetwork import *  
import sys

class MainDialog(QtGui.QDialog):    
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle(u'Screen Curosr Position Displayer')
        self.setFixedSize(500, 150)
        
        xlabel = QLabel(u'X axis:')
        xlabel.setFont(QFont('Roman times', 18, QFont.Bold))  
        xlabel.setFixedSize(100, 55)
        self.xEdit = QLineEdit()  
        self.xEdit.setFixedSize(100, 70)
        self.xEdit.setFont(QFont("Roman times", 27, QFont.Bold))
        self.xEdit.setFocusPolicy(Qt.NoFocus)
        
        ylabel = QLabel(u'Y axis:')
        ylabel.setFont(QFont("Roman times", 18, QFont.Bold))
        ylabel.setFixedSize(100, 55)        
        self.yEdit = QLineEdit()
        self.yEdit.setFixedSize(100, 70)
        self.yEdit.setFont(QFont("Roman times", 27, QFont.Bold))
        self.yEdit.setFocusPolicy(Qt.NoFocus)
        
        hLayout = QHBoxLayout()  
        hLayout.addWidget(xlabel)
        hLayout.addWidget(self.xEdit)
        hLayout.addStretch()
        hLayout.addWidget(ylabel)
        hLayout.addWidget(self.yEdit)
        
        self.aboutBtn = QtGui.QPushButton('About')
        self.aboutBtn.setFocusPolicy(Qt.NoFocus)
        
        vMainLayout = QtGui.QVBoxLayout()  
        vMainLayout.addLayout(hLayout)
        vMainLayout.addWidget(self.aboutBtn)
        self.setLayout(vMainLayout)
        
        self.aboutBtn.clicked.connect(self.onAbout)        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onTimer)
        self.timer.start(500)
        
    def onTimer(self):
        print('In OnTimer ', QCursor().pos())
        pos = QCursor().pos()
        self.xEdit.setText(str(pos.x()))
        self.yEdit.setText(str(pos.y()))
        
    def onAbout(self):
        self.aboutDlg = QMessageBox(QMessageBox.Information, 
                          'About Me', 
                          '''This is a small utility program to display the xy\n'''
                          '''positions of current screen curosr.\n'''
                          '''Author: tusonggao''')
        self.aboutDlg.show()
              
def main():  
    app = QtGui.QApplication(sys.argv)  
    win = MainDialog()
    win.show()
    sys.exit(app.exec_())  
   
if __name__ == '__main__':  
    main()  

