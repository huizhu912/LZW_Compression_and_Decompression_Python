from ascii import asciilist
from encoding import source

def LZWDecompression(f):
    global dictionary2
    dictionary2 = list(asciilist)
    word = ""
    compressedf = f
    global decompressedf
    decompressedf = open('decompressedfile.txt', 'w+') 

    s = compressedf.read()
    indices = s.split(' ')
    indices.pop()
    #print(indices)
	
    y = int(indices[0])
    element = str(dictionary2[y])
    decompressedf.write(element)
    #print(element)
    word = element
    for i in range(1, len(indices)):
        y = int(indices[i])		
        if y not in range(len(dictionary2)):
            element = word + element[0]
        else:
            element = dictionary2[y]
        decompressedf.write(str(element))
        #print(element)
        dictionary2.append(word + element[0])
        word = element

                				
f = open('compressedfile.txt', 'r')
LZWDecompression(f)

decompressedf = open('decompressedfile.txt', 'r+')
de = decompressedf.read()
print("size of dictionary2 = ", len(dictionary2), "\n")

if (de == source):
    print("[Decompressed text is identical to uncompressed text]", "\n")
    decompressedf.write("\n\n" + "[Decompressed text is identical to uncompressed text]" + "\n")

print("Created dictionary for decompression = ", dictionary2)

decompressedf.write("\n" + "Created dictionary for decompression = " + str(dictionary2))
decompressedf.close()
f.close()