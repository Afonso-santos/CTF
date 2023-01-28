## Solution
  1. Download packet capture.
     ```
       $ wget https://artifacts.picoctf.net/c/201/network-dump.flag.pcap
     ```
 2. Have two ways to resolve this exercise. First way, I use wireshark to see the packages. If we look the 4th packages,it has some data, to copy the data. Lets right clik Follow, TPC stream, have a data in string.
       ```
         $ wireshark network-dump.flag.pcap
       ```
   3. The second  way is write this command and if we look we can find a flag.
      ```
         $ cat network-dump.flag.pcap 
      ```
    
   <details>
       <summary> Flag </summary>
  
         picoCTF{p4ck37_5h4rk_01b0a0d6}
  
   </details>
    
