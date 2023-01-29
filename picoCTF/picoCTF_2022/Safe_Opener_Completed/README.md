## Solution
  1. Downoad the java program.
   ```
     $ wget https://artifacts.picoctf.net/c/463/SafeOpener.java
   ```
  2. If we try to run the java program, it will ask one password wich we don'y know. So I look to the script. I find the encode password.

  <details>
    <summary> Password </summary>

        cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz
  </details> 

  

  3. The encode password  looks like a binary data, base 64. Lets do this commad and put between ,"picoCTF{" + "}".  
   ```
     $ echo Password  | base64 -d 
   ```
   <details>
     <summary> Flag </summary>

     picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}

  </details>
