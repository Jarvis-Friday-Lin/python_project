import numpy as np
from numpy.ma.core import shape

a = np.zeros((3, 3))
b = np.ones(a.shape)
print(b)

b = np.ones(shape(a))
print(shape(a))

print(b)


a.shape       # a这个对象的属性shape。这个shape是一个属性，对象的属性
np.shape(a)   # np是表示numpy库，表示的是numpy库里面的一个函数名叫做shape(),  调用numpy库里面的shape函数
shape(a)      # core里面函数shape


# 函数 跟 方法


def a():
    print(a)

class b:
    def ab(self):
        print("ab")

l = [1, 2, 3]
print(l[2:0:-1])
print(l[0:2:-1])

print(l[0:0:-1])
print(l[2:2:-1])

print(l[2:2])
print(l[0:0])
print(l[-1:-1])
print(l[4:4])   # npe

print(l[-1:-2])
print(l[-1:-2:-1])
print(l[-1:2])
l = [1, 2, 3]
print(l[-2:])
print(l[-3:])

# -1 :方向+步长
# 开始索引：找到开始索引的位置，然后根据方向找到结束索引的位置，然后打印


print = 1
del print
print(1)