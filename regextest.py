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
valid = r.isvalid(sys.argv[1], Token.T_INTVAL)
print(valid)