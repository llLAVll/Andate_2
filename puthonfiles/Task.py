#Очевидно, что программа в примере 1 и в индивидуальном задании никак не проверяет
#правильность загружаемых данных формата JSON. В следствие чего, необходимо после загрузки
#из файла JSON выполнять валидацию загруженных данных. Валидацию данных необходимо
#производить с использованием спецификации JSON Schema, описанной на сайте https://json-sch
#ema.org/. Одним из возможных вариантов работы с JSON Schema является использование
#пакета jsonschema , который не является частью стандартной библиотеки Python. Таким
#образом, необходимо реализовать валидацию загруженных данных с помощью спецификации
#JSON Schema.


import json
from jsonschema import validate

# Загружаем JSON Schema из файла
with open('schema.json', 'r') as schema_file:
    schema = json.load(schema_file)

def load_workers(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        data = json.load(fin)
        # Валидация данных из файла с использованием JSON Schema
        validate(instance=data, schema=schema)
        return data