import random

UPPERNUM = 6
MAXBET = 4
BIGPRIZMULT = 10
MIDPRIZEMULT = 5
SMALLPRIZMULT = 3
class SlotMachine:
    maxPrizeWon = 0
    
    def __init__(self, bet=0):
        self.name = "Juliet's Balcony Slot Machine" #if bet == 0 else "machine2"
        self.bet = bet
        self.payOut = 0
        self.reelOne = 0
        self.reelTwo = 0
        self.reelThree = 0

        
    
    @staticmethod
    def getBigJackpot():
        return SlotMachine.maxPrizeWon
    
    def play(self):
        walkAway = False
        while not walkAway:
            print(self.toString())
            #print("The BIGGEST jackpot won is $%d!!!!!!!" % SlotMachine.getBigJackpot())
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
                if self.bet > 0:
                    self.spinReels()
                    self.isWinner()
                    self.resetBet()
                else:
                    print("NO PAY NO PLAY! PLEASE PAY FOR PLAY!!!")
            elif i == 4:
                print("You have chosen to walk away!\nyour current bet is: $%d" % self.bet)
                walkAway = True
                
            else:
                print("You have entered an invalid option.")
    
    def toString(self):
        return "%s\nYour current bet is %d coins. The machine displays: %d-%d-%d" % (self.name, self.bet, self.reelOne, self.reelTwo, self.reelThree)
    
    def spinReels(self):
        self.reelOne = random.randint(0, UPPERNUM - 1)
        self.reelTwo = random.randint(0, UPPERNUM - 1)
        self.reelThree = random.randint(0, UPPERNUM - 1)
    
    def resetBet(self):
        self.bet = 0
    
    def betOne(self):
        if self.bet < MAXBET:
            self.bet += 1
        else:
            print("you are at the maximum allowed bet of %d" % MAXBET)
    
    def isWinner(self):
        if self.reelOne == 0 and self.reelTwo == 0 and self.reelThree == 0:
            print("WINNER WINNER CHICKEN DINNER")
            self.payOut = self.bet * BIGPRIZMULT
            print("you have won $%d!!!" % self.payOut)
            if self.payOut > SlotMachine.maxPrizeWon:
                SlotMachine.maxPrizeWon = self.payOut
        elif self.reelOne == self.reelTwo and self.reelTwo == self.reelThree and self.reelTwo != 0:
            print("winner winner drumstick dinner")
            self.payOut = self.bet * MIDPRIZEMULT
            print("you have won $%d!!!" % self.payOut)
            if self.payOut > SlotMachine.maxPrizeWon:
                SlotMachine.maxPrizeWon = self.payOut

#counter = 0

#print("creating two slot machine objects.............................")
slotMachine1 = SlotMachine()
# slotMachine2 = SlotMachine(0)

#display machine info
#print(slotMachine1.toString())
# print(slotMachine2.toString())

#play both machines
slotMachine1.play()
# slotMachine2.play()


#display both machine info
#print(slotMachine1.toString())
#  print(slotMachine2.toString())

#play machine1
slotMachine1.play()

#display both machine info
#print(slotMachine1.toString())
#print()
# print(slotMachine2.toString())