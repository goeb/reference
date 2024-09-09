import sys
import binascii

data = bytes(sys.argv[1], 'utf-8')
data_hex = binascii.hexlify(data)
print('hexlify:', data_hex) # same as hexlify
print('unhexlify:', binascii.unhexlify(data_hex))
