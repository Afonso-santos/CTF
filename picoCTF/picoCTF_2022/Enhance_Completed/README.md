## Solution
  1. Download the image file.
   ```
     $ wget https://artifacts.picoctf.net/c/138/drawing.flag.svg
   ```
   2. If we open the photo file with vscode we can see the clue of the flag  or use this commad:
   ```
     $ cat drawing.flag.svg 
   ```
   3. The Clue is we see the letters of the flag  in the lines wich ends with "</tspan>
   ```
     $ cat drawing.flag.svg |grep "</tspan" 
   ```
   4. We can already find the flag but if we want the flag without the "<",">"," " and "\n". So lets do this commad.
   ```
    $ cat drawing.flag.svg |grep "</tspan" |cut -d ">" -f2|cut -d "<" -f1|tr -d "\n"|tr -d  " "
   ```
   <details>
       <summary> Flag </summary>
  
         flag = picoCTF{3nh4nc3d_d0a757bf}
  
   </details>
