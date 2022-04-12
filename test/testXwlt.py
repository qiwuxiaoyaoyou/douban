# -*- codeing = utf-8 -*-
# @Time : 2022-01-02 17:41
# @Author : 齐物逍遥游
# @File : testXwlt.py
# @Software: PyCharm

import xlwt
'''
workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
worksheet = workbook.add_sheet('sheet1')    #创建工作表
worksheet.write(0,0,'hello')                #写入数据，参数分别为（第几行、第几列、写入该单元格中的内容）
workbook.save('student.xls')                #保存数据表
'''

workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
worksheet = workbook.add_sheet('sheet1')    #创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')  # 保存数据表