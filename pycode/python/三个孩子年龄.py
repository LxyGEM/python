'''三个孩子年龄'''
'''提取关键信息:岁数相乘是36,岁数相加结果不唯一,年龄最大的孩子只有一个'''
ageList = list(range(1,37))
agegroup=[]  #用来存放所有组合
def age(x,y,z):  #筛选岁数相乘是36的函数
    group=[]
    if x*y*z==36:    
        group.append(x)
        group.append(y)
        group.append(z)  #分开加入
    group.sort()  #原址排序
    if group not in agegroup:  #将group的组合移到agegroup
        agegroup.append(group)  #满足条件一的组合收集完毕

def agesum():  #筛选相加结果不唯一的组合
    sumlist=[]  #用来保存相加结果
    #获得所有组合的和
    for sample in agegroup:
        sumlist.append(sum(sample))
    #找出重复的组合
    for a in sumlist:
        agecount=sumlist.count(a)#在数组中a的个数
        #找到并去掉重复多余的数
        if agecount > 1:
            sumlist.remove(a)
            #找到重复的数对应的组合
            for sample2 in agegroup:
                if sum(sample2)==a:
                    #确定最大值是否唯一
                    if sample2.count(max(sample2))==1:
                        print(sample2)
#将脚本作为主程序运行
if __name__=='__main__':
    for p1 in ageList:
        for p2 in ageList:
            for p3 in ageList:
                age(p1, p2, p3)
    agesum()  #结果是打印最终组合