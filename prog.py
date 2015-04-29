from os import walk, path, name
from re import compile, sub, UNICODE
from time import time
from codecs import open as codecsOpen

OS_NAME = name
TOP_DIR = '.'
SEP = '    '


def writeLineInFile(path, dat):

    # TODO add working subs for linux

    if artistDir.match(path):
        line = sub('[^\\\\]*\\\\', '', path)

    elif albumDir.match(path):
        line = sub('[^\\\\]*\\\\', '', path, count=2)
        line = SEP + '- ' + line

    elif albumSubdirs.match(path):
        if userOtherDirs == 1:
            line = sub('[^\\\\]*\\\\', '', path, count=3)
            line = SEP + SEP + '- ' + line
        else:
            return

    else:
        print('Error during regex matching. Exiting.')
        dat.close()
        exit()

    dat.write(str(line + '\n'))

    return


def regexDirLevels():

    topDirRE = TOP_DIR.replace('.', '\.')

    if OS_NAME == 'nt':    # windows

        dirLevelRE = '(\\\\[^\\\\]+)'    # match '\something'
        artistDir = compile(topDirRE + dirLevelRE + '$', UNICODE)
        albumDir = compile(topDirRE + dirLevelRE + '{2}$', UNICODE)
        albumSubdirs = compile(topDirRE + dirLevelRE + '{3,}$', UNICODE)

    elif OS_NAME == 'posix':    # linux (among others)

        exit()
        # TODO fix linux support
        albumDir = compile('\./(.*?)/')
        albumSubdirs = compile('\./(.*?)/(.*?)/')

    else:

        print('Program not supported for your OS. Exiting.')
        exit()

    return artistDir, albumDir, albumSubdirs


def dirToFile():

    first = True

    if userFileFormat == 1:
        dat = codecsOpen('music_list.txt', 'w', encoding='utf-8')
    elif userFileFormat == 2:
        dat = codecsOpen('music_list.md', 'w', encoding='utf-8')

    '''
    walk produces 3 values for every iteration: path to the dir, subdirs in that dir, files in that dir
    '''
    for root, dirs, files in walk(TOP_DIR):
        if first:
            first = False
            continue
        else:
            writeLineInFile(path.join(root), dat)

    dat.close()

    return


artistDir, albumDir, albumSubdirs = regexDirLevels()
userFileFormat = int(input('List in .txt [1] or .md [2] file? '))
userOtherDirs = int(input('List 3+ level directories (not artists or albums) [0 or 1]? '))

startTime = time()

if (userFileFormat in [1, 2]) and (userOtherDirs in [0, 1]):
    dirToFile()

else:
    print('Input error.')

endTime = time()

print('Run time: ' + str(endTime - startTime) + ' s.')
input('Press any key to exit.')