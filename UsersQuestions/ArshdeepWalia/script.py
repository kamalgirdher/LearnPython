
import os
import re


for fil in os.listdir('multi_input/'):
    with open('multi_input/' + fil) as f:
        fin = f.read()
        try:
            print(re.search(':20:(.*?):23B:',fin).group(1))
        except:
            print('Match not found')
        try:
            print(re.search('WCP(.*?)Commonwealth',fin).group(1))
        except:
            print('Match not found')
    print('------------')
    
