#String Manipulation
#Sarah Friedman
#8/30/17

file = open("guido_vonRossum_speech.txt", "r")

countIndex = 0


def remove_letter(theLetter, theString):
    new = theString.replace(theLetter, "")
    print(new)
    return new


def find_letter(letter, theString):
    counted = theString.count(letter)
    print("'", letter, "' was found the the text ", counted, " times")


def wordCount(string, spaceCount):
    spaceCount = string.count(" ")
    print("There are: ", spaceCount + 1, " words in this document.")


data = file.read()

remove_letter(" ", data)
find_letter("e", data)
find_letter("a", data)
wordCount(data, countIndex)
