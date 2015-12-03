import random

play = False

suits = ('H','S','C','D')

card_num = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

card_val = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

bet = 1

chips = 100

restart = "Press d to deal again or q to quit."


class Card:
	
	def __init__(self,suit,c_num):
		self.suit = suit
		self.c_num = c_num
		
	def __str__(self):
		return self.c_num + self.suit
		
	def get_suit(self):
		return self.suit
		
	def get_num(self):
		return self.c_num
	
	def draw(self):
		# Show the card drawn
		print (self.c_num + self.suit)

class Hand:

	def __init__(self):
		self.cards = []
		# Hand value
		self.h_val = 0
		
		# establish presence of ace since value can be 1 or 11
		self.ace = False
	
	def __str__(self):
		# Return current hand
		cur_hand = ""
		
		for card in self.cards:
			card_name = card.__str__()
			cur_hand += " " + card_name
		
		return "Your hand is %s" % cur_hand
	
	def add_card(self,card):
		self.cards.append(card)
		# Checks to see if the card is an Ace
		if card.c_num == "A":
			self.ace = True
		self.h_val += card_val[card.c_num]
			
	def calc_hand(self):
		# Determines the better hand with ace as 1 or 11
		if (self.ace == True and self.h_val < 12):
			return self.h_val + 10
		else:
			return self.h_val
	
	def draw_card(self,hidden):
		# Hide one card for the dealer
		if hidden == True and play == True:
			start_cards = 1
		else:
			start_cards = 0
		for x in range(start_cards,len(self.cards)):
			self.cards[x].draw()



class Deck:

	def __init__(self):
		# Create a deck
		self.deck = []
		for suit in suits:
			for num in card_num:
				self.deck.append(Card(suit,num))
	
	def shuffle(self):
		# Shuffle the deck
		random.shuffle(self.deck)
	
	def deal(self):
		# Deal the cards from the shuffled deck
		one_card = self.deck.pop()
		return one_card
		
	def __str__(self):
		deck_cards = ""
		for card in self.cards:
			deck_cards += " " + deck_cards.__str__
		return "The deck has " + deck_cards
			
def place_bet():
	
	global bet
	bet = 0
	
	print "How many chips would you like to bet?"
	
	while bet == 0:
		player_bet = int(raw_input())
		if player_bet > 0 and player_bet <= chips:
			bet = player_bet
		else:
			print "This is a bet you can't afford! You only have " + str(chips) + " chips!"
			
def deal():
    # Deal out the cards for the hand
    
    global result,play,deck,players_hand,dealers_hand,chips,bet
    
    # Create a deck and shuffle
    deck = Deck()
    deck.shuffle()
    
    place_bet()
    
    # Create and deal out hands 
    players_hand = Hand()
    dealers_hand = Hand()

    players_hand.add_card(deck.deal())
    players_hand.add_card(deck.deal())
    
    dealers_hand.add_card(deck.deal())
    dealers_hand.add_card(deck.deal())
    
    result = "Would you like to 'Hit' or 'Stand'? Press s or h."
    
    if play == True:
        print 'You fold.'
        chips -= bet
    
    play = True 
    game_step()

def hit():
    
    # Decide whether the player hits or stays
    global play,chips,deck,players_hand,dealers_hand,result,bet
    
    if play:
        if players_hand.calc_hand() <= 21:
            players_hand.add_card(deck.deal())
        
        print "The player's hand is %s" % players_hand
        
        if players_hand.calc_hand() > 21:
            result = 'You busted! ' + restart
            
            chips -= bet
            play = False
    
    else:
        result = "Sorry you can't hit." + restart
    
    game_step()


def stand():
    
    # Once the player stands, the dealer plays
    global play,chips,deck,players_hand,dealers_hand,result,bet
    
    if play == False:
        if players_hand.calc_hand() > 0:
            result = "Sorry, you can't stand!"
    else:
        
        # Dealer rule of 17
        while dealers_hand.calc_hand() < 17:
            dealers_hand.add_card(deck.deal())
            
        # When dealer busts  
        if dealers_hand.calc_hand() > 21:
            result = 'Dealer busts! You win!' + restart
            chips += bet
            play = False
            
        # When player beats dealer
        elif dealers_hand.calc_hand() < players_hand.calc_hand():
            result = 'You beat the dealer, you win!' + restart
            chips += bet
            play = False
        
        # Tie with player and dealer
        elif dealers_hand.calc_hand() == players_hand.calc_hand():
            result = 'Tied up, push!' + restart
            play = False
        
        # When dealer wins
        else:
            result = 'Dealer Wins!' + restart
            chips -= bet
            play = False
    game_step()
    
    
def game_step():
    
    # Show player's hand
    print ""
    print("The player's hand is: "),
    players_hand.draw_card(hidden = False)
    
    print "The player's hand value is: " + str(players_hand.calc_hand())
    
    # Show Dealer's hand
    print("The dealer's hand is: "),
    dealers_hand.draw_card(hidden=True)
    
    # When game is over
    if play == False:
        print " --- for a total of " + str(dealers_hand.calc_hand() )
        print "Chip Total: " + str(chips)
    else: 
        print " with another card hidden."
    
    # Print result of hit or stand.
    print result
    
    player_input()

def game_exit():
    print 'Thanks for playing!'
    exit()

def player_input():
    # Convert input to upper and check for match
    answ = raw_input().upper()
    
    if answ == 'H':
        hit()
    elif answ == 'S':
        stand()
    elif answ == 'D':
    	if chips > 0:
        	deal()
        else:
        	print "Sorry, you're out of chips!"
        	game_exit()
    elif answ == 'Q':
        game_exit()
    else:
        print "Please input h, s, d, or q: "
        player_input()
        
def intro():
    statement = """Let's play some Black Jack! The goal of the game is to get 21! 
    Aces are worth 1 or 11. Beat the dealer to win some chips!"""
    print statement
    


# Create deck and shuffle
deck = Deck()
deck.shuffle()
# Create player and dealer hands
players_hand = Hand()
dealers_hand = Hand()
# Intro to the game
intro()
# Deal out the cards and start
deal()




	
		