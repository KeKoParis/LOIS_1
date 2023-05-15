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
    while curr_expr != expr:
        curr_expr = expr
        expr = se.solve_neg(expr)
        expr = se.solve_disj(expr)
        expr = se.solve_conj(expr)
        expr = se.solve_eq(expr)
        expr = se.solve_impl(expr)

    return expr
