## Solution 
 1. Download the crtpted message.
  ```
    $ wget https://artifacts.picoctf.net/c/529/cipher.txt 
  ```
 2. The message is in Vigenere cipher. I creat this script to decipher the message.
  ```py
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
  ```
 3. So we only need run the code and get the flag. 
   <details>
     <summary> Flag </summary>
        
        picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}
   </details>
