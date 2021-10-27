# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
from datetime import datetime


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    
    # Print first 50 values of each list to verify contents
    # print(dictionary[0:50])
    # print(aliceWords[0:50])
    while (True):
        print("1. Spell Check a Word (Linear Search)\n"
        "2. Spell Check a Word (Binary Search)\n"
        "3. Spell Check Alice in Wonderland (Linear Search)\n"
        "4. Spell check Alice in Wonderland (Binary Search)\n"
        "5. Exit\n"
        "Enter menu selection (1-5)")

        userinput = int(input())

        if userinput == 1:
            iffound = linearWordCheck(dictionary)
            if iffound[0] == -1:
                print(f"{iffound[1]} is NOT in the dictionary ({iffound[2].microseconds} microseconds)")
            else:
                print(f"{iffound[1]} is IN the dictionary at position {iffound[0]} ({iffound[2].microseconds} microseconds)")

        elif userinput == 2:
            iffound = binaryWordCheck(dictionary)
            if iffound[0] == -1:
                print(f"{iffound[1]} is NOT in the dictionary ({iffound[2].microseconds} microseconds)")
            else:
                print(f"{iffound[1]} is IN the dictionary at position {iffound[0]} ({iffound[2].microseconds} microseoncds)")

        elif userinput == 3:
            wordsnowfound = aliceLinearCheck(dictionary, aliceWords)
            print (f"{wordsnowfound[0]} words have NOT been found ({wordsnowfound[1].seconds} seconds)")

        elif userinput == 4:
            wordsnotfound2 = aliceBinaryCheck(dictionary, aliceWords)
            print (f"{wordsnotfound2[0]} words have NOT been found ({wordsnotfound2[1].microseconds} microseconds)")
        
        elif userinput == 5:
          
            return

        else:
            print("Please enter a valid number")

        print("\n")
# end main()

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()



def linearWordCheck(dictionary):
    print("Please enter a word")
    userInput1 = input().lower()
    starttime = datetime.today().now()
    output = linearSearch(dictionary, userInput1)
    endtime = datetime.today().now()

    return output, userInput1, endtime - starttime

def binaryWordCheck (dictionary):
    print("Please enter a word")
    userInput2 = input().lower()
    starttime = datetime.today().now()
    output =  binarySearch(dictionary, userInput2)
    endtime = datetime.today().now()
    
    return output, userInput2, endtime - starttime


def aliceLinearCheck(dictionary, aliceWords):
    counter = 0
    starttime = datetime.today().now()
    for word in aliceWords:
        if linearSearch(dictionary, word.lower()) == -1:
            counter += 1
    endtime = datetime.today().now()
    return counter, endtime - starttime

def aliceBinaryCheck(dictionary, aliceWords):
    counter = 0 
    starttime = datetime.today().now()
    for word in aliceWords:
        if binarySearch(dictionary, word.lower()) == -1:
            counter +=1
    endtime = datetime.today().now()
    return counter, endtime - starttime
    

def binarySearch(anArray, item):
    low = 0
    high = len(anArray)-1

    while low <= high:
        middle = int((low + high)/2)
        
        if anArray[middle] == item:
            return middle
        elif anArray[middle] > item:
            high = middle - 1
        else:
            low = middle + 1

    return -1

def linearSearch (anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1

# Call main() to begin program
main()