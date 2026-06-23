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
        self.layoutWidget = QWidget(recurringProjectEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 101, 421, 251))
        self.recurringGrid = QGridLayout(self.layoutWidget)
        self.recurringGrid.setObjectName(u"recurringGrid")
        self.recurringGrid.setContentsMargins(0, 0, 0, 0)
        self.recurringProjectLayout = QGridLayout()
        self.recurringProjectLayout.setObjectName(u"recurringProjectLayout")
        self.nameLayoutRecurring = QHBoxLayout()
        self.nameLayoutRecurring.setObjectName(u"nameLayoutRecurring")
        self.nameLabelRecurring = QLabel(self.layoutWidget)
        self.nameLabelRecurring.setObjectName(u"nameLabelRecurring")
        font1 = QFont()
        font1.setBold(True)
        self.nameLabelRecurring.setFont(font1)

        self.nameLayoutRecurring.addWidget(self.nameLabelRecurring)

        self.recurringName = QLineEdit(self.layoutWidget)
        self.recurringName.setObjectName(u"recurringName")

        self.nameLayoutRecurring.addWidget(self.recurringName)

        self.nameLayoutRecurring.setStretch(0, 1)
        self.nameLayoutRecurring.setStretch(1, 3)

        self.recurringProjectLayout.addLayout(self.nameLayoutRecurring, 0, 0, 1, 1)

        self.frequencyLayoutRecurring = QHBoxLayout()
        self.frequencyLayoutRecurring.setObjectName(u"frequencyLayoutRecurring")
        self.frequencyLabelRecurring = QLabel(self.layoutWidget)
        self.frequencyLabelRecurring.setObjectName(u"frequencyLabelRecurring")
        self.frequencyLabelRecurring.setFont(font1)

        self.frequencyLayoutRecurring.addWidget(self.frequencyLabelRecurring)

        self.recurringFrequency = QComboBox(self.layoutWidget)
        self.recurringFrequency.addItem("")
        self.recurringFrequency.addItem("")
        self.recurringFrequency.addItem("")
        self.recurringFrequency.addItem("")
        self.recurringFrequency.setObjectName(u"recurringFrequency")
        self.recurringFrequency.setMaxVisibleItems(4)
        self.recurringFrequency.setMaxCount(4)

        self.frequencyLayoutRecurring.addWidget(self.recurringFrequency)

        self.frequencyLayoutRecurring.setStretch(0, 1)
        self.frequencyLayoutRecurring.setStretch(1, 3)

        self.recurringProjectLayout.addLayout(self.frequencyLayoutRecurring, 1, 0, 1, 1)

        self.notesLayoutRecurring = QHBoxLayout()
        self.notesLayoutRecurring.setObjectName(u"notesLayoutRecurring")
        self.notesLabelRecurring = QLabel(self.layoutWidget)
        self.notesLabelRecurring.setObjectName(u"notesLabelRecurring")
        self.notesLabelRecurring.setFont(font1)

        self.notesLayoutRecurring.addWidget(self.notesLabelRecurring)

        self.recurringNotes = QLineEdit(self.layoutWidget)
        self.recurringNotes.setObjectName(u"recurringNotes")

        self.notesLayoutRecurring.addWidget(self.recurringNotes)


        self.recurringProjectLayout.addLayout(self.notesLayoutRecurring, 2, 0, 1, 1)


        self.recurringGrid.addLayout(self.recurringProjectLayout, 0, 0, 1, 1)

        self.recurringProjectManagerGrid = QHBoxLayout()
        self.recurringProjectManagerGrid.setObjectName(u"recurringProjectManagerGrid")
        self.saveRecurring = QPushButton(self.layoutWidget)
        self.saveRecurring.setObjectName(u"saveRecurring")

        self.recurringProjectManagerGrid.addWidget(self.saveRecurring)

        self.clearRecurring = QPushButton(self.layoutWidget)
        self.clearRecurring.setObjectName(u"clearRecurring")

        self.recurringProjectManagerGrid.addWidget(self.clearRecurring)


        self.recurringGrid.addLayout(self.recurringProjectManagerGrid, 1, 0, 1, 1)

        self.recurringMenyLayout = QHBoxLayout()
        self.recurringMenyLayout.setObjectName(u"recurringMenyLayout")
        self.returnToMainRecurring = QPushButton(self.layoutWidget)
        self.returnToMainRecurring.setObjectName(u"returnToMainRecurring")

        self.recurringMenyLayout.addWidget(self.returnToMainRecurring)

        self.exitRecurring = QPushButton(self.layoutWidget)
        self.exitRecurring.setObjectName(u"exitRecurring")

        self.recurringMenyLayout.addWidget(self.exitRecurring)


        self.recurringGrid.addLayout(self.recurringMenyLayout, 2, 0, 1, 1)


        self.retranslateUi(recurringProjectEditor)

        QMetaObject.connectSlotsByName(recurringProjectEditor)
    # setupUi

    def retranslateUi(self, recurringProjectEditor):
        recurringProjectEditor.setWindowTitle(QCoreApplication.translate("recurringProjectEditor", u"Form", None))
        self.recurringLabel.setText(QCoreApplication.translate("recurringProjectEditor", u"Recurring project", None))
        self.nameLabelRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Project name", None))
        self.recurringName.setText("")
        self.frequencyLabelRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Frequency", None))
        self.recurringFrequency.setItemText(0, QCoreApplication.translate("recurringProjectEditor", u"Select frequency", None))
        self.recurringFrequency.setItemText(1, QCoreApplication.translate("recurringProjectEditor", u"Weekly", None))
        self.recurringFrequency.setItemText(2, QCoreApplication.translate("recurringProjectEditor", u"Bi-weekly", None))
        self.recurringFrequency.setItemText(3, QCoreApplication.translate("recurringProjectEditor", u"Other", None))

        self.notesLabelRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Notes", None))
        self.recurringNotes.setText("")
        self.saveRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Save project", None))
        self.clearRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Clear all", None))
        self.returnToMainRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Return to main", None))
        self.exitRecurring.setText(QCoreApplication.translate("recurringProjectEditor", u"Exit program", None))
    # retranslateUi

