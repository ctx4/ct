from instr import *
from PyQt4.QtCore import Qt
from PyQt5.QTWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,GroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QlineEdit)
from second_win import *
from final_win import *
class TextWin(QWidget):
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
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_next1 = QPushButton(txt_sendresults1, self)
        self.btn_next2 = QPushButton(txt_sendresults2, self)
        self.btn_next3 = QPushButton(txt_sendresults3, self)
        self.text_name = QLabel(txt_name)
        self.text_age= QLabel(txt_age)
        self.text_test1 = QLabel(txt_text1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_text3)
        self.text_timer = QLabel(txt_timer)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.test_test2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_test3, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.timer)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

