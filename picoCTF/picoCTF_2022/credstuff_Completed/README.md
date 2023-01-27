## Solution
  1. Download the leak file .
   ```
     $ wget https://artifacts.picoctf.net/c/534/leak.tar
   ```
  2. The question say we need to find a user name "cultiris" and his password, both have the same index. I used this Pyhton script:
   ```py
     passwords= open("passwords.txt","r").read().split('\n')
     usernames= open("usernames.txt", "r").read().split('\n')
      
     posicion= usernames.index("cultiris")
     crypto_flag = passwords[posicion]
   ```
  3. When I'm looking to the passwords and i see the passwords are in rot13. So this is my decipher Caesar:
   ```py
     for letter in crypto_flag:
       if letter.isupper():
         flag += string.ascii_uppercase[(string.ascii_uppercase.find(letter)+13) % 26 ]

       elif letter.islower():
         flag += string.ascii_lowercase[(string.ascii_lowercase.find(letter)+13) % 26 ]

       else:
         flag += letter

      print(flag)
   ```
    
  <details>
       <summary> Flag </summary>
  
         picoCTF{C7r1F_54V35_71M3}
  
   </details>
