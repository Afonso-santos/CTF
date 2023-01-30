## Solutiion 
1. Download the message.
 ```
   $ wget https://artifacts.picoctf.net/c/458/message.txt
 ```
2. I group the message in group of 3  and do this script:
 
  ```py
    message = ["heT" ,"fl " ,"g a", "s i", "icp" ,"CTo" ,"{7F","4NR","P05","1N5", "_16","_35", "P3X", "51N","3_V","9AA", "B1F", "8}7"]
                
    flag = " "
    for group in message:

        flag += group[2]+group[0]+group[1]

    print(flag)
  ```
  <details>
      <summary> Flag </summary>

        picoCTF{7R4N5P051N6_15_3XP3N51V3_A9AFB178}
  </details>
  