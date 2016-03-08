import os.path # for file manip
lastCharChecks = [".", ",", "?", '"', "s"] # exceptions to normal rule
nonPlurals = ["this", "is"] # words to not try to make plural
messagerino = [] # initialize table for finished words
messagerinoFile = open('messagerinoFile.txt', 'w') # opens file for writing
if os.path.isfile('message.txt') == True: # if a message input file exists, use that instead of user input
	messageFile = open('message.txt', 'r')
	message = messageFile.read()
	print("Usingerino messagerino filerino.")
else: # if a message input file DOESN'T exist, use user input
	message = str(raw_input("Pleaserino entererino yourerino messagerino: \n"))
message = message.split() # splits words into table
def messagerinoString(msg): # adds 'erino' or 'rino' depending on if the word ends in 'e'
	if lastChar == "e":
		return str((msg) + "rino")
	else:
		return str((msg) + "erino")
def checkLastChar(lastChar): # checks the last letter to see if it's an exception
	for x in range(len(lastCharChecks)):
		if lastChar == lastCharChecks[x]:
			return lastChar
def checkIfNonPlural(word): # checks if the word excepts the plural rule
	for x in range(len(nonPlurals)):
		if word == nonPlurals[x]:
			return True
for i in range(len(message)): # goes through word table and works on them
	activeWord = message[i] # makes things easier to deal with
	wordLength = len(activeWord)
	lastChar = activeWord[wordLength-1] # since index starts at 0, we need the index of the last char
	if checkLastChar(lastChar) != None and checkIfNonPlural(activeWord) != True: # checks if word is exception to normal rule (punctuation) and plural rule
		activeWord = activeWord[0:(len(activeWord)-1)] # makes the word 1 character shorter
		messagerino.append(str((messagerinoString(activeWord)) + lastChar)) # adds the last char to the end of the finished word
	else:
		messagerino.append(messagerinoString(activeWord)) # just goes through the normal process without dealing with words
for i in range(len(messagerino)): # goes through the finished words table, writes to file
	print(messagerino[i]), # prints all the words on 1 line
	messagerinoFile.write(messagerino[i] + " ")
messagerinoFile.close() # closes file used for writing
if os.path.isfile('message.txt') == True: # closes input file if exists
	messageFile.close()
