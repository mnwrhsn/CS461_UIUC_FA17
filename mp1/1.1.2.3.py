import sys
from Crypto.Cipher import AES
ciphertext_file = sys.argv[1]
output_file = sys.argv[2]

def generateKeyString(i):
    s = hex(i)[2:].zfill(64)
    return s.decode('hex')

with open(ciphertext_file) as f:
    ciphertext = f.read().decode('hex')
    f.close()

IV = b'00000000000000000000000000000000'.decode('hex')

key = generateKeyString(10)
cipher = AES.new(key, AES.MODE_CBC, IV)
plaintext = cipher.decrypt(ciphertext)
print plaintext, key.encode('hex')


with open(output_file, 'w') as f:
    f.write(key.encode('hex'))
    f.close()

