
import re, fileinput
from pyPEG import parse
from pyPEG import keyword, _and, _not, ignore

def comment():          return [re.compile(r"--.*--"), re.compile(r"--.*")]
def typeDefinition():   return id, "::=", [ sequence, choice, terminal ]
def terminal():         return integerType
def integerType():      return "INTEGER", 0, ( "(", literal, ".." , literal, ")" )
def literal():          return re.compile(r'\d+')
def id():               return re.compile(r"\w+")
def optional():         return "OPTIONAL"
def member():           return id, id, 0, optional
def structureMembers(): return member, -1, ( ",", member)
def sequence():         return "SEQUENCE", "{", structureMembers, "}"
def choice():           return "CHOICE", "{", structureMembers, "}"

files = fileinput.input()
result = parse(typeDefinition(), files, True, comment)
print result
