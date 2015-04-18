import struct
import sys

"""
Ascii85 has an expansion factor of 5 to 4 (5 Ascii85 characters can
encode 4 binary bytes)
"""

def a85encode(data):

    a85chars = [chr(i) for i in range(33, 118)]
    a85chars2 = [(a + b) for a in a85chars for b in a85chars]

    padding = len(data) % 4
    if padding:
        data = data + b'\0' * (4-padding)

    result = ""
    for i in range(0, len(data) / 4):
        wordstr = data[i*4:i*4+4]
        word = struct.unpack('!I', wordstr)[0] # convert the 4 bytes to an unsigned integer
        result += a85chars2[word / 614125] + a85chars2[word / 85 % 7225] + a85chars[word % 85]

    return result

print a85encode(sys.argv[1])
