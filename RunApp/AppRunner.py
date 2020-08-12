import json
import os
import webbrowser
import sys


class AppRunner():
    def __init__(self):
        self.program_list = list()
        self.page_list = set()
        self.getUserConfig()

    def getUserConfig(self):
        try:
            with open('./data.json', 'r', encoding='UTF-8') as file:
                json_data = file.read()
                try:
                    data = json.loads(json_data)
                    self.program_list = data['program_list']
                    self.page_list = set(data['page_list'])
                except:
                    pass
        except FileNotFoundError:
            pass

    def addProgram(self, path: str):
        is_in = False
        for program in self.program_list:
            if program['path'] == path:
                is_in = True
                program['amount'] += 1
        if is_in == False:
            self.program_list.append({'path': path, 'amount': 1})

    def addPage(self, url: str):
        if url in self.page_list:
            return
        else:
            if 'https://' in url:
                self.page_list.add(url)
            elif 'https://' not in url:
                self.page_list.add('https://' + url)

    def removeProgram(self, path: str):
        for i in range(len(self.program_list)):
            if self.program_list[i]['path'] == path:
                self.program_list.pop(i)
                return

    def removePage(self, url: str):
        if 'https://' not in url:
            url = 'https://' + url
        self.page_list.discard(url)

    def run(self):
        with open('./data.json', 'w', encoding='UTF-8') as file:
            data = {"program_list": self.program_list,
                    "page_list": list(self.page_list)}
            json_data = json.dumps(data)
            file.write(json_data)
        for program in self.program_list:
            for _ in range(program['amount']):
                path = program['path']
                os.startfile(path)
        for page in self.page_list:
            webbrowser.open_new_tab(page)
        sys.exit()
