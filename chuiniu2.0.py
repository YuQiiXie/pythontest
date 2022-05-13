# -*- coding: utf-8 -*-
import random
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_Form(object):
    def __init__(self):
        self.allpaixu = []


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(469, 490)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 66, 66))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 66, 66))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 10, 66, 66))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(230, 10, 66, 66))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(300, 10, 66, 66))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(370, 10, 66, 66))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(320, 370, 51, 20))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(40, 340, 71, 20))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 420, 411, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clkbutton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 340, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.clkbutton2)
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 370, 81, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(120, 340, 41, 20))
        self.label_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_15.setObjectName("label_15")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(378, 365, 41, 41))
        self.spinBox.setReadOnly(False)
        self.spinBox.setKeyboardTracking(True)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(12)
        self.spinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.spinBox.setProperty("value", 6)
        self.spinBox.setObjectName("spinBox")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 66, 66))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(90, 80, 66, 66))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(160, 80, 66, 66))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(230, 80, 66, 66))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(300, 80, 66, 66))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(370, 80, 66, 66))
        self.label_12.setObjectName("label_12")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(350, 340, 71, 21))
        self.checkBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.checkBox.setBaseSize(QtCore.QSize(0, 0))
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(-40, 170, 721, 2))
        self.textBrowser.setObjectName("textBrowser")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(70, 200, 33, 33))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(110, 200, 33, 33))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(150, 200, 33, 33))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(190, 200, 33, 33))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(230, 200, 33, 33))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(270, 200, 33, 33))
        self.label_22.setObjectName("label_22")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(85, 250, 41, 20))
        self.label_31.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setGeometry(QtCore.QRect(125, 250, 41, 20))
        self.label_32.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(165, 250, 41, 20))
        self.label_33.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(205, 250, 41, 20))
        self.label_34.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(Form)
        self.label_35.setGeometry(QtCore.QRect(245, 250, 41, 20))
        self.label_35.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(Form)
        self.label_36.setGeometry(QtCore.QRect(285, 250, 41, 20))
        self.label_36.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_36.setObjectName("label_36")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.main()

    def clkbutton(self):
        global clinum
        self.allclear()
        self.cleartongji()
        if not self.checkBox.isChecked():
            paixu = []
            spinvalue = int(self.spinBox.value())
            for i in range(1, spinvalue + 1):
                a = random.randint(1, 6)
                paixu.append(a)
                self.xianshi(i, a)
                self.tongji(a)
            clinum += 1
            self.label_15.setText(str(clinum))
        else:
            paixu = []
            spinvalue = int(self.spinBox.value())
            for i in range(1, spinvalue + 1):
                a = random.randint(1, 6)
                paixu.append(a)
                self.tongji(a)
            paixu.sort()
            for j in range(1, len(paixu) + 1):
                self.xianshi(j, paixu[j - 1])
            clinum += 1
            self.label_15.setText(str(clinum))
        self.showtongji()
        self.filesave()

    def clkbutton2(self):
        global clinum, cleannum
        self.allclear()
        self.cleartongji()
        if clinum == 0: return
        clinum = 0
        cleannum += 1
        self.label_15.setText(str(clinum))
        self.textBrowser_2.setText('清空计次:' + str(cleannum))
        self.filesave()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_13.setText(_translate("Form", "总个数"))
        self.label_14.setText(_translate("Form", "点击次数"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "清空"))
        self.label_15.setText(_translate("Form", "0"))
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_22.setText("")
        self.label_31.setText("")
        self.label_32.setText("")
        self.label_33.setText("")
        self.label_34.setText("")
        self.label_35.setText("")
        self.label_36.setText("")
        self.checkBox.setText(_translate("Form", "自动排序"))

    def allclear(self):
        self.label.clear()
        self.label_2.clear()
        self.label_3.clear()
        self.label_4.clear()
        self.label_5.clear()
        self.label_6.clear()
        self.label_7.clear()
        self.label_8.clear()
        self.label_9.clear()
        self.label_10.clear()
        self.label_11.clear()
        self.label_12.clear()


    def xianshi(self, weizhi, shuzi):
        if int(weizhi) == 1:
            localweizhi = self.label
        if int(weizhi) == 2:
            localweizhi = self.label_2
        if int(weizhi) == 3:
            localweizhi = self.label_3
        if int(weizhi) == 4:
            localweizhi = self.label_4
        if int(weizhi) == 5:
            localweizhi = self.label_5
        if int(weizhi) == 6:
            localweizhi = self.label_6
        if int(weizhi) == 7:
            localweizhi = self.label_7
        if int(weizhi) == 8:
            localweizhi = self.label_8
        if int(weizhi) == 9:
            localweizhi = self.label_9
        if int(weizhi) == 10:
            localweizhi = self.label_10
        if int(weizhi) == 11:
            localweizhi = self.label_11
        if int(weizhi) == 12:
            localweizhi = self.label_12
        if int(weizhi) == 17:
            localweizhi = self.label_17
        if int(weizhi) == 18:
            localweizhi = self.label_18
        if int(weizhi) == 19:
            localweizhi = self.label_19
        if int(weizhi) == 20:
            localweizhi = self.label_20
        if int(weizhi) == 21:
            localweizhi = self.label_21
        if int(weizhi) == 22:
            localweizhi = self.label_22
        if int(shuzi) == 1:
            localjpg = './2022051001.jpg'
        if int(shuzi) == 2:
            localjpg = './2022051002.jpg'
        if int(shuzi) == 3:
            localjpg = './2022051003.jpg'
        if int(shuzi) == 4:
            localjpg = './2022051004.jpg'
        if int(shuzi) == 5:
            localjpg = './2022051005.jpg'
        if int(shuzi) == 6:
            localjpg = './2022051006.jpg'
        png = QPixmap(localjpg)
        localweizhi.setPixmap(png)
        localweizhi.setScaledContents(True)

    @staticmethod
    def tongji(a):
        global n1, n2, n3, n4, n5, n6
        if a == 1:
            n1 += 1
        if a == 2:
            n2 += 1
        if a == 3:
            n3 += 1
        if a == 4:
            n4 += 1
        if a == 5:
            n5 += 1
        if a == 6:
            n6 += 1

    def cleartongji(self):
        global n1, n2, n3, n4, n5, n6
        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        n5 = 0
        n6 = 0
        self.label_31.clear()
        self.label_32.clear()
        self.label_33.clear()
        self.label_34.clear()
        self.label_35.clear()
        self.label_36.clear()

    def showtongji(self):
        if not n1 == 0:
            self.label_31.setText(str(n1))
        if not n2 == 0:
            self.label_32.setText(str(n2))
        if not n3 == 0:
            self.label_33.setText(str(n3))
        if not n4 == 0:
            self.label_34.setText(str(n4))
        if not n5 == 0:
            self.label_35.setText(str(n5))
        if not n6 == 0:
            self.label_36.setText(str(n6))

    def filesave(self):
        ls1 = [self.spinBox.value(), self.checkBox.isChecked()]
        pa1 = r"C:\Users\Public\Documents\随机骰子"
        if not os.path.exists(pa1):
            os.makedirs(pa1)
        fp = open(r"C:\Users\Public\Documents\随机骰子\data.txt", "w")
        for i in range(2):
            fp.write(str(ls1[i]))
            fp.write('\n')
        fp.close()

    def fileread(self):
        if not os.path.exists(r"C:\Users\Public\Documents\随机骰子"): return
        try:
            f = open(r"C:\Users\Public\Documents\随机骰子\data.txt", "r")
            flist = f.readlines()
            self.spinBox.setProperty("value", int(flist[0]))
            if flist[1].strip() == 'False' or flist[1].strip() == 'false':
                self.checkBox.setChecked(False)
            if flist[1].strip() == 'True' or flist[1].strip() == 'true':
                self.checkBox.setChecked(True)
            f.close()
            for i in range(1, int(flist[0]) + 1):
                self.xianshi(i, 1)
        except:
            return

    def main(self):
        self.fileread()
        for i in range(1, 7):
            self.xianshi(i + 16, i)


if __name__ == "__main__":
    import sys

    global clinum, cleannum, canread
    global n1, n2, n3, n4, n5, n6
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0
    clinum = 0
    cleannum = 0
    canread = False

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
