def build(table, variables):
    """Function builds pcnf out of table."""
    pcnf_expr = ''
    for i in range(len(table)):
        if table[i][-1] == 0:
            pcnf_expr += ' ('
            for j in range(len(table[i]) - 1):
                if table[i][j] == 0:
                    pcnf_expr += variables[j]
                else:
                    pcnf_expr += '!' + variables[j]
                if j != len(table[i]) - 2:
                    pcnf_expr += '\\/'
            pcnf_expr += ') /\\ '
    pcnf_expr = pcnf_expr[:len(pcnf_expr) - 4]
    return pcnf_expr
