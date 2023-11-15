from PyQt5.QtWidgets import QPushButton, QMainWindow


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Random circles!')

        self.generate_circle = QPushButton('Рисовать', self)
        self.generate_circle.adjustSize()
        self.generate_circle.move(5, 5)
