import base64

hex_string   = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
bytes_string = (bytes.fromhex(hex_string))
print(base64.b64encode(bytes_string))

## crypto/Base+64+Encoding+is+Web+Safe/