# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
csv_file_path = INPUT_FILENAME

def task(csv_file_path, delimiter = ",", line_delimiter = "/n"):
    # TODO считать содержимое csv файла
        with open(csv_file_path, mode="r", newline = "") as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            data = [row for row in reader]


    # TODO Сериализовать в файл с отступами равными 4
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        return json_data

if __name__ == '__main__':

    # Нужно для проверки
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
