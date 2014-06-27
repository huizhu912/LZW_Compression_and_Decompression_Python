from ascii import asciilist

def LZWCompression(source):
    global dictionary1, indices, ratiotext
    dictionary1 = list(asciilist)
    word = x = ''
    compressedf = open('compressedfile.txt', 'w')
    indices = []

    for c in source:
        x = c
        if (word + c) in dictionary1:
            word = word + c
        else:
            compressedf.write(str(dictionary1.index(word)) + ' ')
            indices.append(dictionary1.index(word))
            dictionary1.append(word + c)
            word = c
    compressedf.write(str(dictionary1.index(word)) + ' ')
    indices.append(dictionary1.index(word))
    print("size of dictionary1 = ", len(dictionary1), "\n")
    #print(dictionary1)	
    print("size of indices = ", len(indices), "\n")
    print("Sequence of indices which represent the compressed result:", indices, "\n")
    print("Created dictionary for compression: ", dictionary1, "\n")
    diff = len(source) - len(indices)
    print("Compression ratio = " , round((diff / len(source)) * 100), "%")
    ratiotext = "Compression ratio = " + str(round((diff / len(source)) * 100)) + "%"

global source	
#source = "ACBBAAC"
#source = "AAABAABBBB"
#f = open('testcasea.txt', 'r')
f = open('testcaseb.txt', 'r')
source = f.read()
LZWCompression(source)
dict = open('dictionary1.txt', 'w+')
dict.write("Sequence of indices which represent the compressed result: " + str(indices) + "\r\n")
dict.write("Created dictionary for compression: " + str(dictionary1) + "\r\n")
dict.write(ratiotext)


