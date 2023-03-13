from saleapp.securable_data import decode_data, encode_data, caesar_key,vigenere_key

# Thuat giai Caeser
def decoding_no1 (ciphertext):
    n = 280
    cipherindex_range = []
    plaintext = ""

    data = encode_data()
    decode = decode_data()

    for c in ciphertext:
        cipherindex_range.append(decode[c])

    for c in cipherindex_range:
        index = (c-caesar_key)
        while index < 0:
            index += n
        plaintext += data[index]

    return plaintext

# Thuat ma Vigener
def decoding_no2 (ciphertext):
    n = 280
    cipherindex_range = []
    keyindex_rang = []
    plaintext = ""
    index=0

    encode = encode_data()
    decode = decode_data()

    for c in ciphertext:
        cipherindex_range.append(decode[c])

    for k in vigenere_key:
        keyindex_rang.append(decode[k])

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
        plaintext += encode[index]

    return plaintext