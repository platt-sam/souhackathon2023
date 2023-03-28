import requests

testString = "In fair Verona where we lay our scene From ancient grudge break to new mutiny Where civil blood makes civil hands unclean"


#this function simply tells if the input is 10 syllables long
def isPentameter(inputString):
    if(len(inputString)==0):
        print("EMPTY IMPUT")
        return 0
    with open("apikey.txt","r") as f:
        apikey = f.readline()

    headers = {
        "X-RapidAPI-Key": f"{apikey}",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    syllableCount= 0
    words = inputString.split()
    #for each word, query the API to get a list of syllables and what those syllables are 
    for word in words:
        # #print the word so we're not staring at a blank screen wondering if its working...
        # print(word)
        url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"
        response = requests.request("GET", url, headers=headers)
        js = response.json()
        try:
            syllables = js['syllables']['list']
            syllableCount += js['syllables']['count']
        except:
            syllables=word
            syllableCount +=1
        print(syllables, syllableCount)
    #input must be some multiple of 10 for it to be considered pentameter. 
    #if the input is 20 syllables long, then the input might simply be 2 pentameter passages. 
    if syllableCount%10 == 0:
        print("the input is pentameter.")
        return 1
    else:
        print("NOT PENTAMETER!")
        return 0


isPentameter(testString)

