from PyQt5 import QtCore, QtGui, QtWidgets
from Astar import *
from MapProcessor import *
import pyautogui
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1334, 915)
        MainWindow.setMaximumSize(QtCore.QSize(1334, 915))
        MainWindow.setStyleSheet("background-color: rgb(248, 248, 248)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.map = QtWidgets.QLabel(self.centralwidget)
        self.map.setGeometry(QtCore.QRect(20, 20, 871, 831))
        self.map.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.map.setMouseTracking(False)
        self.map.setText("")
        self.map.setPixmap(QtGui.QPixmap("Saipark - Copy.png"))
        self.map.setScaledContents(True)
        self.map.setObjectName("map")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 891, 851))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setAcceptDrops(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(27, 28, 27)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(850, 10, 51, 181))
        self.frame_2.setStyleSheet("background-color: rgb(223, 223, 223);\n"
"border: 3px solid rgb(27, 28, 27);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.redoButton = QtWidgets.QLabel(self.frame_2)
        self.redoButton.setGeometry(QtCore.QRect(10, 50, 32, 32))
        self.redoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.redoButton.setStyleSheet("background-color: rgb(223, 223, 223)")
        self.redoButton.setText("")
        self.redoButton.setPixmap(QtGui.QPixmap("Redo.png"))
        self.redoButton.setScaledContents(True)
        self.redoButton.setObjectName("redoButton")
        self.undoButton = QtWidgets.QLabel(self.frame_2)
        self.undoButton.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.undoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.undoButton.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.undoButton.setText("")
        self.undoButton.setPixmap(QtGui.QPixmap("Undo.png"))
        self.undoButton.setScaledContents(True)
        self.undoButton.setObjectName("undoButton")
        self.walkButton = QtWidgets.QLabel(self.frame_2)
        self.walkButton.setGeometry(QtCore.QRect(10, 90, 32, 32))
        self.walkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.walkButton.setStyleSheet("background-color: rgb(223, 223, 223)")
        self.walkButton.setText("")
        self.walkButton.setPixmap(QtGui.QPixmap("walk.png"))
        self.walkButton.setScaledContents(True)
        self.walkButton.setObjectName("walkButton")
        self.grassButton = QtWidgets.QLabel(self.frame_2)
        self.grassButton.setGeometry(QtCore.QRect(10, 130, 32, 32))
        self.grassButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.grassButton.setStyleSheet("background-color: rgb(223, 223, 223)")
        self.grassButton.setText("")
        self.grassButton.setPixmap(QtGui.QPixmap("grass.png"))
        self.grassButton.setScaledContents(True)
        self.grassButton.setObjectName("grassButton")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(920, 10, 401, 851))
        self.frame_3.setStyleSheet("background-color: rgb(223, 223, 223);border-radius: 10px;border: 3px solid rgb(27, 28, 27);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(50, 610, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:rgb(223, 223, 223);border:none")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(80, 640, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgb(223, 223, 223);border:none")
        self.label_3.setObjectName("label_3")
        self.encounterSpinBox = QtWidgets.QSpinBox(self.frame_3)
        self.encounterSpinBox.setGeometry(QtCore.QRect(230, 610, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.encounterSpinBox.setFont(font)
        self.encounterSpinBox.setStyleSheet("background-color: rgb(238, 238, 238);border:1px solid rgb(27, 28, 27); border-radius:0px")
        self.encounterSpinBox.setMaximum(999999999)
        self.encounterSpinBox.setObjectName("encounterSpinBox")
        self.timeoutSpinBox = QtWidgets.QSpinBox(self.frame_3)
        self.timeoutSpinBox.setGeometry(QtCore.QRect(230, 640, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeoutSpinBox.setFont(font)
        self.timeoutSpinBox.setStyleSheet("background-color: rgb(238, 238, 238);border:1px solid rgb(27, 28, 27); border-radius:0px")
        self.timeoutSpinBox.setMaximum(999999999)
        self.timeoutSpinBox.setObjectName("timeoutSpinBox")
        self.runButton = QtWidgets.QPushButton(self.frame_3)
        self.runButton.setGeometry(QtCore.QRect(150, 700, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.runButton.setFont(font)
        self.runButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runButton.setStyleSheet("color:white;background-color: #4CAF50;border: None; border-radius:4px;")
        self.runButton.setObjectName("runButton")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(40, 300, 321, 281))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(223, 223, 223);border:none")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(150, 250, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:rgb(223, 223, 223);border:none")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 281, 221))
        self.label_2.setStyleSheet("background-color:rgb(223, 223, 223);border:none")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("hidody.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(250, 250, 40, 40))
        self.label_5.setStyleSheet("border:none")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("lumaStar.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(100, 250, 40, 40))
        self.label_6.setStyleSheet("border:none")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("lumaStar.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.frame_3.raise_()
        self.frame.raise_()
        self.map.raise_()
        self.frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1334, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # manual additions:
        self.mapData = []
        self.walkToggle = False
        self.grassToggle = False
        ####################
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.walkButton.clicked.connect(walkClicked)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SaiBot"))
        self.redoButton.setToolTip(_translate("MainWindow", "Redo"))
        self.undoButton.setToolTip(_translate("MainWindow", "Undo"))
        self.walkButton.setToolTip(_translate("MainWindow", "Show Walkable"))
        self.grassButton.setToolTip(_translate("MainWindow", "Show Grass/Water"))
        self.label_7.setText(_translate("MainWindow", "Encounters/Patch:"))
        self.label_3.setText(_translate("MainWindow", "Timeout (sec):"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.label.setText(_translate("MainWindow", "Create a path by clicking your start and end destinations on the map. You can chain multiple points together to create more complex paths. Clicking in the grass or water will select the whole patch and your character will search the patch until the max encounters limit is reached. Finally, set a timeout to specify when SaiBot should give up the hunt and log you out of your account. After creating your path, hit run and you will have 5 seconds to switch windows to TemTem before automation begins."))
        self.label_4.setText(_translate("MainWindow", "SaiBot"))

    # manual additions:
    def initMapData(self):
        # Only generate walkable data if it doesn't exist
        try:
            self.mapData = np.loadtxt('mapData.csv', delimiter=',')
        except:
            self.mapData = initWalkable()
            np.savetxt('mapData.csv', mapData, delimiter=',')
            
    def undoClicked(self):
        return
    
    def redoClicked(self):
        return
    
    def walkClicked(self):
        painter = QtGui.QPainter(self.map.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor("#808080"))
        painter.setPen(pen)

        height = len(self.mapData)
        width = len(self.mapData[0])
        
        for r in range(0, height):
            for c in range(0, width):
                if self.mapData[r][c] == 0:
                    continue
                elif self.mapData[r][c] > 0:
                    xCoord = c * 10
                    yCoord = r * 10
                    painter.drawRect(xCoord, yCoord, 10, 10)
        
        painter.end()
        
    def grassClicked(self):
        painter = QtGui.QPainter(self.map.pixmap())
        painter.end()
        
    def runClicked(self):
        return
    ####################

if __name__ == "__main__":
    import sys

    # delay between presses will skew pathing
    pyautogui.PAUSE = 0
    pyautogui.FAILSAFE = False
    
    # initialize user interface
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.initMapData()
    MainWindow.show()
        
    sys.exit(app.exec_())
