from os import walk, name as OS_NAME
from re import sub
from time import time
from codecs import open as codecsOpen


TOP_DIR = 'C:\\Users\\Edvin\\Music'
SEP = '    '
ARTIST_COUNT = 0
ALBUM_COUNT = 0


def writeLineInFile(path, dat):

    global ARTIST_COUNT
    global ALBUM_COUNT
    depth = path.count('\\')

    if depth > 0:
        line = sub('[^\\\\]*\\\\', '', path, count=depth)
    else:
        print('  Error in calculating path depth. Exiting.')
        dat.close()
        exit()

    if depth == 1:
        line = '- ' + line
        ARTIST_COUNT += 1

    elif depth == 2:
        line = SEP + '- ' + line
        ALBUM_COUNT += 1

    else:
        if userOtherDirs == 1:
            line = SEP * (depth-1) + '- ' + line
        else:
            return

    dat.write(line + '\n')

    return


def dirToFile():

    firstDir = True
    topDirLen = len(TOP_DIR)

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
            path = root[topDirLen:]    # remove the TOP_DIR substring
            writeLineInFile(path, dat)

    dat.write('\n----------\n\n')
    dat.write('- No. of artists: **' + str(ARTIST_COUNT) + '**\n')
    dat.write('- No. of albums: **' + str(ALBUM_COUNT) + '**')

    dat.close()

    return


if __name__ == "__main__":

    if OS_NAME == 'nt':    # windows

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

    else:

        print('  Program not supported for your OS. Exiting.')
        exit()