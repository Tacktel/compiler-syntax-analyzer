#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

import sys
from regexparser import Regex
from token import Token

possible_tokens = []
tokens_list = []
r = Regex()
charval_state = False
current_line = 1

#
# Check if two arguments were provided to the program
#
def check_args():
    if len(sys.argv) != 2:
        return False
    return True

#
# Open the file and return it's content as a string
#
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

#
# Fill the "possible_tokens" list with the token names validated
# by the regex parser for the substring received as param
#
def check_tokens_for_substring(substr):
    global possible_tokens
    global r
    global charval_state
    if (not charval_state and substr == "\""):
        charval_state = True
        possible_tokens.append(Token.T_CHARVAL)
        return True
    elif (charval_state and substr[-1] == "\""):
        charval_state = False
        if not r.is_valid(substr, Token.T_CHARVAL):
            possible_tokens = []
            return False
        possible_tokens.append(Token.T_CHARVAL)
        return True
    elif (charval_state):
        possible_tokens.append(Token.T_CHARVAL)
        return True
    else:
        for token in Token:      
            if (not charval_state and r.is_valid(substr, token) == True):
                if (token not in possible_tokens):
                    possible_tokens.append(token)
                return True
    return False

#
# Append the token name and its value for a specific substring to the "tokens_list" var
# using the "possible_tokens" list
#
def generate_token_for_substring(substr):
    global possible_tokens
    global current_line
    if possible_tokens[-1].name == "T_WSPACE":
        tokens_list.append("%s" % possible_tokens[-1].name[2:])
        current_line += substr.count('\n')
    else:
        tokens_list.append("%s:%s" % (possible_tokens[-1].name[2:], substr))
    possible_tokens = []

#
# Exit the program and print a string
#
def exit_error(content):
    sys.exit("Error detected at line %d: [%s]" % (current_line, content))

#
# main logic, read the file content with a window contained by i and j
#
def lexical_analysis(file_content):
    global possible_tokens
    i = 0
    file_length = len(file_content)
    while i < file_length:
        j = i + 1
        while j <= file_length:
            exists = check_tokens_for_substring(file_content[i:j])
            if not exists:
                if not possible_tokens:
                    exit_error(file_content[i:j])
                    if i + 1 < j:
                        i = j - 1
                else:
                    generate_token_for_substring(file_content[i:j - 1])
                    i = j - 2
                break
            elif j == file_length:
                if charval_state:
                    exit_error(file_content[i:j])
                elif exists:
                    generate_token_for_substring(file_content[i:j])
                return
            j += 1
        i += 1

#
# open/create a .out file to write the tokens in it
#
def write_to_file():
    file_name = "%s.out" % sys.argv[1][:-2]
    try:
        file = open(file_name, "w+")
    except IOError:
        sys.exit("Error while opening file %s" % file_name)
    if file.mode == "w+":
        for token in tokens_list:
            file.write("%s\n" % token)
    else:
        sys.exit("Error while writing to file %s" % file_name)

def main():
    if check_args() == False:
        sys.exit("USAGE: python3 %s <file_to_analyze>" % sys.argv[0])
    file_content = get_file_content()
    lexical_analysis(file_content)
    write_to_file()

if __name__ == '__main__':
    main()