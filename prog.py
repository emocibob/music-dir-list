from os import walk, name as osName
from re import sub
from time import time
from codecs import open as codecsOpen


OS_NAME = osName
TOP_DIR = 'C:\\Users\\Edvin\\Music'
SEP = '    '
FIRST_LINE = True
ARTIST_COUNT = 0
ALBUM_COUNT = 0


def dirDepth(path):

    if OS_NAME == 'nt':    # windows
        return path.count('\\')
    else:
        print('  Program not supported for your OS. Exiting.')
        exit()


def writeLineInFile(path, dat):

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
        print('  Error in calculating path depth. Exiting.')
        dat.close()
        exit()

    dat.write(line + '\n')

    return


def dirToFile():

    firstDir = True

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
            path = root[len(TOP_DIR):]    # remove the TOP_DIR substring
            writeLineInFile(path, dat)

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