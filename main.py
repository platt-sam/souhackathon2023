import random
from playsound import playsound
UPPERNUM = 6
MAXBET = 4
BIGPRIZMULT = 5
MIDPRIZEMULT = 3
SMALLPRIZMULT = 1
class SlotMachine:
    maxPrizeWon = 0
    
    def __init__(self, bet=0):
        self.name = "Juliet's Balcony Slot Machine" 
        self.bet = bet
        self.payOut = 0
        self.reelOne = 6
        self.reelTwo = 6
        self.reelThree = 6

        
    
    @staticmethod
    def getBigJackpot():
        return SlotMachine.maxPrizeWon
    
    def play(self):
        walkAway = False
        while not walkAway:
            print("your total bet is",self.bet,"this machine is ",self.name)
            print("Please make your choice:\n1. Reset.\n2. Bet one coin.\n3. Pull the handle.\n4. Walk away.")
            
            i = int(input())
            if i == 1:
                print("you have chosen to reset your bet!")
                self.resetBet()
            elif i == 2:
                print("You have chosen to bet one coin.")
                self.betOne()
            elif i == 3:
                print("you have chosen to pull the handle.")
                # for playing note.mp3 file
                playsound('cha-ching.wav')
                if self.bet > 0:
                    self.spinReels()
                    self.isWinner()
                    self.resetBet()
                else:
                    print("NO PAY NO PLAY! PLEASE PAY FOR PLAY!!!")
            elif i == 4:
                print("You have chosen to walk away!\nthe largest payout has been $", self.getBigJackpot(), "Coins")
                walkAway = True
                
            else:
                print("You have entered an invalid option.")
    
    def toString(self):
        return "%s\nYour current bet is %d coins. The machine displays: %d-%d-%d" % (self.name, self.bet, self.reelOne, self.reelTwo, self.reelThree)
    
    def spinReels(self):
        self.reelOne = random.randint(0, UPPERNUM - 1)
        self.reelTwo = random.randint(0, UPPERNUM - 1)
        self.reelThree = random.randint(0, UPPERNUM - 1)
        prizeArray = []
        if self.reelOne == 0:
            prizeArray.append('Juliette')
        elif self.reelOne == 1:
            prizeArray.append('Romeo')
        elif self.reelOne == 2:
            prizeArray.append('Shakespeare')
        elif self.reelOne == 3: #Shakespeare's hometown
            prizeArray.append('Stratford-upon-Avon')
        elif self.reelOne == 4: #Juliette's house
            prizeArray.append('Casa di Giulietta')
        elif self.reelOne == 5: #Romeo's house
            prizeArray.append('Montecchi house')
    
        if self.reelTwo == 0:
            prizeArray.append('Juliette')
        elif self.reelTwo == 1:
            prizeArray.append('Romeo')
        elif self.reelTwo == 2:
            prizeArray.append('Shakespeare')
        elif self.reelTwo == 3: #Shakespeare's hometown
            prizeArray.append('Stratford-upon-Avon')
        elif self.reelTwo == 4: #Juliette's house
            prizeArray.append('Casa di Giulietta')
        elif self.reelTwo == 5: #Romeo's house
            prizeArray.append('Montecchi house')
        
        if self.reelThree == 0:
            prizeArray.append('Juliette')
        elif self.reelThree == 1:
            prizeArray.append('Romeo')
        elif self.reelThree == 2:
            prizeArray.append('Shakespeare')
        elif self.reelThree == 3: #Shakespeare's hometown
            prizeArray.append('Stratford-upon-Avon')
        elif self.reelThree == 4: #Juliette's house
            prizeArray.append('Casa di Giulietta')
        elif self.reelThree == 5: #Romeo's house
            prizeArray.append('Montecchi house')
        print("The display says",prizeArray)
    
    def resetBet(self):
        self.bet = 0
    
    def betOne(self):
        if self.bet < MAXBET:
            self.bet += 1
        else:
            print("you are at the maximum allowed bet of %d" % MAXBET)
    
    def isWinner(self):
        if self.reelOne == self.reelTwo and self.reelTwo == self.reelThree:
            print("MID WIN, THREE OF A KIND!")
            self.payOut = self.bet * MIDPRIZEMULT
            if self.payOut > SlotMachine.maxPrizeWon:
                SlotMachine.maxPrizeWon = self.payOut
            print("you have won $%d!!!" % self.payOut)

        elif self.reelOne == 0 and self.reelTwo == 4 and self.reelThree == 2:
            print("you have Juilette, her home and Shakespere the playwrite this IS A BIG PRIZE!")
            self.payOut = self.bet * BIGPRIZMULT
            if self.payOut > SlotMachine.maxPrizeWon:
                SlotMachine.maxPrizeWon = self.payOut
            print("YOU HAVE WON $%d!!!" % self.payOut)

        elif self.reelOne == 1 and self.reelTwo == 5 and self.reelThree == 2:
            print("you have Romeo, his home town and Shakespere the playwrite this IS A BIG PRIZE!")
            self.payOut = self.bet * BIGPRIZMULT
            if self.payOut > SlotMachine.maxPrizeWon:
                SlotMachine.maxPrizeWon = self.payOut
            print("YOU HAVE WON $%d!!!" % self.payOut)

        elif self.reelOne == self.reelTwo or self.reelTwo == self.reelThree or self.reelOne == self.reelThree:
            print("TWO OF A KIND, THIS IS A SMALL PRIZE!")
            self.payOut = self.bet * SMALLPRIZMULT
            if self.payOut > SlotMachine.maxPrizeWon:    
                SlotMachine.maxPrizeWon = self.payOut
            print("YOU HAVE WON $%d!!!" % self.payOut)
        
        else: #you loose
            print("you have tasted the poison and lost please play again")
            
        if self.payOut > SlotMachine.maxPrizeWon:
                SlotMachine.maxPrizeWon = self.payOut
        
        if self.payOut > SlotMachine.maxPrizeWon:
                SlotMachine.maxPrizeWon = self.payOut


slotMachine1 = SlotMachine()

slotMachine1.play()

slotMachine1.play()
