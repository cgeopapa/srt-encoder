from os import walk
from os import listdir
from os.path import abspath
from os.path import dirname
from os.path import splitext
from io import open
from os.path import join
from msvcrt import getch


def convert(path):
    try:
        with open(path, mode='r', encoding='UTF-8') as file:
            content = file.read()
            file.close

        with open(path, mode='w', encoding='cp1253') as file:
            file.write(content)
            file.close
    except UnicodeDecodeError:
        print('srt file is in correct format')
    except:
        print('This file has a problem. Take a look at it')


dirs = walk(dirname(abspath(__file__)))
for x in dirs:
    for file in x[2]:
        if splitext(file)[1] == '.srt':
            print('Converting: ' + file)
            convert(join(x[0], file))
print('Press any key to exit...')
getch()
