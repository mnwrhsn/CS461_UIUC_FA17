import numpy as np
from fractions import gcd
from Crypto.PublicKey import RSA
from pbp import decrypt
import sys

def read_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        f.close()
    return content

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
	    raise ValueError
    return x % m

if __name__=='__main__':

    mod_filename = 'moduli.hex'
    ciphertext_file = sys.argv[1]
    output_file = sys.argv[2]
    ciphertext = read_from_file(ciphertext_file)
    public_e = 65537L

    moduli = read_from_file(mod_filename)
    moduli = moduli.splitlines()
    moduli = [int(moduli[i], 16) for i in range(0, len(moduli))]

    working_window = moduli
    product = np.product(working_window)
    # mining p and q
    # following the Algorithm in Section 3.3
    for i in range(0, len(working_window)):
        ni2 = np.power(moduli[i], 2)
        zi  = product % ni2
        p = gcd(moduli[i],zi/moduli[i])
	if p == 1:
	    continue
        q = moduli[i] / p
	try:
	    private_d = modinv(public_e, (p-1)*(q-1))
	except ValueError:
	    continue
	tup = (moduli[i], public_e, private_d, p, q)
        rsakey = RSA.construct(tup)
        try:
            plaintext = decrypt(rsakey, ciphertext)
            print i, 'Correct RSA Key!'
            with open(output_file, 'w') as f:
                f.write(plaintext)
            break
        except ValueError:
            print i, 'Wrong RSA Key'
