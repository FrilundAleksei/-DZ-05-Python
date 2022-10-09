# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".

my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из этого абв текста все вабвс слова, содерабващие содержащие "абв" заданный набор букв. Сделаноабв.'

print(f'Исходный текст: {my_text}')

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(f'Текст после изменений: {my_text}')
