##Bruteforce
import string

msg = "PUT CIPHER TEXT HERE"

for i in range(26):
    code = ""

    for s in msg:
        if s.isalpha() == False:
            code +=s
        else:
            n = i - string.ascii_letters.index(s)
            code += string.ascii_letters[n]

    print("Key is '{}' and Data is '{}' \n\n" .format(i,code))