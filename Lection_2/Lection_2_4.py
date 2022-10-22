"""
Лекция 2.4.
Модули filecmp, zipfile, shutil
"""

# чонстые модули
import filecmp # сравнение файлов
import os
import shutil # дополнительные инструменты (утилиты) для работы с консолью
import tempfile # позволяет создавать временные папки/файлы, а потом их автоматически удаляет, они сохран в папке Temp
import zipfile # создает архивы
from pathlib import Path

files_dir = Path("files")

# сравнение файлов, по их путям
result = filecmp.cmp(
    files_dir / "file.txt",
    files_dir / "file2.txt"
)
print(result)

# сравнивает папки с файлами и смотрит на те файлы, кот вы укажете в 3 аргументе
# функция возвращает 3 списка : match (файлы одинак), mismatch (файлы неодинак), errors (ошибки)
result2 = filecmp.cmpfiles(
    "files", "files2", ['file.txt', 'file2.txt', 'file3.txt']
)
# print(result2)
match, mismatch, errors = result2
print(match, mismatch, errors)

# shutil
# shutil.rmtree("files2")  # удаление папки
# os.rmdir("files") # при удалении возникнет ошибка, так как папка не пустая и сначала придется удалить все файлы из нее
# shutil.copytree('files', 'files3') # копирует дерево папок из одного места в другое (папка источник, папка назначения), сам создает папку назначения
# os.copy() не может копировать папку целиком, только отдельные файлы
print(shutil.disk_usage('.')) # показывает использование дискового пр-ва на компе,
# в параметре нужно указать путь до какого-то файла/папки, чтобы программа узнала на каком диске мы находимся

# tempfile
with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_file: # класс, который созд врем файл с именем и расширением
    print(temp_file.name)  # адрес файла
    with zipfile.ZipFile(temp_file, 'w') as zipfile:  # открываем на запись (идентификатор доступа), как обычный файл
        zipfile.write(files_dir / 'file.txt', "file.txt")
        zipfile.write(files_dir / 'file2.txt', "file2.txt")
        # чтобы отредактировать несколько строк сразу, нажимаем Alt и ставим курсор в нужные места
        # архива нет, так как временный файл по умолчанию при выходе из менеджнра контекста удаляется
        # delete=False
        # unzip в консоли распакует архвив в папку с кодом
        # временные файлы периодически удаляет сама операционная система
        # так что не страшно, что мы не удалили архив
        # но лучше так не делать

