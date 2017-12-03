##fin = None
##try:    
##    fin = open('chapter_files.py')
##    for line in fin:
##        print(line)
##except:
##    print('Something went wrong.')
##finally:
##    print('cleaning up')
##    if fin is not None:
##        print('closing the file')
##        fin.close()

fin = None
try:
    print('TRY: open file.')
    fin = open('bad_file')
    print('--> file open successfully.')
except:
    print('EXCEPT: Something went wrong.')
else:
    print('ELSE: Do your thing if all went well.')
    for line in fin:
        print('-->', line)    
finally:
    print('FINALLY: cleaning up.')
    if fin is not None:
        print('--> closing the file.')
        fin.close()
##try:
####    with open('chapter_files.py') as fin:
##    with open('bad_file') as fin:
##        for line in fin:
##            print(line)    
##except:
##    print('Something went wrong.')
        
