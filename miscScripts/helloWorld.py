# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helloWorld.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainButton.setGeometry(QtCore.QRect(300, 240, 161, 61))
        self.mainButton.setObjectName("mainButton")
        self.messageTxt = QtWidgets.QLabel(self.centralwidget)
        self.messageTxt.setGeometry(QtCore.QRect(300, 160, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.messageTxt.setFont(font)
        self.messageTxt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.messageTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.messageTxt.setObjectName("messageTxt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # link button to function
        self.mainButton.clicked.connect(lambda: self.clicked())
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainButton.setText(_translate("MainWindow", "Push Me!"))
        self.messageTxt.setText(_translate("MainWindow", "Hello World"))

    def clicked(self):
        self.messageTxt.setText("Clicked!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
