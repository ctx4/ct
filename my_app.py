from instr import *
from PyQt4.QtCore import Qt
from PyQt5.QTWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,GroupBox, QRadioButton QPushButton, QLabel, QListWidget, QlineEdit)
from second_win import *
from final_win import *
class MainWin(QWidget):
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.insctruction = QLabel(txt_instruction)
        self.button = QPushButton(text_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_txt)
        self.layout.addWidget(self.insctruction)
        self.layout.addWidget(self.button)
    def connects(self):
        pass
    def next_click(self):
        self.hide()
    def next_click(self):
        self.tw=textWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        
app = QApplication([])
mw = MainWin()
app.exec_()