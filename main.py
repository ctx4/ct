from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QListWidget, QLineEdit
from instr import *
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear
        self.initUI
        self.connects
        self.next_click
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_height, win_width)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layuot.addWidget(self.hello.text)
        self.layout.addWidget(self.instryction)
        self.layout.addWidget(self.button)
    def connects(self):
        self.btn_text.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
        
app = QApplication([])
mw = MainWin()
app.exec_()
