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

# Здесь определение вашего JSON Schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "post": {"type": "string"},
        "year": {"type": "integer"}
    },
    "required": ["name", "post", "year"]
}

def load_workers(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        # Загружаем данные из файла
        data = json.load(fin)
        # Проверяем данные по схеме
        validate(instance=data, schema=schema)
        return data

# Остальной код остается неизменным