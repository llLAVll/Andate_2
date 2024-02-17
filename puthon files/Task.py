#Очевидно, что программа в примере 1 и в индивидуальном задании никак не проверяет
#правильность загружаемых данных формата JSON. В следствие чего, необходимо после загрузки
#из файла JSON выполнять валидацию загруженных данных. Валидацию данных необходимо
#производить с использованием спецификации JSON Schema, описанной на сайте https://json-sch
#ema.org/. Одним из возможных вариантов работы с JSON Schema является использование
#пакета jsonschema , который не является частью стандартной библиотеки Python. Таким
#образом, необходимо реализовать валидацию загруженных данных с помощью спецификации
#JSON Schema.

import json
import jsonschema

# Загрузка данных из файла JSON
def load_workers(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)

# Загрузка JSON Schema для валидации
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "post": {"type": "string"},
        "year": {"type": "number"}
    },
    "required": ["name", "post", "year"]
}

# Валидация загруженных данных
def validate_data(data, schema):
    try:
        jsonschema.validate(data, schema)
        print("Данные прошли валидацию по схеме.")
    except jsonschema.exceptions.ValidationError as e:
        print(f"Данные не соответствуют схеме: {e}")

# Загружаем данные
loaded_data = load_workers("workers.json")
# Валидируем данные
validate_data(loaded_data, schema)
