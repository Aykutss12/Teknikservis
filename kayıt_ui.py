
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog,  QPrintPreviewDialog
from PyQt5.QtGui import QPainter,QFont

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 339)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Msi Pro Series\\Desktop\\PROJELER\\AsyaBil\\ikon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 731, 331))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(50, 220, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(60, 120, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(370, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(370, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(380, 210, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 211, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 60, 211, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 90, 211, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 120, 211, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 150, 211, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 180, 211, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(460, 160, 211, 20))
        self.lineEdit_7.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(460, 210, 211, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(120, 220, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(460, 30, 211, 71))
        self.textEdit.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(400, 250, 111, 71))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Msi Pro Series\\Desktop\\PROJELER\\AsyaBil\\ikon/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 250, 111, 71))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Msi Pro Series\\Desktop\\PROJELER\\AsyaBil\\ikon/paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(350, 120, 101, 20))
        self.label_11.setObjectName("label_11")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(460, 110, 211, 41))
        self.textEdit_2.setStyleSheet("background-color: rgb(232, 240, 155);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(50, 270, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(120, 270, 141, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2025, 12, 28), QtCore.QTime(23, 9, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.actionkaydet = QtWidgets.QAction(Form)
        self.actionkaydet.setObjectName("actionkaydet")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Müşteri Kayıt"))
        self.groupBox.setTitle(_translate("Form", "GELEN MÜŞTERİ KAYIT ALANI"))
        self.label.setText(_translate("Form", "Müşteri Adı :"))
        self.label_2.setText(_translate("Form", "Gsm No :"))
        self.label_3.setText(_translate("Form", "Marka :"))
        self.label_4.setText(_translate("Form", "Seri - No :"))
        self.label_5.setText(_translate("Form", "Aksesuar :"))
        self.label_6.setText(_translate("Form", "Garanti :"))
        self.label_7.setText(_translate("Form", "Model : "))
        self.label_8.setText(_translate("Form", "Arıza Bilgisi :"))
        self.label_9.setText(_translate("Form", "Teslim Alan :"))
        self.label_10.setText(_translate("Form", "Özel Kod :"))
        self.comboBox.setItemText(0, _translate("Form", "-"))
        self.comboBox.setItemText(1, _translate("Form", "VAR"))
        self.comboBox.setItemText(2, _translate("Form", "YOK"))
        self.comboBox.setItemText(3, _translate("Form", "SERVİS GARANTİLİ"))
        self.pushButton.setText(_translate("Form", "Kaydet"))
        self.pushButton_2.setText(_translate("Form", "Yazdır"))
        self.label_11.setText(_translate("Form", "Genel Durumu :"))
        self.label_12.setText(_translate("Form", "Tarih :"))
        self.actionkaydet.setText(_translate("Form", "kaydet"))
        self.actionkaydet.setShortcut(_translate("Form", "Return"))
import icon_rc
class kayit_arayüz(QtWidgets.QMainWindow):
        def __init__(self):
             super(kayit_arayüz,self).__init__()
             self.ui=Ui_Form()
             self.ui.setupUi(self)
             self.data(form=any)
             self.ui.pushButton.clicked.connect(self.kaydet)
             self.ui.pushButton_2.clicked.connect(self.print_preview)
             
        def data(self,form):
            self.data=sqlite3.connect("data.db")
            self.cursor=self.data.cursor()
        
        
        
        
        def kaydet(self,form):
            adi=self.ui.lineEdit.text()
            numara=self.ui.lineEdit_2.text()
            marka=self.ui.lineEdit_3.text()
            model=self.ui.lineEdit_4.text()
            serino=self.ui.lineEdit_5.text()
            aksesuar=self.ui.lineEdit_6.text()
            garanti=self.ui.comboBox.currentText()
            ariza=self.ui.textEdit.toPlainText()
            durum=self.ui.textEdit_2.toPlainText()
            teslim=self.ui.lineEdit_7.text()
            özel=self.ui.lineEdit_8.text()
            tarih=self.ui.dateEdit.text()
            try:
                self.cursor.execute("INSERT INTO müs(adi,tel,marka,model,seri_no,aksesuar,garanti,ariza,genedurum,teslim_alan,özel_kod,tarih) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                                   (adi,
                                   numara,
                                   marka,
                                   model,
                                   serino,
                                   aksesuar,
                                   garanti,
                                   ariza,
                                   durum,
                                   teslim
                                   ,özel
                                   ,tarih
                ))            
                self.data.commit()
                self.ui.groupBox.setTitle("Kayıt Başarılı")
                
            except Exception as e:
                self.ui.groupBox.setTitle(f"kayıt başarısız{e}")
            finally:
                self.data.close()
        
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

            # Formdan verileri al
            adi = self.ui.lineEdit.text()
            numara = self.ui.lineEdit_2.text()
            marka = self.ui.lineEdit_3.text()
            model = self.ui.lineEdit_4.text()
            serino = self.ui.lineEdit_5.text()
            aksesuar = self.ui.lineEdit_6.text()
            garanti = self.ui.comboBox.currentText()
            ariza = self.ui.textEdit.toPlainText()
            durum = self.ui.textEdit_2.toPlainText()
            teslim = self.ui.lineEdit_7.text()
            özel = self.ui.lineEdit_8.text()
            tarih=self.ui.dateEdit.text()
            # Yazdırma konumu
            y_offset = 200  # Başlangıç y-offset'ini belirle
            y_step = 390  # Her metin satırı arasında boşluk (y-ekseni adımı)

            # Metni yazdırma
            painter.drawText(100, y_offset, f"ASYA BİLİŞİM KABUL FİŞİ")
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

            painter.end()  # Çizimi sonlandır
            self.temızle()

        def temızle(self):
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear() 
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_6.clear()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_8.clear()
            self.ui.textEdit.clear()
            self.ui.textEdit_2.clear()
            
            
            
            
            
            
                 
if __name__=="__main__":
        app=QtWidgets.QApplication(sys.argv)
        main=kayit_arayüz()
        main.show()
        sys.exit(app.exec_())