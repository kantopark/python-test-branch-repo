import sys
from os import getenv

if __name__ == '__main__':
    code = int(getenv("exit_code", "0"))
    print("%s has exit code: %d" % (sys.argv[0], code))

    exit(code)
