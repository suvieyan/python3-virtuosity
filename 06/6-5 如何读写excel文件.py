"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/8/16'
"""

import xlrd, xlwt

rbook = xlrd.open_workbook('test.xlsx')  # 一个文件就是一个workbook
# rbook.sheets()  # 所有的表
rsheet = rbook.sheet_by_index(0)


k = rsheet.ncols  # 多少列
rsheet.put_cell(0, k, xlrd.XL_CELL_TEXT, '总分', None)  # 添加表头

for i in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(i, 1))  # row的每一行的，从第一列开始
    rsheet.put_cell(i, k, xlrd.XL_CELL_NUMBER, t, None)  # 每一行添加一列，类型，，总分，值


#  写入值
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)  # 传入值

for i in range(rsheet.nrows):
    for j in range(rsheet.ncols):
        # 写入的行坐标、列坐标、值
        wsheet.write(i, j, rsheet.cell_value(i, j))

wbook.save('out.xlsx')
