## Solution:
  1. Download password cheker, encrypted flag and hash file . The files need to stay in the same directory.  
  ```
    $ wget https://artifacts.picoctf.net/c/80/level5.py
    $ wget https://artifacts.picoctf.net/c/80/level5.flag.txt.enc
    $ wget https://artifacts.picoctf.net/c/80/level5.hash.bin
    $ wget https://artifacts.picoctf.net/c/80/dictionary.txt
  ```
  2. We have a dicionary with many possible passwords. I creat a for loop adapting the original code (in file level5_Completed.py).
   <details>
      <summary> for loop </summary>
       
        def level_5_pw_check(user_pw):
          user_pw_hash = hash_pw(user_pw)
    
          if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
          else:
            pass 
                
        for ps in open("dictionary.txt","r").read().split():
          level_5_pw_check(ps)
       
   </details>
   
  3. Run the password cheker with the for loop integrated.
 
   <details>
       <summary> Flag </summary>
  
         picoCTF{h45h_sl1ng1ng_40f26f81}
  
   </details>
  
