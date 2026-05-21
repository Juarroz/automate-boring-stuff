def print_table(table_data):

    col_widths = [0] * len(table_data)

    for i, column in enumerate(table_data):
        max_length = 0
        for word in column:
            if len(word) > max_length:
                max_length = len(word)
        col_widths[i] = max_length
    print(col_widths)

    for row in range(len(table_data[0])):  # recorre las filas: 0, 1, 2, 3
        for col in range(len(col_widths)):  # recorre las columnas: 0, 1, 2
            print(table_data[col][row].rjust(col_widths[col]), end=' ')
        print()  # salto de línea al terminar cada fila

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)