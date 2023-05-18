import os
try:
    os.remove('word_count.py')
except FileNotFoundError:
    print('File already removed')
