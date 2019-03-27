import sys
import re
from subprocess import Popen, PIPE
from src.main import run


def android():
    p = Popen([
        sys.executable, '-m', 'buildozer',
        'android', 'debug', 'deploy', 'run', 'logcat'
        ], stderr=PIPE
    )
    while p.stderr.readable():
        line = re.match(r'^.+python.+$', p.stderr.readline().decode('utf-8'))
        if line:
            print(*line.group(), sep='')


def start():
    run()


if __name__ == '__main__':
    run()
