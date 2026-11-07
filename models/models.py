import datetime

def input_date(prompt):
    while True:
        try:
            return datetime.datetime.strptime(input(prompt), "%Y-%m-%d").date()
        except ValueError:
            print("Ошибка! Введите дату в формате ГГГГ-ММ-ДД")

def input_int(prompt, non_negative=False):
    while True:
        try:
            v = int(input(prompt))
            if non_negative and v < 0:
                print("Значение не может быть отрицательным!")
                continue
            return v
        except ValueError:
            print("Ошибка! Введите целое число")