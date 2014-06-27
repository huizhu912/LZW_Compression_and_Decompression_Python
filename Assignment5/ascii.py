import string

printablechars = string.printable
asciilist = [0 for i in range(32)]

for i in range(len(printablechars)):
    asciilist.append(printablechars[i])  
	
for i in range(132, 256):
    asciilist.append(0)

#print(asciilist, "len = ", len(asciilist))  
#print("index of B", asciilist.index('B'))



