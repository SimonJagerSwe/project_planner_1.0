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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Viewer(object):
    def setupUi(self, Viewer):
        if not Viewer.objectName():
            Viewer.setObjectName(u"Viewer")
        Viewer.resize(592, 600)
        icon = QIcon()
        icon.addFile(u"../images/icon_16.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Viewer.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Viewer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.viewer = QTabWidget(Viewer)
        self.viewer.setObjectName(u"viewer")
        self.currentProjects = QWidget()
        self.currentProjects.setObjectName(u"currentProjects")
        self.layoutWidget = QWidget(self.currentProjects)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 551, 531))
        self.projectTabLayout = QGridLayout(self.layoutWidget)
        self.projectTabLayout.setObjectName(u"projectTabLayout")
        self.projectTabLayout.setContentsMargins(0, 0, 0, 0)
        self.projectMenuLayout = QGridLayout()
        self.projectMenuLayout.setObjectName(u"projectMenuLayout")
        self.projectManagerLayout = QHBoxLayout()
        self.projectManagerLayout.setObjectName(u"projectManagerLayout")
        self.editProject = QPushButton(self.layoutWidget)
        self.editProject.setObjectName(u"editProject")

        self.projectManagerLayout.addWidget(self.editProject)

        self.archiveProject = QPushButton(self.layoutWidget)
        self.archiveProject.setObjectName(u"archiveProject")

        self.projectManagerLayout.addWidget(self.archiveProject)

        self.deleteProject = QPushButton(self.layoutWidget)
        self.deleteProject.setObjectName(u"deleteProject")

        self.projectManagerLayout.addWidget(self.deleteProject)


        self.projectMenuLayout.addLayout(self.projectManagerLayout, 0, 0, 1, 1)

        self.projectsNavigatorLayout = QHBoxLayout()
        self.projectsNavigatorLayout.setObjectName(u"projectsNavigatorLayout")
        self.returnToMainProjects = QPushButton(self.layoutWidget)
        self.returnToMainProjects.setObjectName(u"returnToMainProjects")

        self.projectsNavigatorLayout.addWidget(self.returnToMainProjects)

        self.exitProjects = QPushButton(self.layoutWidget)
        self.exitProjects.setObjectName(u"exitProjects")

        self.projectsNavigatorLayout.addWidget(self.exitProjects)


        self.projectMenuLayout.addLayout(self.projectsNavigatorLayout, 1, 0, 1, 1)


        self.projectTabLayout.addLayout(self.projectMenuLayout, 1, 0, 1, 1)

        self.projectTabs = QTabWidget(self.layoutWidget)
        self.projectTabs.setObjectName(u"projectTabs")
        self.projectTabs.setEnabled(True)
        self.projectTabs.setMinimumSize(QSize(0, 0))
        self.projectTabs.setTabShape(QTabWidget.TabShape.Rounded)
        self.everydayProjectsTab = QWidget()
        self.everydayProjectsTab.setObjectName(u"everydayProjectsTab")
        self.everydayProjects = QListWidget(self.everydayProjectsTab)
        self.everydayProjects.setObjectName(u"everydayProjects")
        self.everydayProjects.setGeometry(QRect(10, 10, 521, 421))
        self.projectTabs.addTab(self.everydayProjectsTab, "")
        self.programmingProjectsTab = QWidget()
        self.programmingProjectsTab.setObjectName(u"programmingProjectsTab")
        self.programmingProjects = QListWidget(self.programmingProjectsTab)
        self.programmingProjects.setObjectName(u"programmingProjects")
        self.programmingProjects.setGeometry(QRect(10, 10, 521, 421))
        self.projectTabs.addTab(self.programmingProjectsTab, "")
        self.allProjectsTab = QWidget()
        self.allProjectsTab.setObjectName(u"allProjectsTab")
        self.allProjects = QListWidget(self.allProjectsTab)
        self.allProjects.setObjectName(u"allProjects")
        self.allProjects.setGeometry(QRect(10, 10, 521, 421))
        self.projectTabs.addTab(self.allProjectsTab, "")
        self.recurringProjectsTab = QWidget()
        self.recurringProjectsTab.setObjectName(u"recurringProjectsTab")
        self.layoutWidget1 = QWidget(self.recurringProjectsTab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(12, 12, 521, 121))
        self.weeklyGrid = QGridLayout(self.layoutWidget1)
        self.weeklyGrid.setObjectName(u"weeklyGrid")
        self.weeklyGrid.setContentsMargins(0, 0, 0, 0)
        self.weeklyLabel = QLabel(self.layoutWidget1)
        self.weeklyLabel.setObjectName(u"weeklyLabel")
        font = QFont()
        font.setBold(True)
        self.weeklyLabel.setFont(font)

        self.weeklyGrid.addWidget(self.weeklyLabel, 0, 0, 1, 1)

        self.recurringWeekly = QListWidget(self.layoutWidget1)
        self.recurringWeekly.setObjectName(u"recurringWeekly")

        self.weeklyGrid.addWidget(self.recurringWeekly, 1, 0, 1, 1)

        self.weeklyButtonLayout = QVBoxLayout()
        self.weeklyButtonLayout.setObjectName(u"weeklyButtonLayout")
        self.weeklyDone = QPushButton(self.layoutWidget1)
        self.weeklyDone.setObjectName(u"weeklyDone")

        self.weeklyButtonLayout.addWidget(self.weeklyDone)

        self.weeklyResetTask = QPushButton(self.layoutWidget1)
        self.weeklyResetTask.setObjectName(u"weeklyResetTask")

        self.weeklyButtonLayout.addWidget(self.weeklyResetTask)

        self.weeklyResetAll = QPushButton(self.layoutWidget1)
        self.weeklyResetAll.setObjectName(u"weeklyResetAll")

        self.weeklyButtonLayout.addWidget(self.weeklyResetAll)


        self.weeklyGrid.addLayout(self.weeklyButtonLayout, 1, 1, 1, 1)

        self.layoutWidget2 = QWidget(self.recurringProjectsTab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(11, 151, 521, 121))
        self.biGrid = QGridLayout(self.layoutWidget2)
        self.biGrid.setObjectName(u"biGrid")
        self.biGrid.setContentsMargins(0, 0, 0, 0)
        self.biLabel = QLabel(self.layoutWidget2)
        self.biLabel.setObjectName(u"biLabel")
        self.biLabel.setFont(font)

        self.biGrid.addWidget(self.biLabel, 0, 0, 1, 1)

        self.recurringBi = QListWidget(self.layoutWidget2)
        self.recurringBi.setObjectName(u"recurringBi")

        self.biGrid.addWidget(self.recurringBi, 1, 0, 1, 1)

        self.biButtonLayout = QVBoxLayout()
        self.biButtonLayout.setObjectName(u"biButtonLayout")
        self.biDone = QPushButton(self.layoutWidget2)
        self.biDone.setObjectName(u"biDone")

        self.biButtonLayout.addWidget(self.biDone)

        self.biResetTask = QPushButton(self.layoutWidget2)
        self.biResetTask.setObjectName(u"biResetTask")

        self.biButtonLayout.addWidget(self.biResetTask)

        self.biResetAll = QPushButton(self.layoutWidget2)
        self.biResetAll.setObjectName(u"biResetAll")

        self.biButtonLayout.addWidget(self.biResetAll)


        self.biGrid.addLayout(self.biButtonLayout, 1, 1, 1, 1)

        self.layoutWidget3 = QWidget(self.recurringProjectsTab)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(11, 301, 521, 111))
        self.otherGrid = QGridLayout(self.layoutWidget3)
        self.otherGrid.setObjectName(u"otherGrid")
        self.otherGrid.setContentsMargins(0, 0, 0, 0)
        self.otherLabel = QLabel(self.layoutWidget3)
        self.otherLabel.setObjectName(u"otherLabel")
        self.otherLabel.setFont(font)

        self.otherGrid.addWidget(self.otherLabel, 0, 0, 1, 1)

        self.recurringOther = QListWidget(self.layoutWidget3)
        self.recurringOther.setObjectName(u"recurringOther")

        self.otherGrid.addWidget(self.recurringOther, 1, 0, 1, 1)

        self.otherButtonLayout = QVBoxLayout()
        self.otherButtonLayout.setObjectName(u"otherButtonLayout")
        self.otherDone = QPushButton(self.layoutWidget3)
        self.otherDone.setObjectName(u"otherDone")

        self.otherButtonLayout.addWidget(self.otherDone)

        self.otherReset = QPushButton(self.layoutWidget3)
        self.otherReset.setObjectName(u"otherReset")

        self.otherButtonLayout.addWidget(self.otherReset)


        self.otherGrid.addLayout(self.otherButtonLayout, 1, 1, 1, 1)

        self.projectTabs.addTab(self.recurringProjectsTab, "")

        self.projectTabLayout.addWidget(self.projectTabs, 0, 0, 1, 1)

        self.viewer.addTab(self.currentProjects, "")
        self.archive = QWidget()
        self.archive.setObjectName(u"archive")
        self.layoutWidget4 = QWidget(self.archive)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(9, 9, 551, 531))
        self.archiveTabLayout = QGridLayout(self.layoutWidget4)
        self.archiveTabLayout.setObjectName(u"archiveTabLayout")
        self.archiveTabLayout.setContentsMargins(0, 0, 0, 0)
        self.archivedTabs = QTabWidget(self.layoutWidget4)
        self.archivedTabs.setObjectName(u"archivedTabs")
        self.archivedTabs.setElideMode(Qt.TextElideMode.ElideNone)
        self.archivedTabs.setTabsClosable(False)
        self.everydayArchiveTab = QWidget()
        self.everydayArchiveTab.setObjectName(u"everydayArchiveTab")
        self.everydayArchive = QListWidget(self.everydayArchiveTab)
        self.everydayArchive.setObjectName(u"everydayArchive")
        self.everydayArchive.setGeometry(QRect(10, 10, 521, 421))
        self.archivedTabs.addTab(self.everydayArchiveTab, "")
        self.programmingArchiveTab = QWidget()
        self.programmingArchiveTab.setObjectName(u"programmingArchiveTab")
        self.programmingArchive = QListWidget(self.programmingArchiveTab)
        self.programmingArchive.setObjectName(u"programmingArchive")
        self.programmingArchive.setGeometry(QRect(10, 10, 521, 421))
        self.archivedTabs.addTab(self.programmingArchiveTab, "")
        self.fullArchiveTab = QWidget()
        self.fullArchiveTab.setObjectName(u"fullArchiveTab")
        self.fullArchive = QListWidget(self.fullArchiveTab)
        self.fullArchive.setObjectName(u"fullArchive")
        self.fullArchive.setGeometry(QRect(10, 10, 521, 421))
        self.archivedTabs.addTab(self.fullArchiveTab, "")

        self.archiveTabLayout.addWidget(self.archivedTabs, 0, 0, 1, 1)

        self.archiveMenuLayout = QGridLayout()
        self.archiveMenuLayout.setObjectName(u"archiveMenuLayout")
        self.archiveManagerLayout = QHBoxLayout()
        self.archiveManagerLayout.setObjectName(u"archiveManagerLayout")
        self.restoreArchived = QPushButton(self.layoutWidget4)
        self.restoreArchived.setObjectName(u"restoreArchived")

        self.archiveManagerLayout.addWidget(self.restoreArchived)

        self.deleteArchived = QPushButton(self.layoutWidget4)
        self.deleteArchived.setObjectName(u"deleteArchived")

        self.archiveManagerLayout.addWidget(self.deleteArchived)


        self.archiveMenuLayout.addLayout(self.archiveManagerLayout, 0, 0, 1, 1)

        self.archiveNavigatorLayout = QHBoxLayout()
        self.archiveNavigatorLayout.setObjectName(u"archiveNavigatorLayout")
        self.returnToMainArchive = QPushButton(self.layoutWidget4)
        self.returnToMainArchive.setObjectName(u"returnToMainArchive")

        self.archiveNavigatorLayout.addWidget(self.returnToMainArchive)

        self.exitArchive = QPushButton(self.layoutWidget4)
        self.exitArchive.setObjectName(u"exitArchive")

        self.archiveNavigatorLayout.addWidget(self.exitArchive)


        self.archiveMenuLayout.addLayout(self.archiveNavigatorLayout, 1, 0, 1, 1)


        self.archiveTabLayout.addLayout(self.archiveMenuLayout, 1, 0, 1, 1)

        self.viewer.addTab(self.archive, "")

        self.gridLayout.addWidget(self.viewer, 0, 0, 1, 1)


        self.retranslateUi(Viewer)

        self.viewer.setCurrentIndex(0)
        self.projectTabs.setCurrentIndex(3)
        self.archivedTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Viewer)
    # setupUi

    def retranslateUi(self, Viewer):
        Viewer.setWindowTitle(QCoreApplication.translate("Viewer", u"Project Planner 1.0 - Viewer", None))
        self.editProject.setText(QCoreApplication.translate("Viewer", u"Edit project", None))
        self.archiveProject.setText(QCoreApplication.translate("Viewer", u"Archive project", None))
        self.deleteProject.setText(QCoreApplication.translate("Viewer", u"Delete project", None))
        self.returnToMainProjects.setText(QCoreApplication.translate("Viewer", u"Return to main menu", None))
        self.exitProjects.setText(QCoreApplication.translate("Viewer", u"Exit program", None))
        self.projectTabs.setTabText(self.projectTabs.indexOf(self.everydayProjectsTab), QCoreApplication.translate("Viewer", u"Everyday projects", None))
        self.projectTabs.setTabText(self.projectTabs.indexOf(self.programmingProjectsTab), QCoreApplication.translate("Viewer", u"Programming projects", None))
        self.projectTabs.setTabText(self.projectTabs.indexOf(self.allProjectsTab), QCoreApplication.translate("Viewer", u"All projects", None))
        self.weeklyLabel.setText(QCoreApplication.translate("Viewer", u"Weekly tasks", None))
        self.weeklyDone.setText(QCoreApplication.translate("Viewer", u"Task done", None))
        self.weeklyResetTask.setText(QCoreApplication.translate("Viewer", u"Reset task", None))
        self.weeklyResetAll.setText(QCoreApplication.translate("Viewer", u"Reset all", None))
        self.biLabel.setText(QCoreApplication.translate("Viewer", u"Bi-weekly tasks", None))
        self.biDone.setText(QCoreApplication.translate("Viewer", u"Task done", None))
        self.biResetTask.setText(QCoreApplication.translate("Viewer", u"Reset task", None))
        self.biResetAll.setText(QCoreApplication.translate("Viewer", u"Reset all", None))
        self.otherLabel.setText(QCoreApplication.translate("Viewer", u"Other tasks", None))
        self.otherDone.setText(QCoreApplication.translate("Viewer", u"Task done", None))
        self.otherReset.setText(QCoreApplication.translate("Viewer", u"Reset task", None))
        self.projectTabs.setTabText(self.projectTabs.indexOf(self.recurringProjectsTab), QCoreApplication.translate("Viewer", u"Recurring tasks", None))
        self.viewer.setTabText(self.viewer.indexOf(self.currentProjects), QCoreApplication.translate("Viewer", u"Current projects", None))
        self.archivedTabs.setTabText(self.archivedTabs.indexOf(self.everydayArchiveTab), QCoreApplication.translate("Viewer", u"Everyday projects", None))
        self.archivedTabs.setTabText(self.archivedTabs.indexOf(self.programmingArchiveTab), QCoreApplication.translate("Viewer", u"Programming projects", None))
        self.archivedTabs.setTabText(self.archivedTabs.indexOf(self.fullArchiveTab), QCoreApplication.translate("Viewer", u"All projects", None))
        self.restoreArchived.setText(QCoreApplication.translate("Viewer", u"Restore", None))
        self.deleteArchived.setText(QCoreApplication.translate("Viewer", u"Delete project", None))
        self.returnToMainArchive.setText(QCoreApplication.translate("Viewer", u"Return to main menu", None))
        self.exitArchive.setText(QCoreApplication.translate("Viewer", u"Exit program", None))
        self.viewer.setTabText(self.viewer.indexOf(self.archive), QCoreApplication.translate("Viewer", u"Archive", None))
    # retranslateUi

