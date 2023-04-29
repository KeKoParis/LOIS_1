'''
Лабораторная работа № 1 по ЛОИС
Вариант 8 (Построение СКНФ)
Выполнил Войткус Станислав,
        Мирошниченко Константин,
        Лапковский Михаил
Дата выполнения 18.04.2023
'''


def solve(table, variables, expr):
    """Function solves expression and puts results into the table."""
    for i in table:
        curr_expr = expr
        while True:
            prev_curr_expr = curr_expr
            curr_expr = solve_subexpr(i, variables, curr_expr)
            if prev_curr_expr == curr_expr:
                break
        if curr_expr == '0' or curr_expr == '1':
            i[-1] = int(curr_expr)
        else:
            return False


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
