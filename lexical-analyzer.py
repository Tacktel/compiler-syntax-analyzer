#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

import sys

def check_args():
    if len(sys.argv) != 2:
        return False
    return True

def main():
    if check_args() == False:
        sys.exit("USAGE: python3 %s <file_to_analyze>" % sys.argv[0])

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()