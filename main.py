import sys
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt

import admin
import login
import register
import student

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QLineEdit, QMainWindow
from PyQt5 import QtWidgets
import pandas as pd

import datetime



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

    def closeEvent(self, event):
        event.ignore()
        if self.type == "stu":
            stu_register_Dlg.hide()
            login.show()
        else:
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

    def backbook(self):
        ISBN = self.ui.lineEdit_27.text()
        ID = self.ui.lineEdit_26.text()
        pass

class StudentWindow(QMainWindow):
    
    now_pattern = 'find'
    
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.find_way = "name"
        self.ui = student.Ui_student()
        self.ui.setupUi(self)
        

    
    #查找书函数
    def find_book(self, search_index, book_name=None, book_type = None, isbn=None, writer=None, pubdate=None):
        
        df = pd.read_excel('books.xlsx')  
        if book_name:
            row_index = df[df['书名'] == search_index].index.tolist()    
        elif book_type:
            row_index = df[df['类型'] == search_index].index.tolist() 
        elif isbn:
            row_index = df[df['ISBN号'] == search_index].index.tolist()
        elif writer:
            row_index = df[df['作者'] == search_index].index.tolist()
        elif pubdate:
            row_index = df[df['出版时间'] == search_index].index.tolist()
            
            
        if len(row_index)>0:  
            return row_index
        else:  
            return False
        
        
    def start_find(self):
        df = pd.read_excel('books.xlsx')
        text = self.ui.lineEdit.text()
        global book_row
        
        is_find = True
        if self.find_way == "name":
            row_index = self.find_book(text,book_name = True)
        elif self.find_way == "type":
            row_index = self.find_book(text,book_type = True)
        elif self.find_way == "ISBN":
            row_index = self.find_book(text,isbn = True)
        elif self.find_way == "time":
            row_index = self.find_book(text,pubdate = True)
        elif self.find_way == "au":
            row_index = self.find_book(text,writer = True)
            
        if row_index == False:
            is_find = False
            
        # 找到的图书像这样显示
        #若没找到图书，book_row = -1
        
        if is_find:
            book_row = row_index[0]
            item = self.ui.tableWidget.verticalHeaderItem(0)
            item.setText(df.loc[row_index[0],'书名'])
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 0, item)
            item = self.ui.tableWidget.item(0, 0)
            item.setText(str(df.loc[row_index[0],'ISBN号']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 1, item)
            item = self.ui.tableWidget.item(0, 1)
            item.setText(df.loc[row_index[0],'作者'])
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 2, item)
            item = self.ui.tableWidget.item(0, 2)
            item.setText(str(df.loc[row_index[0],'出版时间']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 3, item)
            item = self.ui.tableWidget.item(0, 3)
            item.setText(str(df.loc[row_index[0],'数量']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 4, item)
            item = self.ui.tableWidget.item(0, 4)
            item.setText(str(df.loc[row_index[0],'标价']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 5, item)
            item = self.ui.tableWidget.item(0, 5)
            item.setText(str(df.loc[row_index[0],'可借阅时间']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 6, item)
            item = self.ui.tableWidget.item(0, 6)
            item.setText(str(df.loc[row_index[0],'可借阅数量']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 7, item)
            item = self.ui.tableWidget.item(0, 7)
            item.setText(df.loc[row_index[0],'库存书架号'])
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(0, 8, item)
            item = self.ui.tableWidget.item(0, 8)
            item.setText(df.loc[row_index[0],'类型'])
        else:
            QMessageBox.warning(None, "查找失败", "未找到相关图书", QMessageBox.Ok)
            book_row = -1


    #借书
    def borrow(self):
        name = self.ui.lineEdit.text()
        self.ui.pushButton.setText("确认借阅")
        
        #按钮的功能转换
        if self.now_pattern == 'find':
            self.ui.pushButton.clicked.disconnect(self.start_find)
        elif self.now_pattern == 'borrow':
            self.ui.pushButton.clicked.disconnect(self.start_borrow)
        elif self.now_pattern == 'back':
            self.ui.pushButton.clicked.disconnect(self.start_back)
        elif self.now_pattern == 'longer':
            self.ui.pushButton.clicked.disconnect(self.start_longer)
            
        self.ui.pushButton.clicked.connect(self.start_borrow)
        now_pattern = 'borrow'
        

    def start_borrow(self, book_isbn):
        student = pd.read_excel('User_Message.xlsx')
        books = pd.read_excel('books.xlsx')
        date_after_30_days = datetime.date.today() + datetime.timedelta(days=30)
        global book_row 
        
        
        if int(books.loc[book_row,'可借阅数量']) < 1 and book_row != -1:
            QMessageBox.warning(None, "借阅失败", "该图书可借阅数量不足", QMessageBox.Ok)
        elif int(student.loc[student['账号'] == int(student_id),'可借阅数量']) < 1 and book_row != -1:
            QMessageBox.warning(None, "借阅失败", "您的借阅数量已到达上限", QMessageBox.Ok)
        elif book_row != -1:
            QMessageBox.warning(None, "借阅成功", "借阅成功！请于" + date_after_30_days.strftime("%Y-%m-%d") + "归还。", QMessageBox.Ok)
            books.loc[book_row,'可借阅数量'] -= 1
            books.to_excel('books.xlsx',index = False)
            student.loc[student['账号'] == int(student_id),'可借阅数量'] = int(student.loc[student['账号'] == int(student_id),'可借阅数量']) - 1
            student.loc[student['账号'] == int(student_id),'借阅列表'] = student.loc[student['账号'] == int(student_id),'借阅列表'].astype('str') + ' ' + str(books.loc[book_row,'ISBN号'])
            student.loc[student['账号'] == int(student_id),'还书时间'] = student.loc[student['账号'] == int(student_id),'还书时间'].astype('str') + ' ' + str(date_after_30_days.strftime("%Y-%m-%d"))
            student.to_excel('User_Message.xlsx',index=False)
        


    #还书
    def back(self):
        name = self.ui.lineEdit.text()
        self.ui.pushButton.setText("确认归还")
        self.ui.pushButton.clicked.disconnect(None)
        self.ui.pushButton.clicked.connect(self.start_back)

    def start_back(self):
        pass

    #续借
    def longer(self):
        name = self.ui.lineEdit.text()
        self.ui.pushButton.setText("确认续借")
        self.ui.pushButton.clicked.disconnect(None)
        self.ui.pushButton.clicked.connect(self.start_longer)

    def start_longer(self):
        pass

    #查借阅记录
    def history(self):
        student = pd.read_excel('User_Message.xlsx')
        books = pd.read_excel('books.xlsx')
        # 类似查找的展示方法
        i = 0
        book_list = student.loc[student['账号'] == student_id,'借阅列表'].split(' ')
        print(book_list)
        for book_isbn in book_list:
            row_index = self.find_book(book_isbn, book_isbn = True)
            item = self.ui.tableWidget.verticalHeaderItem(0)
            item.setText(books.loc[row_index[0],'书名'])
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(i, 0, item)
            item = self.ui.tableWidget.item(0, 0)
            item.setText(str(books.loc[row_index[0],'ISBN号']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(i, 1, item)
            item = self.ui.tableWidget.item(0, 1)
            item.setText(books.loc[row_index[0],'作者'])
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(i, 2, item)
            item = self.ui.tableWidget.item(0, 2)
            item.setText(str(books.loc[row_index[0],'出版时间']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(i, 3, item)
            item = self.ui.tableWidget.item(0, 3)
            item.setText(str(books.loc[row_index[0],'数量']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(i, 4, item)
            item = self.ui.tableWidget.item(0, 4)
            item.setText(str(books.loc[row_index[0],'标价']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(i, 5, item)
            item = self.ui.tableWidget.item(0, 5)
            item.setText(str(books.loc[row_index[0],'可借阅时间']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(i, 6, item)
            item = self.ui.tableWidget.item(0, 6)
            item.setText(str(books.loc[row_index[0],'可借阅数量']))
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(i, 7, item)
            item = self.ui.tableWidget.item(0, 7)
            item.setText(books.loc[row_index[0],'库存书架号'])
            item = QtWidgets.QTableWidgetItem()
            self.ui.tableWidget.setItem(i, 8, item)
            item = self.ui.tableWidget.item(0, 8)
            item.setText(books.loc[row_index[0],'类型'])
            i += 1




    def find_name(self):
        self.ui.label_2.setText("请输入要找的图书名称：")
        self.find_way = "name"
        self.ui.pushButton.setText("开始查找")
        self.ui.pushButton.clicked.disconnect(None)
        self.ui.pushButton.clicked.connect(self.start_find)

    def find_type(self):
        self.ui.label_2.setText("请输入要找的图书类型：")
        self.find_way = "type"
        self.ui.pushButton.setText("开始查找")
        self.ui.pushButton.clicked.disconnect(None)
        self.ui.pushButton.clicked.connect(self.start_find)

    def find_ISBN(self):
        self.ui.label_2.setText("请输入要找的图书ISBN：")
        self.find_way = "ISBN"
        self.ui.pushButton.setText("开始查找")
        self.ui.pushButton.clicked.disconnect(None)
        self.ui.pushButton.clicked.connect(self.start_find)

    def find_time(self):
        self.ui.label_2.setText("请输入要找图书的出版时间：")
        self.find_way = "time"
        self.ui.pushButton.setText("开始查找")
        self.ui.pushButton.clicked.disconnect(None)
        self.ui.pushButton.clicked.connect(self.start_find)

    def find_au(self):
        self.ui.label_2.setText("请输入要找图书的作者：")
        self.find_way = "au"
        self.ui.pushButton.setText("开始查找")
        self.ui.pushButton.clicked.disconnect(None)
        self.ui.pushButton.clicked.connect(self.start_find)


class MainDialog(QDialog):

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = login.Ui_login()
        self.ui.setupUi(self)

    # 学生登录判断，可登录返回True，否则返回False
    def student_can_login(self, username, password):
        is_right = False
        df = pd.read_excel('User_Message.xlsx')
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
        global student_id
        student_id = usrname
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