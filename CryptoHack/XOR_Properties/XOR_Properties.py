from pwn import xor  

## transform hex to bytes 
key1     = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_1   = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_3   = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_123 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

## Find Key1 and Key2 

key2 = xor(key2_1,key1)
    # \x91\x14\x04\xe1?\x94\x88N\xab\xbe\xc9%\x85\x12@\xa5/\xa3\x81\xdd\xb7\x97\x00\xddm\r
key3 = xor(key2_3,key2)
    #  P@S\xb7W\xea\xfd=p\x9dc9\xb1@\xe0=\x98\xb9\xfeb\xb8J\xdd\x032\xcc

flag = xor(flag_123,key1, key2, key3)

print(flag)

## crypto{x0r_i5_ass0c1at1v3}