import build_pcnf as bp
import solve_expresion as se
import table_functions as tf


def get_vars(expr):
    """Function gets all vars from expression."""
    variables = list()
    for i in expr:
        if i.isalpha() == True and check_vars(variables, i):
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
        if i.isupper() == False:
            return False


def main():
    """Function does calls of another functions."""
    expr = input('Enter expression: ').replace(' ', '')
    variables = list()
    variables = get_vars(expr)

    if check_upper(variables) == False:
        return False

    if len(variables) == 0:
        return True


    table = tf.build_table(variables)

    if se.solve(table, variables, expr) == False:
        return False

    print(bp.build(table, variables))


if __name__ == '__main__':
    while True:
        if main() == False:
            print('Wrong syntax')
        if input('Do you want to continue [y/n] ') == 'n':
            break
        print()
