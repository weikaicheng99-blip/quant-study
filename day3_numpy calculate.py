import numpy as np
1
###muliply
a=np.array([100,200,300,400])
b=np.array([1.1,0.9,1.2,1.1])
print(a*b)
print(a+2)
print(a*2)
c=a*b
print(np.round(c[a*b>190],2))



2
###
returns=np.array([0.01,-0.02,0.03,0.04,-0.01])
#平均收益
np.mean(returns)
#最大收益
np.max(returns)
np.min(returns)
#标准差
np.std(returns)
#求和
np.sum(returns)


3
###使用axis
# scores=np.array([[80,90,70],
#                 [60,100,75],
#                 [90,95,88]])
# print(np.mean(scores))
# print(np.mean(scores,axis=1))#每一行的平均
# print(np.mean(scores,axis=0))#每一列的平均