#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

import sys
from regexparser import Regex
from token import Token

"""class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        #self.next = None
"""

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

possible_tokens = []
r = Regex()

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

def check_tokens_for_substring(substr):
    #print("substr -> [%s]" % substr)
    global possible_tokens
    for token in Token:
        if (r.isvalid(substr, token) == True):
            possible_tokens.append(token)
            #print(token.name)
            return True
    return False

def generate_token_for_substring(substr):
    print("generate token %s for [%s]" % (possible_tokens[-1], substr))

def lexical_analysis(file_content):
    global possible_tokens
    i = 0
    file_length = len(file_content)
    while i < file_length:
        #print("i[%d]" % i)
        j = i + 1
        while j <= file_length:
            #print("j[%d]" % j)
            exists = check_tokens_for_substring(file_content[i:j])
            if not exists:
                if not possible_tokens: # remplacer par une vérification du tableau "if tab is empty"
                    print("une erreur ouesh")
                else:
                    generate_token_for_substring(file_content[i:j - 1])
                    possible_tokens = []
                    i = j - 2
                break
            j += 1
        i += 1

def main():
    if check_args() == False:
        sys.exit("USAGE: python3 %s <file_to_analyze>" % sys.argv[0])
    file_content = get_file_content()
    lexical_analysis(file_content)

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()