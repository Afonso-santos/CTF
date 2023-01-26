## Solution
1. Download the Python srcipt
  ```
    $ wget https://artifacts.picoctf.net/c/65/fixme2.py
  ```
 2. We need to fix the code.

With error (fixme2.py):
 ```
 (...)
    if flag = "":
      print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
 ```
 Without error (fixme2_Complted.py):
   ```
    (...)
      if flag =="":
        print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
 ```
 3. Run the script for the flag.
    <details>
       <summary> Flag </summary>
  
         picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}
  
   </details>
