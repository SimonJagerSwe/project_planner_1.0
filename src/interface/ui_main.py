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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_ProjectPlannerMain(object):
    def setupUi(self, ProjectPlannerMain):
        if not ProjectPlannerMain.objectName():
            ProjectPlannerMain.setObjectName(u"ProjectPlannerMain")
        ProjectPlannerMain.resize(447, 600)
        self.actionAdd_project = QAction(ProjectPlannerMain)
        self.actionAdd_project.setObjectName(u"actionAdd_project")
        self.actionView_projects = QAction(ProjectPlannerMain)
        self.actionView_projects.setObjectName(u"actionView_projects")
        self.actionView_archive = QAction(ProjectPlannerMain)
        self.actionView_archive.setObjectName(u"actionView_archive")
        self.actionExit_program = QAction(ProjectPlannerMain)
        self.actionExit_program.setObjectName(u"actionExit_program")
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
        self.viewArchive = QPushButton(self.widget)
        self.viewArchive.setObjectName(u"viewArchive")
        self.viewArchive.setMinimumSize(QSize(131, 131))
        self.viewArchive.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.viewArchive, 1, 0, 1, 1)

        self.addProject = QPushButton(self.widget)
        self.addProject.setObjectName(u"addProject")
        self.addProject.setEnabled(True)
        self.addProject.setMinimumSize(QSize(131, 131))
        self.addProject.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.addProject, 0, 0, 1, 1)

        self.mainExit = QPushButton(self.widget)
        self.mainExit.setObjectName(u"mainExit")
        self.mainExit.setMinimumSize(QSize(131, 131))
        self.mainExit.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.mainExit, 1, 1, 1, 1)

        self.viewProjects = QPushButton(self.widget)
        self.viewProjects.setObjectName(u"viewProjects")
        self.viewProjects.setMinimumSize(QSize(131, 131))
        self.viewProjects.setMaximumSize(QSize(131, 131))

        self.mainMenuLayout.addWidget(self.viewProjects, 0, 1, 1, 1)

        ProjectPlannerMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ProjectPlannerMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 447, 19))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        ProjectPlannerMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ProjectPlannerMain)
        self.statusbar.setObjectName(u"statusbar")
        ProjectPlannerMain.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionAdd_project)
        self.menuMenu.addAction(self.actionView_projects)
        self.menuMenu.addAction(self.actionView_archive)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit_program)

        self.retranslateUi(ProjectPlannerMain)

        QMetaObject.connectSlotsByName(ProjectPlannerMain)
    # setupUi

    def retranslateUi(self, ProjectPlannerMain):
        ProjectPlannerMain.setWindowTitle(QCoreApplication.translate("ProjectPlannerMain", u"Project Planner 1.0 - Main menu", None))
        self.actionAdd_project.setText(QCoreApplication.translate("ProjectPlannerMain", u"Add project", None))
        self.actionView_projects.setText(QCoreApplication.translate("ProjectPlannerMain", u"View projects", None))
        self.actionView_archive.setText(QCoreApplication.translate("ProjectPlannerMain", u"View archive", None))
        self.actionExit_program.setText(QCoreApplication.translate("ProjectPlannerMain", u"Exit program", None))
        self.mainHeader.setText(QCoreApplication.translate("ProjectPlannerMain", u"Project Planner 1.0", None))
        self.viewArchive.setText(QCoreApplication.translate("ProjectPlannerMain", u"View archive", None))
        self.addProject.setText(QCoreApplication.translate("ProjectPlannerMain", u"Add project", None))
        self.mainExit.setText(QCoreApplication.translate("ProjectPlannerMain", u"Exit", None))
        self.viewProjects.setText(QCoreApplication.translate("ProjectPlannerMain", u"View projects", None))
        self.menuMenu.setTitle(QCoreApplication.translate("ProjectPlannerMain", u"Menu", None))
    # retranslateUi

