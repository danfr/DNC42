# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Fri Apr  3 20:01:13 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(774, 540)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../Images/Homer-Simpson-homer-simpson-3065329-800-600.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(600, 100, 160, 361))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listNames = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listNames.setMinimumSize(QtCore.QSize(50, 0))
        self.listNames.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listNames.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setItalic(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.listNames.setFont(font)
        self.listNames.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listNames.setAcceptDrops(False)
        self.listNames.setStyleSheet(_fromUtf8(""))
        self.listNames.setFrameShape(QtGui.QFrame.NoFrame)
        self.listNames.setFrameShadow(QtGui.QFrame.Sunken)
        self.listNames.setLineWidth(1)
        self.listNames.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listNames.setObjectName(_fromUtf8("listNames"))
        self.verticalLayout.addWidget(self.listNames)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 470, 741, 69))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 741, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setInputMask(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_2 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_6 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 100, 561, 40))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_5 = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.txtOutput = QtGui.QTextEdit(Dialog)
        self.txtOutput.setGeometry(QtCore.QRect(20, 160, 561, 291))
        self.txtOutput.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setItalic(False)
        self.txtOutput.setFont(font)
        self.txtOutput.setFocusPolicy(QtCore.Qt.NoFocus)
        self.txtOutput.setAcceptDrops(False)
        self.txtOutput.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtOutput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.txtOutput.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.txtOutput.setObjectName(_fromUtf8("txtOutput"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Nick list", None))
        self.listNames.setSortingEnabled(True)
        self.pushButton.setText(_translate("Dialog", "Send message", None))
        self.label_3.setText(_translate("Dialog", "IP : ", None))
        self.lineEdit_4.setText(_translate("Dialog", "127.0.0.1", None))
        self.label_4.setText(_translate("Dialog", "Port :", None))
        self.lineEdit_3.setText(_translate("Dialog", "2222", None))
        self.label_5.setText(_translate("Dialog", "Pseudo :", None))
        self.lineEdit_2.setText(_translate("Dialog", "anonymous", None))
        self.pushButton_6.setText(_translate("Dialog", "Change pseudo", None))
        self.pushButton_3.setText(_translate("Dialog", "Disconnect", None))
        self.pushButton_2.setText(_translate("Dialog", "Connect", None))
        self.pushButton_5.setText(_translate("Dialog", "Away From Keyboard", None))
        self.txtOutput.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Inconsolata\';\"><br /></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "Welcome to DNC", None))

