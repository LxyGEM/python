'''一只青蛙一次只能跳一级或者两级台阶,青蛙跳到100级台阶有多少种跳法?'''
def jumpFloor(number):  #定义函数
    if number == 1 or number == 2:  #当台阶数为1或2时，方法数为本身
        return number
    a,b = 1,2  #不能在循环里
    for i in range(number-2):  #台阶数大于2时，方法数是前两项相加
        result = a + b
        a,b = b,result
    return result
print(jumpFloor(100))