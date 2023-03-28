import random
#generate arrays up to this size
MAX_ARRAY_SIZE = 20
#number of arrays to generate
NUM_ARRAYS_TO_SORT = 10


def testSorted(input):
    """this function tests if a given array is sorted or not.
    args: 
        input= some array"""
    if input == sorted(input):
        print("list is sorted!")
    else: print("NOT SORTED!")


def shakerSort(input):
    """Sort the given input using the cocktail "SHAKER" method.
    uses insertion sort for anything left over"""
    
    #create min and max arrays
    minarr = []
    maxarr = []
    
    ctr =0
    #find how many times the shaker will run, should be approximately len(array)/2 since
    #it grabs 2 elements per run. 
    if len(input) % 2 == 0:
        numRuns = len(input)/2+1
    else:
        numRuns = (len(input)/2)+.5+1
    #print("numRuns:", numRuns)
    while ctr != numRuns:
        #initialize varaibles
        minIndex = 0
        maxIndex = 0
        mi = input[0]
        ma = input[0]
    #go from left to right finding the max
        for i in range(0,len(input)):
            if input[i] > ma:
                ma = input[i]
                maxIndex = i
    #go from right to left finding the min
        for i in range(len(input)-1,0,-1):
            if input[i] < mi and input[i]!= -1:
                mi = input[i]
                minIndex = i
        #append the min
        if(mi!= -1):
            minarr.append(mi)
        #prepend the max
        if(ma!= -1):
            maxarr = [ma] + maxarr
        input[minIndex]= -1
        input[maxIndex]= -1
        
        #debugging prints
        #print(minarr, maxarr)
        #print(input)

        ctr +=1
    #last pass to make sure we got everything (insertion)
    for elem in input:
        if elem != -1:
            for i in range(len(minarr)):
                try:
                    if minarr[i] < elem and minarr[i+1]> elem:
                        minarr.insert(i+1,elem)
                except IndexError:
                    minarr.append(elem)
    #add the min and max arrays together and return them
    outarr = minarr + maxarr
    return outarr

#driver code
for j in range(NUM_ARRAYS_TO_SORT):
    randInput = []
    m = random.randint(4,MAX_ARRAY_SIZE)
    for i in range(0,m):
        n = random.randint(0,100)
        randInput.append(n)
    #print("original:",arr)
    original = randInput[:]
    #for elem in randInput:
    #    original.append(elem)

    sortedList = shakerSort(randInput)
    print("original:",original, "len:", len(original))
    print("sorted:",sortedList, "len:", len(sortedList))
    testSorted(sortedList)
