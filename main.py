"""
Лабораторная работа № 1 по ЛОИС
Вариант 8 (Построение СКНФ)
Выполнил Войткус Станислав,
        Мирошниченко Константин,
        Лапковский Михаил
Дата выполнения 18.04.2023
"""

import solve_expresion as se
import solve_numeric as sn


def get_vars(expr):
    """Function gets all vars from expression."""
    variables = list()
    for i in expr:
        if i.isalpha() is True and check_vars(variables, i):
            variables.append(i)

    return variables


def check_vars(variables, var):
    """Function checks if all vars are letters."""
    check = 0
    for i in variables:
        if var == i:
            check += 1

    if check != 0:
        return False

    return True


def check_upper(variables):
    """Function checks if all symbols are capital."""
    for i in variables:
        if i.isupper() is False:
            return False


def check_nums(expr):
    for i in expr:
        if 58 > ord(i) > 49:
            return True


def main():
    """Function calls another functions."""
    expr = input('Enter expression: ')
    variables: list = get_vars(expr)

    if expr == '':
        return False

    if check_nums(expr):
        return False

    if len(variables) == 0:
        expr, num_res = sn.solve_num(expr)
        if expr == '0':
            print(num_res)
            return True
        elif expr == '1':
            print("No PDNF")
            return True
        else:
            return False

    if check_upper(variables) is False:
        return False

    if se.solve(variables, expr) is False:
        return False


if __name__ == '__main__':
    while True:
        if main() is False:
            print('Wrong syntax')
        if input('******************     Do you want to continue [y/n]     ******************\n') == 'n':
            break
        print()
