import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def clickable(widget):

    class Filter(QObject):
    
        clicked = pyqtSignal()
        
        def eventFilter(self, obj, event):
        
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        
        label1 = QLabel(self.tr("Hello world!"))
        label2 = QLabel(self.tr("ABC DEF GHI"))
        label3 = QLabel(self.tr("Hello PyQt!"))
        
        clickable(label1).connect(self.showText1)
        clickable(label2).connect(self.showText2)
        clickable(label3).connect(self.showText3)
        
        layout = QHBoxLayout(self)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
    
    def showText1(self):
        print("Label 1 clicked")
    
    def showText2(self):
        print("Label 2 clicked")
    
    def showText3(self):
        print ("Label 3 clicked")


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
