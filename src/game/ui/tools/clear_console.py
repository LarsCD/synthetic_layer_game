import os
import sys

def clear_term() -> None:
    CLEAR = ''
    if sys.platform in ('linux', 'darwin'):
        CLEAR = 'clear'
    elif sys.platform == 'win32':
        CLEAR = 'cls'
    else:
        pass
    os.system(CLEAR)
