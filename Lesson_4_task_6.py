from sys import argv
from itertools import count, cycle
script_name, start_range, end_range = argv
print("part a:")
start_range=int(start_range)
end_range=int(end_range)
print([el for el in range(start_range, end_range)])
print("Part b:")
for i in count(1):
    if i>10:
        break
    else:
        print(i)
part_1=[num for num in range(start_range,end_range)]
part_2=[k for k in range(start_range,end_range)]
cycle_numbers=[part_1, part_2]
iter= cycle(cycle_numbers)
print(next(iter))
print(next(iter))


