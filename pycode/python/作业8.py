'''帽子三红两白'''
def check_color(hats):
    #A回答不知道，说明BC不同时为白帽子
    if hats[1]=='白' and hats[2]=='白':
        return False
    #B回答不知道，说明AC不同时为白帽子
    if hats[0]=='白' and hats[2]=='白':
        return False
    #C听后才知道
    if hats[0]=='红' and hats[1]=='红' and hats[2]=='红':
        return False
    if hats[0]=='白' and hats[1]=='白':
        return False
    if hats[2]=='白':
        return False
    return True
def find_color():
    ls=[]
    for a in ['红','白']:
        for b in ['红','白']:
            for c in ['红','白']:
                hats=[a,b,c]
                if check_color(hats):
                    ls.append(hats)
    return ls  #注意return的位置，不要放在循环里            
result=find_color()
print(f"ABC帽子的颜色分别为:{result}")