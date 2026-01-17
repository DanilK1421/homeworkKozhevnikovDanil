import json

purchase_dict = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line.strip())
            user_id = data.get('user_id')
            category = data.get('category')

            if user_id and category:
                purchase_dict[user_id] = category
        except json.JSONDecodeError:
            continue

with open('visit_log__1_.csv', 'r', encoding='utf-8') as input_file, \
        open('funnel.csv', 'w', encoding='utf-8') as output_file:
    # Читаем заголовок из visit_log.csv
    header = input_file.readline().strip()

    output_file.write(f"{header},category\n")

    for line in input_file:
        line = line.strip()
        if not line:
            continue

        # Разделяем строку на user_id и source
        parts = line.split(',')
        if len(parts) < 2:
            continue

        user_id, source = parts[0], parts[1]

        # Проверяем, есть ли покупка для этого user_id
        if user_id in purchase_dict:
            category = purchase_dict[user_id]
            # Записываем строку в funnel.csv
            output_file.write(f"{user_id},{source},{category}\n")

print("Результат сохранен в файле funnel.csv")

#для проверки
print("\nПервые 5 строк из funnel.csv:")
with open('funnel.csv', 'r', encoding='utf-8') as f:
    for i in range(5):
        line = f.readline().strip()
        if line:
            print(line)