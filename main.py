from PyQt5.QtWidgets import QMainWindow, QApplication

import shousuceshi
from shousuceshi import CanStart
from shousuceshi import MainWindow
from shousuceshiadd_1 import Ui_Form_1
import sys
import threading

class Main(QMainWindow, MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


class Child(QMainWindow, Ui_Form_1):
    def __init__(self):
        super(Child, self).__init__()
        self.setupUi(self)

    def Open(self):
        self.show()


class Start:
    # global eEvent
    # eEvent = threading.Event()
    def start(self):
        pass
        # if (not CanStart()) and shousuceshi.Gettext_7() == 0:
        #     print('start')
        #
        #     child.Open()

    # def get_girl_friend(self):
    #     print(".....".format(eEvent.isSet()))
    #     eEvent.wait()

if __name__ == "__main__":
    # thread_list = list()
    #
    #
    # print('创建并初始化线程')
    # t = threading.Thread(target=Start.get_girl_friend, args=())
    # print('启动线程')
    # t.start()
    # print('将线程句柄添加list列表中')
    # thread_list.append(t)
    #
    # print('所有线程准备完毕，将event内置Flag设置为True,恢复正在阻塞的线程')
    # eEvent.set()
    #
    # print('遍历列表，阻塞主线程')
    # for t in thread_list:
    #     # 阻塞主线程，等待所有子线程结束
    #     t.join()
    app = QApplication(sys.argv)
    main = Main()
    child = Child()
    main.show()
    Start.start(self=Start)
    sys.exit(app.exec_())
