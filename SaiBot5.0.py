from SaiBotInterface import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from MapProcessor import *
from Astar import *


class GraphicsScene(qtw.QGraphicsScene):
    def __init__(self, parent=None):
        qtw.QGraphicsScene.__init__(self, parent)

        # for redraw and destination storage
        self.selected = []
        
    def mousePressEvent(self, event):

        yellowPen = qtg.QPen(qtc.Qt.yellow)
        yellowPen.setWidth(1)

        x = (event.scenePos().x() // 10) * 10
        y = (event.scenePos().y() // 10) * 10

        self.selected.append((x, y))
        self.addRect(x,y,10,10,yellowPen)

    def redrawSelected(self):

        yellowPen = qtg.QPen(qtc.Qt.yellow)
        yellowPen.setWidth(1)
        
        for point in self.selected:
            self.addRect(point[0],point[1],10,10,yellowPen)
        

class MainWindow(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # link up signals/slots
        self.undoButton.clicked.connect(lambda: self.undoClicked())
        self.redoButton.clicked.connect(lambda: self.redoClicked())
        self.walkButton.clicked.connect(lambda: self.walkClicked())
        self.grassButton.clicked.connect(lambda: self.grassClicked())
        self.runButton.clicked.connect(lambda: self.runClicked())

        # only generate walkable data if it doesn't exist
        try:
            self.mapData = np.loadtxt('mapData.csv', delimiter=',')
        except:
            self.mapData = initWalkable()
            np.savetxt('mapData.csv', mapData, delimiter=',')

        # button pressed status
        self.walkToggle = False
        self.grassToggle = False
        self.mapScene = GraphicsScene(self)
        self.mapView.setScene(self.mapScene)

    def mapClicked(self):
        print("Clicked map at: ")

    def undoClicked(self):
        print("UNDO Clicked")

    def redoClicked(self):
        print("REDO Clicked")

    def walkClicked(self):

        if self.walkToggle:
            self.mapScene.clear()
        else:
            self.__drawWalkable(self.mapScene)

        if self.grassToggle:
            self.__drawEncounters(self.mapScene)
        
        self.mapScene.update()
        self.mapScene.redrawSelected()
        self.walkToggle = not self.walkToggle

    def grassClicked(self):

        if self.grassToggle:
            self.mapScene.clear()
        
        if self.walkToggle:
            self.__drawWalkable(self.mapScene)

        if not self.grassToggle:
            self.__drawEncounters(self.mapScene)
                    
        self.mapScene.update()
        self.mapScene.redrawSelected()
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


if __name__ == "__main__":

    app = qtw.QApplication([])

    mainWindow = MainWindow()
    mainWindow.show()
    
    app.exec_()
