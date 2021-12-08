import sys
from PyQt5.QtWidgets import QApplication, QWidget, QWidgetAction, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.interface()

    def interface(self):

        # label
        et1 = QLabel("Number 1:", self)
        et2 = QLabel("Number 2:", self)
        et3 = QLabel("Result", self)

        # assigning widgets to the layout
        layoutT = QGridLayout()
        layoutT.addWidget(et1, 0, 0)
        layoutT.addWidget(et2, 0, 1)
        layoutT.addWidget(et3, 0, 2)

        # set Layout
        self.setLayout(layoutT)

        self.number1Edt = QLineEdit()
        self.number2Edt = QLineEdit()
        self.resultsEdt = QLineEdit()

        self.resultsEdt.setReadOnly = True
        self.resultsEdt.setToolTip("Insert numbers and choose operation")

        # set positions 

        layoutT.addWidget(self.number1Edt, 1, 0)
        layoutT.addWidget(self.number2Edt, 1, 1)
        layoutT.addWidget(self.resultsEdt, 1, 2)

        #button 
        addjBtn = QPushButton("&Add", self)
        subtractBtn = QPushButton("&Subtract", self)
        multiplyBtn = QPushButton("&Multiply", self)
        divideBtn = QPushButton("Divide", self)
        endBtn = QPushButton("&Exit", self)
        endBtn.resize(endBtn.sizeHint())

        layoutH = QHBoxLayout()
        layoutH.addWidget(addjBtn)
        layoutH.addWidget(subtractBtn)
        layoutH.addWidget(divideBtn)
        layoutH.addWidget(multiplyBtn)

        layoutT.addLayout(layoutH, 2, 0, 1, 3)
        layoutT.addWidget(endBtn, 3, 0, 1, 3)

        endBtn.clicked.connect(self.end)
        addjBtn.clicked.connect(self.operations)
        subtractBtn.clicked.connect(self.operations)
        multiplyBtn.clicked.connect(self.operations)
        divideBtn.clicked.connect(self.operations)


        self.resize(300,100)  #set size of frame
        self.setWindowTitle("Simple calculator")
        self.show()

    def end(self):
        self.close()

    def closeEvent(self, event):

        response = QMessageBox.question(
            self, 'Notification',
            "Do You want exit?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if response == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def operations(self):
        s = self.sender()

        try:
            num1 = float(self.number1Edt.text())
            num2= float(self.number2Edt.text())
            result = ""

            if s.text() == "&Add":
                wynik = num1 + num2
            elif s.text() == "&Subtract":
                wynik = num1 - num2
            elif s.text() == "&Multiply":
                wynik = num1 * num2
            else:  # dzielenie
                try:
                    wynik = round(num1 / num2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Error", "Can not divide by zero")
                    return

            self.resultsEdt.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Error", "Data not validate", QMessageBox.Ok)
    

if __name__ == '__main__':
    cal = QApplication(sys.argv)
    window = Calculator()
    sys.exit(cal.exec_())