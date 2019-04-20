#
# Compiler Term Project 1
#
# Team 1 :  Leo PAOL & Christophe MEI
#           50181573 & 50181587
#

from regexparser import Regex
from token import Token
import sys

r = Regex()
valid = r.isvalid("return", Token.T_RETURN)
print(valid)