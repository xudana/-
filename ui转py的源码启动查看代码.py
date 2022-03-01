# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import math
import sys

#换成自己对应目录下的UI文件
ui_file = '运算放大器放大倍数与分贝转换器/运算放大器放大倍数与分贝转换器.ui'


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.ap_data_1 = None
        self.db_data_1 = None
        self.db_data_1_to_float_1 = None
        self.db_data = None
        self.ap_data = None
        self.ap_data_to_float = None
        self.init_ui()
        self.set_signal()


    def init_ui(self):
        loadUi(ui_file, self)
        self.setWindowTitle(u'运算放大器放大倍数与分贝转换器')
        self.lineEdit_dB1.setReadOnly(True)
        self.lineEdit_Ap2.setReadOnly(True)

    def set_signal(self):
        # 放大倍数转dB
        self.pushButton_AptodB.clicked.connect(self.AptodB)
        # dB转放大倍数
        self.pushButton_dBtoAp.clicked.connect(self.dBtoAp)

    # 放大倍数转dB槽
    @QtCore.pyqtSlot()
    def AptodB(self):
        try:
            self.ap_data = float(self.lineEdit_Ap1.text())
            if self.ap_data > 0:
                self.ap_data_to_float = '%.4f' % math.log10(self.ap_data)
                self.db_data = float(self.ap_data_to_float) * 20
                self.lineEdit_dB1.setText(str(self.db_data)[:7])
            elif self.ap_data < 0:
                self.ap_data = abs(self.ap_data)
                self.ap_data_to_float = '%.4f' % math.log10(self.ap_data)
                self.db_data = float(self.ap_data_to_float) * 20
                self.lineEdit_dB1.setText("-" + str(self.db_data)[:7])
        except:
            self.lineEdit_dB1.setText(u'输入错误')

    # dB转放大倍数槽
    @QtCore.pyqtSlot()
    def dBtoAp(self):
        try:
            self.db_data_1 = float(self.lineEdit_dB2.text())
            # if self.db_data_1 >= 0:
            self.db_data_1_to_float_1 = float(self.db_data_1) / 20
            # print(self.db_data_1_to_float_1)
            self.ap_data_1 = math.pow(10, self.db_data_1_to_float_1)
            # print(self.ap_data_1)
            self.lineEdit_Ap2.setText(str(self.ap_data_1)[:10])
        # elif self.db_data_1 < 0:
            self.db_data_1_to_float_1 = float(self.db_data_1) / 20
            # print(self.db_data_1_to_float_1)
            self.ap_data_1 = math.pow(10, self.db_data_1_to_float_1)
            # print(self.ap_data_1)
            self.lineEdit_Ap2.setText(str(self.ap_data_1)[:10])
        except:
            self.lineEdit_Ap2.setText(u'输入错误')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
