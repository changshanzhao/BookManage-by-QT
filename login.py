# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QApplication
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QRectF


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(596, 758)
        self.scene = QGraphicsScene()
        self.pixmap = QPixmap('logo.png')
        self.scaled_pixmap = self.pixmap.scaled(170, 150)
        self.scene.addPixmap(self.scaled_pixmap)
        self.tabWidget = QtWidgets.QTabWidget(login)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 761))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 570, 80, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_1.setGeometry(QtCore.QRect(170, 570, 80, 24))
        self.pushButton_1.setObjectName("pushButton_1")
        self.graphicsView = QtWidgets.QGraphicsView(self.scene, self.tab_1)
        self.graphicsView.setGeometry(QtCore.QRect(200, 10, 181, 161))
        self.graphicsView.setObjectName("graphicsView")
        self.widget = QtWidgets.QWidget(self.tab_1)
        self.widget.setGeometry(QtCore.QRect(100, 180, 371, 281))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.username_1 = QtWidgets.QLineEdit(self.widget)
        self.username_1.setObjectName("username_1")
        self.gridLayout.addWidget(self.username_1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password_1 = QtWidgets.QLineEdit(self.widget)
        self.password_1.setObjectName("password_1")
        self.gridLayout.addWidget(self.password_1, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 570, 80, 24))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 570, 80, 24))
        self.pushButton_8.setObjectName("pushButton_8")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 180, 371, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.username_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.username_2.setObjectName("username_2")
        self.gridLayout_2.addWidget(self.username_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.password_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_2.setObjectName("password_2")
        self.gridLayout_2.addWidget(self.password_2, 1, 1, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.scene, self.tab_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(200, 10, 181, 161))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(login)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_1.clicked.connect(login.register)
        self.pushButton_2.clicked.connect(login.student_login)
        self.pushButton_7.clicked.connect(login.register)
        self.pushButton_8.clicked.connect(login.admin_login)
        self.graphicsView.show()
        self.graphicsView_2.show()
        QtCore.QMetaObject.connectSlotsByName(login)


    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "图书管理系统 design by @赵隽博@万彦楷@李宗睿"))
        self.pushButton_2.setText(_translate("login", "登录"))
        self.pushButton_1.setText(_translate("login", "注册"))
        self.label.setText(_translate("login", "账号："))
        self.label_2.setText(_translate("login", "密码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("login", "学生用户登录"))
        self.pushButton_7.setText(_translate("login", "注册"))
        self.pushButton_8.setText(_translate("login", "登录"))
        self.label_3.setText(_translate("login", "账号："))
        self.label_4.setText(_translate("login", "密码："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("login", "管理员用户登录"))