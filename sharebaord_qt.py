import sys

from PyQt5 import QtCore, QtWebSockets, QtNetwork
from PyQt5.QtCore import QUrl, QCoreApplication, QTimer, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QPlainTextEdit, QLineEdit

from PyQt5.QtCore import QSize
import json



class Client(QtCore.QObject):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = QLabel(alignment=Qt.AlignCenter)

        self.client =  QtWebSockets.QWebSocket("",QtWebSockets.QWebSocketProtocol.Version13,None)
        self.client.error.connect(self.error)


        self.client.textMessageReceived.connect(self.handle_message)
        self.client.open(QUrl("ws://3.27.105.143:8000/ws/board/qt_test/"))
        self.client.pong.connect(self.onPong)

    def send_message(self, msg):
        self.client.sendTextMessage('{"message":"' + msg + ' "}')
    
    def receive_message(self):
        self.client.textMessageReceived()

    def onPong(self, elapsedTime, payload):
        print("onPong - time: {} ; payload: {}".format(elapsedTime, payload))

    def error(self, error_code):
        print("error code: {}".format(error_code))
        print(self.client.errorString())

    def handle_message(self, text):
        try:
            d = json.loads(text)
        except json.decoder.JSONDecodeError as e:
            print("error:", e)
        else:
            if "message" in d:
                intent = d["message"]
                widget.b.clear()
                widget.b.insertPlainText(intent)
            else:
                print('----------------- no message')
                    

    

    def close(self):
        self.client.close()
        

def quit_app():
    print("timer timeout - exiting")
    QCoreApplication.quit()


def send_message():
    msg = widget.b.toPlainText()
    if msg != "":
        client.send_message(msg)
    

def receive_message():
    client.receive_message()

def key_stroke():
    print('----------------- event')



def window():

    

    app = QApplication(sys.argv)
    global widget
    widget = QWidget()

    
    

    widget.b = QPlainTextEdit(widget)
    # widget.b = QLineEdit(widget)


    widget.b.move(10,10)
    widget.b.resize(400,200)
    

    button1 = QPushButton(widget)
    button1.setText("Send")
    button1.move(330,220)
    
    button1.clicked.connect(send_message)

    widget.setGeometry(500,500,425,300)
    widget.setWindowTitle("Share Board")
    widget.show()



        

    

	



    
    sys.exit(app.exec_())


def button1_clicked():
    print("Button 1 clicked")

def button2_clicked():
    print("Button 2 clicked")



if __name__ == '__main__':
    try:
        global client
        app = QApplication(sys.argv)

        QTimer.singleShot(3000, send_message)
        QTimer.singleShot(3000, key_stroke)

        
        

        client = Client(app)
        
        # app.exec_()
        window()

        
    except:
        QTimer.singleShot(5000, quit_app)
    
