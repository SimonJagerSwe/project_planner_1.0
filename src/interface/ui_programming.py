# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'programmingProjectEditor.ui'
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

class Ui_programmingProjectEditor(object):
    def setupUi(self, programmingProjectEditor):
        if not programmingProjectEditor.objectName():
            programmingProjectEditor.setObjectName(u"programmingProjectEditor")
        programmingProjectEditor.resize(447, 600)
        icon = QIcon()
        icon.addFile(u"../images/icon_16.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        programmingProjectEditor.setWindowIcon(icon)
        self.layoutWidget = QWidget(programmingProjectEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 470, 421, 111))
        self.programmingMenuGrid = QGridLayout(self.layoutWidget)
        self.programmingMenuGrid.setObjectName(u"programmingMenuGrid")
        self.programmingMenuGrid.setContentsMargins(0, 0, 0, 0)
        self.programmingSave = QPushButton(self.layoutWidget)
        self.programmingSave.setObjectName(u"programmingSave")

        self.programmingMenuGrid.addWidget(self.programmingSave, 0, 0, 1, 1)

        self.programmingClear = QPushButton(self.layoutWidget)
        self.programmingClear.setObjectName(u"programmingClear")

        self.programmingMenuGrid.addWidget(self.programmingClear, 0, 1, 1, 1)

        self.programmingReturn = QPushButton(self.layoutWidget)
        self.programmingReturn.setObjectName(u"programmingReturn")

        self.programmingMenuGrid.addWidget(self.programmingReturn, 1, 0, 1, 1)

        self.programmingExit = QPushButton(self.layoutWidget)
        self.programmingExit.setObjectName(u"programmingExit")

        self.programmingMenuGrid.addWidget(self.programmingExit, 1, 1, 1, 1)

        self.programmingHeader = QLabel(programmingProjectEditor)
        self.programmingHeader.setObjectName(u"programmingHeader")
        self.programmingHeader.setGeometry(QRect(20, 20, 411, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.programmingHeader.setFont(font)
        self.programmingHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(programmingProjectEditor)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(13, 133, 421, 321))
        self.programmingGridLayout = QGridLayout(self.widget)
        self.programmingGridLayout.setObjectName(u"programmingGridLayout")
        self.programmingGridLayout.setContentsMargins(0, 0, 0, 0)
        self.programmingFinishedLayout = QHBoxLayout()
        self.programmingFinishedLayout.setObjectName(u"programmingFinishedLayout")
        self.programmingFinishLabel = QLabel(self.widget)
        self.programmingFinishLabel.setObjectName(u"programmingFinishLabel")
        self.programmingFinishLabel.setMaximumSize(QSize(16777215, 22))
        font1 = QFont()
        font1.setBold(True)
        self.programmingFinishLabel.setFont(font1)

        self.programmingFinishedLayout.addWidget(self.programmingFinishLabel)

        self.programmingFinish = QDateEdit(self.widget)
        self.programmingFinish.setObjectName(u"programmingFinish")
        self.programmingFinish.setMaximumSize(QSize(16777215, 22))
        self.programmingFinish.setCalendarPopup(True)

        self.programmingFinishedLayout.addWidget(self.programmingFinish)

        self.programmingFinishedLayout.setStretch(0, 1)
        self.programmingFinishedLayout.setStretch(1, 3)

        self.programmingGridLayout.addLayout(self.programmingFinishedLayout, 2, 0, 1, 1)

        self.programmingStartLayout = QHBoxLayout()
        self.programmingStartLayout.setObjectName(u"programmingStartLayout")
        self.programmingStartLabel = QLabel(self.widget)
        self.programmingStartLabel.setObjectName(u"programmingStartLabel")
        self.programmingStartLabel.setMaximumSize(QSize(16777215, 22))
        self.programmingStartLabel.setFont(font1)

        self.programmingStartLayout.addWidget(self.programmingStartLabel)

        self.programmingStart = QDateEdit(self.widget)
        self.programmingStart.setObjectName(u"programmingStart")
        self.programmingStart.setMaximumSize(QSize(16777215, 22))
        self.programmingStart.setCalendarPopup(True)
        self.programmingStart.setDate(QDate(2000, 1, 1))

        self.programmingStartLayout.addWidget(self.programmingStart)

        self.programmingStartLayout.setStretch(0, 1)
        self.programmingStartLayout.setStretch(1, 3)

        self.programmingGridLayout.addLayout(self.programmingStartLayout, 1, 0, 1, 1)

        self.githubLayout = QHBoxLayout()
        self.githubLayout.setObjectName(u"githubLayout")
        self.githubLabel = QLabel(self.widget)
        self.githubLabel.setObjectName(u"githubLabel")
        self.githubLabel.setMaximumSize(QSize(16777215, 22))
        self.githubLabel.setFont(font1)

        self.githubLayout.addWidget(self.githubLabel)

        self.githubEdit = QLineEdit(self.widget)
        self.githubEdit.setObjectName(u"githubEdit")
        self.githubEdit.setMaximumSize(QSize(16777215, 22))

        self.githubLayout.addWidget(self.githubEdit)


        self.programmingGridLayout.addLayout(self.githubLayout, 4, 0, 1, 1)

        self.languagesLayout = QHBoxLayout()
        self.languagesLayout.setObjectName(u"languagesLayout")
        self.languagesLabel = QLabel(self.widget)
        self.languagesLabel.setObjectName(u"languagesLabel")
        self.languagesLabel.setMaximumSize(QSize(16777215, 22))
        self.languagesLabel.setFont(font1)

        self.languagesLayout.addWidget(self.languagesLabel)

        self.languagesEdit = QLineEdit(self.widget)
        self.languagesEdit.setObjectName(u"languagesEdit")
        self.languagesEdit.setMaximumSize(QSize(16777215, 22))
        self.languagesEdit.setSizeIncrement(QSize(0, 22))

        self.languagesLayout.addWidget(self.languagesEdit)


        self.programmingGridLayout.addLayout(self.languagesLayout, 3, 0, 1, 1)

        self.programmingNotesLayout = QHBoxLayout()
        self.programmingNotesLayout.setObjectName(u"programmingNotesLayout")
        self.programmingNotesLabel = QLabel(self.widget)
        self.programmingNotesLabel.setObjectName(u"programmingNotesLabel")
        self.programmingNotesLabel.setMaximumSize(QSize(16777215, 22))
        self.programmingNotesLabel.setFont(font1)

        self.programmingNotesLayout.addWidget(self.programmingNotesLabel)

        self.programmingNotes = QLineEdit(self.widget)
        self.programmingNotes.setObjectName(u"programmingNotes")
        self.programmingNotes.setMaximumSize(QSize(16777215, 22))

        self.programmingNotesLayout.addWidget(self.programmingNotes)


        self.programmingGridLayout.addLayout(self.programmingNotesLayout, 5, 0, 1, 1)

        self.programmingStatusLayout = QHBoxLayout()
        self.programmingStatusLayout.setObjectName(u"programmingStatusLayout")
        self.programmingStatusLabel = QLabel(self.widget)
        self.programmingStatusLabel.setObjectName(u"programmingStatusLabel")
        self.programmingStatusLabel.setMaximumSize(QSize(16777215, 22))
        self.programmingStatusLabel.setFont(font1)

        self.programmingStatusLayout.addWidget(self.programmingStatusLabel)

        self.programmingStatus = QComboBox(self.widget)
        self.programmingStatus.addItem("")
        self.programmingStatus.addItem("")
        self.programmingStatus.addItem("")
        self.programmingStatus.addItem("")
        self.programmingStatus.setObjectName(u"programmingStatus")
        self.programmingStatus.setMaximumSize(QSize(16777215, 22))
        self.programmingStatus.setMaxVisibleItems(4)
        self.programmingStatus.setMaxCount(4)

        self.programmingStatusLayout.addWidget(self.programmingStatus)

        self.programmingStatusLayout.setStretch(0, 1)
        self.programmingStatusLayout.setStretch(1, 3)

        self.programmingGridLayout.addLayout(self.programmingStatusLayout, 7, 0, 1, 1)

        self.programmingProgressLayout = QHBoxLayout()
        self.programmingProgressLayout.setObjectName(u"programmingProgressLayout")
        self.programmingProgressLabel = QLabel(self.widget)
        self.programmingProgressLabel.setObjectName(u"programmingProgressLabel")
        self.programmingProgressLabel.setMaximumSize(QSize(16777215, 22))
        self.programmingProgressLabel.setFont(font1)

        self.programmingProgressLayout.addWidget(self.programmingProgressLabel)

        self.programmingProgressSlider = QSlider(self.widget)
        self.programmingProgressSlider.setObjectName(u"programmingProgressSlider")
        self.programmingProgressSlider.setMaximumSize(QSize(16777215, 22))
        self.programmingProgressSlider.setOrientation(Qt.Orientation.Horizontal)

        self.programmingProgressLayout.addWidget(self.programmingProgressSlider)

        self.programmingProgressPercent = QLabel(self.widget)
        self.programmingProgressPercent.setObjectName(u"programmingProgressPercent")
        self.programmingProgressPercent.setMaximumSize(QSize(16777215, 22))

        self.programmingProgressLayout.addWidget(self.programmingProgressPercent)


        self.programmingGridLayout.addLayout(self.programmingProgressLayout, 6, 0, 1, 1)

        self.programmingNameLayout = QHBoxLayout()
        self.programmingNameLayout.setObjectName(u"programmingNameLayout")
        self.programmingNameLabel = QLabel(self.widget)
        self.programmingNameLabel.setObjectName(u"programmingNameLabel")
        self.programmingNameLabel.setMaximumSize(QSize(16777215, 22))
        self.programmingNameLabel.setFont(font1)

        self.programmingNameLayout.addWidget(self.programmingNameLabel)

        self.programmingName = QLineEdit(self.widget)
        self.programmingName.setObjectName(u"programmingName")
        self.programmingName.setMaximumSize(QSize(16777215, 22))

        self.programmingNameLayout.addWidget(self.programmingName)


        self.programmingGridLayout.addLayout(self.programmingNameLayout, 0, 0, 1, 1)


        self.retranslateUi(programmingProjectEditor)

        QMetaObject.connectSlotsByName(programmingProjectEditor)
    # setupUi

    def retranslateUi(self, programmingProjectEditor):
        programmingProjectEditor.setWindowTitle(QCoreApplication.translate("programmingProjectEditor", u"Project Planner 1.0 - Programming project editor", None))
        self.programmingSave.setText(QCoreApplication.translate("programmingProjectEditor", u"Save project", None))
        self.programmingClear.setText(QCoreApplication.translate("programmingProjectEditor", u"Clear all", None))
        self.programmingReturn.setText(QCoreApplication.translate("programmingProjectEditor", u"Return to main", None))
        self.programmingExit.setText(QCoreApplication.translate("programmingProjectEditor", u"Exit program", None))
        self.programmingHeader.setText(QCoreApplication.translate("programmingProjectEditor", u"Programming project", None))
        self.programmingFinishLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Project finish", None))
        self.programmingFinish.setDisplayFormat(QCoreApplication.translate("programmingProjectEditor", u"dd/MM/yy", None))
        self.programmingStartLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Project start", None))
        self.programmingStart.setDisplayFormat(QCoreApplication.translate("programmingProjectEditor", u"dd/MM/yy", None))
        self.githubLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"GitHub link", None))
        self.githubEdit.setText(QCoreApplication.translate("programmingProjectEditor", u"GitHub link", None))
        self.languagesLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Language(s) ", None))
        self.languagesEdit.setText(QCoreApplication.translate("programmingProjectEditor", u"Language(s)", None))
        self.programmingNotesLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Notes", None))
        self.programmingNotes.setText(QCoreApplication.translate("programmingProjectEditor", u"Notes", None))
        self.programmingStatusLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Status", None))
        self.programmingStatus.setItemText(0, QCoreApplication.translate("programmingProjectEditor", u"Select project status", None))
        self.programmingStatus.setItemText(1, QCoreApplication.translate("programmingProjectEditor", u"Pending", None))
        self.programmingStatus.setItemText(2, QCoreApplication.translate("programmingProjectEditor", u"In progress", None))
        self.programmingStatus.setItemText(3, QCoreApplication.translate("programmingProjectEditor", u"Cancelled", None))

        self.programmingProgressLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Progress", None))
        self.programmingProgressPercent.setText(QCoreApplication.translate("programmingProjectEditor", u"0%", None))
        self.programmingNameLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Project name", None))
        self.programmingName.setText(QCoreApplication.translate("programmingProjectEditor", u"Project name", None))
    # retranslateUi

