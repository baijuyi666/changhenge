# -*- coding:utf-8 -*-
# @Time:  2020/1/7 16:30
# @Author:  wangyangyang
# @Email:  1976572326@qq.com
# @Filename:  Read_excel.py
# @Software:  PyCharm
# 写一个读取Excel内容的类，最终读到的是一个多字典集合的list
import xlrd


class ExcelData():
    def __init__(self,Excelpath,sheetname):  # 初始化表
        self.Excelpath=Excelpath
        self.sheetname=sheetname
        self.data=xlrd.open_workbook(self.Excelpath)  # 打开表
        self.table=self.data.sheet_by_name(self.sheetname)  # 打开工作簿
        self.key=self.table.row_values(0)  # 获取第一行的所用内容，做key值;使用xlrd获取行数和列表类似，从0开始是第一行
        self.nrows=self.table.nrows  # 获取总行数
        self.ncols=self.table.ncols  # 获取总列数

    def ReadExcel(self):  # 定义一个读取Excel的方法
        sheetlist=[]  # 定义一个空列表，用于写进字典用
        for i in range(1,self.nrows):
            sheetdict={}  # 定义一个空字典
            for j in range(self.ncols):
                cell=self.table.cell_value(i,j)  # 获取value值
                sheetdict[self.key[j]]=cell  # 循环写进字典中，key与value一一对应
            sheetlist.append(sheetdict)  # 字典写进列表中
        return sheetlist


if __name__=='__main__':
    Excelpath='E:\\练习python获取Excel内容.xlsx'
    sheetname='学生表'
    get_data=ExcelData(Excelpath,sheetname).ReadExcel()
    print(get_data)



