from SaiBotInterface import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from MapProcessor import *
from Astar import *

class SaiBotWindow(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # link up signals/slots
        self.undoButton.clicked.connect(lambda: self.undoClicked())
        self.redoButton.clicked.connect(lambda: self.redoClicked())
        self.walkButton.clicked.connect(lambda: self.walkClicked())
        self.grassButton.clicked.connect(lambda: self.grassClicked())
        self.runButton.clicked.connect(lambda: self.runClicked())

        # Only generate walkable data if it doesn't exist
        try:
            self.mapData = np.loadtxt('mapData.csv', delimiter=',')
        except:
            self.mapData = initWalkable()
            np.savetxt('mapData.csv', mapData, delimiter=',')

        # button pressed status
        self.walkToggle = False
        self.grassToggle = False

    def mapClicked(self):
        print("Clicked map at: ")

    def undoClicked(self):
        print("UNDO Clicked")

    def redoClicked(self):
        print("REDO Clicked")

    def walkClicked(self):
        scene = qtw.QGraphicsScene()

        if not self.walkToggle:
            scene = self.__drawWalkable(scene)

        if self.grassToggle:
            scene = self.__drawEncounters(scene)
            
        self.mapView.setScene(scene)
        self.walkToggle = not self.walkToggle

    def grassClicked(self):
        scene = qtw.QGraphicsScene()

        if self.walkToggle:
            scene = self.__drawWalkable(scene)

        if not self.grassToggle:
            scene = self.__drawEncounters(scene)
                    
        self.mapView.setScene(scene)
        self.grassToggle = not self.grassToggle

    def runClicked(self):
        print("RUN Clicked")

    def __drawWalkable(self, scene):
        grayPen = qtg.QPen(qtc.Qt.gray)
        grayPen.setWidth(1)
        height = len(self.mapData)
        width = len(self.mapData[0])
        for r in range(0, height):
            for c in range(0, width):
                if self.mapData[r][c] == 0:
                    continue
                else:
                    xCoord = c * 10
                    yCoord = r * 10
                    scene.addRect(xCoord,yCoord,10,10,grayPen)
        return scene

    def __drawEncounters(self, scene):
        redPen = qtg.QPen(qtc.Qt.red)
        redPen.setWidth(1)
        height = len(self.mapData)
        width = len(self.mapData[0])
        for r in range(0, height):
            for c in range(0, width):
                if self.mapData[r][c] != 2:
                    continue
                else:
                    xCoord = c * 10
                    yCoord = r * 10
                    scene.addRect(xCoord,yCoord,10,10,redPen)
        return scene


if __name__ == "__main__":

    app = qtw.QApplication([])

    mainWindow = SaiBotWindow()
    mainWindow.show()
    
    app.exec_()
