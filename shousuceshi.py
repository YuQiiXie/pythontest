# -*- coding: utf-8 -*-
import time
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *


# root = Tk()

#
# def printRect(event):
#     print('rectangle左键事件')
#
#
# def printRect2(event):
#     print('rectangle右键事件')
#
#
# def printLine(event):
#     print('Line事件')


def CanStart():
    global canstart
    return canstart


class MainWindow(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 351)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 180, 461, 171))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(60, 69, 41, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 31, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 60, 21, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 41, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 130, 31, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(170, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(260, 130, 31, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 60, 51, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(300, 40, 141, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(300, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit.setText('5')
        self.pushButton.clicked.connect(self.clk_btn)
        self.pushButton_2.clicked.connect(self.clk_btn2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.main()

    def clk_btn2(self):
        global clknum, isstart, totaltime, canstart, runflag
        if int(str(self.label_7.text())) == 0:
            try:
                totaltime = float(self.lineEdit.text())
                clknum = 0
                canstart = True
                runflag = False
                self.label_7.setText((str(int(totaltime))))
            except:
                self.lineEdit.setText('请输入数字')

    def clk_btn(self):
        global clknum, isstart, totaltime, canstart
        if canstart:
            self.label_7.setText(str(int(totaltime)))
            canstart = False
        if int(str(self.label_7.text())) > 0:

            if isstart:
                clknum += 1
                self.label_5.setText(str(clknum))
            if not isstart:
                self.daojishi()
                clknum += 1
                self.label_5.setText(str(clknum))

    def daojishi(self):
        global restartflag
        global runflag
        if not runflag:
            th = threading.Thread(target=self.cyclethread)
            th.setDaemon(True)
            th.start()
            runflag = True

    def cyclethread(self):
        global totaltime, isstart
        isstart = True
        for i in range(int(totaltime) - 1, -1, -1):
            self.label_7.setText(str(i))
            time.sleep(1)
        isstart = False
        self.history()

    def history(self):
        histime=self.lineEdit.text()
        hisclknum=self.label_5.text()
        self.textBrowser.append('次数:'+hisclknum+' '+'用时:'+histime+'s')

    def main(self):
        global clknum
        global totaltime, isstart, canstart
        global restartflag
        global runflag
        restartflag = True
        runflag = False
        totaltime = 5
        clknum = 0
        isstart = False
        canstart = True

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "疯狂点击此处！"))
        self.label.setText(_translate("Form", "手速测试器"))
        self.label_2.setText(_translate("Form", "时间"))
        self.label_3.setText(_translate("Form", "s"))
        self.label_4.setText(_translate("Form", "次数"))
        self.label_5.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "剩余时间"))
        self.label_7.setText(_translate("Form", "0"))
        self.pushButton_2.setText(_translate("Form", "设置"))
        self.label_8.setText(_translate("Form", "历史次数"))

    # def initmain(self):
    #     self.pushButton_2.clicked.connect(self.click_2)
    #     self.pushButton.clicked.connect(self.click)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainWindow()
    ui.setupUi(Form)
    Form.show()

    cv = Canvas(root, bg='white')
    rt1 = cv.create_rectangle(10, 10, 110, 110, width=8, tags='r1')  # 此长方形标签为r1

    cv.tag_bind('r1', '<Button-1>', printRect)  # 按标签绑定，左键点击r1时，执行printRect事件
    cv.tag_bind('r1', '<Button-3>', printRect2)
    cv.create_line(180, 70, 280, 70, width=10, tags='r2')
    cv.tag_bind('r2', '<Button-1>', printLine)  # 点击r2线条时，执行printLine
    cv.pack()
    root.mainloop()
    sys.exit(app.exec_())
