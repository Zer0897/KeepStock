import sys
import re
import subprocess as subp
from src.main import run


def android():
    subp.run([
        sys.executable, '-m', 'buildozer', '-v',
        'android', 'debug', 'deploy', 'run', 'logcat'
        ])


def start():
    run()


if __name__ == '__main__':
    run()
