"""
Лабораторная работа № 1 по ЛОИС
Вариант 8 (Построение СКНФ)
Выполнил Войткус Станислав,
        Мирошниченко Константин,
        Лапковский Михаил
Дата выполнения 18.04.2023
"""
import math


def get_row(number, num_vars):
    """Function creates a raw of variables' values """
    row = [0 for i in range(num_vars)]

    num = number
    while num > 0:
        index = math.floor(math.log2(num))
        row[index] = 1
        num = num - 2 ** math.floor(math.log2(num))

    return row


def solve(variables, expr):
    """Function solves expression and puts results into the table."""
    number = -1
    flag_br_2 = 0
    result = ""
    for i in range(2 ** len(variables)):

        number += 1

        curr_expr, row = get_value(number, expr, variables)

        if curr_expr == '0':

            result, flag_br_2 = get_expr(curr_expr, row, variables, result, flag_br_2)

        elif curr_expr != '1':
            return False

    result = result[:-2]

    result = result.replace('!!', '!')

    if result != "":
        print(result)
    else:
        print("No PDNF")
    return True


def get_expr(curr_expr, row, variables, result, flag_br_2):
    if curr_expr == '0':
        curr_result = ""
        flag_br_1 = 0
        for j in range(len(variables)):
            if row[j] == 0:
                curr_result += variables[j]
            else:
                curr_result += '(!' + variables[j] + ')'

            if flag_br_1 == 1:
                curr_result = '(' + curr_result + ')'
            flag_br_1 = 1
            curr_result += '\\/'

        result += curr_result[:-2]
        if flag_br_2 == 1:
            result = '(' + result + ')'
        flag_br_2 = 1

        result += '/\\'
        if flag_br_1 == 0:
            result = ')' + result

    return result, flag_br_2


def get_value(number, expr, variables):
    curr_expr = expr

    row = get_row(number, len(variables))
    while True:
        prev_curr_expr = curr_expr
        curr_expr = solve_subexpr(row, variables, curr_expr)
        if prev_curr_expr == curr_expr:
            break

    return curr_expr, row


def solve_subexpr(row, variables, expr):
    """Function solves expression for vars with row value"""
    for i in range(len(variables)):
        expr = expr.replace(variables[i], str(row[i]))

    expr = solve_neg(expr)
    expr = solve_disj(expr)
    expr = solve_conj(expr)
    expr = solve_eq(expr)
    expr = solve_impl(expr)

    return expr


def solve_disj(expr):
    """Function solves disjunction."""
    while expr.find('(0\\/0)') != -1:
        expr = expr.replace('(0\\/0)', '0')
    while expr.find('(1\\/0)') != -1:
        expr = expr.replace('(1\\/0)', '1')
    while expr.find('(0\\/1)') != -1:
        expr = expr.replace('(0\\/1)', '1')
    while expr.find('(1\\/1)') != -1:
        expr = expr.replace('(1\\/1)', '1')
    return expr


def solve_conj(expr):
    """Function solves conjunction."""
    while expr.find('(0/\\0)') != -1:
        expr = expr.replace('(0/\\0)', '0')
    while expr.find('(1/\\0)') != -1:
        expr = expr.replace('(1/\\0)', '0')
    while expr.find('(0/\\1)') != -1:
        expr = expr.replace('(0/\\1)', '0')
    while expr.find('(1/\\1)') != -1:
        expr = expr.replace('(1/\\1)', '1')
    return expr


def solve_eq(expr):
    """Function solves equivalence."""
    while expr.find('(0~0)') != -1:
        expr = expr.replace('(0~0)', '1')
    while expr.find('(1~0)') != -1:
        expr = expr.replace('(1~0)', '0')
    while expr.find('(0~1)') != -1:
        expr = expr.replace('(0~1)', '0')
    while expr.find('(1~1)') != -1:
        expr = expr.replace('(1~1)', '1')
    return expr


def solve_impl(expr):
    """Function solves implication."""
    while expr.find('(0->0)') != -1:
        expr = expr.replace('(0->0)', '1')
    while expr.find('(1->0)') != -1:
        expr = expr.replace('(1->0)', '0')
    while expr.find('(0->1)') != -1:
        expr = expr.replace('(0->1)', '1')
    while expr.find('(1->1)') != -1:
        expr = expr.replace('(1->1)', '1')
    return expr


def solve_neg(expr):
    """Function solves negation"""
    while expr.find('(!0)') != -1:
        expr = expr.replace('(!0)', '1')
    while expr.find('(!1)') != -1:
        expr = expr.replace('(!1)', '0')
    return expr
