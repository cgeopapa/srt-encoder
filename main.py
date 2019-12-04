from os import walk
from os import listdir
from os.path import abspath
from os.path import dirname
from os.path import splitext
from io import open
from os.path import join

def main():
    dirs = walk(dirname(abspath(__file__)))
    for x in dirs:
        for file in x[2]:
            if splitext(file)[1] == '.srt':
                print('Converting: ' + file)
                convert(join(x[0], file))


def convert(path):
    try:
        with open(path, mode='rb') as file:
            content = file.read().decode('UTF-8')
            file.close
        with open(path, mode='w', encoding='cp1253', errors='ignore', newline='\n') as file:
            file.write(content)
            file.close
    except UnicodeDecodeError:
        print('srt file is in correct format')


if __name__ == "__main__":
    main()
