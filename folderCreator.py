import os

list = set()
bannedCharacters = {"/", "\\", ":", "*", "?", '"', "<", '>', "|", "-"}
with open('folderList.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        element = line.replace('\n', '')
        for char in bannedCharacters:
            element = element.replace(char, '-')
        list.add(element)
    print(list)
mainDirectory = 'result'
os.mkdir(mainDirectory)
for element in list:
    path = mainDirectory + "/" + element
    os.mkdir(path)
