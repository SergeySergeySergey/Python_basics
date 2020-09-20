my_tuple=tuple("hello")
fr_set=frozenset("1 2 3")
test_set=set("python")
test_dict=dict(key_1='test')
my_list=["I have a deam", 12345, 40.4, complex(5), None, True, my_tuple, fr_set, test_set, test_dict]
for num, val, in enumerate(my_list, 1):
    print(str(num) + "-" + str(val) + " ", end='')
    print(type(val))