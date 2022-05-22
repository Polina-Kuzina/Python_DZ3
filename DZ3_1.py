# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".


my_str = 'Напишите прогабврамму, удабваляющую из текста все слова, содержащие'
my_str = my_str.split(' ')
result = ' '.join(list(filter(lambda word: word.find('абв') == -1, my_str)))
print(result)