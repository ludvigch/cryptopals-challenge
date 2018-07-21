from binascii import unhexlify
from binascii import Error
import base64

hexstr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
answer = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
def hex_to_b64(hexstr):
    try:
        byte_seq = unhexlify(hexstr)
    except Error as e:
        byte_seq = unhexlify("0"+hexstr)
    return base64.b64encode(byte_seq)

def test():
    encoded = hex_to_b64(hexstr)
    if encoded==answer:
        print("YAY")
    else:
        print("NAY")

if __name__ == '__main__':
    test()
