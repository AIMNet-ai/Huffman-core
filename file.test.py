import classBased as cb
Huffboth = cb.Huffboth()

file = "sample-file.txt"

with open(file, 'rb') as r:
    content = r.read()
    encoded_text = Huffboth.Encode(str(content))
    
    decoded_text = Huffboth.Decode(encoded_text)
    if(str(content) == decoded_text):
        print("File Compression and Decompression Sucessful!")
    else:
        print("Failed!")
        
    fileOP = open("compressed_file.bin", "wb")
    fileOP.write(bytes(encoded_text, 'utf-8'))
    fileOP.close()
