import classBased as cb
Huffboth = cb.Huffboth()
import os

file = "sample-file.txt"
def _to_Bytes(data):
  b = bytearray()
  for i in range(0, len(data), 8):
    b.append(int(data[i:i+8], 2))
  return bytes(b)

with open(file, 'rb') as r:
    content = r.read()
    encoded_text = Huffboth.Encode(str(content))
    
    decoded_text = Huffboth.Decode(encoded_text)
    if(str(content) == decoded_text):
        print("File Compression and Decompression Sucessful!")
    else:
        print("Failed!")
        
    fileOP = open("compressed_file.bin", "wb")
    fileOP.write(_to_Bytes(encoded_text))
    
    _o = os.path.getsize('sample-file.txt')
    _c = os.path.getsize('compressed_file.bin')
    print(f'Original file: {_o} bytes')
    print(f'Compressed file: {_c} bytes')
    print('Compressed file to about {}% of original'.format(round((((_o-_c)/_o)*100), 0)))
    fileOP.close()
