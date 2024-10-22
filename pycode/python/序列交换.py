'''有两个序列a,b,大小都为n,序列元素的值任意整形数,无序,要求:通过交换a,b中的元素,使序列a元素的和与序列b元素的和之间的差最小。'''
import random
def min_diff(a, b):
    a_sum,b_sum= sum(a),sum(b)
    i,j=0,0
    while i<len(a) and j<len(b):
        if abs(a_sum-b_sum)>abs(a_sum-b_sum+2*(-a[i]+b[j])):  #如果交换后差值变小
            a_sum=a_sum-a[i]+b[j]
            b_sum=b_sum+a[i]-b[j]  #先改变和，再交换
            a[i],b[j]=b[j],a[i]
            i+=1
            j+=1  #交换后继续比较
        elif a[i]<b[j]:  #差值没有变小，那根据情况只移动i或j
            i+=1
        else:
            j+=1
    random.shuffle(a)
    random.shuffle(b)  #打乱顺序
def final(a,b):
    try:  #将输入的字符串转换为整数列表
        a = [int(x) for x in a.split(',')]
        b = [int(y) for y in b.split(',')]#split()将字符串分割成列表
    except ValueError:
        print("输入的序列格式不正确，请输入逗号分隔的整数序列。")
        return
    k=0
    for k in range(100):  #交换次数较大，防止局部最优解
        min_diff(a,b)
    a.sort()
    b.sort()  #从小到大排列
    print(a)
    print(b)
# 示例输入
x = input("输入序列x:")
y = input("输入序列y:")
final(x, y)