file = open('file_2.txt', 'r')
text = file.read()
print(f'Содержимое файла: \n {text}')
file = open('file_2.txt', 'r')
text = file.readlines()
print(f'Количество строк в файле - {len(text)}')
file = open('file_2.txt', 'r')
text = file.readlines()
for i in range(len(text)):
    print(f'Окличество символов {i + 1} - ой строки {len(text[i])}')
file = open('file_2.txt', 'r')
text = file.read()
text = text.split()
print(f'Общее количество слов - {len(text)}')
file.close()
