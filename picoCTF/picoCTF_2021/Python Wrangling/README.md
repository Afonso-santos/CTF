##Solution 
1. Download the Python script, the password and the flag.
  ```
    $ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py
    $ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/pw.txt
    $ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/flag.txt.en
  ```
 2. If we try to run the Python script, it will ask one password. The file 'pw.txtx' has a password, so to see the content files we use this comamd
  ```
    $ cat pw.txt
  ```
   <details>
       <summary> Password </summary>
  
          192ee2db192ee2db192ee2db192ee2db
  
   </details>
   
   
 3. Now we have the password. Lest's run the code again now using the password.
 
 ```
    $ python .\ende.py -d .\flag.txt.en
  ```
 4. write the password and we can find the flag
     <details>
       <summary> Flag </summary>
  
         picoCTF{4p0110_1n_7h3_h0us3_192ee2db} 
  
   </details>
