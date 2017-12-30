import sys, math

ciphertext_file = sys.argv[1]
key_file = sys.argv[2]
modulo_file = sys.argv[3]
output_file = sys.argv[4]

with open(ciphertext_file) as f:
    ciphertext = int(f.read().strip(), 16)
    f.close()

with open(key_file) as f:
    key = int(f.read().strip(), 16)
    f.close()

with open(modulo_file) as f:
    modulo = int(f.read().strip(), 16)
    f.close()

# Reference https://en.wikipedia.org/wiki/Modular_exponentiation#Memory-efficient_method

def modular_pow(base, exponent, modulus):
    if modulus is 1:
        return 0
    c = 1
    for i in range(1, exponent+1):
        c = (c * base) % modulus
    return c

# RSA Decryption
# c^d == (m^e)^d == m (mod n)

m = modular_pow(ciphertext, key, modulo)
print 'message:', m, 'hex:', hex(m)[2:].rstrip('L')

with open(output_file, 'w') as f:
    f.write(hex(m)[2:].rstrip('L'))
    f.close()
