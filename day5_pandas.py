# 1
# ###dataFrame
# import pandas as pd
# prices = {
#     "Date": [
#         "2024-01-01",
#         "2024-01-02",
#         "2024-01-03",
#         "2024-01-04",
#         "2024-01-05",
#         "2024-01-08",
#         "2024-01-09"
#     ],
#     "Close": [
#         185,
#         188,
#         186,
#         191,
#         193,
#         192,
#         195
#     ]
# }#相当于一个dictionnary

# df = pd.DataFrame(prices)#搭建一个dataframe对象，相当于是一个表格excel
# print(df["Close"])#相当于单独把"Close"这一列拿出来，且只能取列，不能取行


# #有许多函数只能对dataframe对象使用，不能对numpy数组使用
# #虽然numpy数组和dataframe对象都可以进行数据分析，但dataframe对象更适合处理带有标签的数据，而numpy数组更适合处理数值计算。


# 2
# import pandas as pd

# student = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Math": [90, 85, 95],
#     "English": [88, 92, 80]
# }

# df = pd.DataFrame(student)
# df["total"]=df["Math"]+df["English"]
# df["Average"]=df["total"]/2
# print(df)#这里没有for loop，直接向量化,然后加在df的后面


# 3
# ###iloc(inter location)按照整数位置取数据
# import pandas as pd

# student = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Math": [90, 85, 95],
#     "English": [88, 92, 80]
# }

# df = pd.DataFrame(student)

# print(df.iloc[0])#取整行
# print(df.iloc[0,0])#行，列
# print(df.iloc[:,1])#变成取整列
# print(df.iloc[1:3,0:2])#取行和列的范围,包前不包后

# 4
# ###loc(label location)按照标签位置取数据
# import pandas as pd
# student = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Math": [90, 85, 95],
#     "English": [88, 92, 80]
# }

# df = pd.DataFrame(student)

# df=df.set_index("Name")#把"Name"这一列设置为索引（一般是设置date）这时候开头就是名字了
# print(df.loc["Alice"])#这里可以，因为loc是按照标签位置取数据的，而"Name"这一列已经被设置为索引了，所以可以用标签来取数据了。
# print(df.iloc["Alice"])#这里不行，因为iloc是按照整数位置取数据的，而"Name"这一列已经被设置为索引了，所以不能再用整数位置来取数据了。
# # 需求	用什么
# # 第5行	iloc
# # 第100行	iloc
# # Apple这一行	loc
# # 日期2024-01-01	loc
# # 股票代码AAPL	loc

# # 一句话：

# # 数字 → iloc，名字 → loc。


6
import pandas as pd

stock = {
    "Company": ["Apple", "Tesla", "NVIDIA"],
    "Price": [185, 250, 130],
    "PE": [28.5, 60.2, 72.1]
}

df = pd.DataFrame(stock)

# 然后完成下面 8 个任务（不要急着看答案）：

# 打印整个 DataFrame。
# 用 iloc 取出第二行。
# 用 iloc 取出第三行的 Price。
# 打印 PE 这一列。
# 把 Company 设置成索引。
# 用 loc 取出 Tesla 的整行。
# 用 loc 取出 Apple 的 Price。
# 思考：为什么第 6 题不能用 iloc["Tesla"]？
print(df)
print(df.iloc[1])
print(df.iloc[2,1])
print(df["PE"])#这里得到的是Series
df=df.set_index("Company")
print(df.loc["Tesla"])
print(df.loc["Apple","Price"])