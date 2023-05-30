"""
Лабораторная работа № 1 по ЛОИС
Вариант 8 (Построение СКНФ)
Выполнил Войткус Станислав,
        Мирошниченко Константин,
        Лапковский Михаил
Дата выполнения 18.04.2023
"""

import solve_expresion as se


def solve_num(expr):
    curr_expr = ""
    expression = expr
    while curr_expr != expr:
        curr_expr = expr
        expr = se.solve_neg(expr)
        expr = se.solve_disj(expr)
        expr = se.solve_conj(expr)
        expr = se.solve_eq(expr)
        expr = se.solve_impl(expr)

    return expr, build_pdnf_num(expression)


def get_row(expr):
    row = list()
    for i in expr:
        if i == '0':
            row.append(i)
        if i == '1':
            row.append(i)

    return row


def build_pdnf_num(expr):
    row = get_row(expr)
    result = ""
    left_br = -1

    for i in range(len(row)):
        if i == 0:
            if row[i] == '1':
                result += "(!" + chr(i + 65) + "\\/"
            else:
                result += "(" + chr(i + 65) + "\\/"
        else:
            if row[i] == '1':
                result += '!'
            result += chr(i + 65)
            result += ")\\/"
            left_br += 1

    for i in range(left_br):
        result = "(" + result

    result = result[:-2]

    return result
