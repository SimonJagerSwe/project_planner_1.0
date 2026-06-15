# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recurringProjectEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_recurringProjectEditor(object):
    def setupUi(self, recurringProjectEditor):
        if not recurringProjectEditor.objectName():
            recurringProjectEditor.setObjectName(u"recurringProjectEditor")
        recurringProjectEditor.resize(447, 385)
        recurringProjectEditor.setMinimumSize(QSize(447, 0))
        self.recurringLabel = QLabel(recurringProjectEditor)
        self.recurringLabel.setObjectName(u"recurringLabel")
        self.recurringLabel.setGeometry(QRect(20, 20, 411, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.recurringLabel.setFont(font)
        self.recurringLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(recurringProjectEditor)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 100, 421, 261))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.recurringProjectLayout = QGridLayout()
        self.recurringProjectLayout.setObjectName(u"recurringProjectLayout")
        self.nameLayoutRecurring = QHBoxLayout()
        self.nameLayoutRecurring.setObjectName(u"nameLayoutRecurring")
        self.nameLabelRecurring = QLabel(self.widget)
        self.nameLabelRecurring.setObjectName(u"nameLabelRecurring")
        font1 = QFont()
        font1.setBold(True)
        self.nameLabelRecurring.setFont(font1)

        self.nameLayoutRecurring.addWidget(self.nameLabelRecurring)

        self.projectNameRecurring = QLineEdit(self.widget)
        self.projectNameRecurring.setObjectName(u"projectNameRecurring")

        self.nameLayoutRecurring.addWidget(self.projectNameRecurring)

        self.nameLayoutRecurring.setStretch(0, 1)
        self.nameLayoutRecurring.setStretch(1, 3)

        self.recurringProjectLayout.addLayout(self.nameLayoutRecurring, 0, 0, 1, 1)

        self.frequencyLayoutRecurring = QHBoxLayout()
        self.frequencyLayoutRecurring.setObjectName(u"frequencyLayoutRecurring")
        self.frequencyLabelRecurring = QLabel(self.widget)
        self.frequencyLabelRecurring.setObjectName(u"frequencyLabelRecurring")
        self.frequencyLabelRecurring.setFont(font1)

        self.frequencyLayoutRecurring.addWidget(self.frequencyLabelRecurring)

        self.frequencyComboRecurring = QComboBox(self.widget)
        self.frequencyComboRecurring.addItem("")
        self.frequencyComboRecurring.addItem("")
        self.frequencyComboRecurring.addItem("")
        self.frequencyComboRecurring.addItem("")
        self.frequencyComboRecurring.setObjectName(u"frequencyComboRecurring")
        self.frequencyComboRecurring.setMaxVisibleItems(4)
        self.frequencyComboRecurring.setMaxCount(4)

        self.frequencyLayoutRecurring.addWidget(self.frequencyComboRecurring)

        self.frequencyLayoutRecurring.setStretch(0, 1)
        self.frequencyLayoutRecurring.setStretch(1, 3)

        self.recurringProjectLayout.addLayout(self.frequencyLayoutRecurring, 1, 0, 1, 1)

        self.notesLayoutRecurring = QHBoxLayout()
        self.notesLayoutRecurring.setObjectName(u"notesLayoutRecurring")
        self.notesLabelRecurring = QLabel(self.widget)
        self.notesLabelRecurring.setObjectName(u"notesLabelRecurring")
        self.notesLabelRecurring.setFont(font1)

        self.notesLayoutRecurring.addWidget(self.notesLabelRecurring)

        self.notesEditProgramming = QLineEdit(self.widget)
        self.notesEditProgramming.setObjectName(u"notesEditProgramming")

        self.notesLayoutRecurring.addWidget(self.notesEditProgramming)


        self.recurringProjectLayout.addLayout(self.notesLayoutRecurring, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.recurringProjectLayout, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.saveRecurring = QPushButton(self.widget)
        self.saveRecurring.setObjectName(u"saveRecurring")

        self.horizontalLayout.addWidget(self.saveRecurring)

        self.clearRecurring = QPushButton(self.widget)
        self.clearRecurring.setObjectName(u"clearRecurring")

        self.horizontalLayout.addWidget(self.clearRecurring)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.returnToMainRecurring = QPushButton(self.widget)
        self.returnToMainRecurring.setObjectName(u"returnToMainRecurring")

        self.horizontalLayout_2.addWidget(self.returnToMainRecurring)

        self.exitRecurring = QPushButton(self.widget)
        self.exitRecurring.setObjectName(u"exitRecurring")

        self.horizontalLayout_2.addWidget(self.exitRecurring)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.retranslateUi(recurringProjectEditor)

        QMetaObject.connectSlotsByName(recurringProjectEditor)
    # setupUi

    def retranslateUi(self, recurringProjectEditor):
        recurringProjectEditor.setWindowTitle(QCoreApplication.translate("recurringProjectEditor", u"Form", None))
        self.recurringLabel.setText(QCoreApplication.translate("recurringProjectEditor", u"Recurring project", None))
        self.nameLabelRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Project name", None))
        self.projectNameRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Project name", None))
        self.frequencyLabelRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Frequency", None))
        self.frequencyComboRecurring.setItemText(0, QCoreApplication.translate("recurringProjectEditor", u"Select frequency", None))
        self.frequencyComboRecurring.setItemText(1, QCoreApplication.translate("recurringProjectEditor", u"Weekly", None))
        self.frequencyComboRecurring.setItemText(2, QCoreApplication.translate("recurringProjectEditor", u"Bi-weekly", None))
        self.frequencyComboRecurring.setItemText(3, QCoreApplication.translate("recurringProjectEditor", u"Other", None))

        self.notesLabelRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Notes", None))
        self.notesEditProgramming.setText(QCoreApplication.translate("recurringProjectEditor", u"Notes", None))
        self.saveRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Save project", None))
        self.clearRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Clear all", None))
        self.returnToMainRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Return to main", None))
        self.exitRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Exit program", None))
    # retranslateUi

