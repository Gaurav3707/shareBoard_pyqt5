import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt


class Example(QWidget):
    def __init__(self):
        print("Inititaled")
        super().__init__()

    def keyPressEvent(self, event):
        print("-----------")
        print(event.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = Example()
    demo.show()
    sys.exit(app.exec_())
