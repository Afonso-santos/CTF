string  = "label"
integer = 13 
flag= ""


for i in string:
    numbs = [ord(i)]
    for num in numbs:
        xor_code = [13 ^num ]
        for code in xor_code:
            xor_string+= chr(code)

flaag="crypto{" + flag + "}"
print(flaag)

## flag = crypto{aloha}


from pwn import xor
 

