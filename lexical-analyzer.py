#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

import sys

class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        #self.next = None

""" class LinkedList:
    def __init__(self):
        self.head_val = None

    def print_list(self):
        node = self.head_val
        while node is not None:
            print("[%s - %s]" % (node.name, node.value))
            node = node.next

    def append_to_list(self, name, value):
        new_token = Token(name, value)
        if self.head_val is None:
            self.head_val = new_token
            return
        current_token = self.head_val
        while (current_token.next):
            current_token = current_token.next
        current_token.nextval = new_token """

tokens = []

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