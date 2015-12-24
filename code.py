lastCharChecks = [".", ",", "?", '"', "s"]
nonPlurals = ["this", "is"]
messagerino = []
message = str(raw_input("Pleaserino entererino yourerino messagerino: \n"))
message = message.split()
def messagerinoString(msg):
	if lastChar == "e":
		return str((msg) + "rino")
	else:
		return str((msg) + "erino")
def checkLastChar(lastChar):
	for x in range(len(lastCharChecks)):
		if lastChar == lastCharChecks[x]:
			return lastChar
def checkIfNonPlural(word):
	for x in range(len(nonPlurals)):
		if word == nonPlurals[x]:
			return True
for i in range(len(message)):
	activeWord = message[i]
	wordLength = len(activeWord)
	lastChar = activeWord[wordLength-1]
	if checkLastChar(lastChar) != None and checkIfNonPlural(activeWord) != True:
		activeWord = activeWord[0:(len(activeWord)-1)]
		messagerino.append(str((messagerinoString(activeWord)) + lastChar))
	else:
		messagerino.append(messagerinoString(activeWord))
for i in range(len(messagerino)):
	print(messagerino[i]),
