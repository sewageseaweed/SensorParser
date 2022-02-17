import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from excelParser import *


"""
TODO: Fix layout
TODO: Compile and create executable
TODO: Add drop down for field/ranch and sample
"""


class SensorGUI(QWidget):
    def __init__(self, parent = None):
        super(SensorGUI, self).__init__(parent)
        self.fname = ''
        self.metafname1 = ''
        self.metafname2 = ''
        #self.setFixedSize(650, 100)
        self.initUI()

    def initUI(self):
        print("YO ", self.fname)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        vbox.addWidget(QLabel("What File Type Is The Sensor Data?"))

        self.radiobutton = QRadioButton("CSV")
        self.radiobutton.type = "csv"
        self.radiobutton.toggled.connect(self.onClicked)
        hbox.addWidget(self.radiobutton)

        self.radiobutton = QRadioButton("EXCEL")
        self.radiobutton.setChecked(True)
        self.radiobutton.type = "excel"
        self.radiobutton.toggled.connect(self.onClicked)
        hbox.addWidget(self.radiobutton)

        vbox.addLayout(hbox)
        self.fileName = QLabel("")
        vbox.addWidget(self.fileName)

        self.combo = QComboBox()
        self.combo.addItem("Field")
        self.combo.addItem("Ranch")
        self.combo.addItem("Both")
        vbox.addWidget(self.combo)

        self.btn = QPushButton("Choose Sensor Excel File")
        self.btn.clicked.connect(self.getfile)
        vbox.addWidget(self.btn)

        self.contents = QLineEdit()
        self.contents.setPlaceholderText("Enter Start Column # for Field Weather")
        self.contents.setValidator(QIntValidator())
        vbox.addWidget(self.contents)

        self.contents2 = QLineEdit()
        self.contents2.setPlaceholderText("Enter End Column # for Ranch Weather")
        self.contents2.setValidator(QIntValidator())
        vbox.addWidget(self.contents2)

        self.parseBtn = QPushButton("Parse Information")
        self.parseBtn.clicked.connect(self.parseInfo)
        vbox.addWidget(self.parseBtn)

        vbox.addWidget(QLabel("\n\n\nParsing Meta Data?:"))

        vbox.addWidget(QLabel("\n\nFile 1 file type:"))
        self.file1Drop = QComboBox()
        self.file1Drop.addItem("CSV")
        self.file1Drop.addItem("XLSX")
        vbox.addWidget(self.file1Drop)

        vbox.addLayout(hbox)
        self.metaFileName1 = QLabel("")
        vbox.addWidget(self.metaFileName1)

        self.metabtn1 = QPushButton("Choose 1st Meta Data File")
        self.metabtn1.clicked.connect(self.getMetaFile1)
        vbox.addWidget(self.metabtn1)

        vbox.addWidget(QLabel("\n\nFile 2 file type:"))
        self.file2Drop = QComboBox()
        self.file2Drop.addItem("CSV")
        self.file2Drop.addItem("XLSX")
        vbox.addWidget(self.file2Drop)

        vbox.addLayout(hbox)
        self.metaFileName2 = QLabel("")
        vbox.addWidget(self.metaFileName2)

        self.metabtn2 = QPushButton("Choose 2nd Meta Data File")
        self.metabtn2.clicked.connect(self.getMetaFile2)
        vbox.addWidget(self.metabtn2)

        self.parseMeta = QPushButton("Parse Meta Data")
        self.parseMeta.clicked.connect(self.parseMetaInfo)
        vbox.addWidget(self.parseMeta)

        self.setLayout(vbox)
        self.setWindowTitle("Field Sensor Parser")

    def onClicked(self):
        self.radiobutton = self.sender()

    def getfile(self):
        self.fname = QFileDialog.getOpenFileName(self)[0]
        self.printer()

    def getMetaFile1(self):
        self.metafname1 = QFileDialog.getOpenFileName(self)[0]
        self.metaFileName1.setText(self.metafname1)

    def getMetaFile2(self):
        self.metafname2 = QFileDialog.getOpenFileName(self)[0]
        self.metaFileName2.setText(self.metafname2)

    def printer(self):
        self.fileName.setText(self.fname)
        print(self.fname)

    def parseInfo(self):
        print('starting Parse')
        print(self.fname)
        message = QMessageBox()
        message.setWindowTitle("Current Status Of Info Parse")
        if str(self.combo.currentText()) == "Field" or str(self.combo.currentText()) == "Both":
            message.setText("Currently Processing Field Weather. Do not exit!")
            message.exec_()
            fieldWeather(self.fname, self.contents, self.radiobutton.type)
        if str(self.combo.currentText()) == "Ranch" or str(self.combo.currentText()) == "Both":
            message.setText("Currently Processing Ranch Weather. Do not exit!")
            message.exec_()
            ranchWeather(self.fname, self.contents2, self.radiobutton.type)
        message.setText("Finished! You may exit!")
        message.exec_()
        print('finished Parse')

    def parseMetaInfo(self):
        csv1 = True
        csv2 = True
        print(self.metafname1)
        if(self.file1Drop.currentText() != "CSV"):
            csv1 = False
        if(self.file2Drop.currentText() != "CSV"):
            csv2 = False
        metaMessage = QMessageBox()
        metaMessage.setWindowTitle("Current Status of Meta Data")
        metaMessage.setText("Currently Processing Meta Data. Do not exit!")
        metaMessage.exec_()
        metaSamples(self.metafname1, self.metafname2, csv1, csv2)
        message.setText("Finished! You may exit!")
        message.exec_()




def main():
    app = QApplication(sys.argv)
    ex = SensorGUI()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
