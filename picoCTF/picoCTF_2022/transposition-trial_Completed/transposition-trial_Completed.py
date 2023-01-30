message = ["heT" ,"fl " ,"g a", "s i", "icp" ,"CTo" ,"{7F","4NR","P05","1N5", "_16","_35", "P3X", "51N","3_V","9AA", "B1F", "8}7"]
                

new_message= ""
flag = " "
word =""
for group in message:

    flag += group[2]+group[0]+group[1]

print(flag)


instance Posicao (Int,Int) -> Eq caminho where:
    EQ::caminho -> caminho -> Bool
    eq c1 c2 = (==) (fazercaminho c  fazercaminho c2)     


fazercaminho ::Caminho -> Posicao
fazercaminho C (x,y) [] = (x,y)
fazercaminho C (x,y) (h:t) 
  | h== Norte = fazercaminho c (x,(y+1)) t 
  | h == Sul  =fazercaminho C (x,(y-1)) t 
  | h== Oeste  = fazercaminho C ((x-1),y) t 
  |otherwise = fazercaminho C ((x+1),y) t

(==):: Posicao -> Posicao -> Bool
(==):: (x,y) (h,t) 
  | x== h && y==t = True
  | otherwise = False 
