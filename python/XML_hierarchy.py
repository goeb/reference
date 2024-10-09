import xml.parsers.expat
import sys

def str_hierarchy() :
    global current_hierarchy
    result=""
    for i in current_hierarchy :
        if i==0 : return result
        result = result + str(i) + "."

def start_element(name, attrs):
    global level, current_hierarchy
    level = level + 1
    if level > len(current_hierarchy) :
        print("error: too many levels (" + str(level) + ")")
        sys.exit(1)

    # zero all sub-levels
    for i in range(level, len(current_hierarchy)) :
        current_hierarchy[i] = 0

    # increase current level
    current_hierarchy[level-1] = current_hierarchy[level-1] + 1

    print(str_hierarchy(), name)

def end_element(name):
    global level
    level = level - 1

def char_data(data):
    None

p = xml.parsers.expat.ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

f=open("t.xml", "rb")
level = 0
current_hierarchy = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] # 16 levels

p.ParseFile(f)
