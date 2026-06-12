# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewerTabs.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QWidget)

class Ui_Viewer(object):
    def setupUi(self, Viewer):
        if not Viewer.objectName():
            Viewer.setObjectName(u"Viewer")
        Viewer.resize(447, 600)
        self.viewer = QTabWidget(Viewer)
        self.viewer.setObjectName(u"viewer")
        self.viewer.setGeometry(QRect(10, 20, 431, 571))
        self.currentProjects = QWidget()
        self.currentProjects.setObjectName(u"currentProjects")
        self.tabWidget = QTabWidget(self.currentProjects)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 401, 481))
        self.everydayProjectsTab = QWidget()
        self.everydayProjectsTab.setObjectName(u"everydayProjectsTab")
        self.tabWidget.addTab(self.everydayProjectsTab, "")
        self.programmingProjects = QWidget()
        self.programmingProjects.setObjectName(u"programmingProjects")
        self.tabWidget.addTab(self.programmingProjects, "")
        self.allProjects = QWidget()
        self.allProjects.setObjectName(u"allProjects")
        self.tabWidget.addTab(self.allProjects, "")
        self.viewer.addTab(self.currentProjects, "")
        self.archive = QWidget()
        self.archive.setObjectName(u"archive")
        self.tabWidget_2 = QTabWidget(self.archive)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 10, 401, 481))
        self.everydayProjectsTab_2 = QWidget()
        self.everydayProjectsTab_2.setObjectName(u"everydayProjectsTab_2")
        self.tabWidget_2.addTab(self.everydayProjectsTab_2, "")
        self.programmingProjects_2 = QWidget()
        self.programmingProjects_2.setObjectName(u"programmingProjects_2")
        self.tabWidget_2.addTab(self.programmingProjects_2, "")
        self.allProjects_2 = QWidget()
        self.allProjects_2.setObjectName(u"allProjects_2")
        self.tabWidget_2.addTab(self.allProjects_2, "")
        self.viewer.addTab(self.archive, "")

        self.retranslateUi(Viewer)

        self.viewer.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Viewer)
    # setupUi

    def retranslateUi(self, Viewer):
        Viewer.setWindowTitle(QCoreApplication.translate("Viewer", u"Project Planner 1.0 - Viewer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.everydayProjectsTab), QCoreApplication.translate("Viewer", u"Everyday projects", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.programmingProjects), QCoreApplication.translate("Viewer", u"Programming projects", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.allProjects), QCoreApplication.translate("Viewer", u"All projects", None))
        self.viewer.setTabText(self.viewer.indexOf(self.currentProjects), QCoreApplication.translate("Viewer", u"Current projects", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.everydayProjectsTab_2), QCoreApplication.translate("Viewer", u"Everyday projects", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.programmingProjects_2), QCoreApplication.translate("Viewer", u"Programming projects", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.allProjects_2), QCoreApplication.translate("Viewer", u"All projects", None))
        self.viewer.setTabText(self.viewer.indexOf(self.archive), QCoreApplication.translate("Viewer", u"Archive", None))
    # retranslateUi

