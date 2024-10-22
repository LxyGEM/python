'''有一个五位数abcde,乘以4以后变成edcba,abcde是多少?'''
'''法一'''
for i in range(10000,100000):  #range取不到末值 
    a = i // 10000  #//向下取整
    b = i // 1000 % 10  #%取余
    c = i % 1000 // 100
    d = i % 100 // 10
    e = i % 10
    r = a + b*10 + c*100 + d*1000 + e*10000
    if r == 4*i:
        print(i)

'''法二、字符串'''
for i in range(10000,100000):
    s = str(i)
    r = s[-1] + s[-2] + s[2] + s[1] + s[0]  #正向索引和反向索引
    if str(i*4)==r:  #括号内×4
        print(i)

'''法三、生成器'''
l = [i for i in range(10000,100000) if str(i*4)==str(i)[::-1]]  #[::-1]倒序
print(*l)  #加*输出列表里的内容