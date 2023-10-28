import sys
from PyQt5.QtGui import QPixmap,QColor,QPalette,QGuiApplication
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QFormLayout,QComboBox,QMainWindow,QMessageBox,QAction,QTableWidget,QTableWidgetItem,\
QColorDialog,QComboBox,QProgressBar,QFrame,QSlider
from PyQt5.QtWidgets import (QApplication, QWidget,
  QPushButton, QVBoxLayout, QHBoxLayout,QGridLayout,QLineEdit)
import googletrans
from googletrans import Translator

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100,500, 800)
        self.setFixedSize(500,300)
        self.setWindowTitle('Translater and Voice Generator')

        mainM1=self.menuBar()
        newM = mainM1.addMenu('New')
        helpM = mainM1.addMenu('Help')
        exitM = mainM1.addMenu('Exit')

        exitB  = QAction('Exit', self)
        exitM.addAction(exitB)
        exitB.triggered.connect(self.exit_)

        helpB  = QAction('Help', self)
        helpM.addAction(helpB)
        helpB.triggered.connect(self.help_)

        newB  = QAction('New', self)
        newM.addAction(newB)
        newB.triggered.connect(self.new_)

        #original text shown here
        self.label=QLabel(self)
        self.label.move(0,20)
        self.label.resize(500, 300)

        pix = QPixmap(r'C:\Users\Ariya Rayaneh\Desktop\translate.jpg')
        self.label.setPixmap(pix)

        self.line1=QLineEdit(self)
        self.line1.move(180,50)
        self.line1.resize(300, 30)

        #voice push botton
        self.pushbotton1=QPushButton('Voice',self)
        self.pushbotton1.move(20,200)
        self.pushbotton1.clicked.connect(self.voice_)

        self.combo = QComboBox(self)
        self.combo.addItem("Destination Language")
        self.combo.currentIndexChanged.connect(self.translate_)

        for i in googletrans.LANGUAGES.values():

         self.combo.addItem(i)
         self.combo.move(200, 100)
         self.combo.resize(280, 30)

        #final translation showed here
        self.line2=QLineEdit(self)
        self.line2.move(180,150)
        self.line2.resize(300, 30)

        self.line3=QLineEdit('Select destination Language---->',self)
        self.line3.move(20,100)
        self.line3.resize(170, 30)

        self.line4=QLineEdit('Insert original text here---->',self)
        self.line4.move(20,50)
        self.line4.resize(150, 30)

        #original---->dest language
        self.line5=QLineEdit('',self)
        self.line5.move(20,150)
        self.line5.resize(150, 30)

        self.statusBar().showMessage('Reza Mousavi')
        self.show()

    def help_(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Please enter each digit and click the \"Next\" afterwards and click the \"Finish\" after last digit.")
        msgBox.setWindowTitle("Help")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()

    def exit_(self):
        qmb=QMessageBox.question(self,"message",'Do you really want to close?',QMessageBox.Yes | QMessageBox.No | QMessageBox.Help )
        if qmb==QMessageBox.Yes:
            self.close()
        elif qmb==QMessageBox.No:
            pass
        elif qmb==QMessageBox.Help:
            self.help_()

    def new_(self):
        self.line2.setText('')
        self.line5.setText('')
        self.line1.setText('')

    def translate_(self):
        translator = Translator()
        for i in googletrans.LANGUAGES.items():
            if i[1] == self.combo.currentText():
                dest=i[0]
        result = translator.translate(self.line1.text(),dest)
        self.line2.setText(str(result.text))
        self.line5.setText(str(result.src)+'---->'+str(result.dest))


    def voice_(self):
        import pyttsx3
        engine = pyttsx3.init()
        text = self.line2.text()
        engine.say(text)
        engine.runAndWait()

if __name__ == '__main__':
 app = QApplication(sys.argv)
 ex = Example()
 sys.exit(app.exec_())