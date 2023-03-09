def toUpperText(text):
    text.replace(" ", "")
    return text.upper()

# Thuat giai Caeser
def encoding_no1 (plaintext, n, k):
    data = []
    plainindex_range = []
    ciphertext = ""

    ascii_code = 65
    plaintext = toUpperText(plaintext)
    for i in range(n):
        data.append(chr(ascii_code))
        ascii_code += 1

    for p in plaintext:
        for d in range(len(data)):
            if(p == data[d]):
                plainindex_range.append(d)

    for p in plainindex_range:
        index = (p+k)%n
        ciphertext += data[index]

    return ciphertext

#Thuat giai Vigener
def encoding_no2 (plaintext, n, key):
    data = []
    plainindex_range = []
    keyindex_rang = []
    ciphertext = ""
    index=0

    ascii_code = 65
    plaintext = toUpperText(plaintext)
    for i in range(n):
        data.append(chr(ascii_code))
        ascii_code += 1

    for p in plaintext:
        for d in range(len(data)):
            if(p == data[d]):
                plainindex_range.append(d)

    for k in key:
        for d in range(len(data)):
            if(k == data[d]):
                keyindex_rang.append(d)

    while len(plainindex_range) != len(keyindex_rang):
        if len(plainindex_range) > len(keyindex_rang):
            keyindex_rang.append(keyindex_rang[index])
            index += 1
        else:
            keyindex_rang.remove(len(keyindex_rang) - 1)

    for i in range(len(plainindex_range)):
        index = (plainindex_range[i]+keyindex_rang[i])%n
        ciphertext += data[index]

    return ciphertext