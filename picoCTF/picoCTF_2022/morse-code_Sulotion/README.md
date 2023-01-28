## Solution
  1. Download the audio file.
    ```
      $ wget https://artifacts.picoctf.net/c/235/morse_chal.wav
    ```
  2. We can open a audio editor, in my case I use audacity, to covert audio to text. I use "_" as space  (code_morse.txt)
   ```
      .-- .... ....- --... _ .... ....- --... .... _ ----. ----- -.. _ .-- ..---  ----- ..- ----. .... --...
   ```
  3. To decode the morse code I creat this script 
     ```py
      morse_code_dic = { '.-':'a','-...':'b',
                    '-.-.':'c', '-..':'d', '.':'e',
                    '..-.':'F', '--.':'g', '....':'h',
                    '..':'i', '.---':'j', '-.-':'k',
                    '.-..':'l', '--':'m', '-.':'n',
                    '---':'o', '.--.':'p', '--.-':'q',
                    '.-.':'r', '...':'s', '-':'t',
                    '..-':'u', '...-':'v', '.--':'w',
                    '-..-':'x', '-.--':'y', '--..':'z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':', ','.-.-.-':'.',
                    '..--..':'?', '-..-.':'/','-....-': '-',
                    '-.--.':'(','-.--.-': ')', '_':"_"}
      msg = ""

      for letter in open("code_morse.txt","r").read().split():
        msg += morse_code_dic.get(letter)

      print("picoCTF{" + msg + "}" )
     ```
    <details>
       <summary> Flag </summary>
  
         picoCTF{wh47_h47h_90d_w20u9h7}
   
     </details>
