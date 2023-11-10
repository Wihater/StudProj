from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic
class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.a)
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.run(qp)
    def run(self, qp):
        if self.a:
            qp.setBrush(QColor(255, 255, 0))
            x = random.randint(10, 300)
            y = random.randint(10, 200)
            w = random.randint(10, 50)
            qp.drawEllipse(x, y, w, w)
            self.a = False
    def a(self):
        print(1231234)
        self.a = True
        self.update()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
    sys.exit(app.exec_())
