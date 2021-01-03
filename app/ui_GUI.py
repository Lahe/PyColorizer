# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 563)
        MainWindow.setMinimumSize(QtCore.QSize(700, 360))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton{\n"
"color:#4fe3c3;\n"
"border:1px solid #325154;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#4fe3c3;\n"
"color:#262d38;\n"
"border:1px solid #262d38;\n"
"}\n"
"\n"
"QLabel{\n"
"color:#b9c8c8;\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:#12161f;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"background-color:#325154;\n"
"border:0px solid #262d38;\n"
"}\n"
"\n"
"QComboBox {\n"
"color:#4fe3c3;\n"
"border:1px solid #325154;\n"
"font-size:10pt;\n"
"font-family: \"Proxima Nova Rg\";\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #4fe3c3;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"border: 1px solid #325154;\n"
"}\n"
"\n"
"font: 10pt \"Proxima Nova Rg\";")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.modelDropdown = QtWidgets.QComboBox(self.centralwidget)
        self.modelDropdown.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Rg")
        font.setPointSize(10)
        self.modelDropdown.setFont(font)
        self.modelDropdown.setEditable(False)
        self.modelDropdown.setObjectName("modelDropdown")
        self.modelDropdown.addItem("")
        self.modelDropdown.addItem("")
        self.modelDropdown.addItem("")
        self.modelDropdown.addItem("")
        self.horizontalLayout_2.addWidget(self.modelDropdown)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.importImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importImageBtn.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        self.importImageBtn.setFont(font)
        self.importImageBtn.setObjectName("importImageBtn")
        self.horizontalLayout_2.addWidget(self.importImageBtn)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.importVideoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importVideoBtn.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        self.importVideoBtn.setFont(font)
        self.importVideoBtn.setObjectName("importVideoBtn")
        self.horizontalLayout_2.addWidget(self.importVideoBtn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.colorizeImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.colorizeImageBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        self.colorizeImageBtn.setFont(font)
        self.colorizeImageBtn.setObjectName("colorizeImageBtn")
        self.horizontalLayout.addWidget(self.colorizeImageBtn)
        self.colorizeVideoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.colorizeVideoBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        self.colorizeVideoBtn.setFont(font)
        self.colorizeVideoBtn.setObjectName("colorizeVideoBtn")
        self.horizontalLayout.addWidget(self.colorizeVideoBtn)
        self.loadingSpinner = QtWidgets.QLabel(self.centralwidget)
        self.loadingSpinner.setMinimumSize(QtCore.QSize(0, 0))
        self.loadingSpinner.setMaximumSize(QtCore.QSize(32, 32))
        self.loadingSpinner.setText("")
        self.loadingSpinner.setScaledContents(True)
        self.loadingSpinner.setObjectName("loadingSpinner")
        self.horizontalLayout.addWidget(self.loadingSpinner)
        self.loadingText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        self.loadingText.setFont(font)
        self.loadingText.setObjectName("loadingText")
        self.horizontalLayout.addWidget(self.loadingText)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.input = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setMinimumSize(QtCore.QSize(0, 0))
        self.input.setObjectName("input")
        self.image_in = QtWidgets.QWidget()
        self.image_in.setObjectName("image_in")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.image_in)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.imgLabelIn = QtWidgets.QLabel(self.image_in)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgLabelIn.sizePolicy().hasHeightForWidth())
        self.imgLabelIn.setSizePolicy(sizePolicy)
        self.imgLabelIn.setMinimumSize(QtCore.QSize(100, 100))
        self.imgLabelIn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.imgLabelIn.setAutoFillBackground(False)
        self.imgLabelIn.setText("")
        self.imgLabelIn.setScaledContents(True)
        self.imgLabelIn.setObjectName("imgLabelIn")
        self.horizontalLayout_5.addWidget(self.imgLabelIn)
        self.input.addWidget(self.image_in)
        self.video_in = VideoPlayer()
        self.video_in.setObjectName("video_in")
        self.input.addWidget(self.video_in)
        self.horizontalLayout_3.addWidget(self.input)
        self.output = QtWidgets.QStackedWidget(self.centralwidget)
        self.output.setMinimumSize(QtCore.QSize(0, 0))
        self.output.setObjectName("output")
        self.image_out = QtWidgets.QWidget()
        self.image_out.setObjectName("image_out")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.image_out)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.imgLabelOut = QtWidgets.QLabel(self.image_out)
        self.imgLabelOut.setMinimumSize(QtCore.QSize(100, 100))
        self.imgLabelOut.setText("")
        self.imgLabelOut.setScaledContents(True)
        self.imgLabelOut.setObjectName("imgLabelOut")
        self.horizontalLayout_6.addWidget(self.imgLabelOut)
        self.output.addWidget(self.image_out)
        self.video_out = VideoPlayer()
        self.video_out.setObjectName("video_out")
        self.output.addWidget(self.video_out)
        self.horizontalLayout_3.addWidget(self.output)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.input.setCurrentIndex(0)
        self.output.setCurrentIndex(0)
        self.importImageBtn.clicked.connect(MainWindow.importImage)
        self.importVideoBtn.clicked.connect(MainWindow.importVideo)
        self.colorizeVideoBtn.clicked.connect(MainWindow.colorizeVideoClicked)
        self.colorizeImageBtn.clicked.connect(MainWindow.colorizeImageClicked)
        self.modelDropdown.currentIndexChanged['int'].connect(MainWindow.getModel)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.modelDropdown.setCurrentText(_translate("MainWindow", "Choose Model"))
        self.modelDropdown.setItemText(0, _translate("MainWindow", "Choose Model"))
        self.modelDropdown.setItemText(1, _translate("MainWindow", "Pre-trained model"))
        self.modelDropdown.setItemText(2, _translate("MainWindow", "Self-trained model"))
        self.modelDropdown.setItemText(3, _translate("MainWindow", "Self-trained model on faces"))
        self.importImageBtn.setText(_translate("MainWindow", "Import image"))
        self.importVideoBtn.setText(_translate("MainWindow", "Import video"))
        self.colorizeImageBtn.setText(_translate("MainWindow", "Colorize"))
        self.colorizeVideoBtn.setText(_translate("MainWindow", "Colorize"))
        self.loadingText.setText(_translate("MainWindow", "Colorizing..."))

from app.VideoPlayer import VideoPlayer
import app.logg_rc
