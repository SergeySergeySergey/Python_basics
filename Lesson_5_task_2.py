#2.	Создать текстовый файл (не программно), сохранить в нем несколько строк,
#выполнить подсчет количества строк, количества слов в каждой строке.
user_file=open("test_text_task_2.txt", 'a+', encoding="utf-8")
user_string_1=("I have a dream\n")
user_string_2=("Martin Luther King\n")
user_string_3=("мама мыла раму\n")
word_amount=len(user_string_1)+len(user_string_2)+len(user_string_3)
user_file.writelines(user_string_1)
user_file.writelines(user_string_2)
user_file.writelines(user_string_3)
user_file.seek(0)
content=user_file.readlines()
print(content)
str_amount=len(content)
print("количество строк:",str_amount)
print(f"Количество слов: {word_amount}")
test_amount=str_amount*word_amount/3
print(int(test_amount))

user_file.close()