# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'everydayProjectEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSlider, QWidget)

class Ui_everydayProjectEditor(object):
    def setupUi(self, everydayProjectEditor):
        if not everydayProjectEditor.objectName():
            everydayProjectEditor.setObjectName(u"everydayProjectEditor")
        everydayProjectEditor.resize(446, 599)
        self.layoutWidget = QWidget(everydayProjectEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 470, 421, 111))
        self.everydayMenuGrid = QGridLayout(self.layoutWidget)
        self.everydayMenuGrid.setObjectName(u"everydayMenuGrid")
        self.everydayMenuGrid.setContentsMargins(0, 0, 0, 0)
        self.saveButtonEveryday = QPushButton(self.layoutWidget)
        self.saveButtonEveryday.setObjectName(u"saveButtonEveryday")

        self.everydayMenuGrid.addWidget(self.saveButtonEveryday, 0, 0, 1, 1)

        self.clearAllButtonEveryday = QPushButton(self.layoutWidget)
        self.clearAllButtonEveryday.setObjectName(u"clearAllButtonEveryday")

        self.everydayMenuGrid.addWidget(self.clearAllButtonEveryday, 0, 1, 1, 1)

        self.returnToMainEveryday = QPushButton(self.layoutWidget)
        self.returnToMainEveryday.setObjectName(u"returnToMainEveryday")

        self.everydayMenuGrid.addWidget(self.returnToMainEveryday, 1, 0, 1, 1)

        self.exitEveryday = QPushButton(self.layoutWidget)
        self.exitEveryday.setObjectName(u"exitEveryday")

        self.everydayMenuGrid.addWidget(self.exitEveryday, 1, 1, 1, 1)

        self.layoutWidget_2 = QWidget(everydayProjectEditor)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 130, 421, 321))
        self.gridEveryday = QGridLayout(self.layoutWidget_2)
        self.gridEveryday.setObjectName(u"gridEveryday")
        self.gridEveryday.setContentsMargins(0, 0, 0, 0)
        self.nameLayoutEveryday = QHBoxLayout()
        self.nameLayoutEveryday.setObjectName(u"nameLayoutEveryday")
        self.nameLabelEveryday = QLabel(self.layoutWidget_2)
        self.nameLabelEveryday.setObjectName(u"nameLabelEveryday")
        font = QFont()
        font.setBold(True)
        self.nameLabelEveryday.setFont(font)

        self.nameLayoutEveryday.addWidget(self.nameLabelEveryday)

        self.projectNameEveryday = QLineEdit(self.layoutWidget_2)
        self.projectNameEveryday.setObjectName(u"projectNameEveryday")

        self.nameLayoutEveryday.addWidget(self.projectNameEveryday)

        self.nameLayoutEveryday.setStretch(0, 1)
        self.nameLayoutEveryday.setStretch(1, 3)

        self.gridEveryday.addLayout(self.nameLayoutEveryday, 0, 0, 1, 1)

        self.startLayoutEveryday = QHBoxLayout()
        self.startLayoutEveryday.setSpacing(6)
        self.startLayoutEveryday.setObjectName(u"startLayoutEveryday")
        self.startLabelEveryday = QLabel(self.layoutWidget_2)
        self.startLabelEveryday.setObjectName(u"startLabelEveryday")
        self.startLabelEveryday.setFont(font)

        self.startLayoutEveryday.addWidget(self.startLabelEveryday)

        self.startDateEveryday = QDateEdit(self.layoutWidget_2)
        self.startDateEveryday.setObjectName(u"startDateEveryday")

        self.startLayoutEveryday.addWidget(self.startDateEveryday)

        self.startLayoutEveryday.setStretch(0, 1)
        self.startLayoutEveryday.setStretch(1, 3)

        self.gridEveryday.addLayout(self.startLayoutEveryday, 1, 0, 1, 1)

        self.notesEveryday = QHBoxLayout()
        self.notesEveryday.setObjectName(u"notesEveryday")
        self.notesLabelEveryday = QLabel(self.layoutWidget_2)
        self.notesLabelEveryday.setObjectName(u"notesLabelEveryday")
        self.notesLabelEveryday.setFont(font)

        self.notesEveryday.addWidget(self.notesLabelEveryday)

        self.notesEditEveryday = QLineEdit(self.layoutWidget_2)
        self.notesEditEveryday.setObjectName(u"notesEditEveryday")

        self.notesEveryday.addWidget(self.notesEditEveryday)

        self.notesEveryday.setStretch(0, 1)
        self.notesEveryday.setStretch(1, 3)

        self.gridEveryday.addLayout(self.notesEveryday, 3, 0, 1, 1)

        self.progressLayoutEveryday = QHBoxLayout()
        self.progressLayoutEveryday.setObjectName(u"progressLayoutEveryday")
        self.progressLabelEveryday = QLabel(self.layoutWidget_2)
        self.progressLabelEveryday.setObjectName(u"progressLabelEveryday")
        self.progressLabelEveryday.setFont(font)

        self.progressLayoutEveryday.addWidget(self.progressLabelEveryday)

        self.progressSliderEveryday = QSlider(self.layoutWidget_2)
        self.progressSliderEveryday.setObjectName(u"progressSliderEveryday")
        self.progressSliderEveryday.setOrientation(Qt.Orientation.Horizontal)

        self.progressLayoutEveryday.addWidget(self.progressSliderEveryday)

        self.progressLayoutEveryday.setStretch(0, 1)
        self.progressLayoutEveryday.setStretch(1, 3)

        self.gridEveryday.addLayout(self.progressLayoutEveryday, 4, 0, 1, 1)

        self.statusLayoutEveryday = QHBoxLayout()
        self.statusLayoutEveryday.setObjectName(u"statusLayoutEveryday")
        self.statusLabelEveryday = QLabel(self.layoutWidget_2)
        self.statusLabelEveryday.setObjectName(u"statusLabelEveryday")
        self.statusLabelEveryday.setFont(font)

        self.statusLayoutEveryday.addWidget(self.statusLabelEveryday)

        self.statusComboEveryday = QComboBox(self.layoutWidget_2)
        self.statusComboEveryday.addItem("")
        self.statusComboEveryday.addItem("")
        self.statusComboEveryday.addItem("")
        self.statusComboEveryday.addItem("")
        self.statusComboEveryday.setObjectName(u"statusComboEveryday")
        self.statusComboEveryday.setMaxVisibleItems(4)
        self.statusComboEveryday.setMaxCount(4)

        self.statusLayoutEveryday.addWidget(self.statusComboEveryday)

        self.statusLayoutEveryday.setStretch(0, 1)
        self.statusLayoutEveryday.setStretch(1, 3)

        self.gridEveryday.addLayout(self.statusLayoutEveryday, 5, 0, 1, 1)

        self.finishLayoutEveryday = QHBoxLayout()
        self.finishLayoutEveryday.setSpacing(6)
        self.finishLayoutEveryday.setObjectName(u"finishLayoutEveryday")
        self.finishLabelEveryday = QLabel(self.layoutWidget_2)
        self.finishLabelEveryday.setObjectName(u"finishLabelEveryday")
        self.finishLabelEveryday.setFont(font)

        self.finishLayoutEveryday.addWidget(self.finishLabelEveryday)

        self.finishDateEveryday = QDateEdit(self.layoutWidget_2)
        self.finishDateEveryday.setObjectName(u"finishDateEveryday")

        self.finishLayoutEveryday.addWidget(self.finishDateEveryday)

        self.finishLayoutEveryday.setStretch(0, 1)
        self.finishLayoutEveryday.setStretch(1, 3)

        self.gridEveryday.addLayout(self.finishLayoutEveryday, 2, 0, 1, 1)

        self.everydayHeader = QLineEdit(everydayProjectEditor)
        self.everydayHeader.setObjectName(u"everydayHeader")
        self.everydayHeader.setGeometry(QRect(10, 20, 421, 91))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.everydayHeader.setFont(font1)
        self.everydayHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(everydayProjectEditor)

        QMetaObject.connectSlotsByName(everydayProjectEditor)
    # setupUi

    def retranslateUi(self, everydayProjectEditor):
        everydayProjectEditor.setWindowTitle(QCoreApplication.translate("everydayProjectEditor", u"Project Planner 1.0 - Everyday project editor", None))
        self.saveButtonEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Save project", None))
        self.clearAllButtonEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Clear all", None))
        self.returnToMainEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Return to main", None))
        self.exitEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Exit program", None))
        self.nameLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Project name", None))
        self.projectNameEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Project name", None))
        self.startLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Project start", None))
        self.notesLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Notes", None))
        self.notesEditEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Notes", None))
        self.progressLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Progress", None))
        self.statusLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Status", None))
        self.statusComboEveryday.setItemText(0, QCoreApplication.translate("everydayProjectEditor", u"Select project status", None))
        self.statusComboEveryday.setItemText(1, QCoreApplication.translate("everydayProjectEditor", u"Pending", None))
        self.statusComboEveryday.setItemText(2, QCoreApplication.translate("everydayProjectEditor", u"In progress", None))
        self.statusComboEveryday.setItemText(3, QCoreApplication.translate("everydayProjectEditor", u"Cancelled", None))

        self.finishLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Project finish", None))
        self.everydayHeader.setText(QCoreApplication.translate("everydayProjectEditor", u"Everyday project", None))
    # retranslateUi

