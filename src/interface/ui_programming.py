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
        self.programmingHeader = QLineEdit(programmingProjectEditor)
        self.programmingHeader.setObjectName(u"programmingHeader")
        self.programmingHeader.setGeometry(QRect(10, 20, 421, 91))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.programmingHeader.setFont(font)
        self.programmingHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget = QWidget(programmingProjectEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 130, 421, 321))
        self.gridProgramming = QGridLayout(self.layoutWidget)
        self.gridProgramming.setObjectName(u"gridProgramming")
        self.gridProgramming.setContentsMargins(0, 0, 0, 0)
        self.nameLayoutProgramming = QHBoxLayout()
        self.nameLayoutProgramming.setObjectName(u"nameLayoutProgramming")
        self.nameLabelProgramming = QLabel(self.layoutWidget)
        self.nameLabelProgramming.setObjectName(u"nameLabelProgramming")
        font1 = QFont()
        font1.setBold(True)
        self.nameLabelProgramming.setFont(font1)

        self.nameLayoutProgramming.addWidget(self.nameLabelProgramming)

        self.projectNameProgramming = QLineEdit(self.layoutWidget)
        self.projectNameProgramming.setObjectName(u"projectNameProgramming")

        self.nameLayoutProgramming.addWidget(self.projectNameProgramming)

        self.nameLayoutProgramming.setStretch(0, 1)
        self.nameLayoutProgramming.setStretch(1, 3)

        self.gridProgramming.addLayout(self.nameLayoutProgramming, 0, 0, 1, 1)

        self.startLayoutProgramming = QHBoxLayout()
        self.startLayoutProgramming.setSpacing(6)
        self.startLayoutProgramming.setObjectName(u"startLayoutProgramming")
        self.startLabelProgramming = QLabel(self.layoutWidget)
        self.startLabelProgramming.setObjectName(u"startLabelProgramming")
        self.startLabelProgramming.setFont(font1)

        self.startLayoutProgramming.addWidget(self.startLabelProgramming)

        self.startDateProgramming = QDateEdit(self.layoutWidget)
        self.startDateProgramming.setObjectName(u"startDateProgramming")

        self.startLayoutProgramming.addWidget(self.startDateProgramming)

        self.startLayoutProgramming.setStretch(0, 1)
        self.startLayoutProgramming.setStretch(1, 3)

        self.gridProgramming.addLayout(self.startLayoutProgramming, 1, 0, 1, 1)

        self.finishLayoutProgramming = QHBoxLayout()
        self.finishLayoutProgramming.setSpacing(6)
        self.finishLayoutProgramming.setObjectName(u"finishLayoutProgramming")
        self.finishLabelProgramming = QLabel(self.layoutWidget)
        self.finishLabelProgramming.setObjectName(u"finishLabelProgramming")
        self.finishLabelProgramming.setFont(font1)

        self.finishLayoutProgramming.addWidget(self.finishLabelProgramming)

        self.finishDateProgramming = QDateEdit(self.layoutWidget)
        self.finishDateProgramming.setObjectName(u"finishDateProgramming")

        self.finishLayoutProgramming.addWidget(self.finishDateProgramming)

        self.finishLayoutProgramming.setStretch(0, 1)
        self.finishLayoutProgramming.setStretch(1, 3)

        self.gridProgramming.addLayout(self.finishLayoutProgramming, 2, 0, 1, 1)

        self.languagesLayout = QHBoxLayout()
        self.languagesLayout.setObjectName(u"languagesLayout")
        self.languagesLabel = QLabel(self.layoutWidget)
        self.languagesLabel.setObjectName(u"languagesLabel")
        self.languagesLabel.setFont(font1)

        self.languagesLayout.addWidget(self.languagesLabel)

        self.languagesEdit = QLineEdit(self.layoutWidget)
        self.languagesEdit.setObjectName(u"languagesEdit")

        self.languagesLayout.addWidget(self.languagesEdit)

        self.languagesLayout.setStretch(0, 1)
        self.languagesLayout.setStretch(1, 3)

        self.gridProgramming.addLayout(self.languagesLayout, 3, 0, 1, 1)

        self.languagesLayout_2 = QHBoxLayout()
        self.languagesLayout_2.setObjectName(u"languagesLayout_2")
        self.languagesLabel_2 = QLabel(self.layoutWidget)
        self.languagesLabel_2.setObjectName(u"languagesLabel_2")
        self.languagesLabel_2.setFont(font1)

        self.languagesLayout_2.addWidget(self.languagesLabel_2)

        self.languagesEdit_2 = QLineEdit(self.layoutWidget)
        self.languagesEdit_2.setObjectName(u"languagesEdit_2")

        self.languagesLayout_2.addWidget(self.languagesEdit_2)

        self.languagesLayout_2.setStretch(0, 1)
        self.languagesLayout_2.setStretch(1, 3)

        self.gridProgramming.addLayout(self.languagesLayout_2, 4, 0, 1, 1)

        self.nameLayoutProgramming_2 = QHBoxLayout()
        self.nameLayoutProgramming_2.setObjectName(u"nameLayoutProgramming_2")
        self.notesLabelProgramming = QLabel(self.layoutWidget)
        self.notesLabelProgramming.setObjectName(u"notesLabelProgramming")
        self.notesLabelProgramming.setFont(font1)

        self.nameLayoutProgramming_2.addWidget(self.notesLabelProgramming)

        self.notesEditProgramming = QLineEdit(self.layoutWidget)
        self.notesEditProgramming.setObjectName(u"notesEditProgramming")

        self.nameLayoutProgramming_2.addWidget(self.notesEditProgramming)

        self.nameLayoutProgramming_2.setStretch(0, 1)
        self.nameLayoutProgramming_2.setStretch(1, 3)

        self.gridProgramming.addLayout(self.nameLayoutProgramming_2, 5, 0, 1, 1)

        self.progressLayoutProgramming = QHBoxLayout()
        self.progressLayoutProgramming.setObjectName(u"progressLayoutProgramming")
        self.progressLabelProgramming = QLabel(self.layoutWidget)
        self.progressLabelProgramming.setObjectName(u"progressLabelProgramming")
        self.progressLabelProgramming.setFont(font1)

        self.progressLayoutProgramming.addWidget(self.progressLabelProgramming)

        self.progressSliderProgramming = QSlider(self.layoutWidget)
        self.progressSliderProgramming.setObjectName(u"progressSliderProgramming")
        self.progressSliderProgramming.setOrientation(Qt.Orientation.Horizontal)

        self.progressLayoutProgramming.addWidget(self.progressSliderProgramming)

        self.progressLayoutProgramming.setStretch(0, 1)
        self.progressLayoutProgramming.setStretch(1, 3)

        self.gridProgramming.addLayout(self.progressLayoutProgramming, 6, 0, 1, 1)

        self.statusLayoutProgramming = QHBoxLayout()
        self.statusLayoutProgramming.setObjectName(u"statusLayoutProgramming")
        self.statusLabelProgramming = QLabel(self.layoutWidget)
        self.statusLabelProgramming.setObjectName(u"statusLabelProgramming")
        self.statusLabelProgramming.setFont(font1)

        self.statusLayoutProgramming.addWidget(self.statusLabelProgramming)

        self.statusComboProgramming = QComboBox(self.layoutWidget)
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

        self.gridProgramming.addLayout(self.statusLayoutProgramming, 7, 0, 1, 1)

        self.layoutWidget1 = QWidget(programmingProjectEditor)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 470, 421, 111))
        self.programmingMenuGrid = QGridLayout(self.layoutWidget1)
        self.programmingMenuGrid.setObjectName(u"programmingMenuGrid")
        self.programmingMenuGrid.setContentsMargins(0, 0, 0, 0)
        self.saveProgramming = QPushButton(self.layoutWidget1)
        self.saveProgramming.setObjectName(u"saveProgramming")

        self.programmingMenuGrid.addWidget(self.saveProgramming, 0, 0, 1, 1)

        self.clearProgramming = QPushButton(self.layoutWidget1)
        self.clearProgramming.setObjectName(u"clearProgramming")

        self.programmingMenuGrid.addWidget(self.clearProgramming, 0, 1, 1, 1)

        self.returnToMainProgramming = QPushButton(self.layoutWidget1)
        self.returnToMainProgramming.setObjectName(u"returnToMainProgramming")

        self.programmingMenuGrid.addWidget(self.returnToMainProgramming, 1, 0, 1, 1)

        self.exitProgramming = QPushButton(self.layoutWidget1)
        self.exitProgramming.setObjectName(u"exitProgramming")

        self.programmingMenuGrid.addWidget(self.exitProgramming, 1, 1, 1, 1)


        self.retranslateUi(programmingProjectEditor)

        QMetaObject.connectSlotsByName(programmingProjectEditor)
    # setupUi

    def retranslateUi(self, programmingProjectEditor):
        programmingProjectEditor.setWindowTitle(QCoreApplication.translate("programmingProjectEditor", u"Project Planner 1.0 - Programming project editor", None))
        self.programmingHeader.setText(QCoreApplication.translate("programmingProjectEditor", u"Programming project", None))
        self.nameLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project name", None))
        self.projectNameProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project name", None))
        self.startLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project start", None))
        self.finishLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Project finish", None))
        self.languagesLabel.setText(QCoreApplication.translate("programmingProjectEditor", u"Language(s) ", None))
        self.languagesEdit.setText(QCoreApplication.translate("programmingProjectEditor", u"Language(s)", None))
        self.languagesLabel_2.setText(QCoreApplication.translate("programmingProjectEditor", u"GitHub link", None))
        self.languagesEdit_2.setText(QCoreApplication.translate("programmingProjectEditor", u"GitHub link", None))
        self.notesLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Notes", None))
        self.notesEditProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Notes", None))
        self.progressLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Progress", None))
        self.statusLabelProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Status", None))
        self.statusComboProgramming.setItemText(0, QCoreApplication.translate("programmingProjectEditor", u"Select project status", None))
        self.statusComboProgramming.setItemText(1, QCoreApplication.translate("programmingProjectEditor", u"Pending", None))
        self.statusComboProgramming.setItemText(2, QCoreApplication.translate("programmingProjectEditor", u"In progress", None))
        self.statusComboProgramming.setItemText(3, QCoreApplication.translate("programmingProjectEditor", u"Cancelled", None))

        self.saveProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Save project", None))
        self.clearProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Clear all", None))
        self.returnToMainProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Return to main", None))
        self.exitProgramming.setText(QCoreApplication.translate("programmingProjectEditor", u"Exit program", None))
    # retranslateUi

