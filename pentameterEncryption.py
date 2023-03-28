import requests
import math


#print function to not repeat myself 
def printMatrix(arr):
    print("~~~~")
    for r in arr:
        print(r)
#prints the array as a string, again to not repeat myself
def printString(arr, numRows):
    print("~~~~as a string~~~~")
    substrings = []
    for row in arr:
        substr = ""
        for char in row:
            if(type(char)==list):
                substr += char[0]
            else:    
                substr += char
        substrings.append(substr)
    result = " ".join(substrings)
    print(result)
#get the api key from the file so we dont leak API keys (this is a public repo after all)
with open("apikey.txt","r") as f:
    apikey = f.readline()

headers = {
    "X-RapidAPI-Key": f"{apikey}",
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}
plaintextArray = []

#string we want to encrypt
testString = "In fair Verona where we lay our scene From ancient grudge break to new mutiny Where civil blood makes civil hands unclean"
#split the test string into a list of words
words = testString.split()
#for each word, query the API to get a list of syllables and what those syllables are 
for word in words:
    #print the word so we're not staring at a blank screen wondering if its working...
    print(word)
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"
    response = requests.request("GET", url, headers=headers)
    js = response.json()

    try:
        syllables = js['syllables']['list']
        syllableCount = js['syllables']['count']
    except:
        syllables=word
        syllableCount =1
    if syllableCount>1:
        for syl in syllables:
            plaintextArray.append(syl)
        #put the spaces back
        end = len(plaintextArray)-1
        plaintextArray[end] = plaintextArray[end]+" "
    else:
        plaintextArray.append(word+" ")

#the number of rows will change based on the length of our string.
numRows = math.ceil(len(plaintextArray)/10)
#columns is always 10 because Pentameter is a lenght of 10 syllables
cols = 10

matrix = []

#convert the plaintext array into a 2d array for manipluation 
ctr = 0
for i in range(numRows):
    row = []
    for j in range(10):
        value = plaintextArray[ctr]
        row.append(value)
        ctr+=1
    matrix.append(row)
print("~~~original input~~~")
printMatrix(matrix)

#encryption method
def encrypt(arr, numRows):
    for i in range(numRows):
        for j in range (10):
            if j%2 ==0:
                end = arr[i][9]
                if (j+1< 10):
                    tmp = arr[i][j]
                    arr[i][j] = arr[i][j+1]
                    arr[i][j+1] = tmp     
                else:
                    arr[i][0]=end

    return arr                

encryptedArray = encrypt(matrix,numRows)
printMatrix(encryptedArray)
printString(encryptedArray,numRows)

#decryption method 
def decrypt(arr, numRows):
    for i in range(numRows):
        for j in range (10):
            if j%2 ==0:
                end = arr[i][9]
                if (j+1< 10):
                    tmp = arr[i][j]
                    arr[i][j] = arr[i][j+1]
                    arr[i][j+1] = tmp
                else:
                    arr[i][0]=end   
          
    return arr        
     
decryptedArray = decrypt(encryptedArray,numRows)
printMatrix(decryptedArray)
printString(decryptedArray,numRows)
