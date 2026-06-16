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
        self.widget.setGeometry(QRect(14, 127, 421, 321))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.everydayNameLayout = QHBoxLayout()
        self.everydayNameLayout.setObjectName(u"everydayNameLayout")
        self.nameLabelEveryday = QLabel(self.widget)
        self.nameLabelEveryday.setObjectName(u"nameLabelEveryday")
        self.nameLabelEveryday.setMaximumSize(QSize(16777215, 22))
        font1 = QFont()
        font1.setBold(True)
        self.nameLabelEveryday.setFont(font1)

        self.everydayNameLayout.addWidget(self.nameLabelEveryday)

        self.projectNameEveryday = QLineEdit(self.widget)
        self.projectNameEveryday.setObjectName(u"projectNameEveryday")
        self.projectNameEveryday.setMaximumSize(QSize(16777215, 22))

        self.everydayNameLayout.addWidget(self.projectNameEveryday)


        self.gridLayout.addLayout(self.everydayNameLayout, 0, 0, 1, 1)

        self.everydayStartLayout = QHBoxLayout()
        self.everydayStartLayout.setObjectName(u"everydayStartLayout")
        self.startLabelEveryday = QLabel(self.widget)
        self.startLabelEveryday.setObjectName(u"startLabelEveryday")
        self.startLabelEveryday.setMaximumSize(QSize(16777215, 22))
        self.startLabelEveryday.setFont(font1)

        self.everydayStartLayout.addWidget(self.startLabelEveryday)

        self.everydayStart = QDateEdit(self.widget)
        self.everydayStart.setObjectName(u"everydayStart")
        self.everydayStart.setMaximumSize(QSize(16777215, 22))
        self.everydayStart.setMaximumDateTime(QDateTime(QDate(9999, 8, 30), QTime(23, 59, 59)))
        self.everydayStart.setCalendarPopup(True)

        self.everydayStartLayout.addWidget(self.everydayStart)


        self.gridLayout.addLayout(self.everydayStartLayout, 1, 0, 1, 1)

        self.everydayFinishLayout = QHBoxLayout()
        self.everydayFinishLayout.setObjectName(u"everydayFinishLayout")
        self.finishLabelEveryday = QLabel(self.widget)
        self.finishLabelEveryday.setObjectName(u"finishLabelEveryday")
        self.finishLabelEveryday.setMaximumSize(QSize(16777215, 22))
        self.finishLabelEveryday.setFont(font1)

        self.everydayFinishLayout.addWidget(self.finishLabelEveryday)

        self.everydayFinish = QDateEdit(self.widget)
        self.everydayFinish.setObjectName(u"everydayFinish")
        self.everydayFinish.setMaximumSize(QSize(16777215, 22))
        self.everydayFinish.setCalendarPopup(True)

        self.everydayFinishLayout.addWidget(self.everydayFinish)


        self.gridLayout.addLayout(self.everydayFinishLayout, 2, 0, 1, 1)

        self.everydayNotesLayout = QHBoxLayout()
        self.everydayNotesLayout.setObjectName(u"everydayNotesLayout")
        self.notesLabelEveryday = QLabel(self.widget)
        self.notesLabelEveryday.setObjectName(u"notesLabelEveryday")
        self.notesLabelEveryday.setMaximumSize(QSize(16777215, 22))
        self.notesLabelEveryday.setFont(font1)

        self.everydayNotesLayout.addWidget(self.notesLabelEveryday)

        self.notesEditEveryday = QLineEdit(self.widget)
        self.notesEditEveryday.setObjectName(u"notesEditEveryday")
        self.notesEditEveryday.setMaximumSize(QSize(16777215, 22))

        self.everydayNotesLayout.addWidget(self.notesEditEveryday)


        self.gridLayout.addLayout(self.everydayNotesLayout, 3, 0, 1, 1)

        self.everydayProgressLayout = QHBoxLayout()
        self.everydayProgressLayout.setObjectName(u"everydayProgressLayout")
        self.progressLabelEveryday = QLabel(self.widget)
        self.progressLabelEveryday.setObjectName(u"progressLabelEveryday")
        self.progressLabelEveryday.setMaximumSize(QSize(16777215, 22))
        self.progressLabelEveryday.setFont(font1)

        self.everydayProgressLayout.addWidget(self.progressLabelEveryday)

        self.progressSliderEveryday = QSlider(self.widget)
        self.progressSliderEveryday.setObjectName(u"progressSliderEveryday")
        self.progressSliderEveryday.setMaximumSize(QSize(16777215, 22))
        self.progressSliderEveryday.setOrientation(Qt.Orientation.Horizontal)

        self.everydayProgressLayout.addWidget(self.progressSliderEveryday)

        self.progressPercentageEveryday = QLabel(self.widget)
        self.progressPercentageEveryday.setObjectName(u"progressPercentageEveryday")
        self.progressPercentageEveryday.setMaximumSize(QSize(16777215, 22))

        self.everydayProgressLayout.addWidget(self.progressPercentageEveryday)


        self.gridLayout.addLayout(self.everydayProgressLayout, 4, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.statusLabelEveryday = QLabel(self.widget)
        self.statusLabelEveryday.setObjectName(u"statusLabelEveryday")
        self.statusLabelEveryday.setMaximumSize(QSize(16777215, 22))
        self.statusLabelEveryday.setFont(font1)

        self.horizontalLayout_6.addWidget(self.statusLabelEveryday)

        self.everydayNotesLayout_2 = QComboBox(self.widget)
        self.everydayNotesLayout_2.addItem("")
        self.everydayNotesLayout_2.addItem("")
        self.everydayNotesLayout_2.addItem("")
        self.everydayNotesLayout_2.addItem("")
        self.everydayNotesLayout_2.setObjectName(u"everydayNotesLayout_2")
        self.everydayNotesLayout_2.setMaximumSize(QSize(16777215, 22))
        self.everydayNotesLayout_2.setMaxVisibleItems(4)
        self.everydayNotesLayout_2.setMaxCount(4)

        self.horizontalLayout_6.addWidget(self.everydayNotesLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)


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
        self.everydayStart.setDisplayFormat(QCoreApplication.translate("everydayProjectEditor", u"dd/MM/yy", None))
        self.finishLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Project finish", None))
        self.everydayFinish.setDisplayFormat(QCoreApplication.translate("everydayProjectEditor", u"dd/MM/yy", None))
        self.notesLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Notes", None))
        self.notesEditEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Notes", None))
        self.progressLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Progress", None))
        self.progressPercentageEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"0%", None))
        self.statusLabelEveryday.setText(QCoreApplication.translate("everydayProjectEditor", u"Status", None))
        self.everydayNotesLayout_2.setItemText(0, QCoreApplication.translate("everydayProjectEditor", u"Select project status", None))
        self.everydayNotesLayout_2.setItemText(1, QCoreApplication.translate("everydayProjectEditor", u"Pending", None))
        self.everydayNotesLayout_2.setItemText(2, QCoreApplication.translate("everydayProjectEditor", u"In progress", None))
        self.everydayNotesLayout_2.setItemText(3, QCoreApplication.translate("everydayProjectEditor", u"Cancelled", None))

    # retranslateUi

