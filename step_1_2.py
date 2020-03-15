import sys
from os import getenv

if __name__ == '__main__':
    code = int(getenv("exit_code_1_2", "0"))
    print("%s has exit code: %d" % (sys.argv[0], code))

    if code != 0:
        print("An error message printed to std error", file=sys.stderr)
    exit(code)
