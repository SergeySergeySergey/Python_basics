user_input=0
while user_input != (""):
    user_input = input("Введите построчно данные, по окончании ввода оставьте пустую строку: ")
    br_input="\n"
    user_file = open("user_text.txt", 'a+', encoding='utf-8')
    user_file.writelines(user_input)
    user_file.writelines(br_input)
    user_file.close()
else:
    print("Досвидания")