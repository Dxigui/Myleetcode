# -*- coding: utf-8 -*-


#初始位置 (0, 0) 处有一个机器人。给出它的一系列动作
#判断这个机器人的移动路线是否形成一个圆圈，
#换言之就是判断它是否会移回到原来的位置。
#移动顺序由一个字符串表示。每一个动作都是由一个字符来表示的。
#机器人有效的动作有 R（右），L（左），U（上）和 D（下）。
#输出应为 true 或 false，表示机器人移动路线是否成圈。

def judgeCircle(moves):
    start = [0, 0]
    end = [0, 0]
    for step in moves:
        if step == 'L':
            end[0] -= 1
        elif step == 'R':
            end[0] += 1
        elif step == 'D':
            end[1] += 1
        else:
            end[1] -= 1
    return start == end

print(judgeCircle('LRDU'))



def judgeCircle3(moves):
    if len(moves) % 2 != 0:
        return False
    if moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D'):
        return True
    else:
        False

print(judgeCircle3('LRDU'))

def judgeCircle4(moves):
    return moves.count('L') == moves.count('R') and moves.count('D') == moves.count('U')

print(judgeCircle4('LLLL'))

def judgeCircle5(moves):
    direct = {'U':1, 'D': -1, 'L': 1, 'R': -1}
    return 0 == sum(direct[m] for m in moves)

print(judgeCircle4('LRDU'))
