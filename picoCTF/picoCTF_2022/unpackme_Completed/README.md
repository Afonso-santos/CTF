## Solution 
  1. Download the Python program.
   ```
     $ https://artifacts.picoctf.net/c/466/unpackme.flag.py
   ```
  2. Reading the script we find the execute command. If we change "exec" to "print" and run the program, we can see the password and the flag, to see only the flag I use this commad

   ```
     $ python unpackme.flag.py | grep -oE "picoCTF{.*?}" 
   ```

  <details>
    <summary> Flag </summary>

      picoCTF{175_chr157m45_85f5d0ac}
  </details>
