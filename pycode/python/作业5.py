'''运用Monte Carno 方法计算圆周率的近似值'''
#蒙特卡罗方法：通过概率得到近似解
from random import random  #用于生成（0，1】的随机浮点数
times=int(input('输入投掷飞镖数'))
a = 0  #投到圆中的次数
for i in range(times):
    x=random()
    y=random()  #x,y取随机数
    if x*x + y*y <1:
        a+=1
print(4.0*a/times)