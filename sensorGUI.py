import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator


class filedialogdemo(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.fname = ''
        self.initUI()

    def initUI(self):
        print("YO ", self.fname)
        layout = QVBoxLayout()

        self.fileName = QLabel("")

        layout.addWidget(self.fileName)

        self.btn = QPushButton("Choose Sensor Excel File")
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)

        self.contents = QLineEdit()
        self.contents.setPlaceholderText("JOI")
        self.contents.setValidator(QIntValidator())
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("Field Sensor Parser")
        print("END")

    def getfile(self):
        self.fname = QFileDialog.getOpenFileName(self)[0]
        #self.fname = "LPOLOL"
        self.printer()

    def printer(self):
        self.fileName.setText(self.fname)
        print(self.fname)
        pront('testoing lsoa')

def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
