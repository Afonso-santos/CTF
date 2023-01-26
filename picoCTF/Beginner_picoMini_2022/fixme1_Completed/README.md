## Solution
1. Download the Python srcipt
  ```
    $ wget https://artifacts.picoctf.net/c/39/fixme1.py
  ```
 2. We need to fix the code.

With error (fixme1.py):
 ```
 (...)
    flag = str_xor(flag_enc, 'enkidu')
      print('That is correct! Here\'s your flag: ' + flag)
 ```
 Without error (fixme1_Complted.py):
   ```
    (...)
      flag = str_xor(flag_enc, 'enkidu')
      print('That is correct! Here\'s your flag: ' + flag)
 ```
 3. Run the script for the flag.
    <details>
       <summary> Flag </summary>
  
         picoCTF{1nd3nt1ty_cr1515_182342f7}
  
   </details>
