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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_Viewer(object):
    def setupUi(self, Viewer):
        if not Viewer.objectName():
            Viewer.setObjectName(u"Viewer")
        Viewer.resize(447, 600)
        icon = QIcon()
        icon.addFile(u"../images/icon_16.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Viewer.setWindowIcon(icon)
        self.viewer = QTabWidget(Viewer)
        self.viewer.setObjectName(u"viewer")
        self.viewer.setGeometry(QRect(10, 20, 431, 571))
        self.currentProjects = QWidget()
        self.currentProjects.setObjectName(u"currentProjects")
        self.gridLayout_2 = QGridLayout(self.currentProjects)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.currentProjects)
        self.tabWidget.setObjectName(u"tabWidget")
        self.everydayProjectsTab = QWidget()
        self.everydayProjectsTab.setObjectName(u"everydayProjectsTab")
        self.tabWidget.addTab(self.everydayProjectsTab, "")
        self.programmingProjects = QWidget()
        self.programmingProjects.setObjectName(u"programmingProjects")
        self.tabWidget.addTab(self.programmingProjects, "")
        self.allProjects = QWidget()
        self.allProjects.setObjectName(u"allProjects")
        self.tabWidget.addTab(self.allProjects, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.projectButtonsLayout = QGridLayout()
        self.projectButtonsLayout.setObjectName(u"projectButtonsLayout")
        self.projectManagerLayout = QHBoxLayout()
        self.projectManagerLayout.setObjectName(u"projectManagerLayout")
        self.editProject = QPushButton(self.currentProjects)
        self.editProject.setObjectName(u"editProject")

        self.projectManagerLayout.addWidget(self.editProject)

        self.archiveProject = QPushButton(self.currentProjects)
        self.archiveProject.setObjectName(u"archiveProject")

        self.projectManagerLayout.addWidget(self.archiveProject)

        self.deleteProject = QPushButton(self.currentProjects)
        self.deleteProject.setObjectName(u"deleteProject")

        self.projectManagerLayout.addWidget(self.deleteProject)


        self.projectButtonsLayout.addLayout(self.projectManagerLayout, 0, 0, 1, 1)

        self.projectsNavigatorLayout = QHBoxLayout()
        self.projectsNavigatorLayout.setObjectName(u"projectsNavigatorLayout")
        self.returnToMainProjects = QPushButton(self.currentProjects)
        self.returnToMainProjects.setObjectName(u"returnToMainProjects")

        self.projectsNavigatorLayout.addWidget(self.returnToMainProjects)

        self.exitProjects = QPushButton(self.currentProjects)
        self.exitProjects.setObjectName(u"exitProjects")

        self.projectsNavigatorLayout.addWidget(self.exitProjects)


        self.projectButtonsLayout.addLayout(self.projectsNavigatorLayout, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.projectButtonsLayout, 1, 0, 1, 1)

        self.viewer.addTab(self.currentProjects, "")
        self.archive = QWidget()
        self.archive.setObjectName(u"archive")
        self.tabWidget_2 = QTabWidget(self.archive)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 10, 411, 461))
        self.everydayProjectsTab_2 = QWidget()
        self.everydayProjectsTab_2.setObjectName(u"everydayProjectsTab_2")
        self.tabWidget_2.addTab(self.everydayProjectsTab_2, "")
        self.programmingProjects_2 = QWidget()
        self.programmingProjects_2.setObjectName(u"programmingProjects_2")
        self.tabWidget_2.addTab(self.programmingProjects_2, "")
        self.allProjects_2 = QWidget()
        self.allProjects_2.setObjectName(u"allProjects_2")
        self.tabWidget_2.addTab(self.allProjects_2, "")
        self.widget = QWidget(self.archive)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 480, 411, 56))
        self.archiveButtonsLayout = QGridLayout(self.widget)
        self.archiveButtonsLayout.setObjectName(u"archiveButtonsLayout")
        self.archiveButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.archiveManagerLayout = QHBoxLayout()
        self.archiveManagerLayout.setObjectName(u"archiveManagerLayout")
        self.restoreArchivedProject = QPushButton(self.widget)
        self.restoreArchivedProject.setObjectName(u"restoreArchivedProject")

        self.archiveManagerLayout.addWidget(self.restoreArchivedProject)

        self.deletArchivedProject = QPushButton(self.widget)
        self.deletArchivedProject.setObjectName(u"deletArchivedProject")

        self.archiveManagerLayout.addWidget(self.deletArchivedProject)


        self.archiveButtonsLayout.addLayout(self.archiveManagerLayout, 0, 0, 1, 1)

        self.archiveNavigatorLayout = QHBoxLayout()
        self.archiveNavigatorLayout.setObjectName(u"archiveNavigatorLayout")
        self.returnToMainArchive = QPushButton(self.widget)
        self.returnToMainArchive.setObjectName(u"returnToMainArchive")

        self.archiveNavigatorLayout.addWidget(self.returnToMainArchive)

        self.exitArchive = QPushButton(self.widget)
        self.exitArchive.setObjectName(u"exitArchive")

        self.archiveNavigatorLayout.addWidget(self.exitArchive)


        self.archiveButtonsLayout.addLayout(self.archiveNavigatorLayout, 1, 0, 1, 1)

        self.viewer.addTab(self.archive, "")

        self.retranslateUi(Viewer)

        self.viewer.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Viewer)
    # setupUi

    def retranslateUi(self, Viewer):
        Viewer.setWindowTitle(QCoreApplication.translate("Viewer", u"Project Planner 1.0 - Viewer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.everydayProjectsTab), QCoreApplication.translate("Viewer", u"Everyday projects", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.programmingProjects), QCoreApplication.translate("Viewer", u"Programming projects", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.allProjects), QCoreApplication.translate("Viewer", u"All projects", None))
        self.editProject.setText(QCoreApplication.translate("Viewer", u"Edit project", None))
        self.archiveProject.setText(QCoreApplication.translate("Viewer", u"Archive project", None))
        self.deleteProject.setText(QCoreApplication.translate("Viewer", u"Delete project", None))
        self.returnToMainProjects.setText(QCoreApplication.translate("Viewer", u"Return to main menu", None))
        self.exitProjects.setText(QCoreApplication.translate("Viewer", u"Exit program", None))
        self.viewer.setTabText(self.viewer.indexOf(self.currentProjects), QCoreApplication.translate("Viewer", u"Current projects", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.everydayProjectsTab_2), QCoreApplication.translate("Viewer", u"Everyday projects", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.programmingProjects_2), QCoreApplication.translate("Viewer", u"Programming projects", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.allProjects_2), QCoreApplication.translate("Viewer", u"All projects", None))
        self.restoreArchivedProject.setText(QCoreApplication.translate("Viewer", u"Restore project", None))
        self.deletArchivedProject.setText(QCoreApplication.translate("Viewer", u"Delete from archive", None))
        self.returnToMainArchive.setText(QCoreApplication.translate("Viewer", u"Return to main menu", None))
        self.exitArchive.setText(QCoreApplication.translate("Viewer", u"Exit program", None))
        self.viewer.setTabText(self.viewer.indexOf(self.archive), QCoreApplication.translate("Viewer", u"Archive", None))
    # retranslateUi

