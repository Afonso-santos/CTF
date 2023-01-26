## Solution:
  1. Download password cheker, encrypted flag and hash file . The files need to stay in the same directory.  
  ```
    $ wget https://artifacts.picoctf.net/c/59/level4.py
    $ wget https://artifacts.picoctf.net/c/59/level4.flag.txt.enc
    $ wget https://artifacts.picoctf.net/c/59/level4.hash.bin
  ```
  2. We have a list of 7 possible passwords. We can try the 100 passwords , one it will work, but i am lazy to try all teh 100 passwords. So i creat a for loop adapting the original code (in file level4_Completed.py).
   <details>
      <summary> for loop </summary>
       
        def level_4_pw_check(user_pw):
          user_pw_hash = hash_pw(user_pw)
    
          if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
          else:
            pass
        
        pos_pw_list = ["158f", "1655", "d21e", "4966", "ed69", "1010", "dded", "844c", "40ab", "a948", "156c", "ab7f", "4a5f", "e38c", "ba12", "f7fd", "d780", "4f4d", "5ba1", "96c5", "55b9", "8a67", "d32b", "aa7a", "514b", "e4e1", "1230", "cd19", "d6dd", "b01f", "fd2f", "7587", "86c2", "d7b8", "55a2", "b77c", "7ffe", "4420", "e0ee", "d8fb", "d748", "b0fe", "2a37", "a638", "52db", "51b7", "5526", "40ed", "5356", "6ad4", "2ddd", "177d", "84ae", "cf88", "97a3", "17ad", "7124", "eff2", "e373", "c974", "7689", "b8b2", "e899", "d042", "47d9", "cca9", "ab2a", "de77", "4654", "9ecb", "ab6e", "bb8e", "b76b", "d661", "63f8", "7095", "567e", "b837", "2b80", "ad4f", "c514", "ffa4", "fc37", "7254", "b48b", "d38b", "a02b", "ec6c", "eacc", "8b70", "b03e", "1b36", "81ff", "77e4", "dbe6", "59d9", "fd6a", "5653", "8b95", "d0e5"]
        
        for ps in pos_pw_list:
          level_4_pw_check(ps)
       
   </details>
   
   3. Run the password cheker with the for loop integrated.
   
   <details>
       <summary> Flag </summary>
  
         picoCTF{fl45h_5pr1ng1ng_cf341ff1}
  
   </details>
