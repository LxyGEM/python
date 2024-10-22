'''汉诺塔问题编程解答'''
def move(n,a,b,c):  #n为盘子的个数，a为初始塔，b为中间塔，c为目标塔
    if n == 1:   #如果只有一个盘子，直接将盘子从a移动到c
        print(a,"--->",c)  #将盘子从a移动到c
    else:
        move(n-1,a,c,b)  #将n-1个盘子从a移动到b
        print(a,"--->",c)  #将a塔上的最后一个盘子移动到c塔上
        move(n-1,b,a,c)  #将n-1个盘子从b移动到c塔上
num=int(input("请输入汉诺塔层数:"))
move(num,"A","B","C")