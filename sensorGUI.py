import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator


"""
TODO: Fix layout
TODO: Connect to excel parser
TODO: Compile and create executable
"""


class SensorGUI(QWidget):
    def __init__(self, parent = None):
        super(SensorGUI, self).__init__(parent)
        self.fname = ''
        self.setFixedSize(640, 150)
        self.initUI()

    def initUI(self):
        print("YO ", self.fname)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        vbox.addWidget(QLabel("What File Type Is The Sensor Data?"))

        self.radiobutton = QRadioButton("CSV")
        self.radiobutton.type = "csv"
        hbox.addWidget(self.radiobutton)

        self.radiobutton = QRadioButton("EXCEL")
        self.radiobutton.type = "excel"
        hbox.addWidget(self.radiobutton)

        vbox.addLayout(hbox)
        self.fileName = QLabel("")
        vbox.addWidget(self.fileName)

        self.btn = QPushButton("Choose Sensor Excel File")
        self.btn.clicked.connect(self.getfile)
        vbox.addWidget(self.btn)

        self.contents = QLineEdit()
        self.contents.setPlaceholderText("Enter Num of Columns for Field Weather")
        self.contents.setValidator(QIntValidator())
        vbox.addWidget(self.contents)
        self.setLayout(vbox)
        self.setWindowTitle("Field Sensor Parser")
        print("END")

    def getfile(self):
        self.fname = QFileDialog.getOpenFileName(self)[0]
        self.printer()

    def printer(self):
        self.fileName.setText(self.fname)
        print(self.fname)

def main():
    app = QApplication(sys.argv)
    ex = SensorGUI()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
