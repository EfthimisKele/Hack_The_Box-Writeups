#HTB_BABY

#remove 0x from the number you found
a='1st HEX'
b='2nd HEX'
c='3rd HEX'
d='4th HEX'

a=bytearray.fromhex(a).decode()
b=bytearray.fromhex(b).decode()
c=bytearray.fromhex(c).decode()
d=bytearray.fromhex(d).decode()

a="".join(reversed(a))
b="".join(reversed(b))
c="".join(reversed(c))
d="".join(reversed(d))

print (a+b+c+d)