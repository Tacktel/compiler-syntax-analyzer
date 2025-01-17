#
# Compiler Term Project 1
#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

from enum import Enum

class Token(Enum):
    T_INT = 1
    T_CHAR = 2
    T_INTVAL = 3
    T_CHARVAL = 4
    T_RETURN = 5
    T_IF = 6
    T_ELSE = 7
    T_WHILE = 8
    T_ID = 9
    T_OP = 10
    T_ASSIGN = 11
    T_COMP = 12
    T_TERM = 13
    T_LSCOPE = 14
    T_RSCOPE = 15
    T_LPAREN = 16
    T_RPAREN = 17
    T_COMMA = 18
    T_WSPACE = 19

class Tokenvalue():

    t_int = {
        "key" : ['i','n','t','I','N','T'],
        "value" : [
            [1,0,0,4,0,0],
            [0,2,0,0,0,0],
            [0,0,3,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,5,0],
            [0,0,0,0,0,6],
            [0,0,0,0,0,0]
        ],
        "final" : [3,6]
    }

    t_char = {
        "key" : ['c','h','a','r','C','H','A','R'],
        "value" : [
            [1,0,0,0,5,0,0,0],
            [0,2,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0],
            [0,0,0,4,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,6,0,0],
            [0,0,0,0,0,0,7,0],
            [0,0,0,0,0,0,0,8],
            [0,0,0,0,0,0,0,0],
        ],
        "final" : [4, 8]
    }

    t_intval = {
        "key" : ['0','-','nzdigit','digit'],
        "value" : [
            [1,2,3,0],
            [0,0,0,0],
            [0,0,3,0],
            [0,0,0,4],
            [0,0,0,4],
        ],
        "final" : [1,3,4]
    }

    t_charval = {
        "key" : ['"',"digit","letter"," "],
        "value" : [
            [1,0,0,0],
            [5,2,3,4],
            [5,2,3,4],
            [5,2,3,4],
            [5,2,3,4],
            [0,0,0,0],
        ],
        "final" : [5]
    }

    t_id = {
        "key" : ["letter","digit"],
        "value" : [
            [1,0],
            [3,2],
            [3,2],
            [3,2],
        ],
        "final" : [1,2,3]
    }

    t_if = {
        "key" : ['i','f','I','F'],
        "value" : [
            [1,0,3,0],
            [0,2,0,0],
            [0,0,0,0],
            [0,0,0,4],
            [0,0,0,0],
        ],
        "final" : [2, 4]
    }

    t_else = {
        "key" : ['e','l','s','e','E','L','S','E'],
        "value" : [
            [1,0,0,0,5,0,0,0],
            [0,2,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0],
            [0,0,0,4,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,6,0,0],
            [0,0,0,0,0,0,7,0],
            [0,0,0,0,0,0,0,8],
            [0,0,0,0,0,0,0,0],
        ],
        "final" : [4,8]
    }

    t_while = {
        "key" : ['w','h','i','l','e','W','H','I','L','E'],
        "value" : [
            [1,0,0,0,0,6,0,0,0,0],
            [0,2,0,0,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0,0],
            [0,0,0,4,0,0,0,0,0,0],
            [0,0,0,0,5,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,7,0,0,0],
            [0,0,0,0,0,0,0,8,0,0],
            [0,0,0,0,0,0,0,0,9,0],
            [0,0,0,0,0,0,0,0,0,10],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
        ],
        "final" : [5,10]
    }

    t_return = {
        "key" : ['r','e','t','u','r','n','R','E','T','U','R','N'],
        "value" : [
            [1,0,0,0,0,0,7,0,0,0,0,0],
            [0,2,0,0,0,0,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,0,0,0,0],
            [0,0,0,4,0,0,0,0,0,0,0,0],
            [0,0,0,0,5,0,0,0,0,0,0,0],
            [0,0,0,0,0,6,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,8,0,0,0,0],
            [0,0,0,0,0,0,0,0,9,0,0,0],
            [0,0,0,0,0,0,0,0,0,10,0,0],
            [0,0,0,0,0,0,0,0,0,0,11,0],
            [0,0,0,0,0,0,0,0,0,0,0,12],
            [0,0,0,0,0,0,0,0,0,0,0,0],
        ],
        "final" : [6,12]
    }

    t_op = {
        "key" : ['+','-','*','/'],
        "value" : [
            [1,2,3,4],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ],
        "final" : [1,2,3,4]
    }

    t_comp = {
        "key" : ['<','>','=','!'],
        "value" : [
            [1,2,3,4],
            [0,0,5,0],
            [0,0,5,0],
            [0,0,5,0],
            [0,0,5,0],
            [0,0,0,0],
        ],
        "final" : [1,2,5]
    }

    t_wspace = {
        "key" : ['\t','\n',' '],
        "value" : [
            [1,2,3],
            [1,2,3],
            [1,2,3],
            [1,2,3],
        ],
        "final" : [1,2,3]
    }

    t_assign = {
        "key" : ['='],
        "value" : [
            [1],
            [0],
        ],
        "final" : [1]
    }

    t_term = {
        "key" : [';'],
        "value" : [
            [1],
            [0],
        ],
        "final" : [1]
    }

    t_lscope = {
        "key" : ['{'],
        "value" : [
            [1],
            [0],
        ],
        "final" : [1]
    }

    t_rscope = {
        "key" : ['}'],
        "value" : [
            [1],
            [0],
        ],
        "final" : [1]
    }

    t_lparen = {
        "key" : ['('],
        "value" : [
            [1],
            [0],
        ],
        "final" : [1]
    }

    t_rparen = {
        "key" : [')'],
        "value" : [
            [1],
            [0],
        ],
        "final" : [1]
    }

    t_comma = {
        "key" : [','],
        "value" : [
            [1],
            [0],
        ],
        "final" : [1]
    }

    Tokentab = {
        Token.T_INT : t_int,
        Token.T_CHAR : t_char,
        Token.T_INTVAL : t_intval,
        Token.T_CHARVAL : t_charval,
        Token.T_ID : t_id,
        Token.T_IF : t_if,
        Token.T_ELSE : t_else,
        Token.T_WHILE : t_while,
        Token.T_RETURN : t_return,
        Token.T_OP : t_op,
        Token.T_ASSIGN : t_assign,
        Token.T_COMP : t_comp,
        Token.T_TERM : t_term,
        Token.T_LSCOPE : t_lscope,
        Token.T_RSCOPE : t_rscope,
        Token.T_LPAREN : t_lparen,
        Token.T_RPAREN : t_rparen,
        Token.T_COMMA : t_comma,
        Token.T_WSPACE : t_wspace,
    }
