import sys
from Crypto.Cipher import AES
ciphertext_file = sys.argv[1]
key_file = sys.argv[2]
iv_file = sys.argv[3]
output_file = sys.argv[4]

with open(ciphertext_file) as f:
    ciphertext = f.read().strip().decode('hex')
    f.close()

with open(key_file) as f:
    key = f.read().strip().decode('hex')
    f.close()

with open(iv_file) as f:
    IV = f.read().strip().decode('hex')
    f.close()

cipher = AES.new(key, AES.MODE_CBC, IV)

plaintext = cipher.decrypt(ciphertext)
print plaintext

with open(output_file, 'w') as f:
    f.write(plaintext)
    f.close()

