#!/usr/bin/env python3
"""tile.py: methods of brick paving
__author__ = "Liu Yuxin"
__pkuid__  = "1800011832"
__email__  = "1800011832@pku.edu.cn"
"""
import copy
m = int(input("Please input the length of the wall."))
n = int(input("Please input the width of the wall."))
a = int(input("Please input the length of the bricks."))
b = int(input("Please input the width of the bricks."))
wall = [0]*n
lst = [0]*m
for z in range(n):
    wall[z] = copy.deepcopy(lst)
every_result = []
all_methods = []


def crosswise_judgement(i, j, wall):
    """to judge whether crosswise paving is available"""
    if i + a > m or j + b > n:
        return False
    for y in range(b):
        if wall[j+y][i:i+a]!=[0]*a:
            return False
    return True


def lengthways_judgement(i, j, wall):
    """to judge whether lengthways paving is available"""
    if i + b > m or j + a > n:
        return False
    for x in range(a):
        if wall[j+x][i:i+b] != [0]*b:
            return False
    return True


def brick_paving(wall, every_result, all_methods):
    """to pave the bricks whose length is not equal to the width"""
    if wall == [[1]*m]*n:
        all_methods.append(every_result.copy())
        return 
    wall1 = []
    for x in range(n):
        for y in range(m):
            wall1.append(wall[x][y])
    for z in range(len(wall1)):
        if wall1[z] == 0:
            i, j = z % m, z//m
            break
    if crosswise_judgement(i, j, wall):
        every_brick = []
        for x in range(b):
            for y in range(a):
                wall[j+x][i+y] = 1
                every_brick.append(i+y+(j+x)*m)
        every_result.append(tuple(every_brick))
        brick_paving(wall, every_result, all_methods)
        for x in range(b):
            for y in range(a):
                wall[j+x][i+y] = 0
        every_result.remove(tuple(every_brick))
    if lengthways_judgement(i, j, wall):
        every_brick = []
        for x in range(a):
            for y in range(b):
                wall[j+x][i+y] = 1
                every_brick.append(i+y+(j+x)*m)
        every_result.append(tuple(every_brick))
        brick_paving(wall, every_result, all_methods)
        for x in range(a):
            for y in range(b):
                wall[j+x][i+y] = 0
        every_result.remove(tuple(every_brick))
    return


def brick_paving2(wall, every_result, all_methods):
    """to pave the bricks whose length is equal to the width"""
    if wall == [[1]*m]*n:
        all_methods.append(every_result.copy())
        return 
    wall1 = []
    for x in range(n):
        for y in range(m):
            wall1.append(wall[x][y])
    for z in range(len(wall1)):
        if wall1[z] == 0:
            i, j = z % m, z//m
            break
    if crosswise_judgement(i, j, wall):
        every_brick = []
        for x in range(b):
            for y in range(a):
                wall[j+x][i+y] = 1
                every_brick.append(i+y+(j+x)*m)
        every_result.append(tuple(every_brick))
        brick_paving2(wall, every_result, all_methods)
        for x in range(b):
            for y in range(a):
                wall[j+x][i+y] = 0
        every_result.remove(tuple(every_brick))
    return


def visualization(all_methods):
    import turtle
    t = turtle.Turtle()
    t.pencolor("blue")
    q = str(len(all_methods)-1)
    word = "Input number of 0-"+q
    p = int(input(word))
    method = all_methods[p]
    for x in range(n+1):
        t.pd()
        t.goto(20*m, -20*x)
        t.pu()
        t.goto(0, -20*(x+1))
    t.goto(0, 0)
    for x in range(m+1):
        t.pd()
        t.goto(20*x, -20*n)
        t.pu()
        t.goto(20*(x+1), 0)
    for x in range(m):
        for y in range(n):
            t.goto(10*(2*x+1), -20*(y+1))
            text = str(x+y*m)
            t.write(text, align="center")
    t.pencolor("black")
    t.pensize(3)
    for brick in method:
        brick = list(brick)
        li = [i % m for i in brick]
        lj = [j//m for j in brick]
        i1 = 20*(max(li)+1)
        j1 = -20*(max(lj)+1)
        i2 = 20*min(li)
        j2 = -20*min(lj)
        t.goto(i2, j2)
        t.pd()
        t.goto(i1, j2)
        t.goto(i1, j1)
        t.goto(i2, j1)
        t.goto(i2, j2)
        t.pu()


def main():
    """main module"""
    if m*n % a*b != 0:
        print("We can't do it.")
    elif a == b:
        brick_paving2(wall, every_result, all_methods)
        for method in all_methods:
            print(method)
        visualization(all_methods)
    else:
        brick_paving(wall, every_result, all_methods)
        for method in all_methods:
            print(method)
        visualization(all_methods)


if __name__ == '__main__':
    main()
