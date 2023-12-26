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

    def closeEvent(self, event):
        event.ignore()
        if self.type == "stu":
            stu_register_Dlg.hide()
            login.show()
        else:
            adm_register_Dlg.hide()
            login.show()

    # 学生注册检测，全部合法返回True，否则返回False
    def student_can_register(self, usrname, id, password, re_password):
        
        student = pd.read_excel('User_Message.xlsx')
        student_list = student['账号'].tolist()

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
        elif len(password) < 8 or not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
            QMessageBox.warning(None, "注册失败", "密码不安全！，请输入大于8位数且包含数字和字母的密码", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            return False
        
        # 检测是否已注册过
        elif int(id) in student_list:
            QMessageBox.warning(None, "注册失败", "您的账号已注册，请勿重复注册", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            return False
        else:
            # 存入Excel
            QMessageBox.warning(None, "注册成功", "注册成功！", QMessageBox.Ok)
            df = pd.read_excel('User_Message.xlsx')
            new_data = {'用户名': usrname, '账号': id, '密码': password, '可借阅数量': 5}
            df = df.append(new_data, ignore_index=True)
            df.to_excel('User_Message.xlsx', index=False)

            # 清除文本内容
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            return True
        
    # 管理员注册检测，全部合法返回True，否则返回False
    def admin_can_register(self, usrname, id, password, re_password, ps):
        
        admin = pd.read_excel('Admin_Message.xlsx')
        admin_list = admin['账号'].tolist()
        
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
        
        # 检测是否已注册过
        elif int(id) in admin_list:
            QMessageBox.warning(None, "注册失败", "您的账号已注册，请勿重复注册", QMessageBox.Ok)
            # 清空文本框内容
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
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
        
    def start_back(self,student_id,isbn):
        student = pd.read_excel('User_Message.xlsx')
        books = pd.read_excel('books.xlsx')
        today_date = datetime.date.today()
      
        #变量类型适配
        if student.loc[student['账号'] == int(student_id), '借阅列表'].isnull().to_string().split()[1] == 'True':
            book_list = []
            return_time_list = []
        else:
            book_list = student.loc[student['账号'] == int(student_id), '借阅列表'].str.split(' ').tolist()[0]            
            student.loc[student['账号'] == int(student_id), '还书时间'] = student.loc[student['账号'] == int(student_id), '还书时间'].astype('str')
            return_time_list = str(student.loc[student['账号'] == int(student_id),'还书时间'][0]).split(' ')            
        book_row = -1
        book_row = self.find_book(isbn,isbn = True)
            
        if book_row == -1:
            QMessageBox.warning(None, "还书失败", "请先查找图书再还书", QMessageBox.Ok)
        elif book_list == []:
            QMessageBox.warning(None, "还书失败", "您的借阅列表为空", QMessageBox.Ok)
        else:
            list_index = -1
            for i in range(len(book_list)):
                if isbn == book_list[i]:
                    list_index = i
                    break           
            return_time = return_time_list[list_index]
            
            if list_index == -1:
                QMessageBox.warning(None, "还书失败", "在您的借阅列表中未找到该书", QMessageBox.Ok)
            elif datetime.datetime.strptime(return_time, '%Y-%m-%d').date() < today_date:
                QMessageBox.warning(None, "还书失败", "您已超过还书时间，请联系管理员进行还书", QMessageBox.Ok)
            else:
                books.loc[book_row,'可借阅数量'] += 1
                books.to_excel('books.xlsx',index = False)
                book_list.pop(list_index)
                return_time_list.pop(list_index)
                student.loc[student['账号'] == int(student_id),'可借阅数量'] = int(student.loc[student['账号'] == int(student_id),'可借阅数量']) + 1
                student.loc[student['账号'] == int(student_id), '借阅列表'] = ' '.join(book_list)  
                student.loc[student['账号'] == int(student_id), '还书时间'] = ' '.join(return_time_list)
                student.to_excel('User_Message.xlsx', index=False)
                QMessageBox.warning(None, "还书成功", "还书成功！", QMessageBox.Ok)

    def tianjiashu(self, title, ISBN, au, time, num, money, j_time, left_num, snum,topic):
        df = pd.read_excel('books.xlsx')
        new_book_data = {
            '书名': title,
            'ISBN号': ISBN,
            '作者': au,
            '出版时间': time,
            '数量': num,
            '标价': money,
            '可借阅时间': j_time,
            '可借阅数量':left_num,
            '库存书架号': snum,
            '类型': topic,
        }
        new_book_df = pd.DataFrame(new_book_data, index=[0])
        df = pd.concat([df, new_book_df], ignore_index=True)
        df.to_excel('books.xlsx', index=False)

    def xiugaixueshengxinxi(self,number, password , re_password):  # 修改学生的密码，输入学号和新密码
        if password != re_password:
            QMessageBox.warning(None, "修改密码失败", "密码与确认密码不同！，请重新输入", QMessageBox.Ok)
        else:
            dfu = pd.read_excel('User_Message.xlsx')
            dfu.loc[dfu['账号'] == int(number), '密码'] = password
            dfu.to_excel('User_Message.xlsx', index=False)
            QMessageBox.warning(None, "修改密码成功", "密码修改成功", QMessageBox.Ok)

    def find_book(self, search_index, book_name=None, book_type=None, isbn=None, writer=None, pubdate=None):
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

        if len(row_index) > 0:
            return row_index[0]
        else:
            return False

    def xiugaishujixinxi(self,row, available_time=None, available_number=None):
        df = pd.read_excel('books.xlsx')
        if available_time !="":
            df.loc[row, '可借阅时间'] = available_time
            df.to_excel('books.xlsx', index=False)
            QMessageBox.warning(None, "修改成功", "成功修改可借阅时间", QMessageBox.Ok)
        if available_number !="":
            if int(available_number) <= int(df.loc[row, '数量']):
                df.loc[row, '可借阅数量'] = available_number
                df.to_excel('books.xlsx', index=False)
                QMessageBox.warning(None, "修改成功", "成功修改可借阅数量", QMessageBox.Ok)
            else:
                QMessageBox.warning(None, "修改失败", "超出已有数量", QMessageBox.Ok)

    # 增加图书
    def addbook(self):
        title = self.ui.lineEdit.text()
        ISBN = self.ui.lineEdit_2.text()
        au = self.ui.lineEdit_3.text()
        time = self.ui.lineEdit_4.text()
        num = self.ui.lineEdit_5.text()
        money = self.ui.lineEdit_6.text()
        j_time = self.ui.lineEdit_7.text()
        left_num = self.ui.lineEdit_8.text()
        topic = self.ui.lineEdit_9.text()
        snum = self.ui.lineEdit_10.text()
        self.tianjiashu(title, ISBN, au, time, num, money, j_time, left_num, snum, topic)
        pass
    # 修改密码
    def change_pass(self):
        number = self.ui.lineEdit_19.text()
        password = self.ui.lineEdit_21.text()
        re_password = self.ui.lineEdit_22.text()
        self.xiugaixueshengxinxi(number, password , re_password)
        pass
    # 修改借阅信息
    def change_msg(self):
        available_time = self.ui.lineEdit_23.text()
        available_number = self.ui.lineEdit_24.text()
        isbn = self.ui.lineEdit_25.text()
        row = self.find_book(isbn,isbn=True)
        print('row:',row)
        print('isbn:',isbn)
        if row is not False:
            self.xiugaishujixinxi(row, available_time=available_time, available_number=available_number)
        else:
            QMessageBox.warning(None, "修改失败", "找不到匹配的图书", QMessageBox.Ok)
        pass
    def backbook(self):
        isbn = self.ui.lineEdit_27.text()
        student_id = self.ui.lineEdit_26.text()
        self.start_back(student_id,isbn)
        
        pass

class StudentWindow(QMainWindow):
    
    
    
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.find_way = "name"
        self.ui = student.Ui_student()
        self.ui.setupUi(self)
        self.book_row = -1
        self.now_pattern = 'find'

    
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
        books = pd.read_excel('books.xlsx')
        text = self.ui.lineEdit.text()
        
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
            
        print(row_index)
        # 找到的图书像这样显示
        #若没找到图书，book_row = -1
        
        if is_find:
            #清除原有数据
            self.ui.tableWidget.clearContents()
            
            for i in range(len(row_index)):
                self.book_row = row_index[i]
                
                # 设置标题列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(books.loc[self.book_row,'书名'])  
                self.ui.tableWidget.setItem(i, 0, item)  # 使用正确的行索引i  
                  
                # 设置ISBN列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[self.book_row,'ISBN号']))  
                self.ui.tableWidget.setItem(i, 1, item)  # 使用正确的行索引i  
                  
                # 设置作者列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(books.loc[self.book_row,'作者'])  
                self.ui.tableWidget.setItem(i, 2, item)  # 使用正确的行索引i  
                  
                # 设置出版时间列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[self.book_row,'出版时间']))  
                self.ui.tableWidget.setItem(i, 3, item)  # 使用正确的行索引i  
                  
                # 设置数量列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[self.book_row,'数量']))  
                self.ui.tableWidget.setItem(i, 4, item)  # 使用正确的行索引i  
                  
                # 设置标价列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[self.book_row,'标价']))  
                self.ui.tableWidget.setItem(i, 5, item)  # 使用正确的行索引i  
                  
                # 设置可借阅时间列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[self.book_row,'可借阅时间']))  
                self.ui.tableWidget.setItem(i, 6, item)  # 使用正确的行索引i
                
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[self.book_row,'可借阅数量']))  
                self.ui.tableWidget.setItem(i, 7, item)  # 使用正确的行索引i
                
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[self.book_row,'库存书架号']))  
                self.ui.tableWidget.setItem(i, 8, item)  # 使用正确的行索引i
                
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[self.book_row,'类型']))  
                self.ui.tableWidget.setItem(i, 9, item)  # 使用正确的行索引i
            


        else:
            QMessageBox.warning(None, "查找失败", "未找到相关图书", QMessageBox.Ok)
            self.book_row = -1


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
        self.now_pattern = 'borrow'
        

    def start_borrow(self):
        student = pd.read_excel('User_Message.xlsx')
        books = pd.read_excel('books.xlsx')
        date_after_30_days = datetime.date.today() + datetime.timedelta(days=30)

        
        #变量类型适配
        if student.loc[student['账号'] == int(student_id), '借阅列表'].isnull().to_string().split()[1] == 'True':
            book_list = []
        else:
            book_list = student.loc[student['账号'] == int(student_id), '借阅列表'].str.split(' ').tolist()[0]
        
        
        if self.book_row == -1:
            QMessageBox.warning(None, "借阅失败", "请先查找图书再借阅", QMessageBox.Ok)
        else:           
            isbn = str(books.loc[self.book_row, 'ISBN号'])
            if int(books.loc[self.book_row,'可借阅数量']) < 1 and self.book_row != -1:
                QMessageBox.warning(None, "借阅失败", "该图书可借阅数量不足", QMessageBox.Ok)
            elif int(student.loc[student['账号'] == int(student_id),'可借阅数量']) < 1 and self.book_row != -1:
                QMessageBox.warning(None, "借阅失败", "您的借阅数量已到达上限", QMessageBox.Ok)
            elif isbn in book_list:
                QMessageBox.warning(None, "借阅失败", "您已借阅该书，请勿重复借阅！", QMessageBox.Ok)
            elif self.book_row != -1:
                QMessageBox.warning(None, "借阅成功", "借阅成功！请于" + date_after_30_days.strftime("%Y-%m-%d") + "前归还。", QMessageBox.Ok)
                books.loc[self.book_row,'可借阅数量'] -= 1
                books.to_excel('books.xlsx',index = False)
                student.loc[student['账号'] == int(student_id),'可借阅数量'] = int(student.loc[student['账号'] == int(student_id),'可借阅数量']) - 1
                if book_list == []:
                    student.loc[student['账号'] == int(student_id),'借阅列表'] = str(books.loc[self.book_row,'ISBN号'])
                    student.loc[student['账号'] == int(student_id),'还书时间'] = str(date_after_30_days.strftime("%Y-%m-%d"))
                else:                    
                    student.loc[student['账号'] == int(student_id),'借阅列表'] = student.loc[student['账号'] == int(student_id),'借阅列表'].astype('str') + ' ' + str(books.loc[self.book_row,'ISBN号'])
                    student.loc[student['账号'] == int(student_id),'还书时间'] = student.loc[student['账号'] == int(student_id),'还书时间'].astype('str') + ' ' + str(date_after_30_days.strftime("%Y-%m-%d"))
                student.to_excel('User_Message.xlsx',index=False)
        


    #还书
    def back(self):
        name = self.ui.lineEdit.text()
        self.ui.pushButton.setText("确认归还")
        
        #按钮的功能转换
        if self.now_pattern == 'find':
            self.ui.pushButton.clicked.disconnect(self.start_find)
        elif self.now_pattern == 'borrow':
            self.ui.pushButton.clicked.disconnect(self.start_borrow)
        elif self.now_pattern == 'back':
            self.ui.pushButton.clicked.disconnect(self.start_back)
        elif self.now_pattern == 'longer':
            self.ui.pushButton.clicked.disconnect(self.start_longer)
            
        self.ui.pushButton.clicked.connect(self.start_back)
        self.now_pattern = 'back'

    def start_back(self):
        student = pd.read_excel('User_Message.xlsx')
        books = pd.read_excel('books.xlsx')
        today_date = datetime.date.today()
      
        #变量类型适配
        if student.loc[student['账号'] == int(student_id), '借阅列表'].isnull().to_string().split()[1] == 'True':
            book_list = []
            return_time_list = []
        else:
            book_list = student.loc[student['账号'] == int(student_id), '借阅列表'].str.split(' ').tolist()[0]            
            student.loc[student['账号'] == int(student_id), '还书时间'] = student.loc[student['账号'] == int(student_id), '还书时间'].astype('str')
            return_time_list = str(student.loc[student['账号'] == int(student_id),'还书时间'][1]).split(' ')            

                
        if self.book_row == -1:
            QMessageBox.warning(None, "还书失败", "请先查找图书再还书", QMessageBox.Ok)
        elif book_list == []:
            QMessageBox.warning(None, "还书失败", "您的借阅列表为空", QMessageBox.Ok)
        else:
            list_index = -1
            isbn = books.loc[self.book_row, 'ISBN号']
            for i in range(len(book_list)):
                if isbn == book_list[i]:
                    list_index = i
                    break           
            return_time = return_time_list[list_index]
            
            if list_index == -1:
                QMessageBox.warning(None, "还书失败", "在您的借阅列表中未找到该书", QMessageBox.Ok)
            elif datetime.datetime.strptime(return_time, '%Y-%m-%d').date() < today_date:
                QMessageBox.warning(None, "还书失败", "您已超过还书时间，请联系管理员进行还书", QMessageBox.Ok)
            else:
                books.loc[self.book_row,'可借阅数量'] += 1
                books.to_excel('books.xlsx',index = False)
                book_list.pop(list_index)
                return_time_list.pop(list_index)
                student.loc[student['账号'] == int(student_id),'可借阅数量'] = int(student.loc[student['账号'] == int(student_id),'可借阅数量']) + 1
                student.loc[student['账号'] == int(student_id), '借阅列表'] = ' '.join(book_list)  
                student.loc[student['账号'] == int(student_id), '还书时间'] = ' '.join(return_time_list)
                student.to_excel('User_Message.xlsx', index=False)
                QMessageBox.warning(None, "还书成功", "还书成功！", QMessageBox.Ok)

    #续借
    def longer(self):
        name = self.ui.lineEdit.text()
        self.ui.pushButton.setText("确认续借")
        
        #按钮的功能转换
        if self.now_pattern == 'find':
            self.ui.pushButton.clicked.disconnect(self.start_find)
        elif self.now_pattern == 'borrow':
            self.ui.pushButton.clicked.disconnect(self.start_borrow)
        elif self.now_pattern == 'back':
            self.ui.pushButton.clicked.disconnect(self.start_back)
        elif self.now_pattern == 'longer':
            self.ui.pushButton.clicked.disconnect(self.start_longer)  
            
        self.ui.pushButton.clicked.connect(self.start_longer)
        self.now_pattern = 'longer'

    def start_longer(self):
        student = pd.read_excel('User_Message.xlsx')
        books = pd.read_excel('books.xlsx')
        today_date = datetime.date.today()
        #变量类型适配
        if student.loc[student['账号'] == int(student_id), '借阅列表'].isnull().to_string().split()[1] == 'True':
            book_list = []
            return_time_list = []
        else:
            book_list = student.loc[student['账号'] == int(student_id), '借阅列表'].str.split(' ').tolist()[0]            
            student.loc[student['账号'] == int(student_id), '还书时间'] = student.loc[student['账号'] == int(student_id), '还书时间'].astype('str')
            return_time_list = str(student.loc[student['账号'] == int(student_id),'还书时间'][1]).split(' ')            
        
        if self.book_row == -1:
            QMessageBox.warning(None, "续借失败", "请先查找图书再续借", QMessageBox.Ok)
        elif book_list == []:
            QMessageBox.warning(None, "续借失败", "您的借阅列表为空", QMessageBox.Ok)
        else:
            list_index = -1
            isbn = books.loc[self.book_row, 'ISBN号']
            for i in range(len(book_list)):
                if isbn == book_list[i]:
                    list_index = i
                    break           
            return_time = return_time_list[list_index]
            if list_index == -1:
                QMessageBox.warning(None, "续借失败", "在您的借阅列表中未找到该书", QMessageBox.Ok)
            elif datetime.datetime.strptime(return_time, '%Y-%m-%d').date() < today_date:
                QMessageBox.warning(None, "续借失败", "您已超过还书时间，请联系管理员进行续借", QMessageBox.Ok)
            elif today_date + datetime.timedelta(days=30) <= datetime.datetime.strptime(return_time, '%Y-%m-%d').date():
                QMessageBox.warning(None, "续借失败", "您已完成续借，请勿重复续借", QMessageBox.Ok)
            else:
                return_time_list[list_index] = datetime.datetime.strptime(return_time_list[list_index], '%Y-%m-%d').date() + datetime.timedelta(days=30)
                student.loc[student['账号'] == int(student_id), '借阅列表'] = ' '.join(book_list)  
                
                # 将return_time_list中的日期对象转换为字符串  
                for i in range(len(return_time_list)):  
                    return_time_list[i] = str(return_time_list[i])                   
                student.loc[student['账号'] == int(student_id), '还书时间'] = ' '.join(return_time_list)
                
                student.to_excel('User_Message.xlsx', index=False)
                QMessageBox.warning(None, "续借成功", "续借成功！请于" + str(return_time_list[list_index]) + "前归还。", QMessageBox.Ok)
        


    #查借阅记录
    def history(self):
        student = pd.read_excel('User_Message.xlsx')
        books = pd.read_excel('books.xlsx')
        
        
        #变量类型适配
        if student.loc[student['账号'] == int(student_id), '借阅列表'].isnull().to_string().split()[1] == 'True':
            book_list = []
            return_time_list = []
        else:
            book_list = student.loc[student['账号'] == int(student_id), '借阅列表'].str.split(' ').tolist()[0]            
            student.loc[student['账号'] == int(student_id), '还书时间'] = student.loc[student['账号'] == int(student_id), '还书时间'].astype('str')
            return_time_list = str(student.loc[student['账号'] == int(student_id),'还书时间'][1]).split(' ')
            
        if book_list == []:
            QMessageBox.warning(None, "查询失败", "您的借阅列表为空", QMessageBox.Ok)
        else:
            #清除原有数据
            self.ui.tableWidget.clearContents()
            for i in range(len(book_list)):  
                book_isbn = book_list[i]  
                row_index = self.find_book(book_isbn, isbn=True)  
                  
                # 设置标题列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(books.loc[row_index[0],'书名'])  
                self.ui.tableWidget.setItem(i, 0, item)  # 使用正确的行索引i  
                  
                # 设置ISBN列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[row_index[0],'ISBN号']))  
                self.ui.tableWidget.setItem(i, 1, item)  # 使用正确的行索引i  
                  
                # 设置作者列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(books.loc[row_index[0],'作者'])  
                self.ui.tableWidget.setItem(i, 2, item)  # 使用正确的行索引i  
                  
                # 设置出版时间列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[row_index[0],'出版时间']))  
                self.ui.tableWidget.setItem(i, 3, item)  # 使用正确的行索引i  
                  
                # 设置数量列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[row_index[0],'数量']))  
                self.ui.tableWidget.setItem(i, 4, item)  # 使用正确的行索引i  
                  
                # 设置标价列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[row_index[0],'标价']))  
                self.ui.tableWidget.setItem(i, 5, item)  # 使用正确的行索引i  
                  
                # 设置可借阅时间列  
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[row_index[0],'可借阅时间']))  
                self.ui.tableWidget.setItem(i, 6, item)  # 使用正确的行索引i
                
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[row_index[0],'可借阅数量']))  
                self.ui.tableWidget.setItem(i, 7, item)  # 使用正确的行索引i
                
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[row_index[0],'库存书架号']))  
                self.ui.tableWidget.setItem(i, 8, item)  # 使用正确的行索引i
                
                item = QtWidgets.QTableWidgetItem()  
                item.setText(str(books.loc[row_index[0],'类型']))  
                self.ui.tableWidget.setItem(i, 9, item)  # 使用正确的行索引i
                
                item = QtWidgets.QTableWidgetItem()  
                item.setText(return_time_list[i])  
                self.ui.tableWidget.setItem(i, 10, item)  # 使用正确的行索引i





    def find_name(self):
        self.ui.label_2.setText("请输入要找的图书名称：")
        self.find_way = "name"
        self.ui.pushButton.setText("开始查找")
        
        #按钮的功能转换
        if self.now_pattern == 'find':
            self.ui.pushButton.clicked.disconnect(self.start_find)
        elif self.now_pattern == 'borrow':
            self.ui.pushButton.clicked.disconnect(self.start_borrow)
        elif self.now_pattern == 'back':
            self.ui.pushButton.clicked.disconnect(self.start_back)
        elif self.now_pattern == 'longer':
            self.ui.pushButton.clicked.disconnect(self.start_longer)  
            
        self.ui.pushButton.clicked.connect(self.start_find)
        self.now_pattern = 'find'

    def find_type(self):
        self.ui.label_2.setText("请输入要找的图书类型：")
        self.find_way = "type"
        self.ui.pushButton.setText("开始查找")
        
        #按钮的功能转换
        if self.now_pattern == 'find':
            self.ui.pushButton.clicked.disconnect(self.start_find)
        elif self.now_pattern == 'borrow':
            self.ui.pushButton.clicked.disconnect(self.start_borrow)
        elif self.now_pattern == 'back':
            self.ui.pushButton.clicked.disconnect(self.start_back)
        elif self.now_pattern == 'longer':
            self.ui.pushButton.clicked.disconnect(self.start_longer)  
            
        self.ui.pushButton.clicked.connect(self.start_find)
        self.now_pattern = 'find'

    def find_ISBN(self):
        self.ui.label_2.setText("请输入要找的图书ISBN：")
        self.find_way = "ISBN"
        self.ui.pushButton.setText("开始查找")
        
        #按钮的功能转换
        if self.now_pattern == 'find':
            self.ui.pushButton.clicked.disconnect(self.start_find)
        elif self.now_pattern == 'borrow':
            self.ui.pushButton.clicked.disconnect(self.start_borrow)
        elif self.now_pattern == 'back':
            self.ui.pushButton.clicked.disconnect(self.start_back)
        elif self.now_pattern == 'longer':
            self.ui.pushButton.clicked.disconnect(self.start_longer)  
            
        self.ui.pushButton.clicked.connect(self.start_find)
        self.now_pattern = 'find'

    def find_time(self):
        self.ui.label_2.setText("请输入要找图书的出版时间：")
        self.find_way = "time"
        self.ui.pushButton.setText("开始查找")
        
        #按钮的功能转换
        if self.now_pattern == 'find':
            self.ui.pushButton.clicked.disconnect(self.start_find)
        elif self.now_pattern == 'borrow':
            self.ui.pushButton.clicked.disconnect(self.start_borrow)
        elif self.now_pattern == 'back':
            self.ui.pushButton.clicked.disconnect(self.start_back)
        elif self.now_pattern == 'longer':
            self.ui.pushButton.clicked.disconnect(self.start_longer)  
            
        self.ui.pushButton.clicked.connect(self.start_find)
        self.now_pattern = 'find'

    def find_au(self):
        self.ui.label_2.setText("请输入要找图书的作者：")
        self.find_way = "au"
        self.ui.pushButton.setText("开始查找")
        
        #按钮的功能转换
        if self.now_pattern == 'find':
            self.ui.pushButton.clicked.disconnect(self.start_find)
        elif self.now_pattern == 'borrow':
            self.ui.pushButton.clicked.disconnect(self.start_borrow)
        elif self.now_pattern == 'back':
            self.ui.pushButton.clicked.disconnect(self.start_back)
        elif self.now_pattern == 'longer':
            self.ui.pushButton.clicked.disconnect(self.start_longer)  
            
        self.ui.pushButton.clicked.connect(self.start_find)
        self.now_pattern = 'find'


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