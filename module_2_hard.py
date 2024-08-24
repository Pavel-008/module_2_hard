n = int(input('Введите число: '))
list_ = []
for i in range(1, n):
    for j in range(1, n):
        if n % (i + j) == 0 and j > i:
            list_.append(i)
            list_.append(j)
    if i == n // 2:
        break


print(''.join(map(str, list_)))
