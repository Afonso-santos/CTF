def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ''
    j = 0
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
            plaintext += chr((ord(ciphertext[i]) - ord(key[j % len(key)]) + 26) % 26 + 65)
            j += 1
        else :
            plaintext+= ciphertext[i]
    return plaintext


crypto_message = open("cipher.txt","r").read()
key = "CYBLAD"
print(decrypt(crypto_message,key))