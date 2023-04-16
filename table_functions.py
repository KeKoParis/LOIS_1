def build_table(variables):
    len_rows = len(variables) + 1
    len_columns = len(variables) ** 2
    if len_columns % 2 != 0:
        len_columns -= 1
    if len_columns == 0:
        len_columns += 2

    table = [[0 for i in range(len_rows)] for j in range(len_columns)]
    fill_table(table)

    return table


def fill_table(table):
    switch = 1
    for i in range(len(table[0]) - 1):
        parameter = 0
        count = 0
        for j in range(len(table)):
            table[j][i] = parameter
            count += 1
            if count == switch:
                if parameter == 1:
                    parameter = 0
                    count = 0
                else:
                    parameter = 1
                    count = 0
        switch += switch