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
        self.__allPaths = deque()
        self.__undone = deque()
        self.__undonePaths = deque()
        self.walkToggle = False
        self.grassToggle = False
        
    def mousePressEvent(self, event):

        dataX = int(event.scenePos().x() // 10)
        dataY = int(event.scenePos().y() // 10)

        if self.mapData[dataY][dataX] == 0:
            print("Invalid Selection")
            return

        x = dataX * 10
        y = dataY * 10

        self.__selected.append((x, y))
        self.__addPath()
        self.__undone = deque() # upon making a change, undone cache is cleared
        self.__undonePaths = deque()
        self.update()

    def update(self):
        self.clear()
        if (self.walkToggle):
            self.__drawWalkable()
        if (self.grassToggle):
            self.__drawEncounters()
            
        self.__drawAllPaths()
        self.__drawSelected()

    def undo(self):
        if not self.__selected:
            return
        self.__undone.append(self.__selected.pop())

        if not self.__allPaths:
            return
        self.__undonePaths.append(self.__allPaths.pop())

    def redo(self):
        if not self.__undone:
            return
        self.__selected.append(self.__undone.pop())

        if not self.__undonePaths:
            return
        self.__allPaths.append(self.__undonePaths.pop())
        

    def __drawSelected(self):

        orangePen = qtg.QPen(qtg.QColor(255,165,0))
        orangePen.setWidth(2)
        
        for point in self.__selected:
            self.addRect(point[0],point[1],10,10,orangePen)

    def __addPath(self):
        if len(self.__selected) <= 1:
            return

        # start is end of deque (most recently added)
        start = ((self.__selected[-1][1] // 10), (self.__selected[-1][0] // 10))
        end = ((self.__selected[-2][1] // 10), (self.__selected[-2][0] // 10))

        self.__allPaths.append(astar(self.mapData, start, end))
        #print(self.__allPaths)

    def __drawAllPaths(self):

        yellowPen = qtg.QPen(qtc.Qt.yellow)
        yellowPen.setWidth(1)

        for path in self.__allPaths:
            for point in path:
                self.addRect(point[1] * 10,point[0] * 10,10,10,yellowPen)
                

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

    def redoClicked(self):
        self.map.redo()
        self.map.update()

    def walkClicked(self):
        self.map.walkToggle = not self.map.walkToggle
        self.map.update()

    def grassClicked(self):
        self.map.grassToggle = not self.map.grassToggle
        self.map.update()

    def runClicked(self):
        print("RUN Clicked")



if __name__ == "__main__":

    app = qtw.QApplication([])

    mainWindow = MainWindow()
    mainWindow.show()
    
    app.exec_()
