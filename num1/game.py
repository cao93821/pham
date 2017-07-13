#!/user/bin/env python
# encoding: utf-8
"""
The minigame 2048 in python
"""
import random

def init():
    """
    initialize a 2048 matrix. return a matrix list
    :return:
    """
    matrix = [0 for i in range(16)]
    random_lst = random.sample(range(16), 2)  # generate 2 different number
    matrix[random_lst[0]] = matrix[random_lst[1]] = 2
    return matrix


def move(matrix, direction):
    """
    moving the matrix. return a matrix list
    :param matrix:
    :param direction:
    :return:
    """
    mergedList = []  # initial the merged index
    if direction == 'u':
        for i in range(16):
            j = i
            while j - 4 >= 0:
                if matrix[j-4] == 0:
                    matrix[j-4] = matrix[j]
                    matrix[j] = 0
                elif matrix[j-4] == matrix[j] and j - 4 not in mergedList and j not in mergedList:
                    matrix[j-4] *= 2
                    matrix[j] = 0
                    mergedList.append(j-4)
                    mergedList.append(j)  # prevent the number to be merged twice
                j -= 4
    elif direction == 'd':
        for i in range(15,-1,-1):
            j = 1
            while j + 4 < 16:
                if matrix[j+4] == 0:
                    matrix[j+4] = matrix[j]
                    matrix[j] = 0
                elif matrix[j+4] == matrix[j] and j + 4 not in mergedList and j not in mergedList:
                    matrix[j+4] *= 2
                    matrix[j] = 0
                    mergedList.append(j)
                    mergedList.append(j+4)
                j += 4
    elif direction == 'l':
        for i in range(16):
            j = i
            while j % 4 != 0:
                if matrix[j-1] == 0:
                    matrix[j-1] = matrix[j]
                    matrix[j] = 0
                elif matrix[j-1] == matrix[j] and j + 4 not in mergedList and j not in mergedList:
                    matrix[j-1] *= 2
                    matrix[j] = 0
                    mergedList.append(j-1)
                    mergedList.append(j)
                j -= 1
    else:
        for i in range(15,-1,-1):
            j = i
            while j % 4 != 3:
                if matrix[j+1] == 0:
                    matrix[j+1] = matrix[j]
                    matrix[j] = 0
                elif matrix[j+1] == matrix[j] and j + 1 not in mergedList and j not in mergedList:
                    matrix[j+1] *= 2
                    matrix[j] = 0
                    mergedList.append(j)
                    mergedList.append(j+1)
                j += 1
    return matrix


def insert(matrix):
    """
    insert one 2 or 4 into the matrix. return the matrix list
    :param matrix:
    :return:
    """
    getZeroIndex = []
    for i in range(16):
        if matrix[i] == 0:
            getZeroIndex.append(i)
    randomZeroIndex = random.choice(getZeroIndex)
    matrix[randomZeroIndex] = 2
    return matrix


def output(matrix):
    """
    print the matrix. return the matrix list
    :param matrix:
    :return:
    """
    max_num_width = len(str(max(matrix)))
    demarcation = ('+' + '-'*(max_num_width+2)) * 4 + '+'  # generate demarcation line like '+---+---+---+'
    print demarcation
    for i in range(len(matrix)):
        if matrix[i] == 0:
            print_char = ' '
        else:
            print_char = str(matrix[i])
        print '|',
        print '{0:>{1}}'.format(print_char, max_num_width),
        if (i + 1) % 4 == 0:
            print '|'
            print demarcation
    print


def isOver(matrix):
    """
    is game over? return bool
    :param matrix:
    :return:
    """
    if 0 in matrix:
        return False
    else:
        for i in range(16):
            if i % 4 != 3:
                if matrix[i] == matrix[i+1]:
                    return False
            if i < 12:
                if matrix[i] == matrix[i+4]:
                    return False
    return True


def play():
    matrix = init()
    matrix_stack = []  # just used by back function
    matrix_stack.append(list(matrix))
    step = len(matrix_stack) - 1

    while True:
        output(matrix)
        if isOver(matrix) == False:
            if max(matrix) == 2048:
                __input__ = raw_input('The max number is 2048, win the goal! q for quit, others for continue.')
                if __input__ == 'q':
                    exit()
            while True:
                __input__ = raw_input("Step {0:2d} Choose which direction? u(p)/d(own)/l(eft)/r(ight), q for quit, b "
                                  "for back: ".format(step))
                if __input__ in ['u', 'd', 'l', 'r']:
                    matrix = move(matrix, input)
                    if matrix == matrix_stack[-1]:
                        print 'Not changed. Try another direction.'
                    else:
                        insert(matrix)
                    matrix_stack.append(list(matrix))
                    break
                elif __input__ == 'b':
                    if len(matrix_stack) == 1:
                        print 'Cannot back anymore...'
                        continue
                    matrix_stack.pop()
                    matrix = list(matrix_stack[-1])
                    break
                elif __input__ == 'q':
                    print 'Byebye!'
                    exit()
                else:
                    print 'Input error! Try again.'
        else:
            print 'Cannot move anyway. Game Over...'
            exit()
        step = len(matrix_stack) - 1

if __name__ == '__main__':
    play()
    
