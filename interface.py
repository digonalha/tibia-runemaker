import sys
from PyQt4 import QtGui, QtCore
from threading import Thread
import runemaker

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("asmrobot runemaker v.alfa")
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.create_menu_bar()


        self.home()

    def create_menu_bar(self):
        extractAction = QtGui.QAction("Join config", self)
        extractAction.setShortcut("Ctrl+J")
        extractAction.setStatusTip('Configure join api for notifications')

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&Settings')
        fileMenu.addAction(extractAction)


    def home(self):
        btn = QtGui.QPushButton("RUN!", self)
        btn.move(100,100)
        btn.clicked.connect(self.close_application)
        self.show()

    def close_application(self):
        Thread(target = runemaker.runemaker).start()
        #Wsys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()