
import sqlite3
import sys
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from teslim_ui import teslim






class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 413)
        Form.setMaximumSize(QtCore.QSize(1300, 467))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 190, 1300, 200))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setStyleSheet("")
        self.tableView.setObjectName("tableView")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(640, 60, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(34, 34, 34);\n"
"color: rgb(227, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(430, 70, 191, 41))
        self.label_13.setObjectName("label_13")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 40, 131, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(170, 170, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/responsible.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Onarım "))
        self.tableView.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; font-weight:600; color:#ff0000;\">İŞLEM BEKLEYEN MÜŞTERİ</span></p></body></html>"))
        self.pushButton_3.setToolTip(_translate("Form", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "TESLİM ET"))
import icon_rc

  
  #############################################################
class SqlTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, headers=None):
        super(SqlTableModel, self).__init__()
        self.data_list = data  # Veriler
        self.headers = headers  # Sütun başlıkları (None olabilir)

    def rowCount(self, parent=None):
        return len(self.data_list)  # Satır sayısını veriyoruz

    def columnCount(self, parent=None):
        if self.data_list:
            return len(self.data_list[0])  # İlk satırdaki sütun sayısını alıyoruz
        return 0

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self.data_list[row][col])  # Hücredeki veriyi döndürüyoruz

    def headerData(self, section, orientation, role):
        # Başlıkları eklememek için sadece None döndürüyoruz
        return None
  

class onarım(QtWidgets.QMainWindow):
        def __init__(self):
                super(onarım, self).__init__()
                self.ui = Ui_Form()
                self.ui.setupUi(self)
                self.dataload()
                self.ui.pushButton_3.clicked.connect(self.iki)
        def dataload(self):
                try:
                     con=sqlite3.connect("data.db")
                     cursor=con.cursor()
                     cursor.execute("SELECT COUNT(*) FROM müs")
                     
                     row_count = cursor.fetchone()[0]
                     self.ui.lcdNumber.display(row_count)
                     
                     cursor.execute("SELECT * FROM müs")
                     rows=cursor.fetchall()
                     
                     
                     con.close()
                     
                     model = SqlTableModel(rows,headers=None)
                     self.ui.tableView.setModel(model)
                except Exception as e:
                        print(f"Veritabanı Bağlantısı{e}")
                        QtWidgets.QMessageBox.warning(self,"Data hatası",f"veri tabanına bağlanmadı")       

        def iki(self):
                self.sayfa=teslim()
                
                self.sayfa.show()
                
      
if __name__=="__main__":
        app=QtWidgets.QApplication(sys.argv)
        win=onarım()
        win.show()
        sys.exit(app.exec_())
        