
import sys

def WHA(inStr):
    """ Returns the weak hash of given input string """

    mask = 0x3FFFFFFF
    outHash = 0  # initialize

    for s in inStr:
        byte = ord(s)
        # int_val is a pure function of byte (independednt of inStr order)
        int_val = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
        outHash = (outHash & mask) + (int_val & mask)

    return hex(outHash).rstrip("L")

def read_from_file(filename):

    with open(filename, 'r') as f:
        content = f.read()

    return content

def write_to_file(filename, content):

    with open(filename, 'w') as f:
        f.write(content)

if __name__=="__main__":

    # outHash = WHA("Hello world!")
    # print(outHash)

    # outHash = WHA("I am Groot.")
    # print(outHash)


    input_string = read_from_file(sys.argv[1])  # read from file
    weakhash = WHA(input_string)  # calculate hash
    write_to_file(sys.argv[2], weakhash)  # save hash to file
