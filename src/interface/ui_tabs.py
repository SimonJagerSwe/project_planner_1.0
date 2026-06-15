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
        Viewer.resize(592, 600)
        icon = QIcon()
        icon.addFile(u"../images/icon_16.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Viewer.setWindowIcon(icon)
        self.viewer = QTabWidget(Viewer)
        self.viewer.setObjectName(u"viewer")
        self.viewer.setGeometry(QRect(0, 10, 571, 571))
        self.currentProjects = QWidget()
        self.currentProjects.setObjectName(u"currentProjects")
        self.gridLayout_2 = QGridLayout(self.currentProjects)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.projectTabs = QTabWidget(self.currentProjects)
        self.projectTabs.setObjectName(u"projectTabs")
        self.everydayProjectsTab = QWidget()
        self.everydayProjectsTab.setObjectName(u"everydayProjectsTab")
        self.projectTabs.addTab(self.everydayProjectsTab, "")
        self.programmingProjects = QWidget()
        self.programmingProjects.setObjectName(u"programmingProjects")
        self.projectTabs.addTab(self.programmingProjects, "")
        self.allProjects = QWidget()
        self.allProjects.setObjectName(u"allProjects")
        self.projectTabs.addTab(self.allProjects, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.projectTabs.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.projectTabs, 0, 0, 1, 1)

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
        self.archivedTabs = QTabWidget(self.archive)
        self.archivedTabs.setObjectName(u"archivedTabs")
        self.archivedTabs.setGeometry(QRect(8, 10, 551, 463))
        self.everydayArchive = QWidget()
        self.everydayArchive.setObjectName(u"everydayArchive")
        self.archivedTabs.addTab(self.everydayArchive, "")
        self.programmingArchive = QWidget()
        self.programmingArchive.setObjectName(u"programmingArchive")
        self.archivedTabs.addTab(self.programmingArchive, "")
        self.fullArchive = QWidget()
        self.fullArchive.setObjectName(u"fullArchive")
        self.archivedTabs.addTab(self.fullArchive, "")
        self.layoutWidget = QWidget(self.archive)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 480, 549, 56))
        self.archiveButtonsLayout = QGridLayout(self.layoutWidget)
        self.archiveButtonsLayout.setObjectName(u"archiveButtonsLayout")
        self.archiveButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.archiveManagerLayout = QHBoxLayout()
        self.archiveManagerLayout.setObjectName(u"archiveManagerLayout")
        self.restoreProject = QPushButton(self.layoutWidget)
        self.restoreProject.setObjectName(u"restoreProject")

        self.archiveManagerLayout.addWidget(self.restoreProject)

        self.deleteArchived = QPushButton(self.layoutWidget)
        self.deleteArchived.setObjectName(u"deleteArchived")

        self.archiveManagerLayout.addWidget(self.deleteArchived)


        self.archiveButtonsLayout.addLayout(self.archiveManagerLayout, 0, 0, 1, 1)

        self.archiveNavigatorLayout = QHBoxLayout()
        self.archiveNavigatorLayout.setObjectName(u"archiveNavigatorLayout")
        self.returnToMainArchive = QPushButton(self.layoutWidget)
        self.returnToMainArchive.setObjectName(u"returnToMainArchive")

        self.archiveNavigatorLayout.addWidget(self.returnToMainArchive)

        self.exitArchive = QPushButton(self.layoutWidget)
        self.exitArchive.setObjectName(u"exitArchive")

        self.archiveNavigatorLayout.addWidget(self.exitArchive)


        self.archiveButtonsLayout.addLayout(self.archiveNavigatorLayout, 1, 0, 1, 1)

        self.viewer.addTab(self.archive, "")

        self.retranslateUi(Viewer)

        self.viewer.setCurrentIndex(1)
        self.projectTabs.setCurrentIndex(3)
        self.archivedTabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Viewer)
    # setupUi

    def retranslateUi(self, Viewer):
        Viewer.setWindowTitle(QCoreApplication.translate("Viewer", u"Project Planner 1.0 - Viewer", None))
        self.projectTabs.setTabText(self.projectTabs.indexOf(self.everydayProjectsTab), QCoreApplication.translate("Viewer", u"Everyday projects", None))
        self.projectTabs.setTabText(self.projectTabs.indexOf(self.programmingProjects), QCoreApplication.translate("Viewer", u"Programming projects", None))
        self.projectTabs.setTabText(self.projectTabs.indexOf(self.allProjects), QCoreApplication.translate("Viewer", u"All projects", None))
        self.projectTabs.setTabText(self.projectTabs.indexOf(self.tab), QCoreApplication.translate("Viewer", u"Recurring projects", None))
        self.editProject.setText(QCoreApplication.translate("Viewer", u"Edit project", None))
        self.archiveProject.setText(QCoreApplication.translate("Viewer", u"Archive project", None))
        self.deleteProject.setText(QCoreApplication.translate("Viewer", u"Delete project", None))
        self.returnToMainProjects.setText(QCoreApplication.translate("Viewer", u"Return to main menu", None))
        self.exitProjects.setText(QCoreApplication.translate("Viewer", u"Exit program", None))
        self.viewer.setTabText(self.viewer.indexOf(self.currentProjects), QCoreApplication.translate("Viewer", u"Current projects", None))
        self.archivedTabs.setTabText(self.archivedTabs.indexOf(self.everydayArchive), QCoreApplication.translate("Viewer", u"Everyday projects", None))
        self.archivedTabs.setTabText(self.archivedTabs.indexOf(self.programmingArchive), QCoreApplication.translate("Viewer", u"Programming projects", None))
        self.archivedTabs.setTabText(self.archivedTabs.indexOf(self.fullArchive), QCoreApplication.translate("Viewer", u"All projects", None))
        self.restoreProject.setText(QCoreApplication.translate("Viewer", u"Restore", None))
        self.deleteArchived.setText(QCoreApplication.translate("Viewer", u"Delete project", None))
        self.returnToMainArchive.setText(QCoreApplication.translate("Viewer", u"Return to main menu", None))
        self.exitArchive.setText(QCoreApplication.translate("Viewer", u"Exit program", None))
        self.viewer.setTabText(self.viewer.indexOf(self.archive), QCoreApplication.translate("Viewer", u"Archive", None))
    # retranslateUi

