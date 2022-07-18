import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox 

#Card Class
class Card:
    def __init__(self, s, n, p):
        self.suit = s
        self.number = n  
        self.points = int(p)
          
    def __str__(self):
        if self.number == 11:
            return "Jack" + " of " + str(self.suit)
        elif self.number == 12:
            return "Queen" + " of " + str(self.suit)
        elif self.number == 13:
            return "King" + " of " + str(self.suit)
        elif self.number == 1:
            return "Ace" + " of " + str(self.suit)
        else:
            return str(self.number) + " of " + str(self.suit)
    def sayCard(self):  #returns the instance of a card as a comprehensible card 
        if self.number == 11:
            return "Jack" + " of " + str(self.suit)
        elif self.number == 12:
            return "Queen" + " of " + str(self.suit)
        elif self.number == 13:
            return "King" + " of " + str(self.suit)
        elif self.number == 1:
            return "Ace" + " of " + str(self.suit)
        else:
            return str(self.number) + " of " + str(self.suit)

    def giveValue(self):  #the program uses this to compute the total of the cards
        return int(self.points)

    def giveNumber(self):  #the number of a card
        return str(self.number)

    def reduce(self):
        self.points = 1

    def recharge(self):
        self.points = 11
   
#Deck Class        
class Deck(Card):
    def __init__(self,new,counts={}):
        self.cards=[]
        if new == True: 
            for key in counts:
                for i in range(13):
                    for x in range(counts[key][i]):
                        self.cards.append(Card(key,i+1,i+1))
    def show_deck(self):
        for item in self.cards:
            print (item)
    def shuffle(self):
        for i in range(len(self.cards)):
            r=random.randint(0,len(self.cards)-1)
            temp = self.cards[i]
            self.cards[i] = self.cards[r]
            self.cards[r] = temp
    def drawCards(self,n):
        removed_cards=[]
        for i in range(n):
            removed_cards.append(self.cards.pop(0))
            #self.cards.pop(0)
        return removed_cards
    def addCards(self,add):
        self.cards+= add
    def __str__(self):
        s=''
        for i in self.cards:
            s =str(i) 
        return s
    def discardCard(self,dc):
        for i in dc:
            self.cards.append(i)
    
    def points(self, blackjack=False):
        p=0
    
        if blackjack:
          for i in self.cards:
              if i.giveValue() == 1:
                p += 11
              elif i.giveValue() > 10:
                p += 10
              else: 
                p+=i.giveValue() 
        else: 
          for i in self.cards:
              p+=i.giveValue()
          
        return p

    
        
#class BlackJack:
class BlackJack():
    def __init__(self,np):
        self.numplayers=np
        self.officialdeck=Deck(True,{"Spades":[1,1,1,1,1,1,1,1,1,1,1,1,1], "Hearts":[1,1,1,1,1,1,1,1,1,1,1,1,1], "Clubs":[1,1,1,1,1,1,1,1,1,1,1,1,1], "Diamonds":[1,1,1,1,1,1,1,1,1,1,1,1,1]}) #Expresses how many of each suit there is)
       
        self.players=[Deck(False),Deck(False)]     
        self.playerTurn=0
        self.playerList = []
        self.dealerList = []
        self.determinant = 0

        #window where Blackjack will be played
        self.window=tk.Tk()
        self.window.title("BlackJack")
        #creating the green background
        canvas_width = 1200
        canvas_height = 500
        self.my_canvas = tk.Canvas(self.window, width=canvas_width, height=canvas_height, bg="green")
        self.my_canvas.pack()

        #Uploading the image files.
        self.Clubs_2= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-2.png")
        self.Clubs_3= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-3.png")
        self.Clubs_4= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-4.png")
        self.Clubs_5= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-5.png")
        self.Clubs_6= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-6.png")
        self.Clubs_7= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-7.png")
        self.Clubs_8= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-8.png")
        self.Clubs_9= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-9.png")
        self.Clubs_10= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-10.png")
        self.Clubs_Jack= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-Jack.png")
        self.Clubs_Queen= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-Queen.png")
        self.Clubs_King= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-King.png")
        self.Clubs_Ace= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-Ace.png")
        self.Spades_2= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_2_ccexpress.png")
        self.Spades_3= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_3_ccexpress.png")
        self.Spades_4= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_4_ccexpress.png")
        self.Spades_5= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_5_ccexpress.png")
        self.Spades_6= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_6_ccexpress.png")
        self.Spades_7= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_7_ccexpress.png")
        self.Spades_8= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_8_ccexpress.png")
        self.Spades_9= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_9_ccexpress.png")
        self.Spades_10= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_10_ccexpress.png")
        self.Spades_Jack= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_Jack_ccexpress.png")
        self.Spades_Queen= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_Queen_ccexpress.png")
        self.Spades_King= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_King_ccexpress.png")
        self.Spades_Ace= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_Ace_ccexpress.png")
        self.Hearts_2= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_2_ccexpress.png")
        self.Hearts_3= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_3_ccexpress.png")
        self.Hearts_4= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_4_ccexpress.png")
        self.Hearts_5= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_5_ccexpress.png")
        self.Hearts_6= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_6_ccexpress.png")
        self.Hearts_7= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_7_ccexpress.png")
        self.Hearts_8= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_8_ccexpress.png")
        self.Hearts_9= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_9_ccexpress.png")
        self.Hearts_10= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_10_ccexpress.png")
        self.Hearts_Jack= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_Jack_ccexpress.png")
        self.Hearts_Queen= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_Queen_ccexpress.png")
        self.Hearts_King= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_King_ccexpress.png")
        self.Hearts_Ace= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_Ace_ccexpress.png")
        self.Diamonds_2= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_2_ccexpress.png")
        self.Diamonds_3= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_3_ccexpress.png")
        self.Diamonds_4= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_4_ccexpress.png")
        self.Diamonds_5= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_5_ccexpress.png")
        self.Diamonds_6= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_6_ccexpress.png")
        self.Diamonds_7= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_7_ccexpress.png")
        self.Diamonds_8= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_8_ccexpress.png")
        self.Diamonds_9= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_9_ccexpress.png")
        self.Diamonds_10= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_10_ccexpress.png")
        self.Diamonds_Jack= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_Jack_ccexpress.png")
        self.Diamonds_Queen= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_Queen_ccexpress.png")
        self.Diamonds_King= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_King_ccexpress.png")
        self.Diamonds_Ace= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_Ace_ccexpress.png")

        #hiding one hand of the dealer.
        self.imageCover = self.my_canvas.create_rectangle(1090-(2*1*65), 50, 1150-(2*1*65), 130, fill="", outline="")
        
        self.DealerHand=tk.Message(self.window,text="Dealer's Cards:")
        self.DealerHand.pack(side ='right')
        #dealer's cards are placed here
        self.DealerPlayed=tk.Message(self.window,text="")
        self.DealerPlayed.pack(side='right')
       
        self.PlayerHand = tk.Message(self.window, text="Player's Cards:")   
        self.PlayerHand.pack(side ='left')
        #players cards are here
        self.Playerplayed = tk.Message(self.window, text="")
        self.Playerplayed.pack(side='left')
        self.play = tk.Button(self.window, text="Deal the next card", command=self.PLAY)#initiates the game
        self.play.pack(side ='top')

        self.hit = tk.Button(self.window, text="Hit",command=self.HIT)#hits
        self.hit.pack(side='left')
        self.hit["state"] = "disabled"      #the player cannot click on the hit button without first starting a game

        self.surrender = tk.Button(self.window, text="Stay",command=self.STAY)#Stay
        self.surrender.pack(side = 'right')
        self.surrender["state"] = "disabled"    #the player cannot click on the stay button without first starting a game

        Retry = tk.Button(self.window, text="Retry",command=self.RETRY)#destroys the window and creates a brand new one, thus initiating a new game of blackjack
        Retry.pack(side ='top')

        Quit_Button = tk.Button(self.window, text="Quit",command=self.QUIT)#destroys the window
        Quit_Button.pack(side='bottom')

    #def printingPicture(self):
        
    def takeTurn(self):
        drawn = self.officialdeck.drawCards(1)
        self.players[self.playerTurn].addCards(drawn)
        self.playerTurn=(self.playerTurn+1)%self.numplayers
        
    #creates lists of each players' cards and assigns it to image on canvas.     
    def createList(self):
        if str(self.players[0])== '':
            self.playerList = self.playerList
        if str(self.players[0])!= '':
            if self.playerList==[]:
                self.playerList.append(str(self.players[0]))
            if self.playerList!=[]:
                if str(self.players[0])!= self.playerList[-1]:
                    self.playerList.append(str(self.players[0]))
        if str(self.players[1])== '':
            self.dealerList = self.dealerList
        if str(self.players[1])!= '':
            if self.dealerList==[]:
                self.dealerList.append(str(self.players[1]))
            if self.dealerList!=[]:
                if str(self.players[1])!= self.dealerList[-1]:
                    self.dealerList.append(str(self.players[1]))
        self.playerPoints()
        for i in range(len(self.playerList)):
            aP = str(self.playerList[i])
            #covering the existing image
            imageCover = self.my_canvas.create_rectangle(40+(2*i*65), 40, 120+(2*i*65), 140, fill="light blue", outline="black")
            #assigning image to cards
            if aP =="2 of Clubs":
                card_image = self.Clubs_2
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "3 of Clubs":
                card_image = self.Clubs_3
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "4 of Clubs":
                card_image = self.Clubs_4
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "5 of Clubs":
                card_image = self.Clubs_5
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "6 of Clubs":
                card_image = self.Clubs_6
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "7 of Clubs":
                card_image = self.Clubs_7
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "8 of Clubs":
                card_image = self.Clubs_8
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "9 of Clubs":
                card_image = self.Clubs_9
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "10 of Clubs":
                card_image = self.Clubs_10
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Jack of Clubs":
                card_image = self.Clubs_Jack
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Queen of Clubs":
                card_image = self.Clubs_Queen
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "King of Clubs":
                card_image = self.Clubs_King
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Ace of Clubs":
                card_image = self.Clubs_Ace
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP =="2 of Hearts":
                card_image = self.Hearts_2
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "3 of Hearts":
                card_image = self.Hearts_3
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "4 of Hearts":
                card_image = self.Hearts_4
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "5 of Hearts":
                card_image = self.Hearts_5
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "6 of Hearts":
                card_image = self.Hearts_6
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "7 of Hearts":
                card_image = self.Hearts_7
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "8 of Hearts":
                card_image = self.Hearts_8
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "9 of Hearts":
                card_image = self.Hearts_9
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "10 of Hearts":
                card_image = self.Hearts_10
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Jack of Hearts":
                card_image = self.Hearts_Jack
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Queen of Hearts":
                card_image = self.Hearts_Queen
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "King of Hearts":
                card_image = self.Hearts_King
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Ace of Hearts":
                card_image = self.Hearts_Ace
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP =="2 of Diamonds":
                card_image = self.Diamonds_2
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "3 of Diamonds":
                card_image = self.Diamonds_3
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "4 of Diamonds":
                card_image = self.Diamonds_4
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "5 of Diamonds":
                card_image = self.Diamonds_5
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "6 of Diamonds":
                card_image = self.Diamonds_6
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "7 of Diamonds":
                card_image = self.Diamonds_7
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "8 of Diamonds":
                card_image = self.Diamonds_8
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "9 of Diamonds":
                card_image = self.Diamonds_9
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "10 of Diamonds":
                card_image = self.Diamonds_10
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Jack of Diamonds":
                card_image = self.Diamonds_Jack
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Queen of Diamonds":
                card_image = self.Diamonds_Queen
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "King of Diamonds":
                card_image = self.Diamonds_King
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Ace of Diamonds":
                card_image = self.Diamonds_Ace
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            if aP =="2 of Spades":
                card_image = self.Spades_2
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "3 of Spades":
                card_image = self.Spades_3
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "4 of Spades":
                card_image = self.Spades_4
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "5 of Spades":
                card_image = self.Spades_5
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "6 of Spades":
                card_image = self.Spades_6
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "7 of Spades":
                card_image = self.Spades_7
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "8 of Spades":
                card_image = self.Spades_8
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "9 of Spades":
                card_image = self.Spades_9
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "10 of Spades":
                card_image = self.Spades_10
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Jack of Spades":
                card_image = self.Spades_Jack
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Queen of Spades":
                card_image = self.Spades_Queen
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "King of Spades":
                card_image = self.Spades_King
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
            elif aP == "Ace of Spades":
                card_image = self.Spades_Ace
                self.my_canvas.create_image(50+(2*i*65), 50, anchor = NW, image = card_image)
        for i in range(len(self.dealerList)):
            a1 = str(self.dealerList[i])
            #covering the existing image
            imageCover = self.my_canvas.create_rectangle(1080-(2*i*65), 40, 1160-(2*i*65), 140, fill="light blue", outline="black")
            #assigning image to cards
            if a1 =="2 of Clubs":
                card_image = self.Clubs_2
                self.my_canvas.create_image(1090-(2*i*70), 50, anchor = NW, image = card_image)
            elif a1 == "3 of Clubs":
                card_image = self.Clubs_3
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "4 of Clubs":
                card_image = self.Clubs_4
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "5 of Clubs":
                card_image = self.Clubs_5
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "6 of Clubs":
                card_image = self.Clubs_6
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "7 of Clubs":
                card_image = self.Clubs_7
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "8 of Clubs":
                card_image = self.Clubs_8
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "9 of Clubs":
                card_image = self.Clubs_9
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "10 of Clubs":
                card_image = self.Clubs_10
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Jack of Clubs":
                card_image = self.Clubs_Jack
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Queen of Clubs":
                card_image = self.Clubs_Queen
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "King of Clubs":
                card_image = self.Clubs_King
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Ace of Clubs":
                card_image = self.Clubs_Ace
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 =="2 of Hearts":
                card_image = self.Hearts_2
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "3 of Hearts":
                card_image = self.Hearts_3
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "4 of Hearts":
                card_image = self.Hearts_4
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "5 of Hearts":
                card_image = self.Hearts_5
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "6 of Hearts":
                card_image = self.Hearts_6
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "7 of Hearts":
                card_image = self.Hearts_7
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "8 of Hearts":
                card_image = self.Hearts_8
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "9 of Hearts":
                card_image = self.Hearts_9
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "10 of Hearts":
                card_image = self.Hearts_10
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Jack of Hearts":
                card_image = self.Hearts_Jack
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Queen of Hearts":
                card_image = self.Hearts_Queen
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "King of Hearts":
                card_image = self.Hearts_King
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Ace of Hearts":
                card_image = self.Hearts_Ace
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 =="2 of Diamonds":
                card_image = self.Diamonds_2
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "3 of Diamonds":
                card_image = self.Diamonds_3
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "4 of Diamonds":
                card_image = self.Diamonds_4
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "5 of Diamonds":
                card_image = self.Diamonds_5
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "6 of Diamonds":
                card_image = self.Diamonds_6
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "7 of Diamonds":
                card_image = self.Diamonds_7
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "8 of Diamonds":
                card_image = self.Diamonds_8
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "9 of Diamonds":
                card_image = self.Diamonds_9
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "10 of Diamonds":
                card_image = self.Diamonds_10
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Jack of Diamonds":
                card_image = self.Diamonds_Jack
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Queen of Diamonds":
                card_image = self.Diamonds_Queen
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "King of Diamonds":
                card_image = self.Diamonds_King
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Ace of Diamonds":
                card_image = self.Diamonds_Ace
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            if a1 =="2 of Spades":
                card_image = self.Spades_2
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "3 of Spades":
                card_image = self.Spades_3
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "4 of Spades":
                card_image = self.Spades_4
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "5 of Spades":
                card_image = self.Spades_5
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "6 of Spades":
                card_image = self.Spades_6
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "7 of Spades":
                card_image = self.Spades_7
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "8 of Spades":
                card_image = self.Spades_8
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "9 of Spades":
                card_image = self.Spades_9
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "10 of Spades":
                card_image = self.Spades_10
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Jack of Spades":
                card_image = self.Spades_Jack
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Queen of Spades":
                card_image = self.Spades_Queen
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "King of Spades":
                card_image = self.Spades_King
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            elif a1 == "Ace of Spades":
                card_image = self.Spades_Ace
                self.my_canvas.create_image(1090-(2*i*65), 50, anchor = NW, image = card_image)
            #covering the second hand of the dealer. 
            if i ==1:
                self.imageCover = self.my_canvas.create_rectangle(1090-(2*i*65), 50, 1150-(2*i*65), 130, fill="black", outline="red")
        self.Playerplayed['text'] = str(self.playerList)
    #function assigned to Play button. Everytime it is called the lists for player and dealer is updated and the points are checked for winners.     
    def PLAY(self):
        self.officialdeck.shuffle()
        for i in range(1):
            self.takeTurn()
        if len(self.playerList)==2:
            self.play["state"]="disabled"
        self.checkBlackJack()
        self.createList()
        print(self.playerList)#used to check if the lists are created properly and consistent with the pictures shown on window.
        print(self.dealerList)
    #function assigned to stay button. Everytime it is called the lists for player and dealer is updated and the points are checked for winners.
    #it also gives the dealer necessary cards if the dealers total valyue is less than 17 after getting initial cards. 
    def STAY(self):
        self.determinant=1
        self.hit["state"] = "disabled"
        self.surrender["state"]="disabled"
        self.play["state"]="disabled"
        while self.Dlp <17:
            self.players[1].addCards(self.officialdeck.drawCards(1))
            self.createList()
        self.checkPointStay()
        self.DealerPlayed["text"] = str(self.dealerList)
    #function to calculate the player points
    def playerPoints(self):
        CardNamePlayer = self.playerList
        CardNameDealer = self.dealerList
        self.Plp = 0
        self.Dlp = 0
        for i in range(len(self.playerList)): 
            if CardNamePlayer[i][0]=="2":
                self.Plp = self.Plp+int(CardNamePlayer[i][0])
            if CardNamePlayer[i][0]=="3":
                self.Plp = self.Plp+int(CardNamePlayer[i][0])
            if CardNamePlayer[i][0]=="4":
                self.Plp = self.Plp+int(CardNamePlayer[i][0])
            if CardNamePlayer[i][0]=="5":
                self.Plp = self.Plp+int(CardNamePlayer[i][0])
            if CardNamePlayer[i][0]=="6":
                self.Plp = self.Plp+int(CardNamePlayer[i][0])
            if CardNamePlayer[i][0]=="7":
                self.Plp = self.Plp+int(CardNamePlayer[i][0])
            if CardNamePlayer[i][0]=="8":
                self.Plp = self.Plp+int(CardNamePlayer[i][0])
            if CardNamePlayer[i][0]=="9":
                self.Plp = self.Plp+int(CardNamePlayer[i][0])
            if CardNamePlayer[i][0:2]=="10":
                self.Plp = self.Plp+int(CardNamePlayer[i][0:2])
            if CardNamePlayer[i][0:4]=="Jack":
                self.Plp = self.Plp+10
            if CardNamePlayer[i][0:5]=="Queen":
                self.Plp = self.Plp + 10
            if CardNamePlayer[i][0:4]=="King":
                self.Plp = self.Plp+10
            if CardNamePlayer[i][0:3]=="Ace":
                self.Plp = self.Plp+11
        for i in range(len(self.dealerList)):
            if CardNameDealer[i][0]=="2":
                self.Dlp = self.Dlp+int(CardNameDealer[i][0])
            if CardNameDealer[i][0]=="3":
                self.Dlp = self.Dlp+int(CardNameDealer[i][0])
            if CardNameDealer[i][0]=="4":
                self.Dlp = self.Dlp+int(CardNameDealer[i][0])
            if CardNameDealer[i][0]=="5":
                self.Dlp = self.Dlp+int(CardNameDealer[i][0])
            if CardNameDealer[i][0]=="6":
                self.Dlp = self.Dlp+int(CardNameDealer[i][0])
            if CardNameDealer[i][0]=="7":
                self.Dlp = self.Dlp+int(CardNameDealer[i][0])
            if CardNameDealer[i][0]=="8":
                self.Dlp = self.Dlp+int(CardNameDealer[i][0])
            if CardNameDealer[i][0]=="9":
                self.Dlp = self.Dlp+int(CardNameDealer[i][0])
            if CardNameDealer[i][0:2]=="10":
                self.Dlp =self.Dlp + int(CardNameDealer[i][0:2])
            if CardNameDealer[i][0:4]=="Jack":
                self.Dlp = self.Dlp + 10
            if CardNameDealer[i][0:5]=="Queen":
                self.Dlp = self.Dlp + 10
            if CardNameDealer[i][0:4]=="King":
                self.Dlp = self.Dlp + 10
            if CardNameDealer[i][0:3]=="Ace":
                self.Dlp = self.Dlp + 11
            
        

        print(self.Dlp)#check if the points are consistent with the shown cards.
        print(self.Plp)
            
    #funstion that checks whether the player has a blackjack or not. i.e. 21 in total value after getting initial cards. And it notifies the winner. 
    def checkBlackJack(self):
        if len(self.playerList)==2:
            if self.Plp == 21:
                messagebox.showinfo("BlackJack!", "You won the bet.")
                self.hit["state"]= "disabled"
                self.play["state"]="disabled"
                self.surrender["state"]="disabled"
            else:
                self.hit["state"]= "normal"
                self.surrender["state"]="normal"
    #function used to check points for results if the stay button is hit and notifies the winner or the looser. 
    def checkPointStay(self):
        if self.Dlp<=21:
            if self.Plp>self.Dlp:
                messagebox.showinfo("Winner!", "You won the bet.")
            elif self.Plp==self.Dlp:
                messagebox.showinfo("Tie!", "It's a tie.")
            else:
                messagebox.showinfo("Lost!", "You lost the bet.")
        if self.Dlp>21:
            if self.Plp<self.Dlp:
                messagebox.showinfo("Winner!", "You won the bet.")
            elif self.Plp==self.Dlp:
                messagebox.showinfo("Tie!", "It's a tie.")
            else:
                messagebox.showinfo("Lost!", "You lost the bet.")
    #function used in hit button to check is the player is busted or not. 
    def checkPointHit(self):
        if self.Plp>21:
            messagebox.showinfo("Bust!", "You lost the bet.")
            self.hit["state"]= "disabled"
            self.play["state"]="disabled"
            self.surrender["state"]="disabled"
    #hit function for hit button         
    def HIT(self):
        for i in range(1):
            self.players[0].addCards(self.officialdeck.drawCards(1))
        
        self.createList()
        self.checkPointHit()
        print(self.playerList)#checking the consistencies of list and images. 
        print(self.dealerList)


    #destroys the current window and creates a brand new game of blackjack on a new window    
    def RETRY(self):    
        self.window.destroy() 
       
        BlackJack(2)
        
    #just destroys the window and gets to initial window for choosing the ganmes. 
    def QUIT(self):    
        self.window.destroy()
        c=Choose_Game()
        c.window.mainloop()
#the war class.         
class War():
    def __init__(self,np):
        self.numplayers=np
        self.officialdeck=Deck(True,{"Spades":[1,1,1,1,1,1,1,1,1,1,1,1,1], "Hearts":[1,1,1,1,1,1,1,1,1,1,1,1,1], "Clubs":[1,1,1,1,1,1,1,1,1,1,1,1,1], "Diamonds":[1,1,1,1,1,1,1,1,1,1,1,1,1]}) #Expresses how many of each suit there is)
    
        self.players=[Deck(False),Deck(False)]
        self.playerTurn=0
        

        #window where the games will be played will be played
        # create window and give title
        self.win = tk.Tk() 
        self.win.title("Welcome To Game Of WAR!")

        # create a canvas on our window
        canvas_width = 1000
        canvas_height = 400
        self.my_canvas = tk.Canvas(self.win, width=canvas_width, height=canvas_height, bg="green")
        self.my_canvas.pack()
        #Uploading the image files.
        self.Clubs_2= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-2.png")
        self.Clubs_3= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-3.png")
        self.Clubs_4= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-4.png")
        self.Clubs_5= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-5.png")
        self.Clubs_6= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-6.png")
        self.Clubs_7= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-7.png")
        self.Clubs_8= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-8.png")
        self.Clubs_9= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-9.png")
        self.Clubs_10= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-10.png")
        self.Clubs_Jack= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-Jack.png")
        self.Clubs_Queen= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-Queen.png")
        self.Clubs_King= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-King.png")
        self.Clubs_Ace= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Clubs-Ace.png")
        self.Spades_2= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_2_ccexpress.png")
        self.Spades_3= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_3_ccexpress.png")
        self.Spades_4= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_4_ccexpress.png")
        self.Spades_5= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_5_ccexpress.png")
        self.Spades_6= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_6_ccexpress.png")
        self.Spades_7= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_7_ccexpress.png")
        self.Spades_8= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_8_ccexpress.png")
        self.Spades_9= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_9_ccexpress.png")
        self.Spades_10= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_10_ccexpress.png")
        self.Spades_Jack= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_Jack_ccexpress.png")
        self.Spades_Queen= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_Queen_ccexpress.png")
        self.Spades_King= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_King_ccexpress.png")
        self.Spades_Ace= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Spades_Ace_ccexpress.png")
        self.Hearts_2= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_2_ccexpress.png")
        self.Hearts_3= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_3_ccexpress.png")
        self.Hearts_4= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_4_ccexpress.png")
        self.Hearts_5= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_5_ccexpress.png")
        self.Hearts_6= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_6_ccexpress.png")
        self.Hearts_7= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_7_ccexpress.png")
        self.Hearts_8= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_8_ccexpress.png")
        self.Hearts_9= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_9_ccexpress.png")
        self.Hearts_10= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_10_ccexpress.png")
        self.Hearts_Jack= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_Jack_ccexpress.png")
        self.Hearts_Queen= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_Queen_ccexpress.png")
        self.Hearts_King= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_King_ccexpress.png")
        self.Hearts_Ace= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Hearts_Ace_ccexpress.png")
        self.Diamonds_2= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_2_ccexpress.png")
        self.Diamonds_3= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_3_ccexpress.png")
        self.Diamonds_4= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_4_ccexpress.png")
        self.Diamonds_5= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_5_ccexpress.png")
        self.Diamonds_6= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_6_ccexpress.png")
        self.Diamonds_7= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_7_ccexpress.png")
        self.Diamonds_8= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_8_ccexpress.png")
        self.Diamonds_9= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_9_ccexpress.png")
        self.Diamonds_10= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_10_ccexpress.png")
        self.Diamonds_Jack= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_Jack_ccexpress.png")
        self.Diamonds_Queen= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_Queen_ccexpress.png")
        self.Diamonds_King= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_King_ccexpress.png")
        self.Diamonds_Ace= PhotoImage(file = "C:\\Users\\iamin\\OneDrive\\Documents\\Academic\\Python\\Resized deck of cards\\deck png\\Diamonds_Ace_ccexpress.png")
        


        #dealer's cards are placed here
        self.DealerPlayed=tk.Message(self.win, text="Dealer's Card: ")
        self.DealerPlayed.pack(side = 'right')
        
        self.PlayerHand = tk.Message(self.win, text="Your Card: ")   
        self.PlayerHand.pack(side = 'left')
        #players cards are here
        self.Playerplayed = tk.Message(self.win, text="")
        self.Playerplayed.pack(side = 'left')
        #starts the game
        self.play = tk.Button(self.win, text="Start", command=self.PLAY)
        self.play.pack(side = 'top')
        #Player's turn
        self.player_draw = tk.Button(self.win, text="Player Draw",command=self.playerDraw)
        self.player_draw.pack(side ='left')
        #the player cannot draw without first starting a game
        self.player_draw["state"] = "disabled"  
        #Dealer's Turn
        self.dealer_draw = tk.Button(self.win, text="Dealer Draw",command=self.dealerDraw)
        self.dealer_draw.pack(side ='right')
        #the player gets to draw before the dealer. 
        self.dealer_draw["state"] = "disabled"  
        #destroys the existing window and creates a new one which starts a new game of war. 
        playAgain = tk.Button(self.win, text="Play Again",command=self.playAgain)
        playAgain.pack(side ='top')
        #the button to go for war will appear only if it's a tie. 
        self.something = tk.Button(self.win, text = "Go To War", command=self.goToWar)
        self.something.pack(side ='top')
        self.something["state"] = "disabled"
        #Button to surrender if it's a tie.
        self.surrender = tk.Button(self.win, text = "Surrender", command = self.Surrender)
        self.surrender.pack(side ='top')
        self.surrender["state"] = "disabled"
        #Button to quit the game
        Quit_Button = tk.Button(self.win, text="Quit",command=self.QUIT)#destroys the window
        Quit_Button.pack(side ='top')


    #The dealer and the player takes turns.     
    def takeTurn(self):
        drawn = self.officialdeck.drawCards(0)
        self.players[self.playerTurn].addCards(drawn)
        self.Playerplayed['text'] = (self.players[0])
        self.DealerPlayed["text"] = "Dealer's Card: " + str(self.players[1])
        self.playerTurn=(self.playerTurn+1)%self.numplayers
        

    #Creating the frame that will contain the Buttons    
    def create_frames(self):
        card_frame=tk.Frame(self.window,width=300,height=300)
        card_frame.grid(row=1,column=1)
        button_frame = tk.Frame(self.window, width=100, height=100)   
        button_frame.grid(row=2, column=1)
        return card_frame,button_frame

    #starts the game. 
    def PLAY(self):
      self.officialdeck.shuffle()
      for i in range(4):
          self.takeTurn()

      self.play["state"]="disabled"
      self.player_draw["state"]="normal"
      self.dealer_draw["state"]="disabled"

    #dealer draws a crad.    
    def dealerDraw(self):
        self.dealer_draw["state"]="normal"
        self.players[1].addCards(self.officialdeck.drawCards(1))
        self.DealerPlayed["text"] ="Dealer's Card: " + str(self.players[1])
        self.dealer_draw["state"]="disabled"
        CardNamePlayer = str(self.players[0])
        CardNameDealer = str(self.players[1])
        self.Card_of_Dealer()
        self.playerPoints()
        self.findingWinner()
        
        #determining player's and dealer's points.
    def playerPoints(self):
        CardNamePlayer = str(self.players[0])
        CardNameDealer = str(self.players[1])
        self.Plp = 0
        self.Dlp = 0
        if CardNamePlayer[0]=="2":
            self.Plp = int(CardNamePlayer[0])
        if CardNamePlayer[0]=="3":
            self.Plp = int(CardNamePlayer[0])
        if CardNamePlayer[0]=="4":
            self.Plp = int(CardNamePlayer[0])
        if CardNamePlayer[0]=="5":
            self.Plp = int(CardNamePlayer[0])
        if CardNamePlayer[0]=="6":
            self.Plp = int(CardNamePlayer[0])
        if CardNamePlayer[0]=="7":
            self.Plp = int(CardNamePlayer[0])
        if CardNamePlayer[0]=="8":
            self.Plp = int(CardNamePlayer[0])
        if CardNamePlayer[0]=="9":
            self.Plp = int(CardNamePlayer[0])
        if CardNamePlayer[0:2]=="10":
            self.Plp = int(CardNamePlayer[0:2])
        if CardNamePlayer[0:4]=="Jack":
            self.Plp = 11
        if CardNamePlayer[0:5]=="Queen":
            self.Plp = 12
        if CardNamePlayer[0:4]=="King":
            self.Plp = 13
        if CardNamePlayer[0:3]=="Ace":
            self.Plp = 14
        if CardNameDealer[0]=="2":
            self.Dlp = int(CardNameDealer[0])
        if CardNameDealer[0]=="3":
            self.Dlp = int(CardNameDealer[0])
        if CardNameDealer[0]=="4":
            self.Dlp = int(CardNameDealer[0])
        if CardNameDealer[0]=="5":
            self.Dlp = int(CardNameDealer[0])
        if CardNameDealer[0]=="6":
            self.Dlp = int(CardNameDealer[0])
        if CardNameDealer[0]=="7":
            self.Dlp = int(CardNameDealer[0])
        if CardNameDealer[0]=="8":
            self.Dlp = int(CardNameDealer[0])
        if CardNameDealer[0]=="9":
            self.Dlp = int(CardNameDealer[0])
        if CardNameDealer[0:2]=="10":
            self.Dlp = int(CardNameDealer[0:2])
        if CardNameDealer[0:4]=="Jack":
            self.Dlp = 11
        if CardNameDealer[0:5]=="Queen":
            self.Dlp = 12
        if CardNameDealer[0:4]=="King":
            self.Dlp = 13
        if CardNameDealer[0:3]=="Ace":
            self.Dlp = 14
    def Card_of_Player(self):
        #covering the existing image
        imageCover = self.my_canvas.create_rectangle(40, 40, 120, 140, fill="light blue", outline="black")
        #assigning image to cards
        a1 = str(self.players[0])
        if a1 =="2 of Clubs":
            card_image = self.Clubs_2
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "3 of Clubs":
            card_image = self.Clubs_3
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "4 of Clubs":
            card_image = self.Clubs_4
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "5 of Clubs":
            card_image = self.Clubs_5
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "6 of Clubs":
            card_image = self.Clubs_6
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "7 of Clubs":
            card_image = self.Clubs_7
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "8 of Clubs":
            card_image = self.Clubs_8
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "9 of Clubs":
            card_image = self.Clubs_9
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "10 of Clubs":
            card_image = self.Clubs_10
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Jack of Clubs":
            card_image = self.Clubs_Jack
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Queen of Clubs":
            card_image = self.Clubs_Queen
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "King of Clubs":
            card_image = self.Clubs_King
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Ace of Clubs":
            card_image = self.Clubs_Ace
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 =="2 of Hearts":
            card_image = self.Hearts_2
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "3 of Hearts":
            card_image = self.Hearts_3
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "4 of Hearts":
            card_image = self.Hearts_4
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "5 of Hearts":
            card_image = self.Hearts_5
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "6 of Hearts":
            card_image = self.Hearts_6
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "7 of Hearts":
            card_image = self.Hearts_7
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "8 of Hearts":
            card_image = self.Hearts_8
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "9 of Hearts":
            card_image = self.Hearts_9
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "10 of Hearts":
            card_image = self.Hearts_10
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Jack of Hearts":
            card_image = self.Hearts_Jack
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Queen of Hearts":
            card_image = self.Hearts_Queen
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "King of Hearts":
            card_image = self.Hearts_King
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Ace of Hearts":
            card_image = self.Hearts_Ace
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 =="2 of Diamonds":
            card_image = self.Diamonds_2
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "3 of Diamonds":
            card_image = self.Diamonds_3
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "4 of Diamonds":
            card_image = self.Diamonds_4
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "5 of Diamonds":
            card_image = self.Diamonds_5
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "6 of Diamonds":
            card_image = self.Diamonds_6
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "7 of Diamonds":
            card_image = self.Diamonds_7
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "8 of Diamonds":
            card_image = self.Diamonds_8
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "9 of Diamonds":
            card_image = self.Diamonds_9
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "10 of Diamonds":
            card_image = self.Diamonds_10
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Jack of Diamonds":
            card_image = self.Diamonds_Jack
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Queen of Diamonds":
            card_image = self.Diamonds_Queen
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "King of Diamonds":
            card_image = self.Diamonds_King
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Ace of Diamonds":
            card_image = self.Diamonds_Ace
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        if a1 =="2 of Spades":
            card_image = self.Spades_2
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "3 of Spades":
            card_image = self.Spades_3
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "4 of Spades":
            card_image = self.Spades_4
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "5 of Spades":
            card_image = self.Spades_5
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "6 of Spades":
            card_image = self.Spades_6
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "7 of Spades":
            card_image = self.Spades_7
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "8 of Spades":
            card_image = self.Spades_8
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "9 of Spades":
            card_image = self.Spades_9
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "10 of Spades":
            card_image = self.Spades_10
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Jack of Spades":
            card_image = self.Spades_Jack
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Queen of Spades":
            card_image = self.Spades_Queen
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "King of Spades":
            card_image = self.Spades_King
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)
        elif a1 == "Ace of Spades":
            card_image = self.Spades_Ace
            self.my_canvas.create_image(50, 50, anchor = NW, image = card_image)

    def Card_of_Dealer(self):
        #covering the existing image
        imageCover = self.my_canvas.create_rectangle(870, 40, 950, 140, fill="light blue", outline="black")
        #assigning image to cards
        a1 = str(self.players[1])
        if a1 =="2 of Clubs":
            card_image = self.Clubs_2
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "3 of Clubs":
            card_image = self.Clubs_3
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "4 of Clubs":
            card_image = self.Clubs_4
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "5 of Clubs":
            card_image = self.Clubs_5
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "6 of Clubs":
            card_image = self.Clubs_6
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "7 of Clubs":
            card_image = self.Clubs_7
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "8 of Clubs":
            card_image = self.Clubs_8
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "9 of Clubs":
            card_image = self.Clubs_9
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "10 of Clubs":
            card_image = self.Clubs_10
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Jack of Clubs":
            card_image = self.Clubs_Jack
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Queen of Clubs":
            card_image = self.Clubs_Queen
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "King of Clubs":
            card_image = self.Clubs_King
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Ace of Clubs":
            card_image = self.Clubs_Ace
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 =="2 of Hearts":
            card_image = self.Hearts_2
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "3 of Hearts":
            card_image = self.Hearts_3
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "4 of Hearts":
            card_image = self.Hearts_4
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "5 of Hearts":
            card_image = self.Hearts_5
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "6 of Hearts":
            card_image = self.Hearts_6
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "7 of Hearts":
            card_image = self.Hearts_7
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "8 of Hearts":
            card_image = self.Hearts_8
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "9 of Hearts":
            card_image = self.Hearts_9
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "10 of Hearts":
            card_image = self.Hearts_10
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Jack of Hearts":
            card_image = self.Hearts_Jack
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Queen of Hearts":
            card_image = self.Hearts_Queen
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "King of Hearts":
            card_image = self.Hearts_King
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Ace of Hearts":
            card_image = self.Hearts_Ace
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 =="2 of Diamonds":
            card_image = self.Diamonds_2
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "3 of Diamonds":
            card_image = self.Diamonds_3
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "4 of Diamonds":
            card_image = self.Diamonds_4
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "5 of Diamonds":
            card_image = self.Diamonds_5
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "6 of Diamonds":
            card_image = self.Diamonds_6
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "7 of Diamonds":
            card_image = self.Diamonds_7
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "8 of Diamonds":
            card_image = self.Diamonds_8
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "9 of Diamonds":
            card_image = self.Diamonds_9
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "10 of Diamonds":
            card_image = self.Diamonds_10
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Jack of Diamonds":
            card_image = self.Diamonds_Jack
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Queen of Diamonds":
            card_image = self.Diamonds_Queen
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "King of Diamonds":
            card_image = self.Diamonds_King
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Ace of Diamonds":
            card_image = self.Diamonds_Ace
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        if a1 =="2 of Spades":
            card_image = self.Spades_2
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "3 of Spades":
            card_image = self.Spades_3
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "4 of Spades":
            card_image = self.Spades_4
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "5 of Spades":
            card_image = self.Spades_5
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "6 of Spades":
            card_image = self.Spades_6
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "7 of Spades":
            card_image = self.Spades_7
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "8 of Spades":
            card_image = self.Spades_8
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "9 of Spades":
            card_image = self.Spades_9
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "10 of Spades":
            card_image = self.Spades_10
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Jack of Spades":
            card_image = self.Spades_Jack
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Queen of Spades":
            card_image = self.Spades_Queen
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "King of Spades":
            card_image = self.Spades_King
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        elif a1 == "Ace of Spades":
            card_image = self.Spades_Ace
            self.my_canvas.create_image(880, 50, anchor = NW, image = card_image)
        
        
    #determining the winner if not tied.
    def findingWinner(self):
        v = "You won the bet!"
        d = "You lost the bet!"
        t = "It's a tie. Wanna go to WAR!"
        if self.Plp > self.Dlp:
            print(v)
            messagebox.showinfo("Victory!", v)
        if self.Plp<self.Dlp:
            print(d)
            messagebox.showinfo("Defeat!", d)
        if self.Plp==self.Dlp:
            self.something["state"]="normal"
            self.surrender["state"] = "normal"
    #player draws a card.     
    def playerDraw(self):
        self.player_draw["state"]="normal"
        for i in range(1):
            self.players[0].addCards(self.officialdeck.drawCards(1))
            self.Playerplayed['text'] = (self.players[0])
        self.Card_of_Player()
        self.player_draw["state"]="disabled"
        self.dealer_draw["state"]="normal"
        
    #Goes to war and doubles the stakes.     
    def goToWar(self):
        self.something["state"] = "normal"
        self.players[0].addCards(self.officialdeck.drawCards(1))
        self.Playerplayed['text'] = (self.players[0])
        self.players[1].addCards(self.officialdeck.drawCards(1))
        self.DealerPlayed["text"] ="Dealer's Card: " + str(self.players[1])
        CardNamePlayer = str(self.players[0])
        CardNameDealer = str(self.players[1])
        self.playerPoints()
        self.Card_of_Player()
        self.Card_of_Dealer()
        v = "You won the bet!"
        d = "You lost the bet!"
        t = "It's a tie. Wanna go to WAR!"
        if self.Plp > self.Dlp:
            print(v)
            messagebox.showinfo("Victory!", v)
        if self.Plp<self.Dlp:
            print(d)
            messagebox.showinfo("Defeat!", d)
        if self.Plp==self.Dlp:
            print(v)
            messagebox.showinfo("Victory!", v)
        self.surrender["state"] = "disabled"
        self.something["state"] = "disabled"
    def Surrender(self):
        print("defeat")
        self.something["state"]="disabled"
        self.surrender["state"] = "disabled"
        
    #destroys the current window and creates a new game of war on a new window     
    def playAgain(self):    
        self.win.destroy() 
       
        War(2)
        
    #destroys the window
    def QUIT(self): 
        self.win.destroy()
        c=Choose_Game()
        c.window.mainloop()

#class to create the initial window to choose between war and blackjack
class Choose_Game():
  def __init__(self):
    self.window=tk.Tk()
    self.window.title("Choose a Game")
    self.window.geometry("300x100")
    BlackJack_Button = tk.Button(self.window, text="BlackJack",command=self.BlackJack)
    BlackJack_Button.pack(side = "left")
    War_Button=tk.Button(self.window, text="WAR",command=self.War)
    War_Button.pack(side="right")
    Quit_Button = tk.Button(self.window, text="Quit",command=self.Quit)#destroys the window
    Quit_Button.pack(side="bottom")
    
  def BlackJack(self):
    self.window.destroy()
    v = BlackJack(2)
    v.window.mainloop()

  def War(self):
    self.window.destroy()
    w=War(2)
    w.win.mainloop()
  def Quit(self):
      self.window.destroy()





def main():
  c=Choose_Game()
  c.window.mainloop()

if __name__ == "__main__":
    main()
        

