# -*- coding: utf-8 -*-
# @Time    : 2021-02-09 22:15
# @Author  : Wxc
# @FileName: arithmatic_arrangers
# @Software: PyCharm

def max_length(arith):
    max_len = 0
    for el in arith:
        if len(el) > max_len:
            max_len = len(el)
    return max_len


def arithmetic_arranger(problems, ans=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    first_line, second_line, third_line, result_line = [], [], [], []
    for mem in problems:
        el = mem.split()
        if el[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (el[0].isdigit() and el[2].isdigit()):
            return "Error: Numbers must only contain digits."
        max_len = max_length(el)
        if max_len > 4:
            return "Error: Numbers cannot be more than four digits."
        first_line.append((max_len - len(el[0]) + 2) * ' ' + el[0])
        second_line.append(el[1] + ' ' + (max_len - len(el[2])) * ' ' + el[2])
        third_line.append('-' * (max_len + 2))
        result_line.append((max_len - len(str(eval(mem))) + 2) * ' ' + str(eval(mem)))
    arranged_problems = (' ' * 4).join(first_line) + '\n' + (' ' * 4).join(second_line) + '\n' + (' ' * 4).join(
        third_line)
    if ans:
        arranged_problems += ('\n' + (' ' * 4).join(result_line))
    return arranged_problems
