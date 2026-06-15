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
        icon = QIcon()
        icon.addFile(u"../images/icon_16.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        everydayProjectEditor.setWindowIcon(icon)
        self.layoutWidget = QWidget(everydayProjectEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 470, 421, 111))
        self.everydayMenuGrid = QGridLayout(self.layoutWidget)
        self.everydayMenuGrid.setObjectName(u"everydayMenuGrid")
        self.everydayMenuGrid.setContentsMargins(0, 0, 0, 0)
        self.saveEveryday = QPushButton(self.layoutWidget)
        self.saveEveryday.setObjectName(u"saveEveryday")

        self.everydayMenuGrid.addWidget(self.saveEveryday, 0, 0, 1, 1)

        self.clearEveryday = QPushButton(self.layoutWidget)
        self.clearEveryday.setObjectName(u"clearEveryday")

        self.everydayMenuGrid.addWidget(self.clearEveryday, 0, 1, 1, 1)

        self.returnToMainEveryday = QPushButton(self.layoutWidget)
        self.returnToMainEveryday.setObjectName(u"returnToMainEveryday")

        self.everydayMenuGrid.addWidget(self.returnToMainEveryday, 1, 0, 1, 1)

        self.exitEveryday = QPushButton(self.layoutWidget)
        self.exitEveryday.setObjectName(u"exitEveryday")

        self.everydayMenuGrid.addWidget(self.exitEveryday, 1, 1, 1, 1)

        self.programmingLabel = QLabel(everydayProjectEditor)
        self.programmingLabel.setObjectName(u"programmingLabel")
        self.programmingLabel.setGeometry(QRect(20, 20, 411, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.programmingLabel.setFont(font)
        self.programmingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(everydayProjectEditor)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 131, 421, 321))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLayoutEveryday = QHBoxLayout()
        self.nameLayoutEveryday.setObjectName(u"nameLayoutEveryday")
        self.nameLabelEveryday = QLabel(self.widget)
        self.nameLabelEveryday.setObjectName(u"nameLabelEveryday")
        font1 = QFont()
        font1.setBold(True)
        self.nameLabelEveryday.setFont(font1)

        self.nameLayoutEveryday.addWidget(self.nameLabelEveryday)

        self.projectNameEveryday = QLineEdit(self.widget)
        self.projectNameEveryday.setObjectName(u"projectNameEveryday")

        self.nameLayoutEveryday.addWidget(self.projectNameEveryday)

        self.nameLayoutEveryday.setStretch(0, 1)
        self.nameLayoutEveryday.setStretch(1, 3)

        self.gridLayout.addLayout(self.nameLayoutEveryday, 0, 0, 1, 1)

        self.startLayoutEveryday = QHBoxLayout()
        self.startLayoutEveryday.setSpacing(6)
        self.startLayoutEveryday.setObjectName(u"startLayoutEveryday")
        self.startLabelEveryday = QLabel(self.widget)
        self.startLabelEveryday.setObjectName(u"startLabelEveryday")
        self.startLabelEveryday.setFont(font1)

        self.startLayoutEveryday.addWidget(self.startLabelEveryday)

        self.startDateEveryday = QDateEdit(self.widget)
        self.startDateEveryday.setObjectName(u"startDateEveryday")

        self.startLayoutEveryday.addWidget(self.startDateEveryday)

        self.startLayoutEveryday.setStretch(0, 1)
        self.startLayoutEveryday.setStretch(1, 3)

        self.gridLayout.addLayout(self.startLayoutEveryday, 1, 0, 1, 1)

        self.finishLayoutEveryday = QHBoxLayout()
        self.finishLayoutEveryday.setSpacing(6)
        self.finishLayoutEveryday.setObjectName(u"finishLayoutEveryday")
        self.finishLabelEveryday = QLabel(self.widget)
        self.finishLabelEveryday.setObjectName(u"finishLabelEveryday")
        self.finishLabelEveryday.setFont(font1)

        self.finishLayoutEveryday.addWidget(self.finishLabelEveryday)

        self.finishDateEveryday = QDateEdit(self.widget)
        self.finishDateEveryday.setObjectName(u"finishDateEveryday")

        self.finishLayoutEveryday.addWidget(self.finishDateEveryday)

        self.finishLayoutEveryday.setStretch(0, 1)
        self.finishLayoutEveryday.setStretch(1, 3)

        self.gridLayout.addLayout(self.finishLayoutEveryday, 2, 0, 1, 1)

        self.notesEveryday = QHBoxLayout()
        self.notesEveryday.setObjectName(u"notesEveryday")
        self.notesLabelEveryday = QLabel(self.widget)
        self.notesLabelEveryday.setObjectName(u"notesLabelEveryday")
        self.notesLabelEveryday.setFont(font1)

        self.notesEveryday.addWidget(self.notesLabelEveryday)

        self.notesEditEveryday = QLineEdit(self.widget)
        self.notesEditEveryday.setObjectName(u"notesEditEveryday")

        self.notesEveryday.addWidget(self.notesEditEveryday)

        self.notesEveryday.setStretch(0, 1)
        self.notesEveryday.setStretch(1, 3)

        self.gridLayout.addLayout(self.notesEveryday, 3, 0, 1, 1)

        self.everydayInputLayout = QHBoxLayout()
        self.everydayInputLayout.setObjectName(u"everydayInputLayout")
        self.progressLabelEveryday = QLabel(self.widget)
        self.progressLabelEveryday.setObjectName(u"progressLabelEveryday")
        self.progressLabelEveryday.setFont(font1)

        self.everydayInputLayout.addWidget(self.progressLabelEveryday)

        self.progressSliderEveryday = QSlider(self.widget)
        self.progressSliderEveryday.setObjectName(u"progressSliderEveryday")
        self.progressSliderEveryday.setOrientation(Qt.Orientation.Horizontal)

        self.everydayInputLayout.addWidget(self.progressSliderEveryday)

        self.progressPercentageEveryday = QLabel(self.widget)
        self.progressPercentageEveryday.setObjectName(u"progressPercentageEveryday")

        self.everydayInputLayout.addWidget(self.progressPercentageEveryday)


        self.gridLayout.addLayout(self.everydayInputLayout, 4, 0, 1, 1)

        self.statusLayoutEveryday = QHBoxLayout()
        self.statusLayoutEveryday.setObjectName(u"statusLayoutEveryday")
        self.statusLabelEveryday = QLabel(self.widget)
        self.statusLabelEveryday.setObjectName(u"statusLabelEveryday")
        self.statusLabelEveryday.setFont(font1)

        self.statusLayoutEveryday.addWidget(self.statusLabelEveryday)

        self.statusComboEveryday = QComboBox(self.widget)
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

        self.gridLayout.addLayout(self.statusLayoutEveryday, 5, 0, 1, 1)


        self.retranslateUi(everydayProjectEditor)

        QMetaObject.connectSlotsByName(everydayProjectEditor)
    # setupUi

    def retranslateUi(self, everydayProjectEditor):
        everydayProjectEditor.setWindowTitle(QCoreApplication.translate("everydayProjectEditor", u"Project Planner 1.0 - Everyday project editor", None))
        self.saveEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Save project", None))
        self.clearEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Clear all", None))
        self.returnToMainEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Return to main", None))
        self.exitEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Exit program", None))
        self.programmingLabel.setText(QCoreApplication.translate("everydayProjectEditor", u"Everyday project", None))
        self.nameLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Project name", None))
        self.projectNameEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Project name", None))
        self.startLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Project start", None))
        self.finishLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Project finish", None))
        self.notesLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Notes", None))
        self.notesEditEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Notes", None))
        self.progressLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Progress", None))
        self.progressPercentageEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"0%", None))
        self.statusLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Status", None))
        self.statusComboEveryday.setItemText(0, QCoreApplication.translate("everydayProjectEditor", u"Select project status", None))
        self.statusComboEveryday.setItemText(1, QCoreApplication.translate("everydayProjectEditor", u"Pending", None))
        self.statusComboEveryday.setItemText(2, QCoreApplication.translate("everydayProjectEditor", u"In progress", None))
        self.statusComboEveryday.setItemText(3, QCoreApplication.translate("everydayProjectEditor", u"Cancelled", None))

    # retranslateUi

