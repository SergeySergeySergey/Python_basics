factorial = 1
def num_generator(factorial):
    for el in [2,3,4,5,6]:
        factorial *= el
        yield factorial
n=num_generator(factorial)
print(n)
for el in n:
    print(el)