import string

print('Type the message you want to decrypt:')

message = input()

# Message to decrypt is: map

print('The decryption is:')

dmessage = ''

for x in range(0,len(message)):
	letter = message[x]
	letter = ord(letter)
	letter = chr(letter + 2)
	dmessage = dmessage + letter

print(dmessage)

# Solution: ocr