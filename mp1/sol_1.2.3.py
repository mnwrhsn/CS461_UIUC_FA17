import sys,urllib2
import binascii as ba

def get_status(u):
    req = urllib2.Request(u)
    try:
        f = urllib2.urlopen(req)
        return f.code, f.read().strip()
    except urllib2.HTTPError, e:
        return e.code, e.read().strip()

def read_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
        f.close()
    return content

# This method produces a 16-byte long padding string
def pad_string(n):
    n = n % 16
    return chr(0) * n + ''.join(chr(i) for i in range(16, n, -1))

def xor_hex_strings(s1, s2):
    assert len(s1) == len(s2)
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

# This method prduces a string with corresponding position and guess
# e.g. i = 4, guess = 233 --> \x00\x00\x00\x00\xe9\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
def guess_hex_string(i, guess):
    return chr(0) * i + chr(guess) + chr(0) * (16 - i - 1)

if __name__=='__main__':
    input_file = sys.argv[1]
    outout_file = sys.argv[2]
    netid = sys.argv[3]
    hexdata = read_from_file(input_file).decode('hex')

    blocksize = 16  # we have 16-byte block
    n_blocks = len(hexdata)/blocksize # total number of blocks

    # this is the list of all blocks
    block_list = list(hexdata[0+i:blocksize+i] for i in range(0, len(hexdata), blocksize))

    url = 'http://192.17.90.133:9996/mp1/'+ netid + '/?'
    plaintext = ''
    # for each block
    for i in xrange(n_blocks-1):
        # we try to fill in the plaintext
        plainblock = chr(0) * 16
        # for each byte in ith block in a reverse order
        for j in xrange(blocksize-1, -1, -1):
            for guess in [32] + range(65, 256) + range(65): # little optimization: try space and alphbet first
		blk0, blk1 = block_list[i], block_list[i+1]
                # blk0 ^ padding ^ plaintext ^ guess
                temp = xor_hex_strings(xor_hex_strings(blk0, pad_string(j)), plainblock)
                temp = xor_hex_strings(temp, guess_hex_string(j, guess))
                msg = temp.encode('hex') + blk1.encode('hex')
                msg_url = url + msg
                status, payload = get_status(msg_url)
                if status != 500:
                    plainblock = plainblock[0:j] + chr(guess) + plainblock[j+1:]
                    print plainblock
                    break
        plaintext += plainblock
        print plaintext

    with open(outout_file, 'w') as f:
        f.write(plaintext)
        f.close()
