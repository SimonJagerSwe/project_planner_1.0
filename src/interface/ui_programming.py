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
        self.widget.setGeometry(QRect(11, 131, 421, 321))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLayoutProgramming = QHBoxLayout()
        self.nameLayoutProgramming.setObjectName(u"nameLayoutProgramming")
        self.nameLabelProgramming = QLabel(self.widget)
        self.nameLabelProgramming.setObjectName(u"nameLabelProgramming")
        font1 = QFont()
        font1.setBold(True)
        self.nameLabelProgramming.setFont(font1)

        self.nameLayoutProgramming.addWidget(self.nameLabelProgramming)

        self.projectNameProgramming = QLineEdit(self.widget)
        self.projectNameProgramming.setObjectName(u"projectNameProgramming")

        self.nameLayoutProgramming.addWidget(self.projectNameProgramming)

        self.nameLayoutProgramming.setStretch(0, 1)
        self.nameLayoutProgramming.setStretch(1, 3)

        self.gridLayout.addLayout(self.nameLayoutProgramming, 0, 0, 1, 1)

        self.startLayoutProgramming = QHBoxLayout()
        self.startLayoutProgramming.setSpacing(6)
        self.startLayoutProgramming.setObjectName(u"startLayoutProgramming")
        self.startLabelProgramming = QLabel(self.widget)
        self.startLabelProgramming.setObjectName(u"startLabelProgramming")
        self.startLabelProgramming.setFont(font1)

        self.startLayoutProgramming.addWidget(self.startLabelProgramming)

        self.startDateProgramming = QDateEdit(self.widget)
        self.startDateProgramming.setObjectName(u"startDateProgramming")
        self.startDateProgramming.setDate(QDate(2000, 1, 1))

        self.startLayoutProgramming.addWidget(self.startDateProgramming)

        self.startLayoutProgramming.setStretch(0, 1)
        self.startLayoutProgramming.setStretch(1, 3)

        self.gridLayout.addLayout(self.startLayoutProgramming, 1, 0, 1, 1)

        self.finishLayoutProgramming = QHBoxLayout()
        self.finishLayoutProgramming.setSpacing(6)
        self.finishLayoutProgramming.setObjectName(u"finishLayoutProgramming")
        self.finishLabelProgramming = QLabel(self.widget)
        self.finishLabelProgramming.setObjectName(u"finishLabelProgramming")
        self.finishLabelProgramming.setFont(font1)

        self.finishLayoutProgramming.addWidget(self.finishLabelProgramming)

        self.finishDateProgramming = QDateEdit(self.widget)
        self.finishDateProgramming.setObjectName(u"finishDateProgramming")

        self.finishLayoutProgramming.addWidget(self.finishDateProgramming)

        self.finishLayoutProgramming.setStretch(0, 1)
        self.finishLayoutProgramming.setStretch(1, 3)

        self.gridLayout.addLayout(self.finishLayoutProgramming, 2, 0, 1, 1)

        self.languagesLayout = QHBoxLayout()
        self.languagesLayout.setObjectName(u"languagesLayout")
        self.languagesLabel = QLabel(self.widget)
        self.languagesLabel.setObjectName(u"languagesLabel")
        self.languagesLabel.setFont(font1)

        self.languagesLayout.addWidget(self.languagesLabel)

        self.languagesEdit = QLineEdit(self.widget)
        self.languagesEdit.setObjectName(u"languagesEdit")

        self.languagesLayout.addWidget(self.languagesEdit)

        self.languagesLayout.setStretch(0, 1)
        self.languagesLayout.setStretch(1, 3)

        self.gridLayout.addLayout(self.languagesLayout, 3, 0, 1, 1)

        self.githuhLayout = QHBoxLayout()
        self.githuhLayout.setObjectName(u"githuhLayout")
        self.githubLabel = QLabel(self.widget)
        self.githubLabel.setObjectName(u"githubLabel")
        self.githubLabel.setFont(font1)

        self.githuhLayout.addWidget(self.githubLabel)

        self.githubEdit = QLineEdit(self.widget)
        self.githubEdit.setObjectName(u"githubEdit")

        self.githuhLayout.addWidget(self.githubEdit)

        self.githuhLayout.setStretch(0, 1)
        self.githuhLayout.setStretch(1, 3)

        self.gridLayout.addLayout(self.githuhLayout, 4, 0, 1, 1)

        self.nameLayoutProgramming_2 = QHBoxLayout()
        self.nameLayoutProgramming_2.setObjectName(u"nameLayoutProgramming_2")
        self.notesLabelProgramming = QLabel(self.widget)
        self.notesLabelProgramming.setObjectName(u"notesLabelProgramming")
        self.notesLabelProgramming.setFont(font1)

        self.nameLayoutProgramming_2.addWidget(self.notesLabelProgramming)

        self.notesEditProgramming = QLineEdit(self.widget)
        self.notesEditProgramming.setObjectName(u"notesEditProgramming")

        self.nameLayoutProgramming_2.addWidget(self.notesEditProgramming)

        self.nameLayoutProgramming_2.setStretch(0, 1)
        self.nameLayoutProgramming_2.setStretch(1, 3)

        self.gridLayout.addLayout(self.nameLayoutProgramming_2, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressLabelProgramming = QLabel(self.widget)
        self.progressLabelProgramming.setObjectName(u"progressLabelProgramming")
        self.progressLabelProgramming.setFont(font1)

        self.horizontalLayout.addWidget(self.progressLabelProgramming)

        self.progressSliderProgramming = QSlider(self.widget)
        self.progressSliderProgramming.setObjectName(u"progressSliderProgramming")
        self.progressSliderProgramming.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.progressSliderProgramming)

        self.progressPercentageProgramming = QLabel(self.widget)
        self.progressPercentageProgramming.setObjectName(u"progressPercentageProgramming")

        self.horizontalLayout.addWidget(self.progressPercentageProgramming)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.statusLayoutProgramming = QHBoxLayout()
        self.statusLayoutProgramming.setObjectName(u"statusLayoutProgramming")
        self.statusLabelProgramming = QLabel(self.widget)
        self.statusLabelProgramming.setObjectName(u"statusLabelProgramming")
        self.statusLabelProgramming.setFont(font1)

        self.statusLayoutProgramming.addWidget(self.statusLabelProgramming)

        self.statusComboProgramming = QComboBox(self.widget)
        self.statusComboProgramming.addItem("")
        self.statusComboProgramming.addItem("")
        self.statusComboProgramming.addItem("")
        self.statusComboProgramming.addItem("")
        self.statusComboProgramming.setObjectName(u"statusComboProgramming")
        self.statusComboProgramming.setMaxVisibleItems(4)
        self.statusComboProgramming.setMaxCount(4)

        self.statusLayoutProgramming.addWidget(self.statusComboProgramming)

        self.statusLayoutProgramming.setStretch(0, 1)
        self.statusLayoutProgramming.setStretch(1, 3)

        self.gridLayout.addLayout(self.statusLayoutProgramming, 7, 0, 1, 1)


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
        self.nameLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project name", None))
        self.projectNameProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project name", None))
        self.startLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project start", None))
        self.finishLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project finish", None))
        self.languagesLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Language(s) ", None))
        self.languagesEdit.setText(QCoreApplication.translate("programmingProjectEditor", u"Language(s)", None))
        self.githubLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"GitHub link", None))
        self.githubEdit.setText(QCoreApplication.translate("programmingProjectEditor", u"GitHub link", None))
        self.notesLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Notes", None))
        self.notesEditProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Notes", None))
        self.progressLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Progress", None))
        self.progressPercentageProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"0%", None))
        self.statusLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Status", None))
        self.statusComboProgramming.setItemText(0, QCoreApplication.translate("programmingProjectEditor", u"Select project status", None))
        self.statusComboProgramming.setItemText(1, QCoreApplication.translate("programmingProjectEditor", u"Pending", None))
        self.statusComboProgramming.setItemText(2, QCoreApplication.translate("programmingProjectEditor", u"In progress", None))
        self.statusComboProgramming.setItemText(3, QCoreApplication.translate("programmingProjectEditor", u"Cancelled", None))

    # retranslateUi

