## Solution
 1. Download Python script.
  ```
    $ wget https://artifacts.picoctf.net/c/93/serpentine.py
  ```
 
 2. If we try run the code we don't find nothing so is better read the code. The fuction "def main" don't print the flag when you click the correct opction so we need to edit the code, add the print the "def print_flag()".
 
 ```
   (...)
    elif choice == 'b':
      print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
      print(print_flag()) 
   (...)
  ```
 3. Run the code again with the adaptation. 
   <details>
       <summary> Flag </summary>
        
        picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}  
  
   </details>
