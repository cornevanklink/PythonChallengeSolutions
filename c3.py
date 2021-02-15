import re


with open('c3source.txt') as f:
    text = f.read()

message = ""

for i in range(0,len(text)):
	numbool = text[i].isalnum()
	if numbool == True:
		message = message + text[i]

print("The message is")
print(message)
#print(re.sub(r"!|@|#|$|%|^|&|*|(|)|_|+","","!h@e#l$p"))

# Solution: equality