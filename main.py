from UI import UI
import random
import sys
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication


class YellowCircles(UI):
    def __init__(self):
        super().__init__()

        self.do_paint = False
        self.generate_circle.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circles(self, qp):
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.setPen(QColor(255, 255, 255))

        radius = random.randint(10, 100)
        qp.drawEllipse(QPoint(150, 150), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec_())

