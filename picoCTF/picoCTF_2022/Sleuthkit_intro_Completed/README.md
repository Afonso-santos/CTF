## Solution
  1. Lets download the disk image
   ```
     $ wget https://artifacts.picoctf.net/c/114/disk.img.gz
   ```
  2. Because we use "wget" we need to extract the disck image. To find the volume system of th partition layout we use this commad.
   ```
     $ mmls disk.img
   ```  
   <details>
    <summary> Flag </summary>
       
         picoCTF{mm15_f7w!}
  </details>
 