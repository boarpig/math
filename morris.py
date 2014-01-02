#!/usr/bin/python

def morris(n):
    morris = '1'
    merkki = ''
    buff = ''
    for i in range(n - 1):
        yield morris
        for i in morris:
            if merkki == '' or merkki[-1] == i:
                merkki += str(i)
            else:
                buff += str(len(merkki)) + str(merkki[0])
                merkki = str(i)
        buff += str(len(merkki)) + str(merkki[0])
        morris, merkki, buff = buff, '', ''
    yield morris

if __name__ == '__main__':
    for i in morris(6):
        print(i),
