'''法一：定义函数+for循环'''
def factorial(num):  #定义阶乘函数以及自变量
  a=1
  for i in range(1,num+1):  #for循环中range取不到结束值
    a*=i
  return a  #函数结果输出a
n = int(input())  #定义输入值
print(factorial(n))

'''法二：while函数+if else语句'''
n=int(input())
a=n  #不能直接用输入值
i=1
if a==0:
  print(1)
else:
  while i<n:  #if else while都要加：
    a*=i
    i+=1
  print(a)  #print位置与while平齐
  
'''法三：递归函数'''
def factorial(n):
  if n==0:
    return 1  #函数输出结果用return
  else:
    return factorial(n-1)*n  #递归函数
n=int(input())
print(factorial(n))

"""法三写法二"""
def factorial(n):
  return 1 if n<2 else factorial(n-1)*n  #三元运算表达式
n=int(input())
print(factorial(n))

'''法四：借助math库，使用math库的factorial方法'''
import math  #导入数学模块
def fact(num):
  return math.factorial(num)  #模块中阶乘函数
n=int(input())
print(fact(n))