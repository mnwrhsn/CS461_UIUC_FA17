import sys, hashlib

text1_file = sys.argv[1]
text2_file = sys.argv[2]
output_file = sys.argv[3]

def hammingDistance(hash1, hash2):
    bin_str = bin(int(hash1, 16) ^ int(hash2, 16))[2:].rstrip('L')
    return sum(int(c) for c in bin_str)


with open(text1_file) as f:
    text1 = f.read().strip()
    f.close()

with open(text2_file) as f:
    text2 = f.read().strip()
    f.close()

h1 = hashlib.sha256(text1).hexdigest()
h2 = hashlib.sha256(text2).hexdigest()
d = hammingDistance(h1, h2)

with open(output_file, 'w') as f:
    f.write(hex(d)[2:])
    f.close()

