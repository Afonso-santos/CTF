crypto_flag = open("cipher.txt","r").read()
#rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}



def decrypt(crypto_flag):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_key = "CYLAB"
    lower_key ="cylab"
    flag = " "
    n = 0
    for i in range(len(crypto_flag)):
        
        if (ord(crypto_flag[i])>=65) and (ord(crypto_flag[i])<=90) :
            
            x =((ord(crypto_flag[i]))-ord(upper_key[n % len(upper_key)])+26)%26
            
            x+= ord("A")
            flag+= chr(x)
            n+=1

        elif (ord(crypto_flag[i])>=97 ) and (ord(crypto_flag[i])<=122):

            x = ((ord(crypto_flag[i]))- ord(lower_key[n % len(lower_key)])+26) %26
            x+= ord("a")
            flag+=chr(x)
            n+=1
            
        else:
            flag+= crypto_flag[i]

    print(flag)

print(decrypt(crypto_flag))










