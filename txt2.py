import xlwt
workfile=xlwt.Workbook(encoding="encoding utf-8") #初始化，设置编码格式
table=workfile.add_sheet("table1")          #创建表
str=["A","B","C","D"]
for i in range(str.__len__()):
    table.write(0,i,str[i]) #在对应的位置写入数据
    workfile.save("qinhuan.xlsx") #保存并命名