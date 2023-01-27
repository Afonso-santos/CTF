## Solution
 1. Download the "weird message".
  ```
    $ wget https://artifacts.picoctf.net/c/394/message.txt
  ```
 2. The message is a list of numbers. The statement tell us what to do. I do this Python script.
  ```py
    crypto_flag =[202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390 ,383 ,225 ,258, 38, 291, 75,324 ,401, 142, 288, 397]
    abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']
    flag= ""

    for num in crypto_flag:
       key=num % 37
        flag += abc[key]

    print("picoCTF{"+ flag + "}")
  ```
   <details>
       <summary> Flag </summary>
  
         picoCTF{R0UND_N_R0UND_B6B25531}
  
   </details>
 
