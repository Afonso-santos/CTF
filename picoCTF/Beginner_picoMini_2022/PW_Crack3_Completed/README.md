## Solution:
  1. Download password cheker, encrypted flag and hash file . The files need to stay in the same directory.  
  ```
    $ wget https://artifacts.picoctf.net/c/23/level3.py
    $ wget https://artifacts.picoctf.net/c/23/level3.flag.txt.enc
    $ wget https://artifacts.picoctf.net/c/23/level3.hash.bin
  ```
  2. We have a list of 7 possible passwords. We can try the 7 passwords one ir will work, but i am lazy to try all teh 7 passwords. So i creat a for loop adapting the original code (in file level3_Completed.py).
   <details>
      <summary> for loop </summary>
       
        def level_3_pw_check(user_pw):
          user_pw_hash = hash_pw(user_pw)
    
          if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
          print("That password is incorrect")
        
        pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]
        
        for ps in pos_pw_list:
          level_3_pw_check(ps)
       
   </details>
   
   3. Run the password cheker with the for loop integrated.
   <details>
       <summary> Flag </summary>
  
         picoCTF{m45h_fl1ng1ng_2b072a90}
  
   </details>
    
    
