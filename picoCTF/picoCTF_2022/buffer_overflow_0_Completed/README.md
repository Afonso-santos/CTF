## Solution
  1. Download the message.
   ```
      $ wget https://artifacts.picoctf.net/c/522/vuln
      $ wget https://artifacts.picoctf.net/c/522/vuln.c
   ```
  2. To connect to the program the question use this code.
   ```
      $ nc saturn.picoctf.net 51110
   ```
  3. Analiying the code we need to write a string bigger then 16 lenght to catch a flag.
   <details>
       <summary> Flag </summary>
  
         picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}
  
   </details>
