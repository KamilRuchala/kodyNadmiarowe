# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'okno.ui'
#
# Created: Mon Jun 16 00:20:21 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 801, 591))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.lineEdit = QtGui.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 681, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushCode = QtGui.QPushButton(self.tab_3)
        self.pushCode.setGeometry(QtCore.QRect(700, 40, 81, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushCode.setFont(font)
        self.pushCode.setObjectName(_fromUtf8("pushCode"))
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushGenerate = QtGui.QPushButton(self.tab_3)
        self.pushGenerate.setGeometry(QtCore.QRect(10, 90, 191, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushGenerate.setFont(font)
        self.pushGenerate.setObjectName(_fromUtf8("pushGenerate"))
        self.pushOwn = QtGui.QPushButton(self.tab_3)
        self.pushOwn.setGeometry(QtCore.QRect(220, 90, 211, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushOwn.setFont(font)
        self.pushOwn.setObjectName(_fromUtf8("pushOwn"))
        self.user_crc = QtGui.QTextBrowser(self.tab_3)
        self.user_crc.setGeometry(QtCore.QRect(90, 520, 691, 21))
        self.user_crc.setObjectName(_fromUtf8("user_crc"))
        self.crc_32 = QtGui.QTextBrowser(self.tab_3)
        self.crc_32.setGeometry(QtCore.QRect(90, 480, 691, 21))
        self.crc_32.setObjectName(_fromUtf8("crc_32"))
        self.ccitt = QtGui.QTextBrowser(self.tab_3)
        self.ccitt.setGeometry(QtCore.QRect(90, 440, 691, 21))
        self.ccitt.setObjectName(_fromUtf8("ccitt"))
        self.xmodem = QtGui.QTextBrowser(self.tab_3)
        self.xmodem.setGeometry(QtCore.QRect(90, 400, 691, 21))
        self.xmodem.setObjectName(_fromUtf8("xmodem"))
        self.crc_16 = QtGui.QTextBrowser(self.tab_3)
        self.crc_16.setGeometry(QtCore.QRect(90, 360, 691, 21))
        self.crc_16.setObjectName(_fromUtf8("crc_16"))
        self.crc_12 = QtGui.QTextBrowser(self.tab_3)
        self.crc_12.setGeometry(QtCore.QRect(90, 320, 691, 21))
        self.crc_12.setObjectName(_fromUtf8("crc_12"))
        self.crc_10 = QtGui.QTextBrowser(self.tab_3)
        self.crc_10.setGeometry(QtCore.QRect(90, 280, 691, 21))
        self.crc_10.setObjectName(_fromUtf8("crc_10"))
        self.crc_8 = QtGui.QTextBrowser(self.tab_3)
        self.crc_8.setGeometry(QtCore.QRect(90, 240, 691, 21))
        self.crc_8.setObjectName(_fromUtf8("crc_8"))
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(10, 240, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(10, 280, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(10, 320, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(10, 360, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(0, 400, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(10, 440, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(10, 480, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(10, 520, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.clearOut = QtGui.QPushButton(self.tab_3)
        self.clearOut.setGeometry(QtCore.QRect(680, 210, 101, 23))
        self.clearOut.setObjectName(_fromUtf8("clearOut"))
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setMinimumSize(QtCore.QSize(797, 0))
        self.tab_4.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.encodeButton = QtGui.QPushButton(self.tab_4)
        self.encodeButton.setGeometry(QtCore.QRect(700, 40, 81, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.encodeButton.setFont(font)
        self.encodeButton.setObjectName(_fromUtf8("encodeButton"))
        self.label_20 = QtGui.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(10, 20, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.hammingInput = QtGui.QLineEdit(self.tab_4)
        self.hammingInput.setGeometry(QtCore.QRect(10, 40, 681, 20))
        self.hammingInput.setObjectName(_fromUtf8("hammingInput"))
        self.generateButton = QtGui.QPushButton(self.tab_4)
        self.generateButton.setGeometry(QtCore.QRect(10, 90, 171, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.generateButton.setFont(font)
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.kodHamminga = QtGui.QTextBrowser(self.tab_4)
        self.kodHamminga.setGeometry(QtCore.QRect(170, 210, 621, 21))
        self.kodHamminga.setStyleSheet(_fromUtf8(""))
        self.kodHamminga.setObjectName(_fromUtf8("kodHamminga"))
        self.WektorBledu = QtGui.QTextBrowser(self.tab_4)
        self.WektorBledu.setGeometry(QtCore.QRect(170, 240, 621, 21))
        self.WektorBledu.setObjectName(_fromUtf8("WektorBledu"))
        self.HammingWithError = QtGui.QTextBrowser(self.tab_4)
        self.HammingWithError.setGeometry(QtCore.QRect(170, 270, 621, 21))
        self.HammingWithError.setObjectName(_fromUtf8("HammingWithError"))
        self.DetekcjaB = QtGui.QTextBrowser(self.tab_4)
        self.DetekcjaB.setGeometry(QtCore.QRect(170, 300, 621, 21))
        self.DetekcjaB.setObjectName(_fromUtf8("DetekcjaB"))
        self.Skorygowany = QtGui.QTextBrowser(self.tab_4)
        self.Skorygowany.setGeometry(QtCore.QRect(170, 330, 621, 21))
        self.Skorygowany.setObjectName(_fromUtf8("Skorygowany"))
        self.errorButton = QtGui.QPushButton(self.tab_4)
        self.errorButton.setGeometry(QtCore.QRect(180, 90, 171, 23))
        self.errorButton.setObjectName(_fromUtf8("errorButton"))
        self.label_21 = QtGui.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(30, 210, 131, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(10, 270, 171, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(20, 240, 131, 20))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.tab_4)
        self.label_24.setGeometry(QtCore.QRect(0, 300, 171, 16))
        self.label_24.setText(_fromUtf8(""))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(30, 300, 121, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(30, 330, 121, 20))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.l1 = QtGui.QPushButton(self.tab_4)
        self.l1.setGeometry(QtCore.QRect(550, 410, 16, 21))
        self.l1.setStyleSheet(_fromUtf8("background: white;\n"
"color: rgb(153,153,255);\n"
"font: 9pt \"Arial Black\";"))
        self.l1.setObjectName(_fromUtf8("l1"))
        self.label = QtGui.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(550, 370, 151, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.l2 = QtGui.QPushButton(self.tab_4)
        self.l2.setGeometry(QtCore.QRect(550, 440, 16, 21))
        self.l2.setStyleSheet(_fromUtf8("background: white;\n"
"color: rgb(255,153,153);\n"
"font: 9pt \"Arial Black\";"))
        self.l2.setObjectName(_fromUtf8("l2"))
        self.l3 = QtGui.QPushButton(self.tab_4)
        self.l3.setGeometry(QtCore.QRect(550, 470, 16, 21))
        self.l3.setStyleSheet(_fromUtf8("background: white;\n"
"color: rgb(178,255,102);\n"
"font: 9pt \"Arial Black\";\n"
""))
        self.l3.setObjectName(_fromUtf8("l3"))
        self.label_2 = QtGui.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(580, 410, 171, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(580, 440, 171, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(580, 470, 201, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.detekcjaButton = QtGui.QPushButton(self.tab_4)
        self.detekcjaButton.setGeometry(QtCore.QRect(350, 90, 171, 23))
        self.detekcjaButton.setObjectName(_fromUtf8("detekcjaButton"))
        self.korekcjaButton = QtGui.QPushButton(self.tab_4)
        self.korekcjaButton.setGeometry(QtCore.QRect(520, 90, 171, 23))
        self.korekcjaButton.setObjectName(_fromUtf8("korekcjaButton"))
        self.clearOutHam = QtGui.QPushButton(self.tab_4)
        self.clearOutHam.setGeometry(QtCore.QRect(680, 180, 101, 23))
        self.clearOutHam.setObjectName(_fromUtf8("clearOutHam"))
        self.scrollArea = QtGui.QScrollArea(self.tab_4)
        self.scrollArea.setGeometry(QtCore.QRect(50, 400, 221, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 219, 139))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 256, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 281, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.input2z5 = QtGui.QLineEdit(self.tab)
        self.input2z5.setGeometry(QtCore.QRect(10, 40, 681, 20))
        self.input2z5.setObjectName(_fromUtf8("input2z5"))
        self.encode2z5 = QtGui.QPushButton(self.tab)
        self.encode2z5.setGeometry(QtCore.QRect(700, 40, 81, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.encode2z5.setFont(font)
        self.encode2z5.setObjectName(_fromUtf8("encode2z5"))
        self.losowo2z5 = QtGui.QPushButton(self.tab)
        self.losowo2z5.setGeometry(QtCore.QRect(10, 80, 171, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.losowo2z5.setFont(font)
        self.losowo2z5.setObjectName(_fromUtf8("losowo2z5"))
        self.przeplatany2z5 = QtGui.QTextBrowser(self.tab)
        self.przeplatany2z5.setGeometry(QtCore.QRect(10, 200, 761, 21))
        self.przeplatany2z5.setObjectName(_fromUtf8("przeplatany2z5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 761, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 761, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.kod2z5 = QtGui.QTextBrowser(self.tab)
        self.kod2z5.setGeometry(QtCore.QRect(10, 140, 761, 21))
        self.kod2z5.setObjectName(_fromUtf8("kod2z5"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 310, 801, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 260, 741, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.kodPaskowy = QtGui.QPushButton(self.tab)
        self.kodPaskowy.setGeometry(QtCore.QRect(310, 290, 161, 23))
        self.kodPaskowy.setObjectName(_fromUtf8("kodPaskowy"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 230, 741, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.czyscOutput = QtGui.QPushButton(self.tab)
        self.czyscOutput.setGeometry(QtCore.QRect(700, 110, 81, 23))
        self.czyscOutput.setObjectName(_fromUtf8("czyscOutput"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(10, 360, 771, 191))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Kody nadmiarowe", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_3.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p/></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushCode.setText(QtGui.QApplication.translate("MainWindow", "Koduj", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Podaj binararną informacje do zakodowania", None, QtGui.QApplication.UnicodeUTF8))
        self.pushGenerate.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Generuje losowy ciąg binarny</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushGenerate.setWhatsThis(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Generuje losowy ciąg binarny</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushGenerate.setText(QtGui.QApplication.translate("MainWindow", "Generuj Losowo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOwn.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Pozwala wprowadzić własny wielomian(dzielnik)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOwn.setWhatsThis(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Pozwala wprowadzić własny wielomian(dzielnik)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOwn.setText(QtGui.QApplication.translate("MainWindow", "Wprowadź własny wielomian", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "CRC-8", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "CRC-10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "CRC-12", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "CRC-16", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Xmodem16", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "CCITT-16", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "CRC-32", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "UserCRC", None, QtGui.QApplication.UnicodeUTF8))
        self.clearOut.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Czyści output</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.clearOut.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "CRC-Encoding", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_4.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Dekodowanie CRC</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.encodeButton.setText(QtGui.QApplication.translate("MainWindow", "Koduj", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Podaj binararną informacje do zakodowania", None, QtGui.QApplication.UnicodeUTF8))
        self.generateButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Generuje losowy ciąg binarny</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.generateButton.setWhatsThis(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Generuje losowy ciąg binarny</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.generateButton.setText(QtGui.QApplication.translate("MainWindow", "Generuj Losowo", None, QtGui.QApplication.UnicodeUTF8))
        self.errorButton.setText(QtGui.QApplication.translate("MainWindow", "Wektor Błędu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "  Kod Hamminga", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Kod Hamminga z błędem", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "      Wektor błędu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "  Detekcja błędu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "Skorygowany kod ", None, QtGui.QApplication.UnicodeUTF8))
        self.l1.setText(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "LEGENDA:", None, QtGui.QApplication.UnicodeUTF8))
        self.l2.setText(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.l3.setText(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "- miejsca bitów parzystości", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "- pozycja błędu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "- pozycja skorygowanego błędu", None, QtGui.QApplication.UnicodeUTF8))
        self.detekcjaButton.setText(QtGui.QApplication.translate("MainWindow", "Detekcja", None, QtGui.QApplication.UnicodeUTF8))
        self.korekcjaButton.setText(QtGui.QApplication.translate("MainWindow", "Korekcja", None, QtGui.QApplication.UnicodeUTF8))
        self.clearOutHam.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Czyści output</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.clearOutHam.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">saddddddddddddddddddddddddddddddddddddddddd</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Hamming", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Podaj ciąg cyfr dziesiętnych do zakowania", None, QtGui.QApplication.UnicodeUTF8))
        self.encode2z5.setText(QtGui.QApplication.translate("MainWindow", "Koduj", None, QtGui.QApplication.UnicodeUTF8))
        self.losowo2z5.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Generuje losowy ciąg binarny</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.losowo2z5.setWhatsThis(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Generuje losowy ciąg binarny</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.losowo2z5.setText(QtGui.QApplication.translate("MainWindow", "Generuj Losowo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Kod interleaved2of5 (przeplatane 2z5)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Kod 2z5 Standard</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Kod paskowy interleaved2of5</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.kodPaskowy.setText(QtGui.QApplication.translate("MainWindow", "Generuj kod paskowy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Info: Jeśli podano nieparzysty ciąg na wejsciu to w celu poprawnego przeplatania zostanie dodane zero na początku", None, QtGui.QApplication.UnicodeUTF8))
        self.czyscOutput.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "2 z 5", None, QtGui.QApplication.UnicodeUTF8))

