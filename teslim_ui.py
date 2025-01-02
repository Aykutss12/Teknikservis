import sys
import sqlite3
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog,  QPrintPreviewDialog
from PyQt5.QtGui import QPainter,QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from teslimedilenler import veri





class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(653, 824)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 20, 171, 101))
        self.label.setStyleSheet("image: url(:/newPrefix/ikon/responsible.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 420, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 380, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 460, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(320, 180, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(330, 250, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(330, 290, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(330, 330, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_adi = QtWidgets.QLineEdit(Form)
        self.lineEdit_adi.setEnabled(True)
        self.lineEdit_adi.setGeometry(QtCore.QRect(120, 180, 181, 20))
        self.lineEdit_adi.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_adi.setText("")
        self.lineEdit_adi.setObjectName("lineEdit_adi")
        self.lineEdit_tel = QtWidgets.QLineEdit(Form)
        self.lineEdit_tel.setEnabled(True)
        self.lineEdit_tel.setGeometry(QtCore.QRect(120, 220, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_tel.setFont(font)
        self.lineEdit_tel.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_tel.setText("")
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.lineEdit_marka = QtWidgets.QLineEdit(Form)
        self.lineEdit_marka.setEnabled(True)
        self.lineEdit_marka.setGeometry(QtCore.QRect(120, 260, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_marka.setFont(font)
        self.lineEdit_marka.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_marka.setText("")
        self.lineEdit_marka.setObjectName("lineEdit_marka")
        self.lineEdit_model = QtWidgets.QLineEdit(Form)
        self.lineEdit_model.setEnabled(True)
        self.lineEdit_model.setGeometry(QtCore.QRect(120, 300, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_model.setFont(font)
        self.lineEdit_model.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_model.setText("")
        self.lineEdit_model.setObjectName("lineEdit_model")
        self.lineEdit_serino = QtWidgets.QLineEdit(Form)
        self.lineEdit_serino.setEnabled(True)
        self.lineEdit_serino.setGeometry(QtCore.QRect(120, 340, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_serino.setFont(font)
        self.lineEdit_serino.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_serino.setText("")
        self.lineEdit_serino.setObjectName("lineEdit_serino")
        self.lineEdit_garanti = QtWidgets.QLineEdit(Form)
        self.lineEdit_garanti.setEnabled(True)
        self.lineEdit_garanti.setGeometry(QtCore.QRect(120, 380, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_garanti.setFont(font)
        self.lineEdit_garanti.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_garanti.setText("")
        self.lineEdit_garanti.setObjectName("lineEdit_garanti")
        self.lineEdit_grnt = QtWidgets.QLineEdit(Form)
        self.lineEdit_grnt.setEnabled(True)
        self.lineEdit_grnt.setGeometry(QtCore.QRect(120, 420, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_grnt.setFont(font)
        self.lineEdit_grnt.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_grnt.setText("")
        self.lineEdit_grnt.setObjectName("lineEdit_grnt")
        self.lineEdit_zelkod = QtWidgets.QLineEdit(Form)
        self.lineEdit_zelkod.setEnabled(True)
        self.lineEdit_zelkod.setGeometry(QtCore.QRect(120, 460, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_zelkod.setFont(font)
        self.lineEdit_zelkod.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_zelkod.setText("")
        self.lineEdit_zelkod.setObjectName("lineEdit_zelkod")
        self.lineEdit_alan = QtWidgets.QLineEdit(Form)
        self.lineEdit_alan.setEnabled(True)
        self.lineEdit_alan.setGeometry(QtCore.QRect(430, 250, 181, 20))
        self.lineEdit_alan.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_alan.setText("")
        self.lineEdit_alan.setObjectName("lineEdit_alan")
        self.lineEdit_akses = QtWidgets.QLineEdit(Form)
        self.lineEdit_akses.setEnabled(True)
        self.lineEdit_akses.setGeometry(QtCore.QRect(430, 290, 181, 20))
        self.lineEdit_akses.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_akses.setText("")
        self.lineEdit_akses.setObjectName("lineEdit_akses")
        self.lineEdit_gtarih = QtWidgets.QLineEdit(Form)
        self.lineEdit_gtarih.setEnabled(True)
        self.lineEdit_gtarih.setGeometry(QtCore.QRect(430, 330, 181, 20))
        self.lineEdit_gtarih.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lineEdit_gtarih.setText("")
        self.lineEdit_gtarih.setObjectName("lineEdit_gtarih")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(430, 180, 181, 61))
        self.textEdit.setStyleSheet("background-color: rgb(222, 255, 151);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(330, 380, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.textEdit_islem = QtWidgets.QTextEdit(Form)
        self.textEdit_islem.setGeometry(QtCore.QRect(430, 380, 181, 101))
        self.textEdit_islem.setStyleSheet("background-color: rgb(218, 218, 163);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.textEdit_islem.setObjectName("textEdit_islem")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(330, 520, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(330, 560, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(330, 600, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_yapan = QtWidgets.QLineEdit(Form)
        self.lineEdit_yapan.setGeometry(QtCore.QRect(430, 520, 181, 20))
        self.lineEdit_yapan.setStyleSheet("background-color: rgb(218, 218, 163);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.lineEdit_yapan.setObjectName("lineEdit_yapan")
        self.lineEdit_eden = QtWidgets.QLineEdit(Form)
        self.lineEdit_eden.setGeometry(QtCore.QRect(430, 560, 181, 20))
        self.lineEdit_eden.setStyleSheet("background-color: rgb(218, 218, 163);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.lineEdit_eden.setObjectName("lineEdit_eden")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(430, 600, 171, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 12, 30), QtCore.QTime(21, 33, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 700, 111, 91))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/delivery - Kopya.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(70, 70))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 700, 101, 91))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 700, 101, 91))
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(0, 540, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.textEdit_islem_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_islem_2.setGeometry(QtCore.QRect(110, 540, 191, 111))
        self.textEdit_islem_2.setStyleSheet("background-color: rgb(218, 218, 163);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.textEdit_islem_2.setObjectName("textEdit_islem_2")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(140, 140, 401, 31))
        self.label_19.setObjectName("label_19")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 700, 181, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Teslim Sayfası"))
        self.label_2.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"right\">ADI-SOYADI :</p></body></html>"))
        self.label_3.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"right\">İLETİŞİM :</p></body></html>"))
        self.label_4.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"right\">MARKA :</p></body></html>"))
        self.label_5.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"right\">MODEL :</p></body></html>"))
        self.label_6.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"right\">GENEL DURUMU :</p></body></html>"))
        self.label_7.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"right\">SERİ NO :</p></body></html>"))
        self.label_8.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"right\">GARANTİ DURUMU :</p></body></html>"))
        self.label_9.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"right\">ÖZEL KOD :</p></body></html>"))
        self.label_11.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p align=\"right\">ARIZA BİLGİSİ :</p></body></html>"))
        self.label_12.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p align=\"right\">TESLİM ALAN :</p></body></html>"))
        self.label_13.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"right\">AKSESUARI :</p></body></html>"))
        self.label_14.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p align=\"right\">GELDİĞİ TARİH :</p></body></html>"))
        self.lineEdit_adi.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_tel.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_marka.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_model.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_serino.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_garanti.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_grnt.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_zelkod.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_alan.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_akses.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.lineEdit_gtarih.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">s</span></p></body></html>"))
        self.label_10.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"right\">YAPILAN İŞLEM :</p></body></html>"))
        self.label_15.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p align=\"right\">İŞLEMİ YAPAN :</p></body></html>"))
        self.label_16.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p align=\"right\">TESLİM EDEN :</p></body></html>"))
        self.label_17.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"right\">TESLİM TARİHİ :</p></body></html>"))
        self.pushButton.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">VERİ AL</span></p></body></html>"))
        self.pushButton_2.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">YAZDIR</span></p></body></html>"))
        self.pushButton_3.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">KAYIT AL</span></p></body></html>"))
        self.label_18.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p align=\"right\">EK BİLGİ :</p></body></html>"))
        self.label_19.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#aa0000;\">TESLİM EDİLEN ÜRÜNÜ KAYITLAMAYI UNUTMAYINIZ.</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "TESLİM EDİLENLER"))
import icon_rc








class teslim(QtWidgets.QMainWindow):
        def __init__(self):
                super(teslim, self).__init__()
                self.ui = Ui_Form()
                self.ui.setupUi(self)
                self.load()
                
                self.ui.pushButton.clicked.connect(self.sorgula)
                self.ui.pushButton_2.clicked.connect(self.print_preview)
                self.ui.pushButton_3.clicked.connect(self.kaydet)
                self.ui.pushButton_4.clicked.connect(self.verisayfa)
        def load(self):
                try:
                 self.dbcon=sqlite3.connect("data.db")
                 
                except Exception as e:
                   print("bağlanmadı")     
        
        def sorgula(self):
        
          
          try:
            # Kullanıcıdan sorgu almak (lineEdit_adi'ye yazılmış sorgu)
                sorgu = self.ui.lineEdit_adi.text()  # lineEdit_adi'ye girilen değeri alıyoruz
            
                if sorgu.strip() == "":
                         QMessageBox.warning(self, "Sorgu Hatası", "Lütfen sorguyu kontrol ediniz.")
                         return

            # Veritabanına sorguyu gönder
                cursor = self.dbcon.cursor()
                query = "SELECT * FROM müs WHERE adi LIKE ?"
                cursor.execute(query, ('%' + sorgu + '%',))  # LIKE ile sorgu gönderiyoruz
                rows = cursor.fetchall()  # Sorgu sonucu veriler

                if not rows:
                        QMessageBox.information(self, "Sonuç Yok", "Sorguya ait herhangi bir sonuç bulunamadı.")
                        return

                # Eğer sonuç varsa, her bir sonucu QLineEdit'lere yazdırıyoruz
                # Örnek olarak, ilk satırdaki verileri alıyoruz (sorgunun sonuçlarının ilk satırı)
                row = rows[0]  # ilk satır
                self.ui.lineEdit_tel.setText(str(row[2]))  # row[0] -> tel veya istediğiniz sütun
                self.ui.lineEdit_marka.setText(str(row[3]))  # row[1] -> marka veya istediğiniz sütun
                self.ui.lineEdit_model.setText(str(row[4]))  # row[2] -> model vs.
                self.ui.lineEdit_serino.setText(str(row[5]))
                self.ui.lineEdit_akses.setText(str(row[6]))
                self.ui.lineEdit_garanti.setText(str(row[7]))
                self.ui.textEdit.setText(str(row[8]))
                self.ui.lineEdit_grnt.setText(str(row[9]))
                self.ui.lineEdit_alan.setText(str(row[10]))
                self.ui.lineEdit_zelkod.setText(str(row[11]))
                self.ui.lineEdit_gtarih.setText(str(row[12]))
            # Diğer alanları da benzer şekilde yazdırabilirsiniz:
            # self.ui.lineEdit_serino.setText(str(row[3]))  # row[3] -> serino vb.

          except Exception as e:
            print("Sorgu hatası:", e)
            QMessageBox.warning(self, "Sorgu Hatası", f"Sorgu sırasında bir hata oluştu: {e}")     
        
        def print_preview(self):
                try:
                        printer = QPrinter(QPrinter.HighResolution)
                        printer.setOutputFormat(QPrinter.PdfFormat)
                        printer.setOutputFileName("Teslim.pdf")  # PDF dosyasının yolu

                        # Ön izleme penceresini oluştur ve paintRequested sinyaline bağla
                        preview_dialog = QPrintPreviewDialog(printer, self)
                        preview_dialog.paintRequested.connect(self.on_paint_preview)  # paintRequested sinyali ile çizim fonksiyonunu bağla
                        preview_dialog.exec_()  # Ön izleme penceresini aç
                except Exception as e:
                        print(f"Yazdırma Hatası: {e}")
                        QMessageBox.warning(self, "Hata", f"Yazdırma işlemi sırasında bir hata oluştu: {e}")

        def on_paint_preview(self, printer):
                try:
                        painter = QPainter(printer)

                        # QPainter'ı başlatmadan önce kontrol edin
                        if not painter.isActive():
                         print("Painter başlatılamadı.")
                         return  # Eğer painter aktif değilse, işlemden çık

                        painter.begin(printer)  # Yazdırma işlemi başlatılır
                        painter.setFont(QFont("Arial", 15))  # Font ve boyut ayarı

                        # Formdan verileri al
                        adi = self.ui.lineEdit_adi.text()  # QLineEdit'lerden metin al
                        numara = self.ui.lineEdit_tel.text()
                        marka = self.ui.lineEdit_marka.text()
                        model = self.ui.lineEdit_model.text()
                        serino = self.ui.lineEdit_serino.text()
                        aksesuar = self.ui.lineEdit_akses.text()
                        garanti = self.ui.lineEdit_garanti.text()
                        ariza = self.ui.textEdit.toPlainText()  # QTextEdit'ten metin al
                        durum = self.ui.lineEdit_grnt.text()  # Doğru şekilde text() kullanın
                        teslim = self.ui.lineEdit_alan.text()
                        özel = self.ui.lineEdit_zelkod.text()
                        tarih = self.ui.lineEdit_gtarih.text()
                        işlem=self.ui.textEdit_islem.toPlainText()
                        yapan=self.ui.lineEdit_yapan.text()
                        teden=self.ui.lineEdit_eden.text()
                        ekbilgi=self.ui.textEdit_islem_2.toPlainText()
                        teslimtar=self.ui.dateEdit.text()
                        # Yazdırma konumu
                        y_offset = 200  # Başlangıç y-offset'ini belirle
                        y_step = 390  # Her metin satırı arasında boşluk (y-ekseni adımı)

                        # Metni yazdırma
                        painter.drawText(100, y_offset, f"ASYA BİLİŞİM TESLİM FİŞİ")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Geliş Tarihi : {tarih}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Müşteri Adı: {adi}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Gsm No: {numara}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Marka: {marka}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Model: {model}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Seri No: {serino}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Aksesuar: {aksesuar}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Garanti Durumu: {garanti}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Arıza Bilgisi: {ariza}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Geldiğinde ki Durum: {durum}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Teslim Alan: {teslim}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Özel Kod: {özel}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        
                        painter.drawText(100, y_offset, f"Yapılan işlemler : {işlem}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Tamiratı Yapan Personel : {yapan}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Teslimi Gerçekleştiren Personel : {teden}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"EK-Bilgi: {ekbilgi}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        painter.drawText(100, y_offset, f"Teslim Tarihi: {teslimtar}")
                        y_offset += y_step  # Bir satır aşağı kaydır
                        
                        
                
                        painter.end()  # Çizimi sonlandır

                except Exception as e:
                        print(f"Yazdırma sırasında hata: {e}")
                        QMessageBox.warning(self, "Yazdırma Hatası", f"Yazdırma işlemi sırasında bir hata oluştu: {e}")
        
        
        def data(self):
            try:
                con1=sqlite3.connect("teslimveri.db")
                self.cursor1=con1.cursor()
                return con1
            except Exception as e:
                    QMessageBox.critical(None, "Veritabanı Bağlantısı", "Veritabanı bağlantısı başarısız.")
                    return None
        
        
        
        
        def kaydet(self):
    # Veritabanı bağlantısını alıyoruz
                con1 = self.data()
        
                if con1 is None:
                        return  # Eğer veritabanı bağlantısı yoksa, kaydetme işlemine devam etmiyoruz.

                adi = self.ui.lineEdit_adi.text()
                tel = self.ui.lineEdit_tel.text()
                marka = self.ui.lineEdit_model.text()
                model=self.ui.lineEdit_model.text()
                serino = self.ui.lineEdit_serino.text()
                özelkod = self.ui.lineEdit_zelkod.text()

                teslimalan = self.ui.lineEdit_alan.text()
                teslimeden = self.ui.lineEdit_eden.text()
                tamireden = self.ui.lineEdit_yapan.text()
                arizabilgi = self.ui.textEdit.toPlainText()
                yapılanişlem = self.ui.textEdit_islem.toPlainText()
                geltar = self.ui.lineEdit_gtarih.text()
                teslimtar = self.ui.dateEdit.text()
                bilgi = self.ui.textEdit_islem_2.toPlainText()

                try:
                # SQL sorgusunu doğru parametrelerle oluşturuyoruz
                   self.cursor1.execute("""
                        INSERT INTO teslim(ADİ, TELEFON, MARKA, MODEL, SERİNO, ÖZELKOD, TESLİMALAN, 
                                        TESLİMEDEN, TAMİREDEN, ARIZABİLGİSİ, YAPILANİŞLEM, GELİŞ, 
                                        TESLİMTARİHİ, EKBİLGİ) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (
                        adi, tel, marka,model, serino, özelkod, teslimalan, teslimeden, tamireden, 
                        arizabilgi, yapılanişlem, geltar, teslimtar, bilgi
                        ))

                # Veritabanı işlemini kaydediyoruz
                   con1.commit()
                   self.ui.label_19.setText("Kayıt Başarılı")
                   
                except sqlite3.Error as e:
                        # SQL hatalarını daha detaylı gösteriyoruz
                 error_message = f"Veritabanı Hatası: {e}"
                 print(error_message)  # Terminalde hata mesajını yazdırıyoruz
                 self.ui.label_19.setText("Kayıt Başarısız: " + error_message)  # Hata mesajını GUI'de gösteriyoruz
                
                finally:
                        # Veritabanı bağlantısını doğru şekilde kapatıyoruz
                 con1.close()
                
        def verisayfa(self):
                self.veri=veri()
                
                self.veri.show()
                      
                
if __name__=="__main__":
        app=QtWidgets.QApplication(sys.argv)

        dd=teslim()
        dd.show()
        sys.exit(app.exec_())