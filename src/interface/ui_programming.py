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
        self.saveProgramming = QPushButton(self.layoutWidget)
        self.saveProgramming.setObjectName(u"saveProgramming")

        self.programmingMenuGrid.addWidget(self.saveProgramming, 0, 0, 1, 1)

        self.clearProgramming = QPushButton(self.layoutWidget)
        self.clearProgramming.setObjectName(u"clearProgramming")

        self.programmingMenuGrid.addWidget(self.clearProgramming, 0, 1, 1, 1)

        self.returnToMainProgramming = QPushButton(self.layoutWidget)
        self.returnToMainProgramming.setObjectName(u"returnToMainProgramming")

        self.programmingMenuGrid.addWidget(self.returnToMainProgramming, 1, 0, 1, 1)

        self.exitProgramming = QPushButton(self.layoutWidget)
        self.exitProgramming.setObjectName(u"exitProgramming")

        self.programmingMenuGrid.addWidget(self.exitProgramming, 1, 1, 1, 1)

        self.programmingLabel = QLabel(programmingProjectEditor)
        self.programmingLabel.setObjectName(u"programmingLabel")
        self.programmingLabel.setGeometry(QRect(20, 20, 411, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.programmingLabel.setFont(font)
        self.programmingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(programmingProjectEditor)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(13, 133, 421, 321))
        self.programmingGridLayout = QGridLayout(self.widget)
        self.programmingGridLayout.setObjectName(u"programmingGridLayout")
        self.programmingGridLayout.setContentsMargins(0, 0, 0, 0)
        self.programmingFinishedLayout = QHBoxLayout()
        self.programmingFinishedLayout.setObjectName(u"programmingFinishedLayout")
        self.finishLabelProgramming = QLabel(self.widget)
        self.finishLabelProgramming.setObjectName(u"finishLabelProgramming")
        self.finishLabelProgramming.setMaximumSize(QSize(16777215, 22))
        font1 = QFont()
        font1.setBold(True)
        self.finishLabelProgramming.setFont(font1)

        self.programmingFinishedLayout.addWidget(self.finishLabelProgramming)

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
        self.startLabelProgramming = QLabel(self.widget)
        self.startLabelProgramming.setObjectName(u"startLabelProgramming")
        self.startLabelProgramming.setMaximumSize(QSize(16777215, 22))
        self.startLabelProgramming.setFont(font1)

        self.programmingStartLayout.addWidget(self.startLabelProgramming)

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
        self.notesLabelProgramming = QLabel(self.widget)
        self.notesLabelProgramming.setObjectName(u"notesLabelProgramming")
        self.notesLabelProgramming.setMaximumSize(QSize(16777215, 22))
        self.notesLabelProgramming.setFont(font1)

        self.programmingNotesLayout.addWidget(self.notesLabelProgramming)

        self.notesEditProgramming = QLineEdit(self.widget)
        self.notesEditProgramming.setObjectName(u"notesEditProgramming")
        self.notesEditProgramming.setMaximumSize(QSize(16777215, 22))

        self.programmingNotesLayout.addWidget(self.notesEditProgramming)


        self.programmingGridLayout.addLayout(self.programmingNotesLayout, 5, 0, 1, 1)

        self.programmingStatusLayout = QHBoxLayout()
        self.programmingStatusLayout.setObjectName(u"programmingStatusLayout")
        self.statusLabelProgramming = QLabel(self.widget)
        self.statusLabelProgramming.setObjectName(u"statusLabelProgramming")
        self.statusLabelProgramming.setMaximumSize(QSize(16777215, 22))
        self.statusLabelProgramming.setFont(font1)

        self.programmingStatusLayout.addWidget(self.statusLabelProgramming)

        self.statusComboProgramming = QComboBox(self.widget)
        self.statusComboProgramming.addItem("")
        self.statusComboProgramming.addItem("")
        self.statusComboProgramming.addItem("")
        self.statusComboProgramming.addItem("")
        self.statusComboProgramming.setObjectName(u"statusComboProgramming")
        self.statusComboProgramming.setMaximumSize(QSize(16777215, 22))
        self.statusComboProgramming.setMaxVisibleItems(4)
        self.statusComboProgramming.setMaxCount(4)

        self.programmingStatusLayout.addWidget(self.statusComboProgramming)

        self.programmingStatusLayout.setStretch(0, 1)
        self.programmingStatusLayout.setStretch(1, 3)

        self.programmingGridLayout.addLayout(self.programmingStatusLayout, 7, 0, 1, 1)

        self.programmingProgressLayout = QHBoxLayout()
        self.programmingProgressLayout.setObjectName(u"programmingProgressLayout")
        self.progressLabelProgramming = QLabel(self.widget)
        self.progressLabelProgramming.setObjectName(u"progressLabelProgramming")
        self.progressLabelProgramming.setMaximumSize(QSize(16777215, 22))
        self.progressLabelProgramming.setFont(font1)

        self.programmingProgressLayout.addWidget(self.progressLabelProgramming)

        self.progressSliderProgramming = QSlider(self.widget)
        self.progressSliderProgramming.setObjectName(u"progressSliderProgramming")
        self.progressSliderProgramming.setMaximumSize(QSize(16777215, 22))
        self.progressSliderProgramming.setOrientation(Qt.Orientation.Horizontal)

        self.programmingProgressLayout.addWidget(self.progressSliderProgramming)

        self.progressPercentageProgramming = QLabel(self.widget)
        self.progressPercentageProgramming.setObjectName(u"progressPercentageProgramming")
        self.progressPercentageProgramming.setMaximumSize(QSize(16777215, 22))

        self.programmingProgressLayout.addWidget(self.progressPercentageProgramming)


        self.programmingGridLayout.addLayout(self.programmingProgressLayout, 6, 0, 1, 1)

        self.programmingNameLayout = QHBoxLayout()
        self.programmingNameLayout.setObjectName(u"programmingNameLayout")
        self.nameLabelProgramming = QLabel(self.widget)
        self.nameLabelProgramming.setObjectName(u"nameLabelProgramming")
        self.nameLabelProgramming.setMaximumSize(QSize(16777215, 22))
        self.nameLabelProgramming.setFont(font1)

        self.programmingNameLayout.addWidget(self.nameLabelProgramming)

        self.projectNameProgramming = QLineEdit(self.widget)
        self.projectNameProgramming.setObjectName(u"projectNameProgramming")
        self.projectNameProgramming.setMaximumSize(QSize(16777215, 22))

        self.programmingNameLayout.addWidget(self.projectNameProgramming)


        self.programmingGridLayout.addLayout(self.programmingNameLayout, 0, 0, 1, 1)


        self.retranslateUi(programmingProjectEditor)

        QMetaObject.connectSlotsByName(programmingProjectEditor)
    # setupUi

    def retranslateUi(self, programmingProjectEditor):
        programmingProjectEditor.setWindowTitle(QCoreApplication.translate("programmingProjectEditor", u"Project Planner 1.0 - Programming project editor", None))
        self.saveProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Save project", None))
        self.clearProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Clear all", None))
        self.returnToMainProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Return to main", None))
        self.exitProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Exit program", None))
        self.programmingLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Programming project", None))
        self.finishLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project finish", None))
        self.programmingFinish.setDisplayFormat(QCoreApplication.translate("programmingProjectEditor", u"dd/MM/yy", None))
        self.startLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project start", None))
        self.programmingStart.setDisplayFormat(QCoreApplication.translate("programmingProjectEditor", u"dd/MM/yy", None))
        self.githubLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"GitHub link", None))
        self.githubEdit.setText(QCoreApplication.translate("programmingProjectEditor", u"GitHub link", None))
        self.languagesLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Language(s) ", None))
        self.languagesEdit.setText(QCoreApplication.translate("programmingProjectEditor", u"Language(s)", None))
        self.notesLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Notes", None))
        self.notesEditProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Notes", None))
        self.statusLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Status", None))
        self.statusComboProgramming.setItemText(0, QCoreApplication.translate("programmingProjectEditor", u"Select project status", None))
        self.statusComboProgramming.setItemText(1, QCoreApplication.translate("programmingProjectEditor", u"Pending", None))
        self.statusComboProgramming.setItemText(2, QCoreApplication.translate("programmingProjectEditor", u"In progress", None))
        self.statusComboProgramming.setItemText(3, QCoreApplication.translate("programmingProjectEditor", u"Cancelled", None))

        self.progressLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Progress", None))
        self.progressPercentageProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"0%", None))
        self.nameLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project name", None))
        self.projectNameProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project name", None))
    # retranslateUi

