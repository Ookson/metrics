from models import input_date, input_int

def init_catalog():
    files = []
    n = input_int("Введите количество файлов: ", non_negative=True)
    for i in range(n):
        print(f"\nФайл #{i + 1}")
        name = input("Имя файла: ").strip()
        while not name:
            print("Имя не может быть пустым!")
            name = input("Имя файла: ").strip()
        date = input_date("Дата создания (ГГГГ-ММ-ДД): ")
        count = input_int("Количество обращений: ", non_negative=True)
        files.append({'name': name, 'date': date, 'count': count})
    return files

def print_files(files):
    if not files:
        print("Каталог пуст.")
        return
    print(f"{'Имя файла':<20}{'Дата создания':<15}{'Обращений':<10}")
    print("-" * 45)
    for f in files:
        print(f"{f['name']:<20}{str(f['date']):<15}{f['count']:<10}")

def delete_older(files):
    if not files:
        print("Каталог пуст.")
        return files
    border = input_date("Удалить файлы, созданные раньше даты: ")
    before = len(files)
    files = [f for f in files if f['date'] >= border]
    print(f"Удалено файлов: {before - len(files)}")
    return files

def most_accessed(files):
    if not files:
        print("Каталог пуст.")
        return
    best = files[0]
    for f in files:
        if f['count'] > best['count']:
            best = f
    print(f"Файл с наибольшим числом обращений: {best['name']} "
          f"(дата: {best['date']}, обращений: {best['count']})")