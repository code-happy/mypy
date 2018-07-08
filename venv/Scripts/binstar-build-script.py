#!C:\Users\Together\PycharmProjects\untitled1\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'anaconda-build==0.14.0','console_scripts','binstar-build'
__requires__ = 'anaconda-build==0.14.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('anaconda-build==0.14.0', 'console_scripts', 'binstar-build')()
    )
