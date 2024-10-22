'''简单文本到HTTML的转换'''
import sys  #读取标准输入
import re  #正则表达式
from util import *  #导入文本生成器util.py

print('<html><head><title>hello</title></head><body>')  #输出HTML文件的开头标签

title = True  #初始化标题标志位
for block in blocks(sys.stdin):  #遍历从标准输入读取的文本块
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)  #将文本块中的*文本*替换为<em>文本</em>

    if title:  #如果title为True，输出标题标签和文本块
        print('<h1>')  #输出标题标签

        print(block)  #输出处理后的文本块
        print('</h1>')  #输出标题标签的结束标签

        title = False  #将title标志位设置为False，下次循环时不再输出标题标签

    else:
        print('<p>')  #输出段落标签

        print(block)  #输出处理后的文本块

        print('</p>')  #输出段落标签的结束标签

print('</body></html>')