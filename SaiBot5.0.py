from SaiBotInterface import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from collections import deque
from MapProcessor import *
from Astar import *


class Map(qtw.QGraphicsScene):
    def __init__(self, parent=None):
        qtw.QGraphicsScene.__init__(self, parent)

        # only generate walkable data if it doesn't exist
        try:
            self.mapData = np.loadtxt('mapData.csv', delimiter=',')
        except:
            self.mapData = initWalkable()
            np.savetxt('mapData.csv', mapData, delimiter=',')
        
        self.__selected = deque()
        self.__undone = deque()
        self.walkToggle = False
        self.grassToggle = False
        
    def mousePressEvent(self, event):

        yellowPen = qtg.QPen(qtc.Qt.yellow)
        yellowPen.setWidth(1)

        x = (event.scenePos().x() // 10) * 10
        y = (event.scenePos().y() // 10) * 10

        self.__selected.append((x, y))
        self.addRect(x,y,10,10,yellowPen)
        self.__undone = [] # upon making a change, undone cache is cleared

    def update(self):
        self.clear()
        if (self.walkToggle):
            self.__drawWalkable()
        if (self.grassToggle):
            self.__drawEncounters()

        self.__drawSelected()
        super().update()

    def undo(self):
        if not self.__selected:
            return
        self.__undone.append(self.__selected.pop())

    def redo(self):
        if not self.__undone:
            return
        self.__selected.append(self.__undone.pop())
        

    def __drawSelected(self):

        yellowPen = qtg.QPen(qtc.Qt.yellow)
        yellowPen.setWidth(1)
        
        for point in self.__selected:
            self.addRect(point[0],point[1],10,10,yellowPen)

    def __drawWalkable(self):
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
                    self.addRect(xCoord,yCoord,10,10,grayPen)

    def __drawEncounters(self):
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
                    self.addRect(xCoord,yCoord,10,10,redPen)


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

        self.map = Map(self)
        self.mapView.setScene(self.map)

    def undoClicked(self):
        self.map.undo()
        self.map.update()
        print("UNDO Clicked")

    def redoClicked(self):
        self.map.redo()
        self.map.update()
        print("REDO Clicked")

    def walkClicked(self):
        print("WALK Clicked")
        self.map.walkToggle = not self.map.walkToggle
        self.map.update()

    def grassClicked(self):
        print("GRASS Clicked")
        self.map.grassToggle = not self.map.grassToggle
        self.map.update()

    def runClicked(self):
        print("RUN Clicked")



if __name__ == "__main__":

    app = qtw.QApplication([])

    mainWindow = MainWindow()
    mainWindow.show()
    
    app.exec_()
