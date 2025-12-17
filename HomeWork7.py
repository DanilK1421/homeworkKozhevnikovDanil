class Client:

    def __init__(self, name, sex, age, device_type, browser, bill, region):
        self.name = name
        self.sex = sex
        self.age = age
        self.device_type = device_type
        self.browser = browser
        self.bill = bill
        self.region = region


    def get_russian_sex(self):
        #Переводим на русский
        if self.sex == "female":
            return "женского"
        else:
            return "мужского"

    def get_russian_device(self):
        #Переводим на русский
        devices = {
            "mobile": "мобильного",
            "tablet": "планшета",
            "desktop": "десктопного",
            "laptop": "ноутбука"
        }
        return devices.get(self.device_type, self.device_type)

    def get_verb(self):
        if self.sex == "female":
            return "совершила"
        else:
            return "совершил"



    def get_description(self):
        try:
            age_str = str(int(float(self.age)))
        except:
            age_str = str(self.age)

        #Обрабатываем регион в данных есть так как есть -
        if self.region == "-":
            region_str = "не указан"
        else:
            region_str = self.region

        #Формируем описание
        description = (
            f"Пользователь {self.name} {self.get_russian_sex()} пола, "
            f"{age_str} лет {self.get_verb()} покупку на {self.bill} у.е. "
            f"с {self.get_russian_device()} браузера {self.browser}. "
            f"Регион, из которого совершалась покупка: {region_str}."
        )

        return description




def read_csv_file(filename):
    clients = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        #Пропускаем заголовок
        for line in lines[1:]:
            line = line.strip()
            if line:  # Проверяем строку что она не пустая
                clients.append(line)


    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

    return clients



def parse_client_data(line):
    #Разделяем строку по запятым
    parts = line.split(',')

    #Проверяем что у нас достаточно частей
    if len(parts) < 7:
        return None

    #Обрабатываем случай если имя содержит запятые
    if len(parts) > 7:
        #Объединяем первые части как имя
        name_parts = parts[:-6]
        name = ','.join(name_parts)
        device_type = parts[-6]
        browser = parts[-5]
        sex = parts[-4]
        age = parts[-3]
        bill = parts[-2]
        region = parts[-1]
    else:
        name = parts[0]
        device_type = parts[1]
        browser = parts[2]
        sex = parts[3]
        age = parts[4]
        bill = parts[5]
        region = parts[6]

    #Создаем client
    return Client(name, device_type, browser, sex, age, bill, region)


def generate_descriptions(filename):
    #генерации описаний

    lines = read_csv_file(filename)

    if not lines:
        return []

    descriptions = []

    for line in lines:
        client = parse_client_data(line)
        if client:
            description = client.get_description()
            descriptions.append(description)

    return descriptions


def save_to_file(descriptions, output_filename):
    #Сохраняем в txt
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            for i, description in enumerate(descriptions, 1):
                file.write(f"{description}\n\n")
        print(f"Файл {output_filename} успешно создан.")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")



def main():
    print("Программа для генерации описаний клиентов")

    input_filename = "web_clients_correct (1).csv"

    #Генерируем описания
    descriptions = generate_descriptions(input_filename)

    if descriptions:
        #Сохраняем в файл
        output_filename = "clients_descriptions.txt"
        save_to_file(descriptions, output_filename)

        #несколько примеров
        print("\nПримеры описаний:")
        for i in range(min(2, len(descriptions))):
            print(f"Пример {i + 1}:")
            print(descriptions[i])
            print()
    else:
        print("Не удалось сгенерировать описания.")


if __name__ == "__main__":
    main()