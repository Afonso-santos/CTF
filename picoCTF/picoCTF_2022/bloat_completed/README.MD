## Solution
 1. Download the Python script and the crypted flag.
  ```
    $ wget https://artifacts.picoctf.net/c/430/bloat.flag.py
    $ wget https://artifacts.picoctf.net/c/430/flag.txt.enc
  ```

 2. Open the script and read we can see many strings in  index sum (`a[71]+a[64]+a[79]+a[79]+a[88]...`). I reorgenise the code and turn the script more simple and finding the password, you can see in `bloat.flag_simpledield.py`.
    <details>
      <summary> Password </summary>

        happy chance
    </details>
 3. Now with password and the optimized script we can run and get the flag.
    <details>
      <summary> Flag </summary>

        picoCTF{d30bfu5c4710n_f7w_5e14b257}
    </details>