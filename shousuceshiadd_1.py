# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_Form_1(object):

    def setupUi(self, Form):
        print('bbbb')
        Form.setObjectName("Form")
        Form.resize(304, 211)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 130, 61, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 51, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(100, 130, 61, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(200, 10, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(260, 10, 31, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 50, 151, 61))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "点击次数"))
        self.label_2.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "用时"))
        self.label_4.setText(_translate("Form", "0"))
        self.label_5.setText(_translate("Form", "上次次数"))
        self.label_6.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", "恭喜你！"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
