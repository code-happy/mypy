import  xlrd


wrokfile=xlrd.open_workbook("qinhuan.xlsx")
wrokfile.sheet_names()
table=wrokfile.sheet_by_index(0) #通过索引获取工作表

for i in range(table.nrows): #table.nrows表示获取行数
    print(table.row_values(i))