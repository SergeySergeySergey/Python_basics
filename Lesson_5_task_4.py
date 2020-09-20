user_file=open('text_4.txt', 'r', encoding='utf-8')
user_file_copy=open('text_4_copy.txt', 'w', encoding='utf-8')
content_user_file=user_file.readlines()
user_file.close()
content_user_file[0]='Один - 1\n'
content_user_file[1]='Два - 2\n'
content_user_file[2]='Три - 3\n'
content_user_file[3]='Четыре -4\n'
user_file_copy.writelines(content_user_file)
print(content_user_file)
user_file_copy.close()