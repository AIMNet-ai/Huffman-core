import urllib
import huffman as h

input = "aababcabcd"
h.huffman(input)

#({'a': '0', 'c': '111', 'b': '10', 'd': '110'}, '0010010111010111110')

print(len(input) * 8, len(h.huffman(input)[1]))

#(80, 19)

input = "the quick brown fox jumps over the lazy dog"
h.huffman(input)

#({' ': '00', 'a': '10000', 'c': '10011', 'b': '110000', 'e': '1010', 'd': '111111', 'g': '110111', 'f': '01001', 'i': '110101', 'h': '11110', 'k': '110011', 'j': '111110', 'm': '110001', 'l': '110010', 'o': '1011', 'n': '01000', 'q': '10010', 'p': '110110', 's': '110100', 'r': '11101', 'u': '0101', 't': '11100', 'w': '01111', 'v': '10001', 'y': '01100', 'x': '01110', 'z': '01101'}, '111001111010100010010010111010110011110011001100001110110110111101000000100110110111000111110010111000111011011010000101110001101011101001110011110101000110010100000110101100001111111011110111')
print(len(input) * 8, len(h.huffman(input)[1]))

#(344, 192)

# input = urllib.urlopen("http://docs.python.org/lib/front.html").read()

# print(len(input) * 8, len(h.huffman(input)[1]))

#(57808, 36340)

# input = file("wrnpc12.txt").read()
# print(len(input) * 8, len(h.huffman(input)[1]))
#(26281320, 14962010)
