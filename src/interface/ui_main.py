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

class Ui_ProjectPlannerMain(object):
    def setupUi(self, ProjectPlannerMain):
        if not ProjectPlannerMain.objectName():
            ProjectPlannerMain.setObjectName(u"ProjectPlannerMain")
        ProjectPlannerMain.resize(447, 600)
        self.centralwidget = QWidget(ProjectPlannerMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainHeader = QLabel(self.centralwidget)
        self.mainHeader.setObjectName(u"mainHeader")
        self.mainHeader.setGeometry(QRect(100, 50, 271, 81))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainHeader.sizePolicy().hasHeightForWidth())
        self.mainHeader.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.mainHeader.setFont(font)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 250, 423, 282))
        self.mainMenuLayout = QGridLayout(self.widget)
        self.mainMenuLayout.setObjectName(u"mainMenuLayout")
        self.mainMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.viewArchivePushButton = QPushButton(self.widget)
        self.viewArchivePushButton.setObjectName(u"viewArchivePushButton")
        self.viewArchivePushButton.setMinimumSize(QSize(131, 131))
        self.viewArchivePushButton.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.viewArchivePushButton, 1, 0, 1, 1)

        self.addProjectPushButton = QPushButton(self.widget)
        self.addProjectPushButton.setObjectName(u"addProjectPushButton")
        self.addProjectPushButton.setEnabled(True)
        self.addProjectPushButton.setMinimumSize(QSize(131, 131))
        self.addProjectPushButton.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.addProjectPushButton, 0, 0, 1, 1)

        self.mainExitPushButton = QPushButton(self.widget)
        self.mainExitPushButton.setObjectName(u"mainExitPushButton")
        self.mainExitPushButton.setMinimumSize(QSize(131, 131))
        self.mainExitPushButton.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.mainExitPushButton, 1, 1, 1, 1)

        self.viewProjectsPushButton = QPushButton(self.widget)
        self.viewProjectsPushButton.setObjectName(u"viewProjectsPushButton")
        self.viewProjectsPushButton.setMinimumSize(QSize(131, 131))
        self.viewProjectsPushButton.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.viewProjectsPushButton, 0, 1, 1, 1)

        ProjectPlannerMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ProjectPlannerMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 447, 19))
        ProjectPlannerMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ProjectPlannerMain)
        self.statusbar.setObjectName(u"statusbar")
        ProjectPlannerMain.setStatusBar(self.statusbar)

        self.retranslateUi(ProjectPlannerMain)

        QMetaObject.connectSlotsByName(ProjectPlannerMain)
    # setupUi

    def retranslateUi(self, ProjectPlannerMain):
        ProjectPlannerMain.setWindowTitle(QCoreApplication.translate("ProjectPlannerMain", u"Project Planner 1.0 - Main menu", None))
        self.mainHeader.setText(QCoreApplication.translate("ProjectPlannerMain", u"Project Planner 1.0", None))
        self.viewArchivePushButton.setText(QCoreApplication.translate("ProjectPlannerMain", u"View archive", None))
        self.addProjectPushButton.setText(QCoreApplication.translate("ProjectPlannerMain", u"Add project", None))
        self.mainExitPushButton.setText(QCoreApplication.translate("ProjectPlannerMain", u"Exit", None))
        self.viewProjectsPushButton.setText(QCoreApplication.translate("ProjectPlannerMain", u"View projects", None))
    # retranslateUi

