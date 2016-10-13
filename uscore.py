'''
underscore.py
Substitutes blanks with underscores for all files and directories in the
directory given by specified path. If the path was not specified, renames
entries in current working directory.
'''
import os
import re
import sys

def underscore(path):
    '''
    Substitutes blanks with underscores for all files
    and directories in the directory given by path.
    '''
    regex = re.compile(r'\s+')
    renamed = 0
    for entry in os.listdir(path):
        if ' ' in entry:
            underscored = regex.sub('_', entry)
            base, ext = os.path.splitext(underscored)
            underscored = base.strip('_')  + ext
            os.rename(os.path.join(path, entry),
                      os.path.join(path, underscored))
            renamed += 1
            print('{}) "{}" -> "{}"'.format(renamed, entry, underscored))


def main():
    if len(sys.argv) == 1:
        path = os.getcwd()
    else:
        path = sys.argv[1]
    underscore(path)


if __name__ == '__main__':
    main()
