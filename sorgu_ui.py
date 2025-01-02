import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog,  QPrintPreviewDialog
from PyQt5.QtGui import QPainter,QFont
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog,  QPrintPreviewDialog
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel,QSqlQuery
from PyQt5.QtGui import QStandardItemModel, QStandardItem


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(693, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(0, 390, 691, 211))
        self.tableView.setObjectName("tableView")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 80, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 30, 101, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("color: rgb(170, 0, 0);\n"
"color: rgb(0, 85, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/searching.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 321, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 120, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 220, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 250, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(270, 120, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(460, 120, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(30, 280, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(30, 310, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(30, 340, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(270, 160, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(270, 220, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 160, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 190, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 220, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 250, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 280, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 310, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(90, 340, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(360, 220, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(140, 120, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(330, 120, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(530, 120, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(360, 160, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 30, 101, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setStyleSheet("color: rgb(170, 0, 0);\n"
"color: rgb(0, 85, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/dust.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 320, 111, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setStyleSheet("color: rgb(170, 0, 0);\n"
"color: rgb(0, 85, 0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/delivery - Kopya.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 320, 111, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_4.setStyleSheet("color: rgb(170, 0, 0);\n"
"color: rgb(0, 85, 0);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(280, 260, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(360, 260, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 240, 155);")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 320, 111, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_5.setStyleSheet("color: rgb(170, 0, 0);\n"
"color: rgb(0, 85, 0);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sorgulama"))
        self.pushButton.setText(_translate("Form", "Sorgula"))
        self.label_3.setText(_translate("Form", "Özel Kod :"))
        self.label_2.setText(_translate("Form", "Müşteri Adı :"))
        self.label.setText(_translate("Form", "Sorgulama Alanı "))
        self.label_4.setText(_translate("Form", "ADI-SOYADI :"))
        self.label_5.setText(_translate("Form", "İLETİŞİM :"))
        self.label_6.setText(_translate("Form", "TARİHİ :"))
        self.label_7.setText(_translate("Form", "MARKA :"))
        self.label_8.setText(_translate("Form", "MODEL :"))
        self.label_9.setText(_translate("Form", "SIRA NO :"))
        self.label_10.setText(_translate("Form", "ÖZEL KOD :"))
        self.label_11.setText(_translate("Form", "SERİ NO : "))
        self.label_12.setText(_translate("Form", "GARANTİ :"))
        self.label_13.setText(_translate("Form", "DURUMU :"))
        self.label_14.setText(_translate("Form", "ARIZA BİLGİSİ :"))
        self.label_15.setText(_translate("Form", "TESLİM ALAN :"))
        self.pushButton_2.setText(_translate("Form", "Temizle"))
        self.pushButton_3.setText(_translate("Form", "Güncelle"))
        self.pushButton_4.setText(_translate("Form", "Yazdır"))
        self.label_16.setText(_translate("Form", "AKSESUAR : "))
        self.pushButton_5.setText(_translate("Form", "Sil"))
import icon_rc
class sorgu_arayüz(QtWidgets.QMainWindow):
    def __init__(self):
             super(sorgu_arayüz,self).__init__()
             self.ui=Ui_Form()
             self.ui.setupUi(self)
             self.ui.pushButton.clicked.connect(self.sorgula)
             self.ui.pushButton_2.clicked.connect(self.temizle)
             self.ui.pushButton_3.clicked.connect(self.update)
             self.ui.pushButton_4.clicked.connect(self.print_preview)
             self.ui.pushButton_5.clicked.connect(self.sil)                                                                                                                                                                                                                                                        
    def __init__(self):
        super(sorgu_arayüz, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sorgula)
            # Veritabanı bağlantısını başlatıyoruz
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.db")  # Veritabanı dosyasının yolu
        self.ui.tableView.doubleClicked.connect(self.on_cell_double_clicked)
        self.ui.pushButton_2.clicked.connect(self.temizle)
        self.ui.pushButton_3.clicked.connect(self.update)
        self.ui.pushButton_4.clicked.connect(self.print_preview)
        self.ui.pushButton_5.clicked.connect(self.sil)
        
        
        
    def data(self):
        try:
                con = sqlite3.connect("data.db")  # Veritabanı dosyasının yolunu doğru verdiğinizden emin olun
                return con
        except Exception as e:
                print(f"Veritabanı bağlantı hatası: {e}")
                return None

                
    def temizle(self):
        QMessageBox.information(self, "Başarılı", "temizlendi")
        # Tüm QLineEdit'leri temizle
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()
        self.ui.lineEdit_10.clear()
        self.ui.lineEdit_11.clear()
        self.ui.lineEdit_12.clear()
        self.ui.lineEdit_13.clear()
        self.ui.lineEdit_14.clear()
        # QTextEdit temizle
        self.ui.textEdit.clear()

        # TableView'i temizle
        self.ui.tableView.setModel(None)
        
        
    def print_preview(self):
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName("output.pdf")  # PDF dosyasının yolu

    # Ön izleme penceresini oluştur ve paintRequested sinyaline bağla
            preview_dialog = QPrintPreviewDialog(printer, self)
            preview_dialog.paintRequested.connect(self.on_paint_preview)  # paintRequested sinyali ile çizim fonksiyonunu bağla
            preview_dialog.exec_()  # Ön izleme penceresini aç       
    
    def on_paint_preview(self, printer):
            painter = QPainter(printer)
    
    # QPainter'ı başlatmadan önce kontrol edin
            if not painter.isActive():
                print("Painter başlatılamadı.")
                return  # Eğer painter aktif değilse, işlemden çık
    
            painter.begin(printer)  # Yazdırma işlemi başlatılır
            painter.setFont(QFont("Arial", 15))  # Font ve boyut ayarı
            adi = self.ui.lineEdit_3.text()
            numara = self.ui.lineEdit_4.text()
            marka = self.ui.lineEdit_5.text()
            model = self.ui.lineEdit_6.text()
            serino = self.ui.lineEdit_7.text()
            aksesuar = self.ui.lineEdit_14.text()
            garanti = self.ui.lineEdit_8.text()
            ariza = self.ui.textEdit.toPlainText()
            durum = self.ui.lineEdit_9.text()
            teslim = self.ui.lineEdit_7.text()
            özel = self.ui.lineEdit_8.text()
            tarih = self.ui.lineEdit_11.text()
            sirano=self.ui.lineEdit_12.text()
            
            y_offset = 200  # Başlangıç y-offset'ini belirle
            y_step = 390  # Her metin satırı arasında boşluk (y-ekseni adımı)

            # Metni yazdırma
            painter.drawText(100, y_offset, f"ASYA BİLİŞİM KABUL  DEĞİŞİM FİŞİ ")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Tarih : {tarih}")
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
            painter.drawText(100, y_offset, f"Durum: {durum}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Teslim Alan: {teslim}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Özel Kod: {özel}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Sira No : {sirano}")
        
            painter.end()  # Çizimi sonlandır

            
               
                
    
    
    
    def sorgula(self):
    # Veritabanı bağlantısını kuruyoruz
                db = QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName("data.db")  # Veritabanı dosyasının yolu

                if not db.open():
                        QMessageBox.critical(None, "Veritabanı Bağlantısı", "Veritabanı bağlantısı başarısız.")
                        return

    # Kullanıcının girdiği verileri alıyoruz
                adi_text = self.ui.lineEdit.text()
                kod_text = self.ui.lineEdit_2.text()

                # Eğer her iki lineEdit de boşsa, hiçbir şey yapmadan çıkıyoruz
                if not adi_text and not kod_text:
                        QMessageBox.warning(None, "Uyarı", "Lütfen arama yapmak için bir değer girin.")
                        db.close()
                        return

    # Dinamik sorgu oluşturma
                query = "SELECT * FROM müs WHERE 1=1"  # 1=1 her zaman doğru olduğu için başlangıçta bir temel koşul ekliyoruz.

                # Sadece kullanıcı tarafından girilen alanları sorguya dahil ediyoruz
                if adi_text:
                        query += " AND adi LIKE :adi COLLATE NOCASE"  # `adi` için büyük/küçük harf duyarsız filtre ekliyoruz
                if kod_text:
                        query += " AND özel_kod LIKE :kod COLLATE NOCASE"  # `özel_kod` için büyük/küçük harf duyarsız filtre ekliyoruz
 # `özel_kod` için filtre ekliyoruz

                # QSqlQuery nesnesi oluşturuluyor
                q = QSqlQuery()
                q.prepare(query)

                # Parametreleri sorguya bağlama
                if adi_text:
                        q.bindValue(":adi", f"%{adi_text}%")
                if kod_text:
                        q.bindValue(":kod", f"%{kod_text}%")

    # Sorguyu çalıştırma
                if not q.exec_():
                        QMessageBox.critical(None, "Sorgu Hatası", q.lastError().text())
                        db.close()
                        return

                # Sonuçları bir QSqlQueryModel'e yerleştirme
                model = QSqlQueryModel()
                model.setQuery(q)

                # Hata kontrolü
                if model.lastError().isValid():
                        QMessageBox.critical(None, "Model Hatası", model.lastError().text())
                else:
                        # Veritabanı sorgu sonucu başarıyla alındığında, tabloya modeli ekliyoruz
                        self.ui.tableView.setModel(model)
                        db.close()
    def on_cell_double_clicked(self, index):
        model = self.ui.tableView.model()

        if not model or not index.isValid():
            QMessageBox.warning(self, "Hata", "Geçersiz model veya seçim.")
            return

        # Çift tıklanan hücredeki veri alınır
        row = index.row()

        try:
            # Verileri alınan satırdan LineEdit'lere aktar
            self.ui.lineEdit_12.setText(str(model.data(model.index(row, 0))))  # 1. sütun - Ad
            self.ui.lineEdit_3.setText(str(model.data(model.index(row, 1))))  # 2. sütun - Kod
            self.ui.lineEdit_4.setText(str(model.data(model.index(row, 2))))  # 3. sütun - Tarih
            self.ui.lineEdit_5.setText(str(model.data(model.index(row, 3))))  # 4. sütun - Seri No
            self.ui.lineEdit_6.setText(str(model.data(model.index(row, 4))))  # 5. sütun - Marka
            self.ui.lineEdit_6.setText(str(model.data(model.index(row, 5))))  # 6. sütun - Model
            self.ui.lineEdit_7.setText(str(model.data(model.index(row, 6))))  # 7. sütun - Sıra No
            self.ui.lineEdit_8.setText(str(model.data(model.index(row, 7))))  # 8. sütun - Durum
            self.ui.textEdit.setText(str(model.data(model.index(row, 8))))  # 9. sütun - Açıklama
            self.ui.lineEdit_9.setText(str(model.data(model.index(row, 9))))  # 10. sütun - Arıza
            self.ui.lineEdit_10.setText(str(model.data(model.index(row, 10))))  # 11. sütun - Teslim Alan
            self.ui.lineEdit_13.setText(str(model.data(model.index(row, 11))))  # 12. sütun - Seri No
            self.ui.lineEdit_11.setText(str(model.data(model.index(row, 12))))  # 13. sütun - Garanti
            self.ui.lineEdit_14.setText(str(model.data(model.index(row, 6))))  # 14. stun Aksesuar
        except Exception as e:
            QMessageBox.warning(self, "Hata", f"Bir hata oluştu: {str(e)}")
    
    
    def sil(self):
        try:
                con = sqlite3.connect('data.db')
                cursor = con.cursor()

                serino = self.ui.lineEdit_12.text()  # Değeri almak için text() kullanmalısınız

                cursor.execute('DELETE FROM müs WHERE sirano= ?', (serino,))  # SQL sorgusu doğru yazılmalı
                con.commit()  # Değişiklikleri kaydet
                QMessageBox.warning(self,"Başarılı","Kayıtlı kişi Silindi")
                self.temizle()
                                    
        except Exception as e:
                QMessageBox.warning(self,"hata",f"bir hata oluştu{str(e)}")
                
        
        finally:
                con.close()  # Bağlantıyı kapatmak iyi bir alışkanlıktır
    
    def update(self):
        # QLineEdit'lerden verileri al
        adi = self.ui.lineEdit_3.text()
        numara = self.ui.lineEdit_4.text()
        marka = self.ui.lineEdit_5.text()
        model = self.ui.lineEdit_6.text()
        serino = self.ui.lineEdit_7.text()
        aksesuar = self.ui.lineEdit_14.text()
        garanti = self.ui.lineEdit_8.text()
        ariza = self.ui.textEdit.toPlainText()
        durum = self.ui.lineEdit_9.text()
        teslim = self.ui.lineEdit_7.text()
        özel = self.ui.lineEdit_13.text()
        tarih = self.ui.lineEdit_11.text()
        sirano=self.ui.lineEdit_12.text()
        # Veritabanı bağlantısını al
        con = self.data()  # Bu fonksiyonun bağlantıyı sağladığını varsayıyorum
        cursor = con.cursor()

        # Güncellenmesi gereken kaydın hangi koşulda olduğunu belirtmek için WHERE kullanmalısınız
        # Örneğin, güncelleme yaparken özel_kod'a göre güncelleme yapalım (veya id'ye göre)
        update_query = ("UPDATE müs SET adi = ? ,tel=?, marka=?, model=?, seri_no=?, aksesuar=?, garanti=?, ariza=?, genedurum=?, teslim_alan=?, özel_kod=?, tarih=? WHERE sirano =?")

        # Parametreleri sırayla yerleştir
        params = (adi,numara, marka, model, serino, aksesuar, garanti, ariza, durum, teslim, özel, tarih,sirano)

        try:
                # Sorguyu çalıştır
                cursor.execute(update_query, params)
                con.commit()  # Değişiklikleri kaydet

                QMessageBox.information(self, "Kayıt Güncellendi", "Değişim Fişi için Çıktı Alabilirsiniz..")
        except Exception as e:
                con.rollback()  # Hata durumunda rollback işlemi
                QMessageBox.warning(self, "Hata", f"Güncelleme işlemi sırasında bir hata oluştu: {e}")

        # Veritabanı bağlantısını kapat
        cursor.close()
        con.close()
        self.temizle()
    
   
                
if __name__=="__main__":
        app=QtWidgets.QApplication(sys.argv)
        main=sorgu_arayüz()
        main.show()
        sys.exit(app.exec_())