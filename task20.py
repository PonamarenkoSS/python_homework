# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

scrable = {}
list_en_1 = 'A, E, I, O, U, L, N, S, T, R'.split(', ')
list_en_2 = 'D, G'.split(', ')
list_en_3 = 'B, C, M, P'.split(', ')
list_en_4 = 'F, H, V, W, Y'.split(', ')
list_en_5 = 'K'
list_en_8 = 'J, X'.split(', ')
list_en_10 = 'Q, Z'.split(', ')
for i in list_en_1:
    scrable.setdefault(i, 1)
for i in list_en_2:
    scrable.setdefault(i, 2)
for i in list_en_3:
    scrable.setdefault(i, 3)
for i in list_en_4:
    scrable.setdefault(i, 4)
for i in list_en_5:
    scrable.setdefault(i, 5)
for i in list_en_8:
    scrable.setdefault(i, 8)
for i in list_en_10:
    scrable.setdefault(i, 10)
list_ru_1 = 'А, В, Е, И, Н, О, Р, С, Т'.split(', ')
list_ru_2 = 'Д, К, Л, М, П, У'.split(', ')
list_ru_3 = 'Б, Г, Ё, Ь, Я'.split(', ')
list_ru_4 = 'Й, Ы'.split(', ')
list_ru_5 = 'Ж, З, Х, Ц, Ч'.split(', ')
list_ru_8 = 'Ш, Э, Ю'.split(', ')
list_ru_10 = 'Ф, Щ, Ъ'.split(', ')
for i in list_ru_1:
    scrable.setdefault(i, 1)
for i in list_ru_2:
    scrable.setdefault(i, 2)
for i in list_ru_3:
    scrable.setdefault(i, 3)
for i in list_ru_4:
    scrable.setdefault(i, 4)
for i in list_ru_5:
    scrable.setdefault(i, 5)
for i in list_ru_8:
    scrable.setdefault(i, 8)
for i in list_ru_10:
    scrable.setdefault(i, 10)    

text_input = input("Введите слово на русском или английском языке (используйте заглавные буквы): ")
sum_of_word = 0
for i in range(len(text_input)):
    sum_of_word += scrable.get(text_input[i])
print(f"Стоимость слова {text_input} составляет {sum_of_word} очков/очка.")