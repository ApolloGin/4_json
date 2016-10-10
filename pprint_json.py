import json


def load_data(filepath):
    data = None
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


def pretty_print_json(data):
    return json.dumps(data, indent = 2, ensure_ascii = False)


if __name__ == '__main__':
    data = load_data(input('Введите имя файла с json-ом: '))
    print(pretty_print_json(data))
