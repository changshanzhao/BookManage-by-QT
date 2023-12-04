import sys
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
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

    login = MainDialog()
    stu_register_Dlg = registerDialog("stu")
    adm_register_Dlg = registerDialog("adm")

    student_Win = StudentWindow()

    login.show()

    sys.exit(myapp.exec_())