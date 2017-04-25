from operator import xor

def encrypt(string, key):
    hasil=[None] *len(string)
    charhasil=[None]*len(string)

    leftmost=[None]*4
    rightmost=[None]*4
    for i in range(0,4):
        leftmost[i]=key[i]
        rightmost[i]=key[i+4]

    index=0
    blok=len(string)/4
    for i in range(0, blok):
        for j in range(0,4):
            hasil[index]=xor(string[index], leftmost[j])
            index+=1

    index=0

    for i in range(0, blok):
        for j in range(0,4):
            hasil[index]=hasil[index]+rightmost[j]
            hasil[index]=hasil[index]%256
            index+=1

    for i in range(0,len(string)):
        charhasil[i] = chr(hasil[i])

    print "HASIL ENCRYPT", charhasil
    print "HASIL ENCRYPT (ASCI", hasil

    #FUNGSI DECRYPT

    temp=[None]*len(string)
    for i in range(0, len(string)):
        temp[i]=ord(charhasil[i])

    tempafter=[None]*len(string)
    index=0
    for i in range(0, blok):
        for j in range(0,4):
            tempafter[index]=temp[index]-rightmost[j]
            index+=1

    tempxor=[None]*len(string)
    index=0

    for i in range(0, blok):
        for j in range(0,4):
            tempxor[index]=xor(tempafter[index], leftmost[j])
            index+=1

    hasildecrypt=[None]*len(string)
    for i in range(0, len(string)):
        hasildecrypt[i] = chr(tempxor[i])

    print "HASIL DECRYPT", hasildecrypt

    return hasildecrypt

secretkey=raw_input("Input  key: ")
panjangkey=len(secretkey)
ascikey = [None] * panjangkey
for i in range(0, panjangkey):
    ascikey[i] = ord(secretkey[i])

string=raw_input("Input string: ")
panjangstring=len(string)
panjang=panjangstring

if panjangstring %4 > 0 :
    sisamod=4-(panjangstring%4)
    panjang=panjangstring+sisamod

textdata=[None]*panjang

for i in range(0, panjang):
    if i<panjangstring:
        textdata[i]=string[i]
    else:
        textdata[i]=" "

ascistring = [None] * panjang
for i in range(0, panjang):
    ascistring[i] = ord(string[i])

print "ASCI dari STRING ", ascistring

hasil = encrypt(ascistring, ascikey)
print hasil

