'''100个人集中在一个房间,至少有两个人生日相同的概率有多大?'''
import random  #导入随机模块
def sample(num):  #抽样num个
    number = 0  #相同数初始值为0
    for i in range(num):
        ls=[]  #创建一个空列表装初始生日
        for i in range(100):  #在一百个人中的for循环
            birthday = random.choice(range(365))  #随机从365中取100个数字
            ls.append(birthday)  #将生日填进列表
        collection = set(ls)  #set函数生成一个集合
        if len(collection)!=len(ls):  #比较两集合长度而不是集合本身，才可知是否有相同生日
            number += 1  #有相同生日的事件加一
    return number/num  #事件比总量
print("100个人当中至少有两人生日相同的概率为：{:.2f}%".format(sample(10000)*100))