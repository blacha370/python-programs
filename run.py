import os
list = []
print('ok')
with open('programList.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        element = line.replace("\n", "")
        print(element)
        list.append(element)
for element in list:
    os.startfile(element)
