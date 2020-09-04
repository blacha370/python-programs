import requests
import time

links_to_check = set()
invalid_links = set()
i = 0


def checkLink(url, amount):
    global i
    i += 1
    percentage = i / amount * 100
    try:
        r = requests.get(url)
        if r.status_code != 200:
            invalid_links.add(url)
        print(url, str(r.status_code), str(percentage) + '%')
    except requests.exceptions.ConnectionError:
        invalid_links.add(url)
        print(url, "ConnectionError", str(percentage) + '%')
    time.sleep(4)


with open('linksToCheck.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        elements = line.replace('\n', '').replace(' ', '')
        elements = elements.split('\t')
        for element in elements:
            if element == '':
                continue
            if not element.startswith('http://') and not element.startswith('https://'):
                element = 'http://' + element
            links_to_check.add(element)


links_number = len(links_to_check)
print(links_number)


for link in links_to_check:
    checkLink(link, links_number)


with open('invalidLinks.txt', 'w', encoding='UTF-8') as file:
    if len(invalid_links) == 0:
        print('No invalid links')
        file.write('No invalid links')
    else:
        for element in invalid_links:
            print(invalid_links)
            file.write(element + '\n')
