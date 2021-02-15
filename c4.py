
with open('c4source.txt') as f:
    text = f.read()

message = ""
counter = 0

for i in range(3,len(text)-3):
	if text[i-3].isupper == True:
		counter+=1
	if text[i-2].isupper == True:
		counter+=1
	if text[i-1].isupper == True:
		counter+=1
	if text[i+1].isupper == True:
		counter+=1
	if text[i+2].isupper == True:
		counter+=1
	if text[i+3].isupper == True:
		counter+=1
	if text[i].islower == True:
		counter+=1
	if counter == 7:
		message = message + text[i]
	counter = 0

print("The message is")
print(message)




""" ATTEMPT 1

bool1 = False
bool2 = False
bool3 = False

message = ""
counter = 0

for i in range(len(text)):
	if counter == 0 :
		bool1 = text[i].isupper()
		counter +=1
	if counter == 1 :
		bool2 = text[i].isupper()
		counter +=1
	if counter == 2 :
		bool3 = text[i].isupper()
		counter = 0
	if text[i].islower() == True:
		if bool1 == True and bool2 == True and bool3 == True :
			message = message + text[i]

print(message)

"""