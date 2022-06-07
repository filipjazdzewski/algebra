def print_result(matrix):
    for row in matrix:
        print('  '.join((str(round(element)) for element in row)))

def gauss_elimination(matrix):
    if type(matrix) is not list:
        print("error: nie podałeś macierzy")
        return -1
    lead = 0
    row_count = len(matrix)
    column_count = len(matrix[0])
    for r in range(row_count):
        if lead >= column_count:
            print('Układ jest sprzeczny.')
            return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == row_count:
                i = r
                lead += 1
                if column_count == lead:
                    print('Układ ma nieskończenie wiele rozwiązań.')
                    return
        matrix[i], matrix[r] = matrix[r], matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
        for i in range(row_count):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
        lead += 1
    print("Układ ma jedno rozwiąznie.")
    print_result(matrix)
    return


matrix1 = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 1],
    [3, 2, 1, 2, 1],
    [4, 3, 2, 1, -5]
]

matrix2 = [
    [1, 0, 3, 2, 10],
    [2, 1, 1, 1, 7],
    [2, 0, 2, 4, 8],
    [1, 2, 3, -4, 14]
]

matrix3 = [
    [1, 2, 0, 1, 1],
    [1, 3, 3, 3, 4],
    [0, 1, 4, 4, 8],
    [2, 5, 3, 4, 6]
]


# Wybierz ktora macierz chcesz przetestowac
current_matrix = matrix1

gauss_elimination(current_matrix)
