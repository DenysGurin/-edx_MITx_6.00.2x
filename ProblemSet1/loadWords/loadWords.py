import string
PATH_TO_FILE = 'C:\Users\Denys\Canopy\studing\edx_MITx_6.00.2x\ProblemSet1\loadWords\words.txt'

def loadWords():
	inFile = open(PATH_TO_FILE, 'r', 0)
	#print inFile
	line = inFile.readline()
	print line
	wordlist = string.split(line, ' ')
	#print "  ", len(wordlist), "words loaded."
	return wordlist

print loadWords()

# Uncomment the following function if you want to try the code template
def loadWords2():
    try:
 	    inFile = open(PATH_TO_FILE, 'r', 0)
    except IOError as e:
 	    print "The wordlist doesn't exist; using some fruits for now"
 	    return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", line, len(wordlist), "words loaded."
    return wordlist
PATH_TO_FILE = 'words2.txt'
#print loadWords2()
#PATH_TO_FILE = 'doesntExist.txt'
#loadWords2()
#a = open(PATH_TO_FILE, 'r', 0)
#print a