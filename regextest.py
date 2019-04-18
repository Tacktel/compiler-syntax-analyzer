from regexparser import Regex
from token import Token
import sys

r = Regex()
valid = r.isvalid(sys.argv[1], Token.T_ID)
print(valid)