# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newProject.ui'
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
    QSizePolicy, QWidget)

class Ui_addNewProject(object):
    def setupUi(self, addNewProject):
        if not addNewProject.objectName():
            addNewProject.setObjectName(u"addNewProject")
        addNewProject.resize(450, 232)
        icon = QIcon()
        icon.addFile(u"../images/icon_16.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        addNewProject.setWindowIcon(icon)
        self.widget = QWidget(addNewProject)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(12, 20, 421, 191))
        self.addProjectLayout = QGridLayout(self.widget)
        self.addProjectLayout.setObjectName(u"addProjectLayout")
        self.addProjectLayout.setContentsMargins(0, 0, 0, 0)
        self.projectButtonsLayout = QHBoxLayout()
        self.projectButtonsLayout.setObjectName(u"projectButtonsLayout")
        self.addEveryday = QPushButton(self.widget)
        self.addEveryday.setObjectName(u"addEveryday")
        self.addEveryday.setEnabled(True)
        self.addEveryday.setMinimumSize(QSize(131, 131))
        self.addEveryday.setMaximumSize(QSize(131, 131))

        self.projectButtonsLayout.addWidget(self.addEveryday)

        self.addProgramming = QPushButton(self.widget)
        self.addProgramming.setObjectName(u"addProgramming")
        self.addProgramming.setEnabled(True)
        self.addProgramming.setMinimumSize(QSize(131, 131))
        self.addProgramming.setMaximumSize(QSize(131, 131))

        self.projectButtonsLayout.addWidget(self.addProgramming)

        self.addRecurring = QPushButton(self.widget)
        self.addRecurring.setObjectName(u"addRecurring")
        self.addRecurring.setEnabled(True)
        self.addRecurring.setMinimumSize(QSize(131, 131))
        self.addRecurring.setMaximumSize(QSize(131, 131))

        self.projectButtonsLayout.addWidget(self.addRecurring)


        self.addProjectLayout.addLayout(self.projectButtonsLayout, 0, 0, 1, 1)

        self.projectMenuLayout = QHBoxLayout()
        self.projectMenuLayout.setObjectName(u"projectMenuLayout")
        self.returnToMainAddProject = QPushButton(self.widget)
        self.returnToMainAddProject.setObjectName(u"returnToMainAddProject")

        self.projectMenuLayout.addWidget(self.returnToMainAddProject)

        self.exitAddProject = QPushButton(self.widget)
        self.exitAddProject.setObjectName(u"exitAddProject")

        self.projectMenuLayout.addWidget(self.exitAddProject)


        self.addProjectLayout.addLayout(self.projectMenuLayout, 1, 0, 1, 1)


        self.retranslateUi(addNewProject)

        QMetaObject.connectSlotsByName(addNewProject)
    # setupUi

    def retranslateUi(self, addNewProject):
        addNewProject.setWindowTitle(QCoreApplication.translate("addNewProject", u"Project Planner 1.0 - Add new project", None))
        self.addEveryday.setText(QCoreApplication.translate("addNewProject", u"Add everyday\n"
"project", None))
        self.addProgramming.setText(QCoreApplication.translate("addNewProject", u"Add programming\n"
"project", None))
        self.addRecurring.setText(QCoreApplication.translate("addNewProject", u"Add recurring\n"
"project", None))
        self.returnToMainAddProject.setText(QCoreApplication.translate("addNewProject", u"Return to main menu", None))
        self.exitAddProject.setText(QCoreApplication.translate("addNewProject", u"Exit program", None))
    # retranslateUi

