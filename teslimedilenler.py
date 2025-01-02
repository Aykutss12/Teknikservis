

import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel,QSqlQuery
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog,  QPrintPreviewDialog
from PyQt5.QtGui import QPainter,QFont


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1009, 721)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(0, 440, 1001, 281))
        self.tableView.setObjectName("tableView")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 20, 141, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(216, 216, 162);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 141, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(216, 216, 162);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(6, 60, 71, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 92, 75, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/searching.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 0, 671, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/ikon/cooltext472695298741495.png"))
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 90, 751, 301))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.adi = QtWidgets.QLabel(self.groupBox_2)
        self.adi.setGeometry(QtCore.QRect(50, 20, 131, 31))
        self.adi.setStyleSheet("color: rgb(0, 0, 0);")
        self.adi.setObjectName("adi")
        self.tel = QtWidgets.QLabel(self.groupBox_2)
        self.tel.setGeometry(QtCore.QRect(50, 60, 161, 31))
        self.tel.setStyleSheet("color: rgb(0, 0, 0);")
        self.tel.setObjectName("tel")
        self.marka = QtWidgets.QLabel(self.groupBox_2)
        self.marka.setGeometry(QtCore.QRect(50, 100, 161, 31))
        self.marka.setStyleSheet("color: rgb(0, 0, 0);")
        self.marka.setObjectName("marka")
        self.model = QtWidgets.QLabel(self.groupBox_2)
        self.model.setGeometry(QtCore.QRect(60, 140, 161, 31))
        self.model.setStyleSheet("color: rgb(0, 0, 0);")
        self.model.setObjectName("model")
        self.serino = QtWidgets.QLabel(self.groupBox_2)
        self.serino.setGeometry(QtCore.QRect(60, 180, 161, 31))
        self.serino.setStyleSheet("color: rgb(0, 0, 0);")
        self.serino.setObjectName("serino")
        self.tameden = QtWidgets.QLabel(self.groupBox_2)
        self.tameden.setGeometry(QtCore.QRect(290, 110, 161, 31))
        self.tameden.setStyleSheet("color: rgb(0, 0, 0);")
        self.tameden.setObjectName("tameden")
        self.talan = QtWidgets.QLabel(self.groupBox_2)
        self.talan.setGeometry(QtCore.QRect(290, 20, 161, 31))
        self.talan.setStyleSheet("color: rgb(0, 0, 0);")
        self.talan.setObjectName("talan")
        self.arizabilgi = QtWidgets.QLabel(self.groupBox_2)
        self.arizabilgi.setGeometry(QtCore.QRect(290, 160, 161, 41))
        self.arizabilgi.setStyleSheet("color: rgb(0, 0, 0);")
        self.arizabilgi.setObjectName("arizabilgi")
        self.zelkod = QtWidgets.QLabel(self.groupBox_2)
        self.zelkod.setGeometry(QtCore.QRect(80, 230, 141, 31))
        self.zelkod.setStyleSheet("color: rgb(0, 0, 0);")
        self.zelkod.setObjectName("zelkod")
        self.teeden = QtWidgets.QLabel(self.groupBox_2)
        self.teeden.setGeometry(QtCore.QRect(290, 60, 161, 31))
        self.teeden.setStyleSheet("color: rgb(0, 0, 0);")
        self.teeden.setObjectName("teeden")
        self.ekbilgi = QtWidgets.QLabel(self.groupBox_2)
        self.ekbilgi.setGeometry(QtCore.QRect(570, 170, 161, 51))
        self.ekbilgi.setStyleSheet("color: rgb(0, 0, 0);")
        self.ekbilgi.setObjectName("ekbilgi")
        self.geltarih = QtWidgets.QLabel(self.groupBox_2)
        self.geltarih.setGeometry(QtCore.QRect(590, 10, 161, 31))
        self.geltarih.setStyleSheet("color: rgb(0, 0, 0);")
        self.geltarih.setObjectName("geltarih")
        self.yapilem = QtWidgets.QLabel(self.groupBox_2)
        self.yapilem.setGeometry(QtCore.QRect(290, 220, 211, 61))
        self.yapilem.setStyleSheet("color: rgb(0, 0, 0);")
        self.yapilem.setObjectName("yapilem")
        self.teslimtarih = QtWidgets.QLabel(self.groupBox_2)
        self.teslimtarih.setGeometry(QtCore.QRect(590, 60, 161, 31))
        self.teslimtarih.setStyleSheet("color: rgb(0, 0, 0);")
        self.teslimtarih.setObjectName("teslimtarih")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(-10, 30, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(6, 70, 31, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(0, 110, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(6, 150, 41, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(0, 190, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(0, 240, 61, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(230, 30, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(230, 70, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(230, 110, 47, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(230, 160, 47, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(216, 220, 61, 51))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(530, 10, 47, 41))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(530, 60, 47, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(510, 180, 47, 31))
        self.label_18.setObjectName("label_18")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 160, 91, 71))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/paper.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 250, 91, 71))
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(520, 400, 111, 23))
        self.lcdNumber.setStyleSheet("background-color: rgb(34, 34, 34);\n"
"color: rgb(227, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Veri dataları"))
        self.groupBox.setTitle(_translate("Form", "SORGU ALANI"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">İSİM :</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600;\">ÖZEL KOD :</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Sorgula"))
        self.adi.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.tel.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.marka.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.model.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.serino.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.tameden.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.talan.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.arizabilgi.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.zelkod.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.teeden.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.ekbilgi.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.geltarih.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.yapilem.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.teslimtarih.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">ADI :</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">TEL :</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">MARKA :</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">MODEL :</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">SERİNO:</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">ÖZEL KOD:</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">T.ALAN :</span></p></body></html>"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">T.EDEN :</span></p><p align=\"right\"><br/></p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">TAMİR <br/>EDEN</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">ARIZA<br/>BİLGİ :</span></p></body></html>"))
        self.label_15.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">YAPILAN</span></p><p align=\"right\"><span style=\" font-weight:600;\">İŞLEM</span></p></body></html>"))
        self.label_16.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">GELİŞ<br/>TARİH</span></p></body></html>"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">TESLİM<br/>TARİHİ</span></p></body></html>"))
        self.label_18.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">EK<br/>BİLGİ</span></p></body></html>"))
import icon_rc



class SqlTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, headers=None):
        super(SqlTableModel, self).__init__()
        self.data_list = data
        self.headers = headers if headers else []

    def rowCount(self, parent=None):
        return len(self.data_list)

    def columnCount(self, parent=None):
        if self.data_list:
            return len(self.data_list[0])
        return 0

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self.data_list[row][col])

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal and self.headers:
                return self.headers[section]
        return None


class veri(QtWidgets.QMainWindow):
        def __init__(self):
                super(veri, self).__init__()
                self.ui = Ui_Form()
                self.ui.setupUi(self)
                self.dataload()
                self.ui.tableView.doubleClicked.connect(self.on_cell_double_clicked)
                self.ui.pushButton_3.clicked.connect(self.sil)
                self.ui.pushButton.clicked.connect(self.ara)
                self.ui.pushButton_2.clicked.connect(self.print_preview)
                
        def dataload(self):
                try:
                     con=sqlite3.connect("teslimveri.db")
                     cursor=con.cursor()
                     cursor.execute("SELECT COUNT(*) FROM teslim")
                     
                     row_count = cursor.fetchone()[0]
                     self.ui.lcdNumber.display(row_count)
                     
                     cursor.execute("SELECT * FROM teslim")
                     rows=cursor.fetchall()
                     
                     
                     con.close()
                     headers = ["Ad", "Telefon", "Marka", "Model", "Seri No", "Özel Kod", "Teslim Alan", "Teslim Eden", "Tamir Eden", "Arıza Bilgisi", "Yapılan İşlem", "Geliş Tarihi", "Teslim Tarihi", "Ek Bilgi"]
                     model = SqlTableModel(rows,headers)
                     self.ui.tableView.setModel(model)
                except Exception as e:
                        print(f"Veritabanı Bağlantısı{e}")
                        QtWidgets.QMessageBox.warning(self,"Data hatası",f"veri tabanına bağlanmadı")
        
        
        def on_cell_double_clicked(self, index):
            model = self.ui.tableView.model()

            if not model or not index.isValid():
                QMessageBox.warning(self, "Hata", "Geçersiz model veya seçim.")
                return

        # Çift tıklanan hücredeki veri alınır
            row = index.row()

            try:
                # Verileri alınan satırdan LineEdit'lere aktar
                self.ui.adi.setText(str(model.data(model.index(row, 0))))  # 1. sütun - Ad
                self.ui.tel.setText(str(model.data(model.index(row, 1))))  # 2. sütun - Kod
                self.ui.marka.setText(str(model.data(model.index(row, 2))))  # 3. sütun - Tarih
                self.ui.model.setText(str(model.data(model.index(row, 3))))  # 4. sütun - Seri No
                self.ui.serino.setText(str(model.data(model.index(row, 4))))  # 5. sütun - Marka
                self.ui.zelkod.setText(str(model.data(model.index(row, 5))))  # 6. sütun - Model
                self.ui.talan.setText(str(model.data(model.index(row, 6))))  # 7. sütun - Sıra No
                self.ui.teeden.setText(str(model.data(model.index(row, 7))))  # 8. sütun - Durum
                self.ui.tameden.setText(str(model.data(model.index(row, 8))))  # 9. sütun - Açıklama
                self.ui.arizabilgi.setText(str(model.data(model.index(row, 9))))  # 10. sütun - Arıza
                self.ui.yapilem.setText(str(model.data(model.index(row, 10))))  # 11. sütun - Teslim Alan
                self.ui.geltarih.setText(str(model.data(model.index(row, 11))))  # 12. sütun - Seri No
                self.ui.teslimtarih.setText(str(model.data(model.index(row, 12))))  # 13. sütun - Garanti
                self.ui.ekbilgi.setText(str(model.data(model.index(row, 13))))  # 14. stun Aksesuar
            except Exception as e:
                QMessageBox.warning(self, "Hata", f"Bir hata oluştu: {str(e)}")                          
                
        def sil(self):
            try:
                    con = sqlite3.connect('teslimveri.db')
                    cursor = con.cursor()

                    adi = self.ui.adi.text()  # Değeri almak için text() kullanmalısınız

                    cursor.execute('DELETE FROM teslim WHERE ADİ= ?', (adi,))  # SQL sorgusu doğru yazılmalı
                    con.commit()  # Değişiklikleri kaydet
                    QMessageBox.warning(self,"Başarılı","Kayıtlı kişi Silindi")
                   
                                        
            except Exception as e:
                    QMessageBox.warning(self,"hata",f"bir hata oluştu{str(e)}")
                    
            
            finally:
                    con.close()  # Bağlantıyı kapatmak iyi bir alışkanlıktır       
        
        def ara(self):
    # Veritabanı bağlantısını kuruyoruz
                db = QSqlDatabase.addDatabase("QSQLITE")
                db.setDatabaseName("teslimveri.db")  # Veritabanı dosyasının yolu

                if not db.open():
                        QMessageBox.critical(None, "Veritabanı Bağlantısı", "Veritabanı bağlantısı başarısız.")
                        return

    # Kullanıcının girdiği verileri alıyoruz
                adi_text = self.ui.lineEdit_2.text()
                kod_text = self.ui.lineEdit.text()

                # Eğer her iki lineEdit de boşsa, hiçbir şey yapmadan çıkıyoruz
                if not adi_text and not kod_text:
                        QMessageBox.warning(None, "Uyarı", "Lütfen arama yapmak için bir değer girin.")
                        db.close()
                        return

    # Dinamik sorgu oluşturma
                query = "SELECT * FROM teslim WHERE 1=1"  # 1=1 her zaman doğru olduğu için başlangıçta bir temel koşul ekliyoruz.

                # Sadece kullanıcı tarafından girilen alanları sorguya dahil ediyoruz
                if adi_text:
                        query += " AND ADİ LIKE :adi COLLATE NOCASE"  # `adi` için büyük/küçük harf duyarsız filtre ekliyoruz
                if kod_text:
                        query += " AND ÖZELKOD LIKE :özelkod COLLATE NOCASE"  # `özel_kod` için büyük/küçük harf duyarsız filtre ekliyoruz
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
        
        
        def print_preview(self):
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName("veri.pdf")  # PDF dosyasının yolu

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
            adi = self.ui.adi.text()
            numara = self.ui.tel.text()
            marka = self.ui.marka.text()
            model = self.ui.model.text()
            serino = self.ui.serino.text()
            özelkod=self.ui.zelkod.text()
            teslimalan = self.ui.talan.text()
            teslimeden = self.ui.teeden.text()
            tamireden = self.ui.tameden.text()
            arizabilgi = self.ui.arizabilgi.text()
            yapılanişlem = self.ui.yapilem.text()
            geltar = self.ui.geltarih.text()
            teslimtar = self.ui.teslimtarih.text()
            bilgi = self.ui.ekbilgi.text()
            
            y_offset = 200  # Başlangıç y-offset'ini belirle
            y_step = 390  # Her metin satırı arasında boşluk (y-ekseni adımı)

            # Metni yazdırma
            painter.drawText(100, y_offset, f"ASYA BİLİŞİM GEÇMİŞ VERİ ÇIKTISI ")
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
            painter.drawText(100, y_offset, f"ÖZEL KOD: {özelkod}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Teslim Alan: {teslimalan}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Teslim Eden: {teslimeden}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Tamir Eden: {tamireden}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Arıza Bilgisi : {arizabilgi}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Yapılan İşlem: {yapılanişlem}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Geliş Tarihi : {geltar}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"Teslim Tarihi: {teslimtar}")
            y_offset += y_step  # Bir satır aşağı kaydır
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.drawText(100, y_offset, f"EK BİLGİ: {bilgi}")
            y_offset += y_step  # Bir satır aşağı kaydır
            painter.end()  # Çizimi sonlandır
        

if __name__=="__main__":
        app=QtWidgets.QApplication(sys.argv)
        win=veri()
        win.show()
        sys.exit(app.exec_())                