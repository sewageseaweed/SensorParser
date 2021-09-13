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
        self.setFixedSize(650, 250)
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

        self.setLayout(vbox)
        self.setWindowTitle("Field Sensor Parser")

    def onClicked(self):
        self.radiobutton = self.sender()

    def getfile(self):
        self.fname = QFileDialog.getOpenFileName(self)[0]
        self.printer()

    def printer(self):
        self.fileName.setText(self.fname)
        print(self.fname)

    def parseInfo(self):
        print('starting Parse')
        print(self.fname)
        message = QMessageBox()
        message.setWindowTitle("Current Status")
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


def main():
    app = QApplication(sys.argv)
    ex = SensorGUI()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
