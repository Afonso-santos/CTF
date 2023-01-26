## Solution:
  1. Download password cheker and encrypted flag. The files need to stay in the same directory.  
  ```
    $ wget https://artifacts.picoctf.net/c/18/level2.py
    $ wget https://artifacts.picoctf.net/c/18/level2.flag.txt.enc
  ```
  2. If we start the password cheker it will ask one password but we don't have password.
  
  3. I start to read the code and find the correct password encrypted, hex string. 
  
  4. Open the python 3, in terminal. Paste the previous hex String, to uncrtypted.
   <details>
     <summary> Correct password </summary>
       
       39ce = chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65)
  
   </details>
    
  5. Run the passowrd cheker, writing the correct password uncrtypted.
    
   <details>
       <summary> Flag </summary>
  
         picoCTF{tr45h_51ng1ng_502ec42e}
  
   </details>
