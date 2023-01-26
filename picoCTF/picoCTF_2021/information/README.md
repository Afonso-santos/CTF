## Solution
  1. Download the image.
   ```
    $ wget https://mercury.picoctf.net/static/d1375e383810d8d957c04eef9e345732/cat.jpg
   ```
  2. To read a meta information  in files we use wxitfool.
   ```
    $ exiftool cat.jpg  
  ```
  3. We can see many information but one thing caght my attention is the "License".
    ```
      cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
    ```
    
  5. License look like a bash string  base 64 so, lets use this commad.
   ```
    $ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
   ```
   <details>
       <summary> Flag </summary>
  
         picoCTF{1nd3nt1ty_cr1515_182342f7}
  
   </details>
