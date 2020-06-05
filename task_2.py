test_list=list(input("Ведите числа без пробела:"))

for i in range(1, len(test_list), 2):
    test_list[i-1], test_list[i] = test_list[i], test_list[i-1]
print(test_list)
