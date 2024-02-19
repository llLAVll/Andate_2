#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def main():
    # Ввод данных с клавиатуры в список, состоящий из словарей
    data = []
    n = int(input("Введите количество записей: "))
    for i in range(n):
        record = {}
        record['расчетный счет плательщика'] = input("Введите расчетный счет плательщика: ")
        record['расчетный счет получателя'] = input("Введите расчетный счет получателя: ")
        record['перечисляемая сумма в руб'] = float(input("Введите перечисляемую сумму в рублях: "))
        data.append(record)

    # Сортировка записей в списке по расчетным счетам плательщиков
    data = sorted(data, key=lambda x: x['расчетный счет плательщика'])

    # Запись данных в файл формата JSON
    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # Чтение данных из файла формата JSON
    with open('data.json') as f:
        data = json.load(f)

    # Вывод информации о сумме, снятой с расчетного счета плательщика
    search_account = input("Введите расчетный счет плательщика для поиска: ")
    found = False
    for record in data:
        if record['расчетный счет плательщика'] == search_account:
            output = {
                "расчетный счет плательщика": record['расчетный счет плательщика'],
                "расчетный счет получателя": record['расчетный счет получателя'],
                "перечисляемая сумма в руб": record['перечисляемая сумма в руб']
            }
            print(json.dumps(output, ensure_ascii=False, indent=4))
            found = True

    if not found:
        print("Расчетный счет не найден в базе данных.")

if __name__ == "__main__":
    main()
