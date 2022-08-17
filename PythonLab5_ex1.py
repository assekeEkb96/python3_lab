file = open('test.txt', 'w')
string = input('Введите текст\n')
while string:
    file.writelines(string)
    string = input('Введите текст\n')
    if not string:
        break

file.close()
file = open('test.txt', 'r')
text = file.readlines()
print(text)
file.close()


