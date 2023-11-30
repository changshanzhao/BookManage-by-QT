import sys
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
import login
import register
import student

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit, QMainWindow


class registerDialog(QDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = register.Ui_register()
        self.ui.setupUi(self)

    def reg(self):
        usrname = self.ui.lineEdit.text()
        id = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit_3.text()
        re_password = self.ui.lineEdit_4.text()
        # if password == re_password: # 看看用户是否已注册过啥的，你们加判断几个条件
        # 和账号有关的逻辑你们写吧，我直接转UI了
        register_Dlg.hide()
        myDlg.show()

class StudentWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.find_way = "name"
        self.ui = student.Ui_student()
        self.ui.setupUi(self)
    def start_find(self):
        text = self.ui.lineEdit.text()
        is_find = True
        if self.find_way == "name":
            # 按名称查找,pass占位，填完功能就把他删了
            pass
        elif self.find_way == "type":
            pass
        elif self.find_way == "ISBN":
            pass

        # 找到的图书像这样显示
        if is_find:
            item = self.ui.tableWidget.verticalHeaderItem(0)
            item.setText(text)
            item = self.ui.tableWidget.item(0, 0)
            item.setText("计算机")
            item = self.ui.tableWidget.item(0, 1)
            item.setText("111")
            item = self.ui.tableWidget.item(0, 2)
            item.setText("是")

    def find_name(self):
        self.ui.label_2.setText("请输入要找的图书名称：")
        self.find_way = "name"

    def find_type(self):
        self.ui.label_2.setText("请输入要找的图书类型：")
        self.find_way = "type"

    def find_ISBN(self):
        self.ui.label_2.setText("请输入要找的图书ISBN：")
        self.find_way = "ISBN"


class MainDialog(QDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = login.Ui_login()
        self.ui.setupUi(self)

    def register(self):
        myDlg.hide()
        register_Dlg.show()



    def student_login(self):
        usrname = self.ui.username_1.text()
        password = self.ui.password_1.text()
        '''
        这儿用数据库还是啥，你们看看
        得到一个是否能登录的标志
        is_right
        '''
        is_right = True
        if is_right:
            student_Win.show()
            myDlg.hide()

        else:
            QMessageBox.warning(None, "登录失败", "用户名或密码输入错误！", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.username_1.clear()
            self.ui.password_1.clear()

            # 设置焦点
            self.ui.username_1.setFocus()

    def admin_login(self):
        usrname = self.ui.username_2.text()
        password = self.ui.password_2.text()
        '''
        这儿用数据库还是啥，你们看看
        得到一个是否能登录的标志
        is_right
        '''
        is_right = False
        if is_right:
            pass
        else:
            QMessageBox.warning(None, "登录失败", "用户名或密码输入错误！", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.username_2.clear()
            self.ui.password_2.clear()

            # 设置焦点
            self.ui.username_2.setFocus()


if __name__ == '__main__':

    myapp = QApplication(sys.argv)

    myDlg = MainDialog()
    register_Dlg = registerDialog()
    student_Win = StudentWindow()


    myDlg.show()

    sys.exit(myapp.exec_())