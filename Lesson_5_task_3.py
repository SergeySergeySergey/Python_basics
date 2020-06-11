content_dict={}
total_salary=0
with open("text_3.txt", 'r', encoding='utf-8') as file:
    for line in file:
        key, *value = line.split()
        content_dict[key] = value
for i, b in content_dict.items():
    b=''.join(b)
    b=float(b)
    total_salary += b
    if b<20000:
        print(i)
salary_len=len(content_dict.keys())
print(f"Общее число сотрудников:{salary_len}")
average_salary=total_salary/salary_len
print(f"Средняя заработная плата сотрудника:{average_salary}")
