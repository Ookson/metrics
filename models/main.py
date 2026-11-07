import catalog
import menu

def main():
    print("=== Формирование каталога ===")
    files = catalog.init_catalog()
    while True:
        choice = menu.show_menu()
        if choice == '1':
            catalog.print_files(files)
        elif choice == '2':
            files = catalog.delete_older(files)
        elif choice == '3':
            catalog.most_accessed(files)
        elif choice == '0':
            print("Выход.")
            break
        else:
            print("Неверный пункт меню!")

if __name__ == "__main__":
    main()