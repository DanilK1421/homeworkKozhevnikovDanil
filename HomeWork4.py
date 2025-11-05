documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

while True:
    command = input("\nВведите команду: ")
    if command == "q":
        print("Пока")
        break
    elif command == "p":
        number = input("Введите номер документа: ")
        found = False
        for doc in documents:
            if doc['number'] == number:
                print(f"Владелец документа: {doc['name']}")
                found = True
                break
        if not found:
            print("Владелец документа: владелец не найден")