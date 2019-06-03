#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

import sys

translation_table = {
    "INT": "vtype",
    "CHAR": "vtype",
    "INTVAL": "num",
    "CHARVAL": "literal",
    "RETURN": "return",
    "IF": "if",
    "ELSE": "else",
    "WHILE": "while",
    "ID": "id",
    "ASSIGN": "assign",
    "COMP": "comp",
    "TERM": "semi",
    "LSCOPE": "lbrace",
    "RSCOPE": "rbrace",
    "LPAREN": "lparen",
    "RPAREN": "rparen",
    "COMMA": "comma"
}

tokens = []

slr = [
	["", "vtype", "num", "literal", "id", "if", "else", "while", "return", "addsub", "multdiv", "assign", "comp", "semi", "comma", "lparen", "rparen", "lbrace", "rbrace", "$", "CODE", "VDECL", "FDECL", "ARG", "MOREARGS", "BLOCK", "STMT", "RHS", "EXPR", "TERM", "FACTOR", "COND", "RETURN"], 
	[1, "S6", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 86, 3, 4, "", "", "", "", "", "", "", "", "", ""], 
	[2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(1)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[3, "S6", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(1)", 2, 3, 4, "", "", "", "", "", "", "", "", "", ""], 
	[4, "S6", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(1)", 5, 3, 4, "", "", "", "", "", "", "", "", "", ""], 
	[5, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(1)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[6, "", "", "", "S7", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[7, "", "", "", "", "", "", "", "", "", "", "", "", "S8", "", "S9", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[8, "R(2)", "", "", "R(2)", "R(2)", "", "R(2)", "R(2)", "", "", "", "", "", "", "", "", "", "R(2)", "R(2)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[9, "S25", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S10", "", "", "", "", "", "", 17, "", "", "", "", "", "", "", "", ""], 
	[10, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S11", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[11, "S6", "", "", "S79", "S37", "", "S59", "S32", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", 12, 35, "", "", "", "", "", 15], 
	[12, "", "", "", "", "", "", "", "S32", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 13], 
	[13, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S14", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[14, "R(3)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(3)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[15, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S16", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[16, "R(3)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(3)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[17, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S18", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[18, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S19", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[19, "S6", "", "", "S79", "S37", "", "S59", "S32", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", 20, 35, "", "", "", "", "", 23], 
	[20, "", "", "", "", "", "", "", "S32", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 21], 
	[21, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S22", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[22, "R(3)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(3)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[23, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S24", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[24, "R(3)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(3)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[25, "", "", "", "S26", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[26, "", "", "", "", "", "", "", "", "", "", "", "", "", "S28", "", "R(4)", "", "", "", "", "", "", "", 27, "", "", "", "", "", "", "", ""], 
	[27, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(4)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[28, "S29", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[29, "", "", "", "S30", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[30, "", "", "", "", "", "", "", "", "", "", "", "", "", "S28", "", "R(5)", "", "", "", "", "", "", "", 31, "", "", "", "", "", "", "", ""], 
	[31, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(5)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[32, "", "S78", "", "S85", "", "", "", "", "", "", "", "", "", "", "S75", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 33, "", ""], 
	[33, "", "", "", "", "", "", "", "", "", "", "", "", "S34", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[34, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(15)", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[35, "S6 or R(6)", "", "", "S79", "S37", "", "S59", "R(6)", "", "", "", "", "", "", "", "", "", "R(6)", "R(6)", "", "", "", "", "", 36, 35, "", "", "", "", "", ""], 
	[36, "R(6)", "", "", "", "", "", "", "R(6)", "", "", "", "", "", "", "", "", "", "R(6)", "R(6)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[37, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S38", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[38, "", "S78", "", "S85", "", "", "", "", "", "", "", "", "", "", "S75", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 56, 39, ""], 
	[39, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S40", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[40, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S41", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[41, "S6", "", "", "S79", "S37", "", "S59", "", "", "", "", "", "", "", "", "", "", "S42", "", "", 3, "", "", "", 49, 35, "", "", "", "", "", ""], 
	[42, "", "", "", "", "", "S43", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[43, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S44", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[44, "S6", "", "", "S79", "S37", "", "S59", "", "", "", "", "", "", "", "", "", "", "S47", "", "", 3, "", "", "", 45, 35, "", "", "", "", "", ""], 
	[45, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S46", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[46, "R(8)", "", "", "R(8)", "R(8)", "", "R(8)", "R(8)", "", "", "", "", "", "", "", "", "", "R(8)", "R(8)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[47, "R(8)", "", "", "R(8)", "R(8)", "", "R(8)", "R(8)", "", "", "", "", "", "", "", "", "", "R(8)", "R(8)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[48, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S62", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[49, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S50", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[50, "", "", "", "", "", "S51", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[51, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S52", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[52, "S6", "", "", "S79", "S37", "", "S59", "", "", "", "", "", "", "", "", "", "", "S55", "", "", 3, "", "", "", 53, 35, "", "", "", "", "", ""], 
	[53, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S54", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[54, "R(8)", "", "", "R(8)", "R(8)", "", "R(8)", "R(8)", "", "", "", "", "", "", "", "", "", "R(8)", "R(8)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[55, "R(8)", "", "", "R(8)", "R(8)", "", "R(8)", "R(8)", "", "", "", "", "", "", "", "", "", "R(8)", "R(8)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[56, "", "", "", "", "", "", "", "", "", "", "", "S57", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[57, "", "S78", "", "S85", "", "", "", "", "", "", "", "", "", "", "S75", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 58, "", ""], 
	[58, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(14)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[59, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S60", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[60, "", "S78", "", "S85", "", "", "", "", "", "", "", "", "", "", "S75", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 72, 61, ""], 
	[61, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S48", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[62, "S6", "", "", "S79", "S37", "", "S59", "", "", "", "", "", "", "", "", "", "", "S65", "", "", 3, "", "", "", 63, 35, "", "", "", "", "", ""], 
	[63, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S64", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[64, "R(9)", "", "", "R(9)", "R(9)", "", "R(9)", "R(9)", "", "", "", "", "", "", "", "", "", "R(9)", "R(9)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[65, "R(9)", "", "", "R(9)", "R(9)", "", "R(9)", "R(9)", "", "", "", "", "", "", "", "", "", "R(9)", "R(9)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[66, "", "", "", "", "", "", "", "", "S67", "", "", "", "R(11)", "", "", "R(11)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[67, "", "S78", "", "S85", "", "", "", "", "", "", "", "", "", "", "S75", "", "", "", "", "", "", "", "", "", "", "", "", 68, 66, 69, "", ""], 
	[68, "", "", "", "", "", "", "", "", "", "", "", "", "R(11)", "", "", "R(11)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[69, "", "", "", "", "", "", "", "", "R(12)", "S70", "", "", "R(12)", "", "", "R(12)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[70, "", "S78", "", "S85", "", "", "", "", "", "", "", "", "", "", "S75", "", "", "", "", "", "", "", "", "", "", "", "", "", 71, 69, "", ""], 
	[71, "", "", "", "", "", "", "", "", "R(12)", "", "", "", "R(12)", "", "", "R(12)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[72, "", "", "", "", "", "", "", "", "", "", "", "S73", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[73, "", "S78", "", "S85", "", "", "", "", "", "", "", "", "", "", "S75", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 74, "", ""], 
	[74, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(14)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[75, "", "S78", "", "S85", "", "", "", "", "", "", "", "", "", "", "S75", "", "", "", "", "", "", "", "", "", "", "", "", 76, 66, 69, "", ""], 
	[76, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "S77", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[77, "", "", "", "", "", "", "", "", "R(13)", "R(13)", "", "R(13)", "R(13)", "", "", "R(13)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[78, "", "", "", "", "", "", "", "", "R(13)", "R(13)", "", "R(13)", "R(13)", "", "", "R(13)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[79, "", "", "", "", "", "", "", "", "", "", "S80", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[80, "", "S78", "S84", "S85", "", "", "", "", "", "", "", "", "", "", "S75", "", "", "", "", "", "", "", "", "", "", "", 81, 83, 66, 69, "", ""], 
	[81, "", "", "", "", "", "", "", "", "", "", "", "", "S82", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[82, "R(7)", "", "", "R(7)", "R(7)", "", "R(7)", "R(7)", "", "", "", "", "", "", "", "", "", "R(7)", "R(7)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[83, "", "", "", "", "", "", "", "", "", "", "", "", "R(10)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[84, "", "", "", "", "", "", "", "", "", "", "", "", "R(10)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[85, "", "", "", "", "", "", "", "", "R(13)", "R(13)", "", "R(13)", "R(13)", "", "", "R(13)", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
	[86, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "R(0)", "", "", "", "", "", "", "", "", "", "", "", "", ""], 
]

cfg = [
    ["S",
    ["CODE"],
    ],

    ["CODE",
    ["VDECL","CODE"],
    ["FDECL","CODE"],
    ["VDECL"],
    ["FDECL"],
    ],

    ["VDECL",
    ["vtype","id","semi"]
    ],

    ["FDECL",
    ["vtype","id","lparen","ARG","rparen","lbrace","BLOCK","RETURN","rbrace"],
    ["vtype","id","lparen","rparen","lbrace","BLOCK","RETURN","rbrace"],
    ["vtype","id","lparen","ARG","rparen","lbrace","RETURN","rbrace"],
    ["vtype","id","lparen","rparen","lbrace","RETURN","rbrace"],
    ],

    ["ARG",
    ["vtype","id","MOREARGS"],
    ["vtype","id"],
    ],

    ["MOREARGS",
    ["comma","vtype","id","MOREARGS"],
    ["comma","vtype","id"],
    ],

    ["BLOCK",
    ["STMT","BLOCK"],
    ["STMT"],
    ],

    ["STMT",
    ["VDECL"],
    ["id","assign","RHS","semi"],
    ],

    ["STMT",
    ["if","lparen","COND","rparen","lbrace","BLOCK","rbrace","else","lbrace","BLOCK","rbrace"],
    ["if","lparen","COND","rparen","lbrace","rbrace","else","lbrace","BLOCK","rbrace"],
    ["if","lparen","COND","rparen","lbrace","BLOCK","rbrace","else","lbrace","rbrace"],
    ["if","lparen","COND","rparen","lbrace","rbrace","else","lbrace","rbrace"],
    ],

    ["STMT",
    ["while","lparen","COND","rparen","lbrace","BLOCK","rbrace"],
    ["while","lparen","COND","rparen","lbrace","rbrace"],
    ],

    ["RHS",
    ["EXPR"],
    ["literal"],
    ],

    ["EXPR",
    ["TERM","addsub","EXPR"],
    ["TERM"],
    ],

    ["TERM",
    ["FACTOR","multdiv","TERM"],
    ["FACTOR"],
    ],

    ["FACTOR",
    ["lparen","EXPR","rparen"],
    ["id"],
    ["num"],
    ],

    ["COND",
    ["FACTOR","comp","FACTOR"],
    ],

    ["RETURN",
    ["return","FACTOR","semi"],
    ],
]

stack = [1,]
current_state = 1
next_sym = None
shift_cursor = 0

def get_col_of(string):
    index = 0
    for key in slr[0]:
        if key == string:
            return index
        index += 1

def next_step(state):
    nxt = slr[state][get_col_of(next_sym)]
    return nxt

def next_step_with_prev_sym(prev_sym):
    index = 0
    for key in slr[0]:
        if key == prev_sym:
            return slr[current_state][index]
        index += 1

def parse_next(nxt):
    if nxt == "":
        return None
    elif type(nxt) is str and nxt[0] == 'S':
        return ['S', int(nxt[1:])]
    elif type(nxt) is str and  nxt[0] == 'R':
        return ['R', int(nxt[2:-1])]
    else:
        return ['G', nxt]

def do_shift(state):
    global shift_cursor
    global current_state

    shift_cursor += 1           # shift
    stack.append(state)         # add state to stack
    current_state = stack[-1]   # get top of stack

def find_right_statement(cfg_state):
    statement_index = 0
    for state in cfg[cfg_state]:
        if statement_index >= 1:
            i = len(state) - 1
            j = shift_cursor - 1
            while i >= 0 and j >= 0:
                if state[i] != tokens[j]:
                    break
                i -= 1
                j -= 1
            if i == -1:
                return statement_index
        statement_index += 1

    return 0

def reduce_statement(cfg_state, index):
    global shift_cursor

    state = cfg[cfg_state][index]
    i = shift_cursor - len(state)
    j = len(state)
    count = 0
    while count < j:
        tokens.pop(i)
        stack.pop()
        count += 1
    tokens.insert(i, cfg[cfg_state][0])
    shift_cursor = i + 1

def do_reduce(cfg_state):
    global current_state
    right_statement = find_right_statement(cfg_state)   # find the good one
    if right_statement == 0:
        error = "Syntax invalid1: "
        sys.exit(error)
    reduce_statement(cfg_state, right_statement)
    current_state = stack[-1]

def do_goto(state):
    global current_state

    stack.append(state)
    current_state = stack[-1]

def check_syntax():
    global next_sym

    reduced = False
    while tokens != ["S","$"]:
        
        next_sym = tokens[shift_cursor]
        if reduced == False:
            nxt = next_step(current_state) # get content from the table
            decision = parse_next(nxt)     # parse into tuple [R/S, value]
            if decision == None:
                error = "Syntax invalid2: "
                sys.exit(error)
            elif decision[0] == 'S':
                do_shift(decision[1])

            elif decision[0] == 'R':
                do_reduce(decision[1])
                reduced = True
        else:
            nxt = next_step_with_prev_sym(tokens[shift_cursor - 1]) # get content from the table
            decision = parse_next(nxt)
            do_goto(decision[1])
            reduced = False
        print(tokens)

def check_args():
    if len(sys.argv) != 2:
        return False
    return True

def fill_tokens():
    try:
        file = open(sys.argv[1], "r")
    except IOError:
        sys.exit("Error while opening file %s" % sys.argv[1])
    if file.mode == "r":
        for line in file:
            try:
                (token_type, token_value) = line.split(':')
                if token_type != "OP":
                    tokens.append(translation_table[token_type])
                elif token_value == "+\n" or token_value == "-\n":
                    tokens.append("addsub")
                elif token_value == "*\n" or token_value == "/\n":
                    tokens.append("multdiv")
            except ValueError:
                continue
        tokens.append("$")
    else:
        sys.exit("Error while reading file %s" % sys.argv[1])

def main():
    global tokens

    if check_args() == False:
        sys.exit("USAGE: python3 %s <file_to_analyze>" % sys.argv[0])
    fill_tokens()
    tokens = ["vtype","id","lparen","rparen","lbrace","id","assign","num","semi","return","num", "semi","rbrace","$"]
    print(tokens)
    check_syntax()
    print("Syntax is valid!")

if __name__ == '__main__':
    main()