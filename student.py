# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_student(object):
    def setupUi(self, student):
        student.setObjectName("student")
        student.resize(1581, 805)
        self.centralwidget = QtWidgets.QWidget(student)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 1211, 651))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(1270, 350, 301, 241))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1270, 280, 201, 31))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 0, 791, 91))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 40, 351, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 181, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(690, 40, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 110, 791, 621))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, item)
        student.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(student)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1581, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        student.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(student)
        self.statusbar.setObjectName("statusbar")
        student.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(student)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(student)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(student)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(student)
        self.action_4.setObjectName("action_4")
        self.actionISBN = QtWidgets.QAction(student)
        self.actionISBN.setObjectName("actionISBN")
        self.action_5 = QtWidgets.QAction(student)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(student)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(student)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(student)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(student)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(student)
        self.action_10.setObjectName("action_10")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.actionISBN)
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menu_3.addAction(self.action_8)
        self.menu_4.addAction(self.action_9)
        self.menu_5.addAction(self.action_10)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(student)
        self.action.triggered.connect(student.find_name)
        self.action_2.triggered.connect(student.find_type)
        self.actionISBN.triggered.connect(student.find_ISBN)
        self.pushButton.clicked.connect(student.start_find)
        self.action_6.triggered.connect(student.find_time)
        self.action_5.triggered.connect(student.find_au)
        self.action_7.triggered.connect(student.borrow)
        self.action_8.triggered.connect(student.back)
        self.action_9.triggered.connect(student.longer)
        self.action_10.triggered.connect(student.history)
        QtCore.QMetaObject.connectSlotsByName(student)

    def retranslateUi(self, student):
        _translate = QtCore.QCoreApplication.translate
        student.setWindowTitle(_translate("student", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("student", "书名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("student", "ISBN号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("student", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("student", "出版时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("student", "数量"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("student", "标价"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("student", "可借阅时间"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("student", "可借阅数量"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("student", "库存书架号"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("student", "类型"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("student", "还书时间"))
        self.label.setText(_translate("student", "当前时间："))
        self.label_2.setText(_translate("student", "请输入要找的图书名称："))
        self.pushButton.setText(_translate("student", "开始查找"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("student", "《微积分》"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("student", "《斗破苍穹》"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("student", "《SQL入门》"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("student", "图书类型"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("student", "借阅人数"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("student", "当前是否可借阅"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("student", "高等数学"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("student", "111"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("student", "是"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("student", "小说"))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("student", "23"))
        item = self.tableWidget_2.item(1, 2)
        item.setText(_translate("student", "是"))
        item = self.tableWidget_2.item(2, 0)
        item.setText(_translate("student", "计算机技术"))
        item = self.tableWidget_2.item(2, 1)
        item.setText(_translate("student", "34"))
        item = self.tableWidget_2.item(2, 2)
        item.setText(_translate("student", "否"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.menu.setTitle(_translate("student", "查阅图书"))
        self.menu_2.setTitle(_translate("student", "借阅图书"))
        self.menu_3.setTitle(_translate("student", "归还图书"))
        self.menu_4.setTitle(_translate("student", "续借图书"))
        self.menu_5.setTitle(_translate("student", "个人借阅历史"))
        self.action.setText(_translate("student", "按图书名称查找"))
        self.action_2.setText(_translate("student", "按图书类型查找"))
        self.action_3.setText(_translate("student", "热度排行榜"))
        self.action_4.setText(_translate("student", "进入借阅界面"))
        self.actionISBN.setText(_translate("student", "ISBN"))
        self.action_5.setText(_translate("student", "按作者"))
        self.action_6.setText(_translate("student", "按出版时间"))
        self.action_7.setText(_translate("student", "借阅"))
        self.action_8.setText(_translate("student", "归还"))
        self.action_9.setText(_translate("student", "续借"))
        self.action_10.setText(_translate("student", "查看个人借阅历史"))
