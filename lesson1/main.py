import os

# print(os.name)

# print(os.getcwd())
# os.chdir('files')
# print(os.getcwd())
#
# print(os.access('1.txt', os.F_OK))
# print(os.access('1.txt', os.R_OK))
# print(os.access('wfgsfghysfjk.txt', os.F_OK))
#
# os.chdir('..')
# print(os.getcwd())
# print(os.listdir())

# for currentdir, dirs, files in os.walk('files'):
#     print(currentdir, dirs, files)

print(os.path.exists('files/3'))
print(os.path.isdir('files/3'))
print(os.path.abspath('files'))