n=8
maxN=25
a=[0 for i in range(1,maxN+1,1)]
c=[False for i in range(1,maxN+1,1)]
d=[False for i in range(1,2*maxN+1,1)]
e=[False for i in range(1,2*maxN+2,1)]
ans=0
def Queen(x):
    global n,a,c,d,e,ans
    if x>n:
        ans+=1
        print(f"第{ans}种解法:")
        for i in range(1,n+1,1):
            print(f"第{i}行的王后放在第{a[i]}列")
        print("")
        return
    for j in range(1,n+1,1):
        if((not c[j]) and (not d[x-j+n]) and (not e[x+j])):
            c[j]=d[x-j+n]=e[x+j]=True
            a[x]=j
            Queen(x+1)
            c[j]=d[x-j+n]=e[x+j]=False
            a[x]=0
Queen(1)
print(f"{n}皇后问题共有{ans}种解")