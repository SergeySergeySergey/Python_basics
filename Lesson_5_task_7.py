import json
user_file=open('text_7.txt', 'r', encoding='utf-8')
file_content=user_file.readlines()
file_content=''.join(file_content)
file_content=file_content.replace('\n', ' ')
file_content=file_content.split()
brooms_profit=int(file_content[2])-int(file_content[3])
tandoor_profit=int(file_content[6])-int(file_content[7])
honey_cake_profit=int(file_content[10])-int(file_content[11])
matrioshka_profit=int(file_content[14])-int(file_content[15])
skazka_profit=int(file_content[18])-int(file_content[19])
all_profit={"Brooms": brooms_profit, "Honey-cake": honey_cake_profit, "Matrioshka": matrioshka_profit, "Сказка": skazka_profit}
loss_companies={"Tandoor": tandoor_profit}
average_profit=int(brooms_profit+honey_cake_profit+matrioshka_profit+skazka_profit)/5
average_profit_dict={"Средняя прибыль": average_profit}
print(f'Прибыль компаний составляет: {all_profit},\n{average_profit_dict}, \nУбыточные компании: {loss_companies}')
total_list=[all_profit,average_profit_dict, loss_companies]
print(total_list)
with open("Lesson_5_task_7.json", 'w', encoding='utf-8') as test_wr:
    json.dump(total_list, test_wr, ensure_ascii=False)
user_file.close()