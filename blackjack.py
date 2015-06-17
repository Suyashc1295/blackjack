import random
#from deckofcards import values
#from deckofcards import deck
#from deckofcards import rules

deck = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
values = {'2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9,
          'T': 10,
          'J': 10,
          'Q': 10,
          'K': 10
         }

rules = """---------
    Black jack is a card game played between the player and the dealer.

    At the start, both you and the dealer are dealt two cards. The dealer shows
you his first.

    Your cards, or hand, have a score. You get your score by
adding up the values of each card in your hand. Every number card's value is
its number, and any face card is worth 10. Ace is worth 1 or 11, whichever is
most beneficial for the player. The winner of the game is whoever's score is
closest to 21. Ties go to the dealer.

    With your two cards, you have the option to hit or stay. Hit means draw one
more card. Stay means you're happy with your score.
---------"""
def draw_two():
    """Creates a list with two random values drawn from the "deck". This serves
    as an inital hand."""
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    hand = []
    hand.append(card1)
    hand.append(card2)
    return hand

def draw_one(hand):
    """Randomly adds one value to the given list. Equivilent to "Hit Me\""""
    card = random.choice(deck)
    hand.append(card)
    return hand

def counth(hand):
    """Evaluates the "score" of a given hand. """
    count = 0
    for i in hand:
        if i in values:
            count += values[i]
        else:
            pass
    for x in hand:
        if x == 'A':
        ## makes exception for aces
            if count + 11 > 21:
                count += 1
            elif hand.count('A') == 1:
                count += 11
            else:
                count += 1
        else:
            pass
    return count

def dealer():
    """Simulates a random dealer hand.
    The dealer starts with two cards --dh(0) and dh(1)--,
    then hits if his score is below a mandatory score X.
    If there is an ace among his first two cards, he must hit.
    Returns the hand. (which is a list)"""

    dh = draw_two()
    count = counth(dh)

    # forces hit if ace in first two cards
    if 'A' in dh:
        dh = draw_one(dh)
        count = counth(dh)

    ## defines maximum hit score X
    while count < 16:
        draw_one(dh)
        count = counth(dh)
    return dh

def player(dh):
    ph = draw_two()
    count = counth(ph)
    print "Your cards: %s" % " ".join(ph)
    print "Your score: %d" % count
    print "The dealer shows: %s" % dh[0]
    print "hit or stay?"
    a = True
    while a:
        choice = raw_input("> ")
        if choice == "hit":
            ph = draw_one(ph)
            count = counth(ph)
            print "Your cards: %s" % " ".join(ph)
            print "Your score: %d" % count
            print "The dealer shows: %s" % dh[0]
            if count >= 21:
                a = False
            else:
                print "hit or stay?"
        elif choice == "stay":
            a = False
        else:
            print "You must select hit or stay."
    return ph



def game():
    dh = dealer()
    ph = player(dh)
    dc = counth(dh)
    pc = counth(ph)
    if dc > 21 and pc <= 21:
        print "----------------------"
        print " The dealer's hand: %s" % " ".join(dh)
        print "The dealer's score: %d" % dc
        print "        Your score: %d" %pc
        print " The dealer went bust!"
        print "*******You win!*******"
    elif pc > 21:
        print "----------------------"
        print "You went bust!"
        print "**You lose!!**"
    elif dc >= pc:
        print "----------------------"
        print " The dealer's hand: %s" % " ".join(dh)
        print "The dealer's score: %d" % dc
        print "        Your score: %d" %pc
        print "******You  lose!******"
    else:
        print "----------------------"
        print " The dealer's hand: %s" % " ".join(dh)
        print "The dealer's score: %d" % dc
        print "        Your score: %d" %pc
        print "  You beat the dealer!"

def start():
    a = True
    print "Welcome to Blackjack."
    while a == True:
        print "\n1.Rules\n2.New Game\n3.Exit"
        choice = raw_input("[1 2 or 3] > ")
        if choice == "1":
            print rules
        elif choice == "2":
            game()
        elif choice == "3":
            print "Bye!"
            a = False
        else:
            print "Thats not an option!"

start()
