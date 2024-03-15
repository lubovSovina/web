import shutil

# shutil.copy('files/3/Описание.txt', 'files/Копия.txt')
# shutil.rmtree('Путь до папки')
# shutil.move('files/3/Описание.txt', 'files/Копия.txt')

print(shutil.get_archive_formats())

shutil.make_archive('archive', 'zip', root_dir='files')