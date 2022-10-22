"""
Лекция 2.1.
Работа с файлами
"""

print("Файл MAIN.py:")
file = open("main.py", "r", encoding="utf-8")  # открываем файл только для чтения
print(file.read())  # читаем файл полностью от начала до конца, он схраняется в оперативной памяти
file.close()

# если файлы большие, они не поместятся в оперативную память, мы не сможем их сразу полностью прочитать
# будем читать файл построчно
print("Файл Lection_1_5.py:")
file = open("../Lection_1/Lection_1_5.py", "r", encoding="utf-8")
for line in file:
    # при выводе строк образуется 2 переноса
    # strip() убирает символы пустого места и переноса с начала и конца каждой строки
    print(line.strip())
file.close()

# чтобы не забыть закрыть файл, можно исп менеджер контекста
with open("../Lection_1/Lection_1_5.py", "r", encoding="utf-8") as file:
    # открывает файл
    for line in file:
        print(line.strip())
# закрывает файл

print("end")

# запись в файл в формате .txt
# они не несут смысловой нагрузки, поэтому сразу добавляем их в .gitignore
# *.txt

with open("file.txt", "w", encoding="utf-8") as file:
    file.write("123")

# открыть файл одновременно на чтение и на запись w+
with open("file.txt", "w+", encoding="utf-8") as file:
    file.write("123")
    # после выполнения этой функции указатель будет находится в конце файла, поэтому читать нечего
    # переносим указатель на начало файла
    file.seek(0)
    print(file.read())

# a открывает файл на дозапись, а+ позволяет читать файл во время записи
with open("file.txt", "a+", encoding="utf-8") as file:
    file.write("123")
    file.seek(0)
    print(file.read())
    file.write("123")
    file.seek(0)
    print(file.read())
    file.write("123")
    file.seek(0)
    print(file.read())

# rb, wb открывает файл в бинарнм виде
# x открывает файл на запись, но выдает исключение, если файла не существует
