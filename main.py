import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 500, 600, 600)
        self.setWindowTitle("de mon coeur à mon coeur")
        self.setWindowIcon(QIcon("images\heart.png"))
        
        self.label = QLabel("Confession", self)
        self.button = QPushButton("Say it!", self)
        
        self.initUI()

    def initUI(self):
        self.label.setGeometry(0, 0, 600, 100)
        self.label.setStyleSheet("""
            background-color: #e8a0dc;
            color: #8a1977;
        """)
        self.label.setFont(QFont("Poppins", 50))
        self.setStyleSheet("background-color: #e8a0dc;")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.button.setStyleSheet("""
            background-color: #8a1977;
            color: white;
            font-size: 20px;
            border-radius: 10px;
        """)

        self.centerButton()

        self.button.clicked.connect(self.onClick)

    def centerButton(self):
        buttonWidth, buttonHeight = 150, 50
        windowWidth, windowHeight = self.width(), self.height()

        x = (windowWidth - buttonWidth) // 2
        y = (windowHeight - buttonHeight) // 2

        self.button.setGeometry(x, y, buttonWidth, buttonHeight)

    def onClick(self):
        self.label.setText("I love you!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()