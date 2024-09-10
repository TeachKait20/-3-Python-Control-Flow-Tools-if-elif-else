# что ещё умеет %

number = 1371

# можно узнать на что число заканчивается
print(number % 10, number % 100, number % 1000)

# например, нам необходимо число кратное 3 и заканчивающееся на 1. выполним проверку:
if number % 3 == 0 and number % 10 == 1:
    print(True)
else:
    print(False)
