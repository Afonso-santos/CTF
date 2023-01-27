import string

passwords= open("passwords.txt","r").read().split('\n')
usernames= open("usernames.txt", "r").read().split('\n')

posicion= usernames.index("cultiris")

crypto_flag = passwords[posicion]

flag=""

# when we look to the paswords list we can see indication  it is Caesar cyphre with a rotation 13

for letter in crypto_flag:
    if letter.isupper():
        flag += string.ascii_uppercase[(string.ascii_uppercase.find(letter)+13) % 26 ]

    elif letter.islower():
        flag += string.ascii_lowercase[(string.ascii_lowercase.find(letter)+13) % 26 ]

    else:
        flag += letter

print(flag)

# 