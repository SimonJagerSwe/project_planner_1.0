# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        if not mainMenu.objectName():
            mainMenu.setObjectName(u"mainMenu")
        mainMenu.resize(447, 600)
        self.centralwidget = QWidget(mainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainHeader = QLabel(self.centralwidget)
        self.mainHeader.setObjectName(u"mainHeader")
        self.mainHeader.setGeometry(QRect(100, 40, 271, 81))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainHeader.sizePolicy().hasHeightForWidth())
        self.mainHeader.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.mainHeader.setFont(font)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 240, 423, 282))
        self.mainMenuLayout = QGridLayout(self.layoutWidget)
        self.mainMenuLayout.setObjectName(u"mainMenuLayout")
        self.mainMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.viewArchive = QPushButton(self.layoutWidget)
        self.viewArchive.setObjectName(u"viewArchive")
        self.viewArchive.setMinimumSize(QSize(131, 131))
        self.viewArchive.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.viewArchive, 1, 0, 1, 1)

        self.addProject = QPushButton(self.layoutWidget)
        self.addProject.setObjectName(u"addProject")
        self.addProject.setEnabled(True)
        self.addProject.setMinimumSize(QSize(131, 131))
        self.addProject.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.addProject, 0, 0, 1, 1)

        self.mainExit = QPushButton(self.layoutWidget)
        self.mainExit.setObjectName(u"mainExit")
        self.mainExit.setMinimumSize(QSize(131, 131))
        self.mainExit.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.mainExit, 1, 1, 1, 1)

        self.viewProjects = QPushButton(self.layoutWidget)
        self.viewProjects.setObjectName(u"viewProjects")
        self.viewProjects.setMinimumSize(QSize(131, 131))
        self.viewProjects.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.viewProjects, 0, 1, 1, 1)

        mainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 447, 19))
        mainMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainMenu)
        self.statusbar.setObjectName(u"statusbar")
        mainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(mainMenu)

        QMetaObject.connectSlotsByName(mainMenu)
    # setupUi

    def retranslateUi(self, mainMenu):
        mainMenu.setWindowTitle(QCoreApplication.translate("mainMenu", u"Project Planner 1.0 - Main menu", None))
        self.mainHeader.setText(QCoreApplication.translate("mainMenu", u"Project Planner 1.0", None))
        self.viewArchive.setText(QCoreApplication.translate("mainMenu", u"View archive", None))
        self.addProject.setText(QCoreApplication.translate("mainMenu", u"Add project", None))
        self.mainExit.setText(QCoreApplication.translate("mainMenu", u"Exit", None))
        self.viewProjects.setText(QCoreApplication.translate("mainMenu", u"View projects", None))
    # retranslateUi

