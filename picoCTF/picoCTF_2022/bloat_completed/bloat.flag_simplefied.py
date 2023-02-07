import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
def Confirm_password(input_pw):
  if input_pw == "happychance": 
    return True
  else:
    print("this password incorrect")
    sys.exit(0)
    return False

def retrieve_flag(encrpted_flag):
  return decrypt_flag(encrpted_flag.decode(), "rapscallion") 

def ask_passowrd():
  return input( "Please enter correct password for flag: ") 

def read_flag():
  return open('flag.txt.enc', 'rb').read()

def text_fot_flag():
  print("Welcome back... your flag, user:")

def decrypt_flag(input_pw, key):
    arg433 = key
    i = 0
    while len(arg433) < len(input_pw):
        arg433 = arg433 + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(input_pw,arg433)])


encrpted_flag = read_flag()
input_pw = ask_passowrd()
Confirm_password(input_pw)
text_fot_flag()
key = retrieve_flag(encrpted_flag)
print(key)
sys.exit(0)
