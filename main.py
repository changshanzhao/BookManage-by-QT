import sys
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

import admin
import login
import register
import student

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit, QMainWindow
import pandas as pd



class registerDialog(QDialog):

    def __init__(self, type, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = register.Ui_register()
        self.type = type
        self.ui.setupUi(self)
        if type == "stu":
            self.ui.label_5.hide()
            self.ui.lineEdit_5.hide()

    # 学生注册检测，全部合法返回True，否则返回False
    def student_can_register(self, usrname, id, password, re_password):
        # 检测id是否合法
        if not (len(id) == 8 and id.isdigit()):
            QMessageBox.warning(None, "注册失败", "账号不合法！，请输入学号", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.lineEdit_2.clear()
            return False


        # 检测密码与确认密码是否相同
        elif password != re_password:
            QMessageBox.warning(None, "注册失败", "密码与确认密码不同！，请重新输入", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            return False


        # 检测密码是否安全（大于8位且包含字母和数字）
        elif len(password) < 8 or not any(char.isalpha() for char in password) or not any(
                char.isdigit() for char in password):
            QMessageBox.warning(None, "注册失败", "密码不安全！，请输入大于8位数且包含数字和字母的密码", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            return False

        else:
            # 存入Excel
            QMessageBox.warning(None, "注册成功", "注册成功！", QMessageBox.Ok)
            df = pd.read_excel('User_Message.xlsx', sheet_name='Student')
            new_data = {'用户名': usrname, '账号': id, '密码': password}
            df = df.append(new_data, ignore_index=True)
            df.to_excel('User_Message.xlsx', index=False, sheet_name='Student')

            # 清除文本内容
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            return True
    # 学生注册检测，全部合法返回True，否则返回False
    def admin_can_register(self, usrname, id, password, re_password, ps):
        # 检测id是否合法
        if not (len(id) == 8 and id.isdigit()):
            QMessageBox.warning(None, "注册失败", "账号不合法！，请输入学号", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.lineEdit_2.clear()
            return False

        # 检测密码与确认密码是否相同
        elif password != re_password:
            QMessageBox.warning(None, "注册失败", "密码与确认密码不同！，请重新输入", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            return False


        # 检测密码是否安全（大于8位且包含字母和数字）
        elif len(password) < 8 or not any(char.isalpha() for char in password) or not any(
                char.isdigit() for char in password):
            QMessageBox.warning(None, "注册失败", "密码不安全！，请输入大于8位数且包含数字和字母的密码", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            return False

        elif ps != "admin":
            QMessageBox.warning(None, "注册失败", "管理员安全密码不正确！", QMessageBox.Ok)
            self.ui.lineEdit_5.clear()
            return False

        else:
            # 存入Excel
            QMessageBox.warning(None, "注册成功", "注册成功！", QMessageBox.Ok)
            df = pd.read_excel('Admin_Message.xlsx', sheet_name='Administrator')
            new_data = {'用户名': usrname, '账号': id, '密码': password}
            df = df.append(new_data, ignore_index=True)
            df.to_excel('Admin_Message.xlsx', index=False, sheet_name='Administrator')

            # 清除文本内容
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            return True


    def reg(self):
        usrname = self.ui.lineEdit.text()
        id = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit_3.text()
        re_password = self.ui.lineEdit_4.text()
        ps = self.ui.lineEdit_5.text()
        if self.type == "stu":
            if self.student_can_register(usrname, id, password, re_password):
                stu_register_Dlg.hide()
                login.show()
        else:
            if self.admin_can_register(usrname, id, password, re_password, ps):
                adm_register_Dlg.hide()
                login.show()

class adminDialog(QDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = admin.Ui_admin()
        self.ui.setupUi(self)
    # 增加图书
    def addbook(self):
        titel = self.ui.lineEdit.text()
        ISBN = self.ui.lineEdit_2.text()
        au = self.ui.lineEdit_3.text()
        time = self.ui.lineEdit_4.text()
        num = self.ui.lineEdit_5.text()
        money = self.ui.lineEdit_6.text()
        j_time = self.ui.lineEdit_7.text()
        left_num = self.ui.lineEdit_8.text()
        topic = self.ui.lineEdit_9.text()
        pass
    # 修改密码
    def change_pass(self):
        ID = self.ui.lineEdit_19.text()
        name = self.ui.lineEdit_20.text()
        password = self.ui.label_21.text()
        re_password = self.ui.lineEdit_22.text()
        pass
    # 修改借阅信息
    def change_msg(self):
        time = self.ui.lineEdit_23.text()
        num = self.ui.lineEdit_24.text()
        pass

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
        elif self.find_way == "time":
            pass
        elif self.find_way == "au":
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

    def borrow(self):
        name = self.ui.lineEdit.text()
        self.ui.pushButton.setText("确认借阅")
        self.ui.pushButton.clicked.connect(self.start_borrow)

    def start_borrow(self):
        pass

    def back(self):
        name = self.ui.lineEdit.text()
        self.ui.pushButton.setText("确认归还")
        self.ui.pushButton.clicked.connect(self.start_back)

    def start_back(self):
        pass

    def longer(self):
        self.ui.label_3.show()
        self.ui.lineEdit_2.show()
        name = self.ui.lineEdit.text()
        time = self.ui.lineEdit_2.text()
        self.ui.pushButton.setText("确认续借")
        self.ui.pushButton.clicked.connect(self.start_longer)

    def start_longer(self):
        pass

    def history(self):
        # 类似查找的展示方法
        pass

    def find_name(self):
        self.ui.label_2.setText("请输入要找的图书名称：")
        self.find_way = "name"

    def find_type(self):
        self.ui.label_2.setText("请输入要找的图书类型：")
        self.find_way = "type"

    def find_ISBN(self):
        self.ui.label_2.setText("请输入要找的图书ISBN：")
        self.find_way = "ISBN"

    def find_time(self):
        self.ui.label_2.setText("请输入要找图书的出版时间：")
        self.find_way = "time"

    def find_au(self):
        self.ui.label_2.setText("请输入要找图书的作者：")
        self.find_way = "au"


class MainDialog(QDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = login.Ui_login()
        self.ui.setupUi(self)

    # 学生登录判断，可登录返回True，否则返回False
    def student_can_login(self, username, password):
        is_right = False
        df = pd.read_excel('User_Message.xlsx', sheet_name='Student')
        # 遍历账号密码
        for index, row in df.iterrows():
            username_al = str(row['账号'])
            password_al = str(row['密码'])

            # 判断账号密码是否相同
            if username == username_al and password == password_al:
                is_right = True
                break

        return is_right

    # 管理员登录判断，可登录返回True，否则返回False
    def admin_can_login(self, username, password):
        is_right = False
        df = pd.read_excel('Admin_Message.xlsx', sheet_name='Administrator')
        # 遍历账号密码
        for index, row in df.iterrows():
            username_al = str(row['账号'])
            password_al = str(row['密码'])

            # 判断账号密码是否相同
            if username == username_al and password == password_al:
                is_right = True
                break

        return is_right

    def student_register(self):
        login.hide()
        stu_register_Dlg.show()

    def admin_register(self):
        login.hide()
        adm_register_Dlg.show()


    def student_login(self):
        usrname = self.ui.username_1.text()
        password = self.ui.password_1.text()
        is_right = self.student_can_login(usrname, password)
        if is_right:
            student_Win.show()
            login.hide()

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

        is_right = self.admin_can_login(usrname, password)

        if is_right:
            admin_Dlg.show()
            login.hide()
        else:
            QMessageBox.warning(None, "登录失败", "用户名或密码输入错误！", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.username_2.clear()
            self.ui.password_2.clear()

            # 设置焦点
            self.ui.username_2.setFocus()


if __name__ == '__main__':

    myapp = QApplication(sys.argv)

    login = MainDialog()
    stu_register_Dlg = registerDialog("stu")
    adm_register_Dlg = registerDialog("adm")

    student_Win = StudentWindow()
    admin_Dlg = adminDialog()

    login.show()

    sys.exit(myapp.exec_())