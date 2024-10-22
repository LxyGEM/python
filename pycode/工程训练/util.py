#encoding:utf-8
#生成器，for循环时会依次返回每一行，它只在文件的最后追加了一个空行\n
def lines(file):
    for line in file:yield line  #读取每一行
    yield '\n' #最后加一个空行
#生成器，for循环时会依次返回文本块组成的函数
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():  #如果不是空行
            block.append(line)  #加入到文本块中
        elif block:  #如果是空行，说明文本块结束
            yield ''.join(block).strip()  #join将文本块组成字符串，strip去除前后空格，返回文本块
            block = []  #清空文本块