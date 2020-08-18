
class AppRunner():
    def __init__(self):
        self.program_list = list()
        self.page_list = set()

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
