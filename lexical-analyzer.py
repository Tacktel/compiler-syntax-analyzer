#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

import sys

def check_args():
    if len(sys.argv) != 2:
        return False
    return True

def get_file_content():
    try:
        file = open(sys.argv[1], "r")
    except IOError:
        sys.exit("Error while opening file %s" % sys.argv[1])
    if file.mode == "r":
        file_content = file.read()
    else:
        sys.exit("Error while reading file %s" % sys.argv[1])

    return file_content

def main():
    if check_args() == False:
        sys.exit("USAGE: python3 %s <file_to_analyze>" % sys.argv[0])
    file_content = get_file_content()

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()