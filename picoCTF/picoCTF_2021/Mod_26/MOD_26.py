## function wich resolve cryptography  rot13 

def rote13(pharse):
  abc = "abcdefghijklmnopqrstuvwxyz"
  ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  especialChar="{\/}.:,;-_<>'|1234567890«»"
  phrase = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"
  flag = ""

  for letter in phrase:
    if letter  not in especialChar:
      if letter in abc:
        result= [*abc,*abc][(abc.find(letter)+13 )]
        flag+=result
      else:
        result=[*ABC,*ABC][(ABC.find(letter)+13)]
        flag+= result
    else:
        flag+=letter
  return(flag)


print(rote13("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"))

