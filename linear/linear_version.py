import datetime

def input_date(prompt):
    while True:
        try:
            s = input(prompt)
            return datetime.datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print("Ошибка! Введите дату в формате ГГГГ-ММ-ДД")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Введите целое число")

def print_files(files):
    if not files:
        print("Каталог пуст.")
        return
    print(f"{'Имя файла':<20}{'Дата создания':<15}{'Обращений':<10}")
    print("-" * 45)
    for f in files:
        print(f"{f['name']:<20}{str(f['date']):<15}{f['count']:<10}")

files = []

print("=== Формирование каталога ===")
n = input_int("Введите количество файлов: ")
for i in range(n):
    print(f"\nФайл #{i + 1}")
    name = input("Имя файла: ").strip()
    while not name:
        print("Имя не может быть пустым!")
        name = input("Имя файла: ").strip()
    date = input_date("Дата создания (ГГГГ-ММ-ДД): ")
    count = input_int("Количество обращений: ")
    while count < 0:
        print("Количество обращений не может быть отрицательным!")
        count = input_int("Количество обращений: ")
    files.append({'name': name, 'date': date, 'count': count})

while True:
    print("\n=== МЕНЮ ===")
    print("1. Вывод каталога файлов")
    print("2. Удалить файлы, созданные раньше заданной даты")
    print("3. Файл с наибольшим количеством обращений")
    print("0. Выход")
    choice = input("Выбор: ").strip()

    if choice == '1':
        print_files(files)

    elif choice == '2':
        if not files:
            print("Каталог пуст.")
            continue
        border = input_date("Удалить файлы, созданные раньше даты: ")
        before = len(files)
        files = [f for f in files if f['date'] >= border]
        print(f"Удалено файлов: {before - len(files)}")

    elif choice == '3':
        if not files:
            print("Каталог пуст.")
            continue
        best = files[0]
        for f in files:
            if f['count'] > best['count']:
                best = f
        print(f"Файл с наибольшим числом обращений: {best['name']} "
              f"(дата: {best['date']}, обращений: {best['count']})")

    elif choice == '0':
        print("Выход.")
        break
    else:
        print("Неверный пункт меню!")