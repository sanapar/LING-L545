# Tokenizer

import sys
import re

infile = sys.stdin.readline()

sentence_idx = 1

while infile != '':
    print('sentence ID =', sentence_idx)
    sentence_idx += 1
    comma = infile.replace(',', ' , ')
    period = comma.replace('.', ' .')
    par1 = period.replace('(', ' ( ')
    par2 = par1.replace(')', ' ) ')
    par3 = re.sub('  *', ' ', par2)
    print('sentence =', par3)
    sentence = par3.split(' ')
    index = 1
    for i in sentence:
        if i != '.':
            print (index, i, '  _', '   _', '   _', '   _', '   _', '   _', '   _', '   _')
            index += 1
        else:
            print (index, '.', '  _', '   _', '   _', '   _', '   _', '   _', '   _', '   _')
    infile = sys.stdin.readline()
