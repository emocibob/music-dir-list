from os import walk, path, name
from re import sub
from time import time
from codecs import open as codecsOpen

OS_NAME = name
TOP_DIR = '.'
SEP = '    '
FIRST_LINE = True
ARTIST_COUNT = 0
ALBUM_COUNT = 0

def dirDepth(path):

    if OS_NAME == 'nt':    # windows

        return path.count('\\')

    elif OS_NAME == 'posix':    # linux (among others)

        print('  Program not supported for your OS. Exiting.')
        exit()

    else:

        print('  Program not supported for your OS. Exiting.')
        exit()


def writeLineInFile(path, dat):

    # TODO add linux support
    global FIRST_LINE
    global ARTIST_COUNT
    global ALBUM_COUNT
    depth = dirDepth(path)

    if depth == 1:
        line = sub('[^\\\\]*\\\\', '', path)
        if FIRST_LINE:
            FIRST_LINE = False
        else:
            line = '\n' + line
        ARTIST_COUNT += 1


    elif depth == 2:
        line = sub('[^\\\\]*\\\\', '', path, count=2)
        line = SEP + '- ' + line
        ALBUM_COUNT += 1

    elif depth >= 3:
        if userOtherDirs == 1:
            path = sub('[^\\\\]*\\\\', '', path, count=depth)
            line = SEP * (depth-1) + '- ' + path
        else:
            return

    else:
        print('  Error during regex matching. Exiting.')
        dat.close()
        exit()

    dat.write(str(line + '\n'))

    return


def dirToFile():

    firstDir = True
    albumCount = 0
    artistCount = 0

    if userFileFormat == 1:
        dat = codecsOpen('music_list.txt', 'w', encoding='utf-8')
    elif userFileFormat == 2:
        dat = codecsOpen('music_list.md', 'w', encoding='utf-8')

    '''
    walk produces 3 values for every iteration: path to the dir, subdirs in that dir, files in that dir
    '''
    for root, dirs, files in walk(TOP_DIR):
        if firstDir:
            firstDir = False
            continue
        else:
            writeLineInFile(path.join(root), dat)

    dat.write('\n----------\n\n')
    dat.write('No. of artists: ' + str(ARTIST_COUNT) + '\n')
    dat.write('No. of albums: ' + str(ALBUM_COUNT))

    dat.close()

    return


if __name__ == "__main__":

    userFileFormat = int(input('  List in .txt [1] or .md [2] file? '))
    userOtherDirs = int(input('  List 3+ level directories (not artists or albums) [0 or 1]? '))

    startTime = time()

    if (userFileFormat in [1, 2]) and (userOtherDirs in [0, 1]):
        dirToFile()

    else:
        print('  Input error.')

    endTime = time()

    print('  Run time: ' + str(endTime - startTime) + ' s.')
    input('  Press any key to exit.')