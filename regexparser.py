# Compiler Term Project 1
# Team 1
# Christophe Mei 50181587
# Leo Paol 50181573

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

    def isvalid(self, string, token):
        i = 0
        current_state = 0

        t = self.__get_tokentab(token)

        while i < len(string):
            # for each char of string
            for index, tokenkey in enumerate(t["key"]):
                #for each key char
                if tokenkey == "digit":
                    if self.__is_digit(string[i]) and t["value"][current_state][index] != 0:
                        current_state = t["value"][current_state][index]
                        break
                elif tokenkey == "nzdigit":
                    if self.__is_nzdigit(string[i]) and t["value"][current_state][index] != 0:
                        current_state = t["value"][current_state][index]
                        break
                elif tokenkey == "letter":
                    if self.__is_letter(string[i]) and t["value"][current_state][index] != 0:
                        current_state = t["value"][current_state][index]
                        break
                else:
                    if string[i] == tokenkey and t["value"][current_state][index] != 0:
                        current_state = t["value"][current_state][index]
                        break
                
            else:
                if index + 1 >= len(t["key"]):
                    return False
            i += 1

        if current_state == 0:
            return False
        
        return current_state in t["final"]
