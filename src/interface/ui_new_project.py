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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(375, 290)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 351, 251))
        self.addProjectMenuLayout = QGridLayout(self.widget)
        self.addProjectMenuLayout.setObjectName(u"addProjectMenuLayout")
        self.addProjectMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.addProjectLayout = QHBoxLayout()
        self.addProjectLayout.setObjectName(u"addProjectLayout")
        self.addEveryday = QPushButton(self.widget)
        self.addEveryday.setObjectName(u"addEveryday")
        self.addEveryday.setEnabled(True)
        self.addEveryday.setMinimumSize(QSize(131, 131))
        self.addEveryday.setMaximumSize(QSize(131, 131))

        self.addProjectLayout.addWidget(self.addEveryday)

        self.addProgramming = QPushButton(self.widget)
        self.addProgramming.setObjectName(u"addProgramming")
        self.addProgramming.setEnabled(True)
        self.addProgramming.setMinimumSize(QSize(131, 131))
        self.addProgramming.setMaximumSize(QSize(131, 131))

        self.addProjectLayout.addWidget(self.addProgramming)


        self.addProjectMenuLayout.addLayout(self.addProjectLayout, 0, 0, 1, 1)

        self.returnExitLayout = QVBoxLayout()
        self.returnExitLayout.setObjectName(u"returnExitLayout")
        self.returnToMainAddProject = QPushButton(self.widget)
        self.returnToMainAddProject.setObjectName(u"returnToMainAddProject")

        self.returnExitLayout.addWidget(self.returnToMainAddProject)

        self.addProjectExit = QPushButton(self.widget)
        self.addProjectExit.setObjectName(u"addProjectExit")

        self.returnExitLayout.addWidget(self.addProjectExit)


        self.addProjectMenuLayout.addLayout(self.returnExitLayout, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Project Planner 1.0 - Add new project", None))
        self.addEveryday.setText(QCoreApplication.translate("Form", u"Add everyday\n"
"project", None))
        self.addProgramming.setText(QCoreApplication.translate("Form", u"Add programming\n"
"project", None))
        self.returnToMainAddProject.setText(QCoreApplication.translate("Form", u"Return to main menu", None))
        self.addProjectExit.setText(QCoreApplication.translate("Form", u"Exit program", None))
    # retranslateUi

