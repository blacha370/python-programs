import json


class AppRunner:
    def __init__(self):
        self.data = dict()
        self.getUserConfig()

    def getUserConfig(self):
        try:
            with open('./data.json', 'r', encoding='UTF-8') as file:
                json_data = file.read()
                try:
                    data = json.loads(json_data)
                except json.JSONDecodeError:
                    return
                finally:
                    self.data['programs_list'] = data['programs_list']
                    self.data['pages_list'] = set(data['pages_list'])
        except FileNotFoundError:
            return

    def addProgram(self, path: str):
        is_in = False
        for program in self.program_list:
            if program['path'] == path:
                is_in = True
                program['amount'] += 1
        if is_in:
            self.program_list.append({'path': path, 'amount': 1})

    def addPage(self, url: str):
        if url in self.page_list:
            return
        else:
            if 'https://' in url:
                self.page_list.add(url)
            elif 'https://' not in url:
                self.page_list.add('https://' + url)

    def remove(self, resource_to_delete, path: str):
        structure = self.data[resource_to_delete]
        if type(structure) == list:
            for program in self.data[resource_to_delete]:
                if program['path'] == path:
                    self.data[resource_to_delete].remove(program)
                    return
        elif type(structure) == set:
            self.data[resource_to_delete].discard(path)
            return
