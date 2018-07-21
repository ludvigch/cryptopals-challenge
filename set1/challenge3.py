# crack single byte xor cipher
import challenge2 as c2
from binascii import unhexlify
import math
cipher_text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ENGLISH_FREQS = [
0.0651738, 0.0124248, 0.0217339, 0.0349835, # 'A', 'B', 'C', 'D',...
0.1041442, 0.0197881, 0.0158610, 0.0492888, 
0.0558094, 0.0009033, 0.0050529, 0.0331490,
0.0202124, 0.0564513, 0.0596302, 0.0137645, 
0.0008606, 0.0497563, 0.0515760, 0.0729357, 
0.0225134, 0.0082903, 0.0171272, 0.0013692, 
0.0145984, 0.0007836, 0.1918182] #'Y', 'Z', ' '

def singlechar_xor(key, in_bytes):
    output = b''
    for char in in_bytes:
        output += bytes([char ^ key])
    return output

def get_chi2(binstr):
    # count letter and space frequency
    counted_freqs = [0]*27
    ignored = 0
    for byte in binstr:
        char = chr(byte)
        if ord(char) in range(97, 123): # lowercase
            counted_freqs[ord(char)-97] += 1
        elif ord(char) in range(65, 91): # uppercase
            counted_freqs[ord(char)-65] += 1
        elif char==' ': # space
            counted_freqs[26] += 1
        elif ord(char) in range(33, 127): # ignore symbols such as ! and # etc.
            ignored += 1
        elif ord(char) in [9,10,13]: # ignore tab, newline and CR
            ignored += 1
        else: # non-ascii character => not a correct string
            return (math.inf, binstr)

    # calculate the chi2 from gathered frequencies
    length = len(binstr)-ignored
    chi2 = 0
    for i in range(0,27):
        observed = counted_freqs[i]
        expected = length * ENGLISH_FREQS[i]
        if expected==0:
            expected=1
        diff = observed-expected
        chi2 += (diff*diff)/expected
    return (chi2, binstr)

# returns list of all combos sorted descending according to their chi2 score
# returns: [(score, text, key), ...]
def crack(text):
    score_list = []
    bin_rep = unhexlify(text)
    #print(score(clear))
    for key in range(0, 256):
        clear = singlechar_xor(key, bin_rep)
        score, txt = get_chi2(clear)
        score_list += [(score, txt, chr(key))]
    return sorted(score_list, key=lambda entry: entry[0])

def test():
    meme = crack(cipher_text)
    for x in range(5):
        tehone = meme[x]
        print("key: "+tehone[2]+
              "\ndecr:\t"+str(tehone[1])+
              "\nscore:\t"+str(tehone[0])+"\n")

if __name__ == '__main__':
    test()

# 1010 1111 CLEAR   XOR
# 1100 1100 KEY     
# 0110 0011 CIPHER XOR
# 1100 1100 KEY 
# 1010 1111 CLEAR TEXT
# x XOR y = x'*y + x*y'