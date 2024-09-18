def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix1 = []
        matrix.append(matrix1)
        for j in range(m):
            matrix1.append(value)
    return matrix



result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(4, 0, 13) # так как передал аргумент со значением 0, то возвращается пустой список
print(result1)
print(result2)
print(result3)
print(result4)