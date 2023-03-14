from saleapp.securable_data import create_encode, create_decode, caesar_key, vigenere_key
# Thuat giai Caeser
def encoding_no1 (plaintext):
    n = 280
    plainindex_range = []
    ciphertext = ""
    decode = create_decode()
    encode = create_encode()


    for p in plaintext:
        plainindex_range.append(decode[p])

    for p in plainindex_range:
        index = (p+caesar_key)%n
        ciphertext += encode[index]

    return ciphertext

#Thuat giai Vigener
def encoding_no2 (plaintext):
    n = 280
    plainindex_range = []
    keyindex_rang = []
    ciphertext = ""
    index=0

    decode = create_decode()
    encode = create_encode()

    for p in plaintext:
        plainindex_range.append(decode[p])

    for k in vigenere_key:
        keyindex_rang.append(decode[k])

    while len(plainindex_range) != len(keyindex_rang):
        if len(plainindex_range) > len(keyindex_rang):
            keyindex_rang.append(keyindex_rang[index])
            index += 1
        else:
            keyindex_rang.remove(len(keyindex_rang) - 1)

    for i in range(len(plainindex_range)):
        index = (plainindex_range[i]+keyindex_rang[i])%n
        ciphertext += encode[index]

    return ciphertext
