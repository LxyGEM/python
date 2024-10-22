'''八皇后问题'''
#建立一个冲突函数，判断当前位置是否和之前的位置冲突
def conflict(state, nextColumn):
    """
    检查在给定的棋盘状态下，将一个皇后放在下一列是否会导致冲突。

    参数：
    state:一个列表，代表当前棋盘上皇后的位置。
    nextColumn:一个整数,表示下一个皇后将要放置的列。

    返回：
    如果存在冲突，返回 True:否则返回 False。
    """
    # 获取棋盘的行数
    nextRow = rows = len(state)

    # 遍历当前棋盘的每一行
    for row in range(rows):
        # 获取当前行中皇后所在的列
        column = state[row]

        """
        判断是否存在冲突：
        1. 如果列的差值为0，说明两皇后在同一列。
        2. 如果列的差值等于行的差值，说明两皇后在对角线上。
        """
        # 检查是否存在列冲突或对角线冲突
        if abs(column - nextColumn) in [0, nextRow - row]:
            # 如果存在冲突，返回 True
            return True

    # 如果没有冲突，返回 False
    return False


# 采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置
def queens(num, state=()):
    # 每一行的列坐标都是从0:7的
    # 0,1,2,3,4,5,6,7
    for pos in range(num):
        # 默认state为空。长度为0，但是是不冲突的
        # 判断是否冲突，state为空时不冲突
        if not conflict(state, pos): # 回溯法的体现
            # 如果state的长度为7，即到达了倒数第二行，也就是前7行皇后都已经找到了位置，最后一行又没有冲突，返回最后一行的列坐标
            if len(state) == num - 1:
                # 最后一行的（pos,）=最后一行的result，然后再递归回去求倒数第二行的result
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    """
                    递归实现求state：
                        1. 向下递归
                        第一次（行）： pos=0，刚开始不会进入if len(state) == num - 1，进入执行else，会执行queens(num, state + (pos, ))，
                        第二次（行）： 进入else，再调用queens(num, state + (pos, )),递归执行queens(num, state + (pos,) + (pos,))
                        第三次（行）： 进入else，再调用queens(num, state + (pos,) + (pos,),递归执行queens(num, state + (pos,) + (pos,) + (pos,))
                        ...
                        第七次（行）： 执行和上面的一样，不过此时state的长度为7
                        第八次（行）： 执行f len(state) == num - 1:求出最后一行的列坐标(pos,)
                        
                        2.向上递归
                        求出第八行的列坐标，就可以求出第七行的（pos,），返回的是第七行和第八行的列坐标（（pos，） + result）
                        根据下一行的结果依次求出上一行的结果；
                        ....
                        最后求出第一行的列坐标，返回整体结果
                    """
                    yield (pos,) + result

def prettyprint(solution):
    """
    进行友好展示：为了至关表现棋盘，用X表示皇后的位置
    :param solution:
    :return:
    """
    def line(pos, length=len(solution)):
        return '.' * (pos) + 'X' + '.' * (length - pos -1)

    for pos in solution:
        print(line(pos))


if __name__ == '__main__':
    solutions = queens(8)
    for index, solution in enumerate(solutions):
        print('第%d种解决方案：' %(index + 1), solution )
        prettyprint(solution)
        print('*' * 50)