crypto_flag =[104  ,290  ,356 ,313 ,262 ,337 ,354 ,229 ,146 ,297 ,118, 373 ,221 ,359 ,338 ,321,288 ,79 ,214 ,277 ,131 ,190 ,377]


abc=['a','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']

flag=""


for crypto in crypto_flag:
    key= (pow(crypto,-1,41))
    flag+= abc[key]

print("picoCTF{"+flag+"}")

# picoCTF{1NV3R53LY_H4RD_8A05D939}