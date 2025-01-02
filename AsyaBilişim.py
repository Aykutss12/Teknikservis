

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from kayıt_ui import kayit_arayüz
from sorgu_ui import sorgu_arayüz
from onarım_ui import onarım
from teslim_ui import teslim

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 303)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ikon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 160, 571, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/ikon/cooltext472695298741495.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 81, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/ikon/computer.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 10, 91, 81))
        self.pushButton.setStyleSheet("color: rgb(0, 170, 0);\n"
"image: url(:/newPrefix/ikon/people.png);\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 10, 91, 81))
        self.pushButton_2.setStyleSheet("image: url(:/newPrefix/ikon/searching.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 10, 91, 81))
        self.pushButton_3.setStyleSheet("image: url(:/newPrefix/ikon/computer.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setShortcut("")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 10, 91, 81))
        self.pushButton_4.setStyleSheet("\n"
"image: url(:/newPrefix/ikon/responsible.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setToolTipDuration(-1)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(True)
        self.label_3.setIndent(6)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 100, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.label_4.setToolTipDuration(-1)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(True)
        self.label_4.setIndent(6)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 100, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_5.setFont(font)
        self.label_5.setToolTipDuration(-1)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(True)
        self.label_5.setIndent(6)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 100, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setToolTipDuration(-1)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(True)
        self.label_6.setIndent(6)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(210, 40, 61, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(360, 40, 61, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(510, 40, 61, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(490, 260, 301, 21))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/ikon/cooltext472942123166566.png"))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Teknik Servis"))
        self.label_3.setText(_translate("MainWindow", "MÜŞTERİ KAYIT"))
        self.label_4.setText(_translate("MainWindow", "ÜRÜN SORGULAMA"))
        self.label_5.setText(_translate("MainWindow", "ONARIMDAKİLER"))
        self.label_6.setText(_translate("MainWindow", "TESLİM ET"))
import icon_rc
class main(QtWidgets.QMainWindow):
        def __init__(self):
                super(main, self).__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                self.ui.pushButton.clicked.connect(self.kayit)
                
                self.ui.pushButton_2.clicked.connect(self.sorgu)
                
                self.ui.pushButton_3.clicked.connect(self.onarim)
                
                self.ui.pushButton_4.clicked.connect(self.teslim)
                
                
        def sorgu(self):
                self.sayfa=sorgu_arayüz()
                self.sayfa.show()
        
        
        def kayit(self):
                self.sayfa=kayit_arayüz()
                self.sayfa.show()
        
        def onarim(self):
                self.s=onarım()
                self.s.show()
        
        def teslim(self):
                self.sayfa=teslim()
                self.sayfa.show()
        
        
                
if __name__=="__main__":
        app=QtWidgets.QApplication(sys.argv)
        win=main()
        win.show()
        sys.exit(app.exec_())                
                