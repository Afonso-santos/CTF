
def decode(nums):
    flag=" "
    for num in nums:
        char=chr(num)
        flag+=char
    return (flag)

crypto=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print(decode(crypto))

## flag = crypto{ASCII_pr1nt4bl3}