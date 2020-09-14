msg = "PUT_YOUR_TEXT_HERE"
msg = msg.split()

text = ""

for i in msg:
    text += chr(int(i))

print("Text is:- {}".format(text))
