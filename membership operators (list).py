numbers = [2, 5, 6, 7, 10]

# проверка элемента из списка на чётность
if numbers[0] % 2 == 0:
    print(True)
else:
    print(False)

# проверка нескольких элементов из списка на чётность (строгое условие)
if numbers[0] % 2 == 0 and numbers[1] % 2 == 0:
    print(True)
else:
    print(False)

# проверка нескольких элементов из списка на чётность (нестрогое условие)
if numbers[0] % 2 == 0 or numbers[1] % 2 == 0:
    print(True)
else:
    print(False)
