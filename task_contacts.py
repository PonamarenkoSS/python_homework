# Телефонный справочник

def ask_user():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = int(input("Введите номер: "))
    return last_name, first_name, phone_number

def save_to_file(data: tuple, file, mode = 'a'):
    data_string = ' '.join(map(str, data))
    # 'cp-1251'
    with open(file, mode, encoding='utf-8') as file_1:
        file_1.write(f'{data_string}\n')

def read_file(file):
    with open(file, 'r', encoding='utf-8') as file_1:
        lines = file_1.readlines()
        # print(lines)
        headers = ['Фамилия', 'Имя', 'Номер телефона']
        list_contacts = []
        for line in lines:
            # line.replace('\n', '')
            line = line.strip().split()
            list_contacts.append(dict(zip(headers, line)))
        return list_contacts

def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in list_contacts:
        if contact[param_dict[param]] == what:
            found_contacts.append(contact)
    return found_contacts

def ask_search():
    print('По какому полю выполнить поиск?')
    search_param = input('1 - фамилия, 2 - имя, 3 - номер телефона: ')
    what = None
    if search_param == '1':
        what = input('Введите фамилию для поиска: ')
    elif search_param == '2':
        what = input('Введите имя для поиска: ')
    elif search_param == '3':
        what = input('Введите номер для поиска: ')
    return search_param, what

def del_contact(file):  
    input_delete_contact = input("Введите фамилию, имя или номер для поиска удаляемого контакта: ")
    line_delete = None
    with open(file, 'r', encoding='utf-8') as file_1:
        lines = file_1.readlines()
        for line in lines:
            if input_delete_contact in line:
                line_delete = line
                print(f'Удаляемый контакт: {line_delete}')
        file_1.close()
    print("Удалить этот контакт?")
    input_choise = int(input("Введите 1, если хотите удалить этот контакт: "))
    if input_choise == 1:
        with open(file, 'w', encoding='utf-8') as file_1:
            for line in lines:
                if line != line_delete:
                    file_1.write(line)
        print("Контакт удален") 

def change_contact(file):
    input_change_contact = input("Введите фамилию, имя или номер для поиска изменяемого контакта: ")
    line_change = None
    with open(file, 'r', encoding='utf-8') as file_1:
        lines = file_1.readlines()
        for line in lines:
            if input_change_contact in line:
                line_change = line
                print(f'Изменяемый контакт: {line_change}')
        file_1.close()
    print("Изменить этот контакт?")
    input_choise = int(input("Введите 1, если хотите изменить этот контакт: "))
    if input_choise == 1:
        with open(file, 'w', encoding='utf-8') as file_1:
            for line in lines:
                if line != line_change:
                    file_1.write(line)
                else:
                    file_1.write(input("Введите измененные фамилию, имя и номер контакта: "))
        print("Контакт изменён") 

def main_menu():
    while True:
        user_choice = input('1 - добавить новый контакт\n 2 - найти контакт\n 3 - посмотреть все контакты\n 4 - удалить контакт\n 5 - изменить контакт\n 0 - выйти: ')
        if user_choice == '1':
            save_to_file(ask_user(), file_contacts)
        elif user_choice == '2':
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
        elif user_choice == '3':
            lst_contacts = read_file(file_contacts)
            print(lst_contacts)
        elif user_choice == '4':
            del_contact(file_contacts)
        elif user_choice == '5':
            change_contact(file_contacts)    
        elif user_choice == '0':
            print("До свидания")
            break

if __name__ == '__main__':
    file_contacts = 'file.txt'
    main_menu()

