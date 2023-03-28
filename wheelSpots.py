def wheelLocations(reelOne, reelTwo, reelThree):
    prizeArray = []
    if reelOne == 0:
        prizeArray.append('Juliette')
    elif reelOne == 1:
        prizeArray.append('Romeo')
    elif reelOne == 2:
        prizeArray.append('Shakespeare')
    elif reelOne == 3: #Shakespeare's hometown
        prizeArray.append('Stratford-upon-Avon')
    elif reelOne == 4: #Juliette's house
        prizeArray.append('Casa di Giulietta')
    elif reelOne == 5: #Romeo's house
        prizeArray.append('Montecchi house')
    
    if reelTwo == 0:
        prizeArray.append('Juliette')
    elif reelTwo == 1:
        prizeArray.append('Romeo')
    elif reelTwo == 2:
        prizeArray.append('Shakespeare')
    elif reelTwo == 3: #Shakespeare's hometown
        prizeArray.append('Stratford-upon-Avon')
    elif reelTwo == 4: #Juliette's house
        prizeArray.append('Casa di Giulietta')
    elif reelTwo == 5: #Romeo's house
        prizeArray.append('Montecchi house')
        
    if reelThree == 0:
        prizeArray.append('Juliette')
    elif reelThree == 1:
        prizeArray.append('Romeo')
    elif reelThree == 2:
        prizeArray.append('Shakespeare')
    elif reelThree == 3: #Shakespeare's hometown
        prizeArray.append('Stratford-upon-Avon')
    elif reelThree == 4: #Juliette's house
        prizeArray.append('Casa di Giulietta')
    elif reelThree == 5: #Romeo's house
        prizeArray.append('Montecchi house')

    return prizeArray
