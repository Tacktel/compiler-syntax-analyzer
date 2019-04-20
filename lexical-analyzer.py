#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

import sys
from regexparser import Regex
from token import Token

possible_tokens = []
r = Regex()
charval_state = False

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
    global possible_tokens
    global r
    global charval_state
    #print("substr[%s]" % substr)
    if (not charval_state and substr == "\""):
        #print("A")
        charval_state = True
        possible_tokens.append(Token.T_CHARVAL)
        return True
    elif (charval_state and substr[-1] == "\""):
        #print("C")
        charval_state = False
        if not r.isvalid(substr, Token.T_CHARVAL):
            possible_tokens = []
            return False
        possible_tokens.append(Token.T_CHARVAL)
        return True
    elif (charval_state):
        #print("B")
        possible_tokens.append(Token.T_CHARVAL)
        return True
    else:
        for token in Token:      
            if (not charval_state and r.isvalid(substr, token) == True):
                if (token not in possible_tokens):
                    possible_tokens.append(token)
                return True
    return False

def generate_token_for_substring(substr):
    global possible_tokens
    if possible_tokens[-1].name == "T_WSPACE":
        print("%s" % possible_tokens[-1].name[2:])
    else:
        print("%s:%s" % (possible_tokens[-1].name[2:], substr))
    possible_tokens = []

def lexical_analysis(file_content):
    global possible_tokens
    i = 0
    file_length = len(file_content)
    while i < file_length:
        j = i + 1
        while j <= file_length:
            exists = check_tokens_for_substring(file_content[i:j])
            if not exists:
                #print("not exists")
                if not possible_tokens:
                    print("une erreur ouesh")
                    if i + 1 < j:
                        i = j - 1
                else:
                    #print("else")
                    generate_token_for_substring(file_content[i:j - 1])
                    i = j - 2
                break
            elif j == file_length:
                #print("elif")
                if exists:
                    #print("exists")
                    generate_token_for_substring(file_content[i:j])
                return
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