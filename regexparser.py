#
# Compiler Term Project 1
#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

from token import Token
from token import Tokenvalue
import sys

class Regex:

    def __get_tokentab(self, token):
        return Tokenvalue.Tokentab[token]

    def __is_digit(self, char):
        tab = ['0','1','2','3','4','5','6','7','8','9']
        return char in tab

    def __is_nzdigit(self, char):
        tab = ['1','2','3','4','5','6','7','8','9']
        return char in tab

    def __is_letter(self, char):
        tab = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        return char in tab

    def __is_valid_char(self, char, tokenkey):
        if tokenkey == "digit":
            return self.__is_digit(char)
        elif tokenkey == "nzdigit":
            return self.__is_nzdigit(char)
        elif tokenkey == "letter":
            return self.__is_letter(char)
        else:
            return char == tokenkey

    def is_valid(self, string, token):
        t = self.__get_tokentab(token)
        current_state = 0

        for i, char in enumerate(string):
            for index, tokenkey in enumerate(t["key"]):
                if self.__is_valid_char(char, tokenkey) and t["value"][current_state][index] != 0:
                    current_state = t["value"][current_state][index]
                    break
            else:
                if index + 1 >= len(t["key"]):
                    return False
        return current_state in t["final"]
