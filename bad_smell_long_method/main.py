# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`
import operator

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_result(file: str) -> [dict]:
    read_file = get_read_file(file)
    sorted_file = _get_sorted(read_file)
    filtered_file = _get_filtered(sorted_file)
    return filtered_file


def get_read_file(file: str) -> [dict]:
    # Чтение данных из строки
    data = []
    for line in file.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


# Сортировка по возрасту по возрастанию
def _get_sorted(data: [dict]) -> [dict]:
    sorted_data = sorted(data, key=operator.itemgetter('age'))
    return sorted_data


# Фильтрация
def _get_filtered(data: [dict]) -> [dict]:
    return [element for element in data if element['age'] > 10]


if __name__ == '__main__':
    result = get_result(csv)
    print(result)
