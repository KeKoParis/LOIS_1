import build_pcnf as bp
import solve_expresion as se
import table_functions as tf


def get_vars(expr):
    variables = list()
    for i in expr:
        if i.isalpha() == True and check_vars(variables, i):
            variables.append(i)

    return variables


def check_vars(variables, var):
    check = 0
    for i in variables:
        if var == i:
            check += 1

    if check != 0:
        return False

    return True


def check_upper(variables):
    for i in variables:
        if i.isupper() == False:
            return False


# main() function. There's all calls of another functions
def main():
    expr = input('Enter expression: ').replace(' ', '')
    variables = list()
    variables = get_vars(expr)

    if check_upper(variables) == False:
        return False

    table = tf.build_table(variables)

    if se.solve(table, variables, expr) == False:
        return False

    print(bp.build(table, variables))


if __name__ == '__main__':
    if main() == False:
        print('Wrong syntax')
