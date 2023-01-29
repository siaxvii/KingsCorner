######################################################################
# Import randint and shuffle from random module.
from random import randint, shuffle

######################################################################
# createDeck() produces a new, cannonically ordered, 52 card deck
# using a nested comprehension. Providing a value less than 13
# produces a smaller deck, like the semi-standard 40 card 4 suit 1-10
# deck used in many older card games (including tarot cards). Here,
# we'll use it with default values.
#
def createDeck(N=13, S=('spades', 'hearts', 'clubs', 'diamonds')):
    return([ (v, s) for s in S for v in range(1, N+1) ]) 

######################################################################
# Construct the representation of a given card using special unicode
# characters for hearts, diamonds, clubs, and spades. The input is a
# legal card, c, which is a (v, s) tuple. The output is a 2 or
# 3-character string 'vs' or 'vvs', where 's' here is the unicode
# character corresponding to the four standard suites (spades, hearts,
# diamonds or clubs -- provided), and v is a 1 or 2 digit string
# corresponding to the integers 2-10 and the special symbols 'A', 'K',
# 'Q', and 'J'.
#
# Example:
#    >>> displayCard((1, 'spades'))
#    'A♠'
#    >>> displayCard((12, 'hearts'))
#    'Q♡'
#
def displayCard(c):
    suits = {'spades':'\u2660', 'hearts':'\u2661', 'diamonds':'\u2662', 'clubs':'\u2663'}
    
    #Assigned ranks to a list of all the ranks of cards 
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    
    #assigning v,s where "v" is a rank and "s" is a suit to card representation c
    v,s = c
    
    #returns the rank minus 1 because of the way lists are indexed along with the unicode representation of a suit
    return ranks[v-1] + suits[s]

######################################################################
# Print out an indexed representation of the state of the table:
# foundation piles are numbered 0-3, corner piles 4-7.
# Example:
#   >>> showTable(F, C)
#     F0: 9♡...9♡
#     F1: 2♢...2♢
#     F2: 7♡...7♡
#     F3: 8♡...8♡
#     C4:
#     C5:
#     C6:
#     C7:
# Or, mid-game:
#     F0: 8♣...A♢
#     F1: J♣...J♣
#     F2: A♠...A♠
#     F3: 
#     C4: K♡...K♡
#     C5: 
#     C6: 
#     C7:
def showTable(F, C):
    #assigning corners and foundations to empty list
    corners = []
    foundation = []
    for i in C:   #iterating through each element inputted into C (lists that are nested in C that correspond to various corner piles)
        if i == []:           
            corners.append("")     #if the elements in C are an empty list, append "" to the list associated with corners       
        else:
            corners.append(displayCard(i[0]) + "..." + displayCard(i[-1]))    #else, appends the first card of the pile, puts dots, and then appends the last card of the pile
    for i in F:   #iterating through each element inputted into F (lists that are nested in F that correspond to various foundation piles)
        if i == []:
            foundation.append("")
        else:
            foundation.append(displayCard(i[0]) + "..." + displayCard(i[-1])) 
    #Giant print statement that is separated by the new line character that essentially sets up the table representation
    print("\n".join(["F" + str(i) + ": " + foundation[i] for i in range(4)] + ["C" + str(i+4) + ": " + corners[i] for i in range(4)]))
######################################################################
# Print out an indexed list of the cards in input list H, representing
# a hand. Entries are numbered starting at 8 (indexes 0-3 are reserved
# for foundation piles, and 4-7 are reserved for corners). The
# indexing is used to select cards for play.
#
# Example:
#   >>> showHand(H[0])
#   Hand: 8:A♢ 9:4♢ 10:3♡ 11:5♠ 12:6♠ 13:7♠ 14:8♠
#   >>> showHand(H[1])
#   Hand: 8:9♣ 9:5♢ 10:8♢ 11:9♢ 12:10♡ 13:A♠ 14:4♠
#
def showHand(H):
    
    #assigning x to a list of values that go from 8 to as many cards as there are in the hand
    x = [str(num)+ ":" for num in range(8, len(H)+len(H))]    
    
    #assigning y to list of values that displayCard(h) puts out in the form of a hand
    H.sort(reverse = True)   #sorts values from highest to lowest
    y = [str(displayCard(h))+ " " for h in H] 
    
    #alternating x and y so that it comes out in a format that has the index number (with a colon) and then the card in the hand
    result = [None]*(len(x)+len(y))     
    result[::2] = x
    result[1::2] = y
    sorted(y)
    #prints out the elements of the now conjoined, alternating list 
    print(''.join(result))
    
    
    
######################################################################
# We'll use deal(N, D) to set up the game. Given a deck (presumably
# produced by createDeck()), shuffle it, then deal 7 cards to each of
# N players, and seed the foundation piles with 4 additional cards.
# Returns D, H, F, where D is what remains of the deck, H is a list of
# N 7-card "hands", and F is a list of lists corresponding to the four
# "seeded" foundation piles.
# 
# N --> hands based on number of people playing
# H --> List of all the hands (list of 2 hands by default)
# F --> List of lists corresponding to cards in Foundation piles
# D --> Representing remaining cards in the deck 

# Example:
#   >>> D, H, F = deal(2, D)
#   >>> len(D)
#   34
#   >>> len(H)
#   2
#   >>> H[0][:3]
#   [(5, 'clubs'), (12, 'clubs'), (3, 'diamonds')]
#   >>> F[2]
#   [(11, 'hearts')]
#
def deal(N, D):
    # Shuffle the deck, then return what's left of it after dealing 7
    # Cards to each player and seeding the foundation piles.
    shuffle(D)       #Shuffles the deck
    FoundPile = []   #Cards in foundation piles
    Hands = []   #List that contains all the hands(that are lists themselves)
    for n in range(N): #Going through each person playing giving them an empty hand
        x = []
        Hands.append(x) 
    for person in range(N): #Going through each player
        for i in range(7):
            Hands[person].append(D.pop(i))   #Popping out a card 7 times into each list that is inside Hands
    for i in range(4):
        FoundPile.append([D.pop(i)])         #Dealing a card to each of the four foundation piles 
    return D, Hands, FoundPile
######################################################################
# Returns True if card c can be appended to stack S. To be legal, c
# must be one less in value than S[-1], and should be of the "other"
# color (red vs black).
# Example:
#   >>> legal([(2, 'diamonds')], (1, 'spades'))
#   True
#   >>> legal([(2, 'diamonds')], (1, 'hearts'))
#   False
#
def legal(S, c):
    if S == []:
        return False 
    def altcolor(c1,c2):
        red = ['diamonds', 'hearts'] 
        black = ['clubs', 'spades']
        if c1 in red:                     #if the card is red
            if c2 in black:
                return True                  #returns "red" if the color of the last card in the stack is red
        elif c1 in black:
            if c2 in red:
                return True
        else: 
            return False                  #otherwise, returns black
    if S[-1][0] == c[0]+1:           #if the rank of the last card in the stack is one more than the inputted card
        if altcolor(S[-1][1],c[1]) is True:
            return True
        else:
            return False
    else:
        return False                
######################################################################
# Governs game play for N players (2 by default). This function sets
# up the game variables, D, H, F and C, then chooses the first player
# randomly from the N players. By convention, player 0 is the user,
# while all other player numbers are played by the auto player.   
#
# Each turn, the current player draws a card from the deck D, if any
# remain, and then is free to make as many moves as he/she chooses. 
def play(N=2):
    # Set up the game.
    D, H, F = deal(N, createDeck())
    
    C = [ [] for i in range(4) ]   # Corners, initially empty.

    # Randomly choose a player to start the game.
    player = randint(0,N-1)
    print('Player {} moves first.'.format(player))

    # Start the play loop; we'll need to exit explicitly when
    # termination conditions are realized.
    while True:
        # Draw a card if there are any left in the deck.
        if len(D) > 0:
            H[player].append(D[0])
            D.remove(D[0])
        print('\n\nPlayer {} ({} cards) to move.'.format(player, len(H[player])))
        print('Deck has {} cards left.'.format(len(D)))
        # Now show the table.
        showTable(F, C)

        # Let the current player have a go.
        if player != 0:
            automove(F, C, H[player])
        else:
            usermove(F, C, H[player])

        # Check to see if player is out; if so, end the game.
        if H[player] == []:
            print('\n\nPlayer {} wins!'.format(player))
            showTable(F, C)
            break
        # Otherwise, go on to next player.
        else:
            if player < N-1:
                player = player + 1
            else:
                player = 0

######################################################################
# Prompts a user to play their hand.

def usermove(F, C, hand):
    # valid() is an internal helper function that checks if the index
    # i indicates a valid F, C or hand index.  To be valid, it cannot
    # be an empty pile or an out-of-range hand index. Remember, 0-3
    # are foundation piles, 4-7 are corner piles, and 8 and up index
    # into the hand.
    def valid(i): 
        if i == "." or i == "/":
            return True        
        elif i in range(4):      #foundation pile valid index check
            return True
        elif i in range(4,8):  #corner pile valid index check
            return True
        elif i >= 8:           #hand index valid check
            if len(hand)+7 > i:
                return True
            else:
                return False
        else:
            return False
    # Ensure the hand is sorted, integrating newly drawn card.
    sorted(hand) 

    # Give some instruction.
    print('Enter your move as "src dst": press "/" to refresh display; "." when done')

    # Manage any number of moves.
    while True:           # Until the user quits with a .
        # Display current hand.
        showHand(hand)
        # Read inputs and construct a tuple.
        move = []
        while not move or not valid(move[0]) or not valid(move[1]):
            move = input("Your move? ").split()
            if len(move) == 1:
                if move[0] == '.':
                    print("Finished move, next player's turn!")
                    move = []
                    return False
                elif move[0] == '/':
                    showTable(F,C)
                    showHand(hand)
                    move = []
                    continue
            try:
                move = [int(move[0]), int(move[1])]
                # Execute the command, which looks like [from, to].
                # Remember, 0-3 are foundations, 4-7 are corners, 8+
                # are from your hand.
                #
                # What follows here is an if/elif/else statement for
                # each of the following cases.
                # Playing a card from your hand to a foundation pile.
                if move[0] >= 8 and move[1] in range(5) and legal(F[move[1]], hand[move[0]-8]):   
                    print("Moving {} to F{}".format(displayCard(hand[move[0]]),move[1]))
                    F[move[1]].append(hand[move[0]-8])
                    hand.pop(move[0]-8)  
                # Moving a foundation pile to a foundation pile.
                elif move[0] <= 3 and move[1] <= 3 and legal(F[move[1]],F[move[0]][0]):  
                    print("Moving F{} to F{}".format(move[0], move[1]))
                    F[move[1]].append(F[move[0]])
                    F[move[0]] = []  
                    
                # Playing a card from your hand to a corner pile (K only to empty pile).
                elif hand[move[0]-8][0] == "13" and move[1] == C[move[1]-4] and C[move[1]-4] == []:
                    print("Moving {} to C{}".format(displayCard(hand[move[0]]),move[1]))
                    C[move[1]-4].append(hand[move[0]-8])
                    hand.pop(hand[move[0]-8]) 
                    
                # Moving a foundation pile to a corner pile.
                elif move[0] <= 3 and move[1] in range(5) and legal(C[move[1]-4], F[move[0]][0]):   
                    print("Moving {} to {}".format(F[move[0]],C[move[1]])) 
                    C[move[1]-4].append(F[move[0]])
                    F[move[0]] = []
                    
                # Otherwise, print "Illegal move" warning. 
                else:
                    print("Illegal move, try again!") 
            except:
                    # Any failure to process ends up here.
                print('Ill-formed move {}'.format(move))

            # If the hand is empty, return. Otherwise, reset move and
            # keep trying.
            if not hand:
                return
            move = []
            pass

######################################################################
# Plays a hand automatically using a fixed but not particularly
# brilliant strategy. The strategy involves consolidating the table
# (to collapse foundation and corner piles), then scanning cards in
# your hand from highest to lowest, trying to place each card. The
# process is repeated until no card can be placed. 
def automove(F, C, hand):
    # Keep playing cards while you're able to move something.
    moved = True
    while moved:
        moved = False	# Change back to True if you move a card.

        # Start by consolidating the table.        
        consolidate(F, C)
        # Sort the hand (destructively) so that you consider highest
        # value cards first.
        hand.sort()
        # Scan cards in hand from high to low value, which makes removing
        # elements easier.
        for i in range(len(hand)-1, -1, -1):
            # If current card is a king, place in an empty corner
            # location (guaranteed to be one).
                        
            # Otherwise, try to place current card on an existing
            # corner or foundation pile.
            for j in range(4):           #iterates through the 4 lists that F and C contain 
                # Here, you have an if/elif/else that checks each of
                # the stated conditions.
                # Place current card on corner pile.
                if hand[i][0] == "13":
                    if C[j] == []: 
                        print("Moving {} to an open corner".format(displayCard(hand[i])))
                        x.append(hand[i])
                        hand.remove(hand[i])
                        
                if legal(C[j], hand[i]) is True:             #If the current card is appendable to any existing corner pile:
                    print("Moving {} to {}".format(displayCard(hand[i]), C[j]))      #Prints out what it is doing
                    C[j].append(hand[i])                     #Adds it to the legal corner pile 
                    hand.remove(hand[i])                     #Removes the existing card from the hand
                    
                # Place current card on foundation pile.
                if legal(F[j], hand[i]) is True:             #If the current card is appendable to any existing foundation:
                    print("Moving {} to F{}".format(displayCard(hand[i]), j))      #Prints out what it is doing
                    F[j].append(hand[i])                       #Adds it to the legal foundation pile
                    hand.remove(hand[i])                       #Removes the existing card from the hand
                    
                # Start a new foundation pile.              
                if F[j] == []:
                    print("Moving {} to an open foundation".format(displayCard(hand[i])))
                    F[j].append(hand[i])
                    hand.remove(hand[i])
                    break
######################################################################
# consolidate(F, C) looks for opportunities to consolidate by moving a
# foundation pile to a corner pile or onto another foundation pile. It
# is used by the auto player to consolidate elements on the table to
# make it more playable.
#
# Example:
#   >>> showTable(F, C)
#     F0: 6♢...6♢
#     F1: 10♣...10♣
#     F2: J♡...J♡
#     F3: Q♠...Q♠
#     C4: K♢...K♢
#     C5:
#     C6:
#     C7:
#   >>> consolidate(F, C)
#   >>> showTable(F, C)
#     F0: 6♢...6♢
#     F1:
#     F2: 
#     F3: 
#     C4: K♢...10♣
#     C5:
#     C6:
#     C7:

def consolidate(F, C):
    # Consider moving one foundation onto another. 
    if F[0] != []:
        if legal(F[0], F[1][0]) is True:
            F[0].extend(F[1]) 
            F[1] = [] 
            print("Moving F1 to F0")
        if legal(F[0], F[2][0]) is True:
            F[0].extend(F[2])
            F[2] = []
            print("Moving F2 to F0")
        if legal(F[0], F[3][0]) is True:
            F[0].extend(F[3])
            F[3] = []
            print("Moving F3 to F0")        
    if F[1] != []:
        if legal(F[1], F[0][0]) is True:
            F[1].extend(F[0])
            F[0] = []
            print("Moving F0 to F1")
        if legal(F[1], F[2][0]) is True:
            F[1].extend(F[2])
            F[2] = []
            print("Moving F2 to F1")
        if legal(F[1], F[3][0]) is True:
            F[1].extend(F[3])
            F[3] = []
            print("Moving F3 to F1")        
    if F[2] != []:
        if legal(F[2], F[0][0]) is True:
            F[2].extend(F[0])
            F[0] = []
            print("Moving F0 to F2")
        if legal(F[2], F[1][0]) is True:
            F[2].extend(F[1])
            F[1] = []
            print("Moving F1 to F2")
        if legal(F[2], F[3][0]) is True:
            F[2].extend(F[3])
            F[3] = []
            print("Moving F3 to F2")        
    if F[3] != []:
        if legal(F[3], F[0][0]) is True:
            F[3].extend(F[0])
            F[0] = []
            print("Moving F0 to F3")
        if legal(F[3], F[1][0]) is True:
            F[3].extend(F[1])
            F[1] = []
            print("Moving F1 to F3")
        if legal(F[3], F[2][0]) is True:
            F[3].extend(F[2])
            F[2] = []
            print("Moving F2 to F3")        
    # Consider moving a foundation onto a corner.
    if C[0] != []:
        if legal(C[0], F[0][0]) is True:
            C[0].extend(F[0])
            F[0] = []
            print("Moving F0 to C4")
        if legal(C[0], F[1][0]) is True:
            C[0].extend(F[1])
            F[1] = []
            print("Moving F1 to C4")
        if legal(C[0], F[2][0]) is True:
            C[0].extend(F[2])
            F[2] = []
            print("Moving F2 to C4")
        if legal(C[0], F[3][0]) is True:
            C[0].extend(F[3])
            F[3] = []
            print("Moving F3 to C4")
    if C[1] != []:
        if legal(C[1], F[0][0]) is True:
            C[1].extend(F[0])
            F[0] = []
            print("Moving F0 to C5")
        if legal(C[1], F[1][0]) is True:
            C[1].extend(F[1])
            F[1] = []
            print("Moving F1 to C5")
        if legal(C[1], F[2][0]) is True:
            C[1].extend(F[2])
            F[2] = []
            print("Moving F2 to C5")
        if legal(C[1], F[3][0]) is True:
            C[1].extend(F[3])
            F[3] = []
            print("Moving F3 to C5")
    if C[2] != []:
        if legal(C[2], F[0][0]) is True:
            C[2].extend(F[0])
            F[0] = []
            print("Moving F0 to C6")
        if legal(C[2], F[1][0]) is True:
            C[2].extend(F[1])
            F[1] = []
            print("Moving F1 to C6")
        if legal(C[2], F[2][0]) is True:
            C[2].extend(F[2])
            F[2] = []
            print("Moving F2 to C6")
        if legal(C[2], F[3][0]) is True:
            C[2].extend(F[3])
            F[3] = []  
            print("Moving F3 to C6")
    if C[3] != []:
        if legal(C[3], F[0][0]) is True:
            C[3].extend(F[0])
            F[0] = []
            print("Moving F0 to C7")
        if legal(C[3], F[1][0]) is True:
            C[3].extend(F[1])
            F[1] = []
            print("Moving F1 to C7")
        if legal(C[3], F[2][0]) is True:
            C[3].extend(F[2])
            F[2] = []
            print("Moving F2 to C7")
        if legal(C[3], F[3][0]) is True:
            C[3].extend(F[3])
            F[3] = []
            print("Moving F3 to C7")

######################################################################
if __name__ == '__main__':
    # Play two-player version by default.
    play(2)