'''法一：递归法'''
def jumpFloor(number):
    if number in(1,2):
        return number
    return jumpFloor(number-1) + jumpFloor(number-2)  #斐波那契数列
n = int(input())
print(jumpFloor(n))  #阶数过大会造成时间超限

'''法二：循环实现'''
def jumpFloor(number):  #定义函数
    if number == 1 or number == 2:  #当台阶数为1或2时，方法数为本身
        return number
    a,b = 1,2  #不能在循环里
    for i in range(number-2):  #台阶数大于2时，方法数是前两项相加
        result = a + b
        a,b = b,result
    return result
n = int(input())
print(jumpFloor(n))