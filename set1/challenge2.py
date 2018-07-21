from binascii import unhexlify, hexlify
import struct

test_a = "1c0111001f010100061a024b53535009181c"
test_b = "686974207468652062756c6c277320657965"
answer = b'746865206b696420646f6e277420706c6179'


def fixed_xor(a, b):
    bin_a = unhexlify(a)
    bin_b = unhexlify(b)
    zipped = zip(bin_a, bin_b)
    result = []
    for pair in zipped:
        result.append(pair[0] ^ pair[1])
    return bytes(result)

def test():
    calc = hexlify(fixed_xor(test_a, test_b))
    print("%(a)s XOR %(b)s\nis: %(ans)s" % {"a": test_a, "b": test_b, "ans": calc})
    print("matches: "+ str(hexlify(fixed_xor(test_a, test_b)) == answer))

if __name__ == '__main__':
    test()
