from saleapp import encoding

# Thuat giai Caeser
def decoding_no1 (ciphertext, k = 1):
    n = 95
    data = []
    cipherindex_range = []
    plaintext = ""

    encoding.create_data(n, 32, data)

    for i in range(len(ciphertext)):
        for d in range(len(data)):
            if(ciphertext[i] == data[d]):
                cipherindex_range.append(d)

    for c in cipherindex_range:
        index = (c-k)
        while index < 0:
            index += n
        plaintext += data[index]

    return plaintext

# Thuat ma Vigener
def decoding_no2 (ciphertext, key):
    n = 95
    data = []
    cipherindex_range = []
    keyindex_rang = []
    plaintext = ""
    index=0

    encoding.create_data(n, 32, data)

    for c in ciphertext:
        for d in range(len(data)):
            if(c == data[d]):
                cipherindex_range.append(d)

    for k in key:
        for d in range(len(data)):
            if(k == data[d]):
                keyindex_rang.append(d)

    while len(cipherindex_range) != len(keyindex_rang):
        if len(cipherindex_range) > len(keyindex_rang):
            keyindex_rang.append(keyindex_rang[index])
            index += 1
        else:
            keyindex_rang.remove(len(keyindex_rang) - 1)

    for i in range(len(cipherindex_range)):
        index = (cipherindex_range[i]-keyindex_rang[i])
        while index < 0:
            index += n
        plaintext += data[index]

    return plaintext
