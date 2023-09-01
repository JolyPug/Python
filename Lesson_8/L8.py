def add_contact(phonebook, name, phone_number):
    phonebook[name] = phone_number
    save_to_file(phonebook)
    print(f"Контакт '{name}' с номером '{phone_number}' добавлен.")

def display_all_contacts(phonebook):
    if phonebook:
        print("Список контактов:")
        for name, phone_number in phonebook.items():
            print(f"{name}: {phone_number}")
    else:
        print("Телефонная книга пуста.")

def search_contact(phonebook, name):
    if name in phonebook:
        print(f"Контакт '{name}': {phonebook[name]}")
    else:
        print(f"Контакт '{name}' не найден.")

def edit_contact(phonebook, name, new_phone_number):
    if name in phonebook:
        phonebook[name] = new_phone_number
        save_to_file(phonebook)
        print(f"Контакт '{name}' изменен. Новый номер: {new_phone_number}")
    else:
        print(f"Контакт '{name}' не найден.")

def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        save_to_file(phonebook)
        print(f"Контакт '{name}' удален.")
    else:
        print(f"Контакт '{name}' не найден.")

def save_to_file(phonebook):
    with open("phonebook.txt", "w") as file:
        for name, phone_number in phonebook.items():
            file.write(f"{name}: {phone_number}\n")

def load_from_file():
    phonebook = {}
    try:
        with open("phonebook.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, phone_number = line.strip().split(": ")
                phonebook[name] = phone_number
    except FileNotFoundError:
        pass
    return phonebook

def main():
    phonebook = load_from_file()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить контакт")
        print("2. Вывести все контакты")
        print("3. Поиск контакта по фамилии")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выход")

        choice = input()
        
        if choice == '1':
            name = input("Введите фамилию контакта: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(phonebook, name, phone_number)
        elif choice == '2':
            display_all_contacts(phonebook)
        elif choice == '3':
            name = input("Введите фамилию для поиска: ")
            search_contact(phonebook, name)
        elif choice == '4':
            name = input("Введите фамилию контакта для изменения: ")
            new_phone_number = input("Введите новый номер телефона: ")
            edit_contact(phonebook, name, new_phone_number)
        elif choice == '5':
            name = input("Введите фамилию контакта для удаления: ")
            delete_contact(phonebook, name)
        elif choice == '6':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
