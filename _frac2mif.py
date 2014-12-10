import os

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def frac2bin(num, width):
    text = bin(num)
    if text.startswith("-"):
        return bin(int(text[3:], 2) - (1 << width))[3:]
    else:
        return text[2:].zfill(width)

def bin2hex(line):
    out = hex(int(line,2))[2:].upper()
    return '0' * (4 - len(out)) + out
        
def writebin(input):
    fin = open(input, 'r')
    bin16 = open('bin16' + input, 'w')

    for _ in range(0, file_len(input)):
        line = fin.readline()
        line = line.strip()
        num16 = int(float(line) * 10000)
        line16 = str(int(float(line) * 10000))
        bin16.write(frac2bin(num16, 16) + '\n')

    fin.close()
    bin16.close()
    os.remove(os.getcwd() + '\\' + input)

def writemif(temp):
    writebin(temp + '.txt')

    fin = open('bin16' + temp + '.txt', 'r')
    fmif = open(temp + '.mif', 'w')

    fmif.write('WIDTH=16;\nDEPTH=512;\n\nADDRESS_RADIX=UNS;\nDATA_RADIX=HEX;\n\nCONTENT BEGIN\n')
    
    for i in range(0, file_len('bin16' + temp + '.txt')):
        line = fin.readline().strip()
        fmif.write(str(i) + ' : ' + bin2hex(line) + ';\n')
        num = i + 1

    fmif.write('[' + str(num) + '..511] : 0000;\nEND;')
        
    fin.close()
    fmif.close()
    
writemif('X')
writemif('Y')
writemif('Z')

