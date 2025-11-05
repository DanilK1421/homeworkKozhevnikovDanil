

word = input("Введите слово: ")
lenght = len(word)

if lenght % 2 == 0:
    print(word[lenght // 2 - 1 : lenght // 2 + 1])
else:
    print(word[lenght // 2])
