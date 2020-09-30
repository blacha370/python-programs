import csv


class CsvConverter:
    @staticmethod
    def edit_file(file_url: str, delimiter: str = ',', quoting: int = 1, encoding: str = 'utf-8'):
        with open(file_url, newline='', mode='r', encoding=encoding) as csvfile:
            csvfile.seek(0)
            reader = csv.reader(csvfile)
            csv.register_dialect('dialect_name', delimiter=delimiter, quoting=quoting, skipinitialspace=True,
                                 lineterminator='\n')
            with open(file_url[:-4] + '_new.csv', mode='w', encoding=encoding) as file:
                writer = csv.writer(file, dialect='dialect_name')
                for row in reader:
                    writer.writerow(row)
