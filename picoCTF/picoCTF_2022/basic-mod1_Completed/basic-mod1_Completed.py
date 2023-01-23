crypto_flag =[202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390 ,383 ,225 ,258, 38, 291, 75,324 ,401, 142, 288, 397]

abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']


flag= ""

for num in crypto_flag:
    key=num % 37
    flag += abc[key]

print("picoCTF{"+ flag + "}")

## picoCTF{R0UND_N_R0UND_B6B25531}