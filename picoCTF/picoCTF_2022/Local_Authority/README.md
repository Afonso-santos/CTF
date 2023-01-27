## Solution 
  1. Open the website and search in DevTools.
  
   ![image](https://user-images.githubusercontent.com/113265283/215114341-6d53d861-5106-4f82-9266-bed34cf2c011.png)

  2. We will not find nothing .So I tried one login and password randomly , and appear a new page ,"Log in failed".

   ![image](https://user-images.githubusercontent.com/113265283/215115579-dd1d2ea1-6b11-451a-92ea-e03d1a62eef3.png)
  
  3. In DevTools have new files. Opening the file "login.php" we can find the corret: username and password.
    <details>
       <summary> username & password </summary>
  
         username: admin
         password: strongPassword098765
  
     </details>
   
   4. Now writing the right credentias we find the flag.
    <details>
       <summary> Flag </summary>
  
         picoCTF{j5_15_7r4n5p4r3n7_8086bcb1}
  
   </details>
