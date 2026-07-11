import numpy as np 
a=np.array([[10,20,30],
            [40,50,60],
            [70,80,90]])

1
###indexing元素，先row再column
# print(a[0,1])
# print(a[0])#row
# print(a[:,0])#column

2
###slicing
# print(a[1:2])
# print(a[:,1:])#取右两列
# print(a[:,:2])#取左两列

3
###修改元素,numpy can be reset directly
# a[1,1]=999
# print(a)

4
###boolean indexing
# A=np.array([10,20,30,40,50])
# print(A>25)
# print(A[A>25])
