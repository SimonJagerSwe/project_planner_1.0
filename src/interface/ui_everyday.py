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
        self.everydaySave = QPushButton(self.layoutWidget)
        self.everydaySave.setObjectName(u"everydaySave")

        self.everydayMenuGrid.addWidget(self.everydaySave, 0, 0, 1, 1)

        self.everydayClear = QPushButton(self.layoutWidget)
        self.everydayClear.setObjectName(u"everydayClear")

        self.everydayMenuGrid.addWidget(self.everydayClear, 0, 1, 1, 1)

        self.everydayReturn = QPushButton(self.layoutWidget)
        self.everydayReturn.setObjectName(u"everydayReturn")

        self.everydayMenuGrid.addWidget(self.everydayReturn, 1, 0, 1, 1)

        self.everydayExit = QPushButton(self.layoutWidget)
        self.everydayExit.setObjectName(u"everydayExit")

        self.everydayMenuGrid.addWidget(self.everydayExit, 1, 1, 1, 1)

        self.everydayHeader = QLabel(everydayProjectEditor)
        self.everydayHeader.setObjectName(u"everydayHeader")
        self.everydayHeader.setGeometry(QRect(20, 20, 411, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.everydayHeader.setFont(font)
        self.everydayHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget1 = QWidget(everydayProjectEditor)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(14, 127, 421, 321))
        self.everydayGrid = QGridLayout(self.layoutWidget1)
        self.everydayGrid.setObjectName(u"everydayGrid")
        self.everydayGrid.setContentsMargins(0, 0, 0, 0)
        self.everydayNameLayout = QHBoxLayout()
        self.everydayNameLayout.setObjectName(u"everydayNameLayout")
        self.everydayNameLabel = QLabel(self.layoutWidget1)
        self.everydayNameLabel.setObjectName(u"everydayNameLabel")
        self.everydayNameLabel.setMaximumSize(QSize(16777215, 22))
        font1 = QFont()
        font1.setBold(True)
        self.everydayNameLabel.setFont(font1)

        self.everydayNameLayout.addWidget(self.everydayNameLabel)

        self.everydayName = QLineEdit(self.layoutWidget1)
        self.everydayName.setObjectName(u"everydayName")
        self.everydayName.setMaximumSize(QSize(16777215, 22))

        self.everydayNameLayout.addWidget(self.everydayName)


        self.everydayGrid.addLayout(self.everydayNameLayout, 0, 0, 1, 1)

        self.everydayStartLayout = QHBoxLayout()
        self.everydayStartLayout.setObjectName(u"everydayStartLayout")
        self.everydayStartLabel = QLabel(self.layoutWidget1)
        self.everydayStartLabel.setObjectName(u"everydayStartLabel")
        self.everydayStartLabel.setMaximumSize(QSize(16777215, 22))
        self.everydayStartLabel.setFont(font1)

        self.everydayStartLayout.addWidget(self.everydayStartLabel)

        self.everydayStart = QDateEdit(self.layoutWidget1)
        self.everydayStart.setObjectName(u"everydayStart")
        self.everydayStart.setMaximumSize(QSize(16777215, 22))
        self.everydayStart.setMaximumDateTime(QDateTime(QDate(9999, 8, 30), QTime(23, 59, 59)))
        self.everydayStart.setCalendarPopup(True)

        self.everydayStartLayout.addWidget(self.everydayStart)

        self.everydayStartLayout.setStretch(0, 1)
        self.everydayStartLayout.setStretch(1, 3)

        self.everydayGrid.addLayout(self.everydayStartLayout, 1, 0, 1, 1)

        self.everydayFinishLayout = QHBoxLayout()
        self.everydayFinishLayout.setObjectName(u"everydayFinishLayout")
        self.everydayFinishLabel = QLabel(self.layoutWidget1)
        self.everydayFinishLabel.setObjectName(u"everydayFinishLabel")
        self.everydayFinishLabel.setMaximumSize(QSize(16777215, 22))
        self.everydayFinishLabel.setFont(font1)

        self.everydayFinishLayout.addWidget(self.everydayFinishLabel)

        self.everydayFinish = QDateEdit(self.layoutWidget1)
        self.everydayFinish.setObjectName(u"everydayFinish")
        self.everydayFinish.setMaximumSize(QSize(16777215, 22))
        self.everydayFinish.setCalendarPopup(True)

        self.everydayFinishLayout.addWidget(self.everydayFinish)

        self.everydayFinishLayout.setStretch(0, 1)
        self.everydayFinishLayout.setStretch(1, 3)

        self.everydayGrid.addLayout(self.everydayFinishLayout, 2, 0, 1, 1)

        self.everydayNotesLayout = QHBoxLayout()
        self.everydayNotesLayout.setObjectName(u"everydayNotesLayout")
        self.everydayNotesLabel = QLabel(self.layoutWidget1)
        self.everydayNotesLabel.setObjectName(u"everydayNotesLabel")
        self.everydayNotesLabel.setMaximumSize(QSize(16777215, 22))
        self.everydayNotesLabel.setFont(font1)

        self.everydayNotesLayout.addWidget(self.everydayNotesLabel)

        self.everydayNotes = QLineEdit(self.layoutWidget1)
        self.everydayNotes.setObjectName(u"everydayNotes")
        self.everydayNotes.setMaximumSize(QSize(16777215, 22))

        self.everydayNotesLayout.addWidget(self.everydayNotes)


        self.everydayGrid.addLayout(self.everydayNotesLayout, 3, 0, 1, 1)

        self.everydayProgressLayout = QHBoxLayout()
        self.everydayProgressLayout.setObjectName(u"everydayProgressLayout")
        self.everydayProgressLabel = QLabel(self.layoutWidget1)
        self.everydayProgressLabel.setObjectName(u"everydayProgressLabel")
        self.everydayProgressLabel.setMaximumSize(QSize(16777215, 22))
        self.everydayProgressLabel.setFont(font1)

        self.everydayProgressLayout.addWidget(self.everydayProgressLabel)

        self.everydayProgressSlider = QSlider(self.layoutWidget1)
        self.everydayProgressSlider.setObjectName(u"everydayProgressSlider")
        self.everydayProgressSlider.setMaximumSize(QSize(16777215, 22))
        self.everydayProgressSlider.setOrientation(Qt.Orientation.Horizontal)

        self.everydayProgressLayout.addWidget(self.everydayProgressSlider)

        self.everydayProgressPercent = QLabel(self.layoutWidget1)
        self.everydayProgressPercent.setObjectName(u"everydayProgressPercent")
        self.everydayProgressPercent.setMaximumSize(QSize(16777215, 22))

        self.everydayProgressLayout.addWidget(self.everydayProgressPercent)


        self.everydayGrid.addLayout(self.everydayProgressLayout, 4, 0, 1, 1)

        self.everydayStatusLayout = QHBoxLayout()
        self.everydayStatusLayout.setObjectName(u"everydayStatusLayout")
        self.everydayStatusLabel = QLabel(self.layoutWidget1)
        self.everydayStatusLabel.setObjectName(u"everydayStatusLabel")
        self.everydayStatusLabel.setMaximumSize(QSize(16777215, 22))
        self.everydayStatusLabel.setFont(font1)

        self.everydayStatusLayout.addWidget(self.everydayStatusLabel)

        self.everydayStatus = QComboBox(self.layoutWidget1)
        self.everydayStatus.addItem("")
        self.everydayStatus.addItem("")
        self.everydayStatus.addItem("")
        self.everydayStatus.addItem("")
        self.everydayStatus.setObjectName(u"everydayStatus")
        self.everydayStatus.setMaximumSize(QSize(16777215, 22))
        self.everydayStatus.setMaxVisibleItems(4)
        self.everydayStatus.setMaxCount(4)

        self.everydayStatusLayout.addWidget(self.everydayStatus)

        self.everydayStatusLayout.setStretch(0, 1)
        self.everydayStatusLayout.setStretch(1, 3)

        self.everydayGrid.addLayout(self.everydayStatusLayout, 5, 0, 1, 1)


        self.retranslateUi(everydayProjectEditor)

        QMetaObject.connectSlotsByName(everydayProjectEditor)
    # setupUi

    def retranslateUi(self, everydayProjectEditor):
        everydayProjectEditor.setWindowTitle(QCoreApplication.translate("everydayProjectEditor", u"Project Planner 1.0 - Everyday project editor", None))
        self.everydaySave.setText(QCoreApplication.translate("everydayProjectEditor", u"Save project", None))
        self.everydayClear.setText(QCoreApplication.translate("everydayProjectEditor", u"Clear all", None))
        self.everydayReturn.setText(QCoreApplication.translate("everydayProjectEditor", u"Return to main", None))
        self.everydayExit.setText(QCoreApplication.translate("everydayProjectEditor", u"Exit program", None))
        self.everydayHeader.setText(QCoreApplication.translate("everydayProjectEditor", u"Everyday project", None))
        self.everydayNameLabel.setText(QCoreApplication.translate("everydayProjectEditor", u"Project name", None))
        self.everydayName.setText("")
        self.everydayStartLabel.setText(QCoreApplication.translate("everydayProjectEditor", u"Project start", None))
        self.everydayStart.setDisplayFormat(QCoreApplication.translate("everydayProjectEditor", u"dd/MM/yy", None))
        self.everydayFinishLabel.setText(QCoreApplication.translate("everydayProjectEditor", u"Project finish", None))
        self.everydayFinish.setDisplayFormat(QCoreApplication.translate("everydayProjectEditor", u"dd/MM/yy", None))
        self.everydayNotesLabel.setText(QCoreApplication.translate("everydayProjectEditor", u"Notes", None))
        self.everydayNotes.setText("")
        self.everydayProgressLabel.setText(QCoreApplication.translate("everydayProjectEditor", u"Progress", None))
        self.everydayProgressPercent.setText(QCoreApplication.translate("everydayProjectEditor", u"0%", None))
        self.everydayStatusLabel.setText(QCoreApplication.translate("everydayProjectEditor", u"Status", None))
        self.everydayStatus.setItemText(0, QCoreApplication.translate("everydayProjectEditor", u"Select project status", None))
        self.everydayStatus.setItemText(1, QCoreApplication.translate("everydayProjectEditor", u"Pending", None))
        self.everydayStatus.setItemText(2, QCoreApplication.translate("everydayProjectEditor", u"In progress", None))
        self.everydayStatus.setItemText(3, QCoreApplication.translate("everydayProjectEditor", u"Cancelled", None))

    # retranslateUi

