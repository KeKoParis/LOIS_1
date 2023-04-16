def solve(table, variables, expr):

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
    for i in range(len(variables)):
        expr = expr.replace(variables[i], str(row[i]))

    expr = solve_neg(expr)
    expr = solve_disj(expr)
    expr = solve_conj(expr)
    expr = solve_eq(expr)
    expr = solve_impl(expr)

    return expr


def solve_disj(expr):
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
    while expr.find('(!0)') != -1:
        expr = expr.replace('(!0)', '1')
    while expr.find('(!1)') != -1:
        expr = expr.replace('(!1)', '0')
    return expr
