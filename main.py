import time # Importing the time module as I use this throughout the code to make the code sleep for a set period of time, this is to simulate a natural delay which would happen such as dealing the cards or determining a winner. This makes the code more interactive and fluid, rather than just a wall of text being printed to the console.

def play_game():


  """
  ----------------------------------------------------------------
  TASK ONE
  ----------------------------------------------------------------
  """

  ''' Setting up the functions for the welcome screen ''' # The welcome screen is the first screen the user will see when running the code.

  # Creating start_game function:
  # Prompting the user to start the game
  def start_game():
      global startgame # Making the variable 'global' so it can be recognised by the code outside of this function. This 'global' assign appears in multiple functions in the code.
      startgame = 'notstart' # Setting the variable for startgame, so the game is not 'started' and is rather 'notstart'ed.
      while startgame != 'start':
          startgame = input(
              "When you're ready to play, type 'start' to begin!: ") # Whilst the game isn't started, prompts the user to start the game by typing 'start'.
      else:
          startgame = 'start' # If the game is already started (startgame = 'start') then simply load the game. This is to avoid the console prompting the user to start the game if they already have.
          load_game()


  # Creating the load game function to load/begin the game (this will initiate other functions, such as loading the deck and subsequently dealing the deck)
  def load_game():
      global loadgame
      loadgame = 'not loaded'
      if startgame != 'start': # If the game has not started, the game will not load. This is to prevent the game loading and the rest of the script being run if the user has not started the game.
          loadgame = "not loaded"
      else:
          loadgame = "loaded" # If the game is started, load the game.


  # Creating rules function:
  # Displaying the rules of the game to the user
  def rules():
    print("---------------------------------------------------\n---------------------------------------------------")
    print("THE RULES\n")
    print("""This game is a simplified version of Texas Hold'em Poker. You and the AI will compete to win a poker hand. The possible winning hands are based on the full version of the game, though there are a few less types of hands you can win with.
    
    The winning hand types are:
    --- High card - If you have none of the following hands, your highest card is your winning card.
    --- One pair - A pair of cards (with the same number)
    --- Two pair - Two pairs of cards (with the same number)
    --- Three of a kind - Three cards with the same number
    --- Full house - Three of a kind plus a two pair
    --- Flush - Five cards of the same suit
    --- Four of a kind - Four cards with the same number
    
    They are in order! That means two pair beats one pair, full house beats three of a kind, and so on.
    
    You will be dealt two cards. Then three cards will be dealt as the 'flop'. This simply means three cards will be 'laid on the table'. Your two cards combined with the flop make up your hand. The AI will also be dealt 2 cards, but obviously you can't see their cards!

    Your job is to either 'fold' - give up the hand and be dealt a new hand - or play on. The goal is to get a winning hand that is better than your opponent's winning hand!
    
    Good luck!""")
    print("---------------------------------------------------\n---------------------------------------------------\n\n")


  # Creating welcome_screen function:
  # Actions the start_game function to display a welcome screen and prompts the user to start the game
  def welcome_screen():
      print("************************************ Welcome to Texas Hold 'Em! ************************************\n")
      rules() # Print the rules as part of the welcome screen.
      print() # Many print()'s are used throughout the code, purely for aesthetic reasons (spacing between output to the console).
      print("Loading the game...")
      time.sleep(5) # First usage of the sleep function mentioned at the top of this script.
      start_game() # Run the start_game function.
      load_game() # Run the load_game function




  ''' The Welcome Screen '''

  welcome_screen() # Now that the welcome_screen function has been defined, run it.




  ''' Creating the deck of cards '''

  # Creating the dictionary 'card_deck' and assigning the variables for all values a card can have and all of the suits in a deck
  card_deck = {}

  card_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Ten', 'Jack', 'Queen','King'] # 10 is Ten because having ten be comprised of two integers '1' and '0' causes complications when trying to determine a winner by evaluating the hands later in the code, it's easier to name it as though it is a face card and have simply one character represent Ten (T) rather than two (1 and 0)

  card_suits = ['hearts', 'clubs', 'diamonds', 'spades']


  # Using a nested loop to assign each unique card in a 52 pack of cards a 'short name' (Ac, 2c etc) and a 'full name' (Ace of Clubs, 2 of Clubs) where each matching short_name and full_name is assigned to one entry in the dictionary.
  def deck_of_cards():
      if loadgame == "loaded":
          # While loop is used so the deck is not generated until the user has started the game (starting the game prompts loadgame = loaded)

          for suit in range(len(card_suits)): # for each item in the number of items in the 'card_suits' list...
              for value in range(len(card_values)): # and for each value in the number of values in the 'card_values' list...
                    
                    short_name = f'{card_values[value][0]}{card_suits[suit][0]}' # Create a 'short name' which has the format ('f{}') which takes the first (0) character of the specified value iteration (value) in card_values, and does the same for suits, then combines these to form Vs (value and suit, e.g. Ac for Ace of Clubs).

                    full_name = f'{card_values[value].capitalize()} of {card_suits[suit].capitalize()}' # Create a 'full_name' which has the format taking the capitalized value and the capitalized suit (so Ace of Clubs rather than ace of clubs), and combining these to create each card (for every value and every suit).
                    
                    card_deck[short_name] = full_name # Append these formatted variables to the dictionary, where each short name matches the full name.


  # Function to show the deck of cards
  def show_deck():
      if loadgame == "loaded":
        print("Okay! Shuffling the deck...") # This doesn't actually 'shuffle' any cards, just simulates a real-world scenario where cards would be shuffled'
        time.sleep(5) # Setting a delay on showing the cards to the player, to simulate the delay that would happen in actually dealing the cards
        print()
        print()
        print(card_deck)
        print()
        print()


  # Calling the functions to generate the deck of cards
  deck_of_cards()
  
  #Asking the user if they would like to see the deck, and if yes then use the show_deck function.
  show_deck_yes_no = input("Would you like to see the deck of cards? (Y/N): ")
  if ('y' in show_deck_yes_no.lower()): # If the lower case conversion of the user's input is 'y'...
    print() # Aesthetic spacing.
    show_deck() # Show the deck.
    time.sleep(5) # Gives the player time to simply look at the deck.
        # Optional function which shows the deck of cards to the player.
  else:
    print()
    print("Okay...\n")

  print() # Aesthetic spacing in the console.













  """
  ----------------------------------------------------------------
  TASK THREE - Determining who the winner is
  ----------------------------------------------------------------
  """

  def the_showdown(): # All of task 3 (determining the winner) occurs inside the_showdown() function. This is so the folding function (which is written at the end of the script) can return either the_showdown() function (if the user doesn't fold) or the deal_hand() function (if the user folds).


    '''
    SHOW THE CARDS OF EACH PLAYER COMBINED WITH THE FLOP TO CREATE THE 'HAND' FOR EACH PLAYER
    '''

    # Creating the Showdown class which will add each player's cards to the flop and then display them to the player

    class Showdown(object):
      def __init__(self, name, cards, flop):
        # Initializing each parameter as assigned when using the Showdown class
        self.name = name
        self.cards = cards
        self.flop = flop
      
      # Creating a function which combines the cards with the flop and stores it in a new list called extended_hand
      def create_hand(self):
        # The self.name variable is assigned in the parameters when calling the Showdown() class. This means if the player is called, assign the hand to 'p_extended_hand'. Vice versa with the AI, so each hand is stored in a separate list for each player so they are not overwritten
        if self.name == 'Your': # If the player ('Your')...
          global p_extended_hand
          p_extended_hand = [*self.cards, *self.flop] # * is the spread operator
        else:
          global ai_extended_hand
          ai_extended_hand =  [*self.cards, *self.flop]

        # Creating a function which prints the extended_hand to the console
        def show_hand():
          if self.name == 'Your':
            print(self.name + " hand:", p_extended_hand)
          else:
            print(self.name + " hand:", ai_extended_hand) # Prints with the format self.name (either 'Your' or 'AI') + "hand:" so "Your hand" or "AI hand", and then prints the list (which is the cards plus the flop).

        # Running the show_hand function
        show_hand()

      
    # Using the Showdown class to use the hand() function to print out each player's hand combined with the flop

    player_showdown = Showdown('Your', list(pcard_dict.values()), list((flopdict.values()))) # The player's showdown cards call the Showdown function and assign the parameters ('Your' for the self.name, list(dict) which is the player's card dictionary, and list(dict) which is the flop dictionary). List converts the dictionary to a list, which is easier to work with later in the code.
    ai_showdown = Showdown("AI's", list(aicard_dict.values()), list(flopdict.values())) # As above but for the AI.

    # Setting a delay on showing the cards to the player, to simulate the delay that would happen in actually dealing the cards
    print("Time for the showdown! Revealing your cards to the table...\n")
    time.sleep(5)

    print("---------")
    print("SHOWDOWN")
    player_showdown.create_hand()
    ai_showdown.create_hand()
    print("---------")
    print()




    '''
    CALCULATE THE VALUE OF TWO POKER HANDS FROM BOTHER PLAYERS BASED ON A TABLE (OF VALUES)
    '''

    ''' Assigning all cards a rank from 1 to 13, including face cards - e.g. so a highest value can be determined and so they can be sorted in value order'''
    
    # Storing the face cards in a dictionary (ten is included as a face card because of the '10' problem mentioned at the start)
    face_cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    # Converting the face cards to a number so they have a number value
    def to_number(card):
      if card[0].isnumeric(): # If the card parameter assigned (when calling the function) is numeric, simply return the integer of that card (so 4 will return 4)
        return int(card[0])
      else:
        return face_cards[card[0]] # If the card parameter assigned (when calling the function) is not numeric, it is a letter (face card). Take the value from the key,value pair in the dictionary face_cards, and return that card as that value.


    # Sorting the hand to check the face_cards have correctly been given a numeric value
    '''
    p_extended_hand.sort(key=to_number)
    ai_extended_hand.sort(key=to_number)
    print(p_extended_hand)
    print(ai_extended_hand)
    '''




    """
    FUNCTIONS WHICH TEST FOR A TYPE OF HAND
    """

    # Checking for a flush
    def is_flush(hand):

      def get_suits(hand):
        # Gets the suit of each card in the hand
        return [card[-1] for card in hand] # E.g. if a card is Ac, it takes the end of this card (-1) which is c, and returns this. It loops this 'for' every card in the hand.


      def all_equal(suits):
        # If the length of the set of the list is equal to 1, that means there is only 1 set in the list. This is because when a set is created (here with set(list)) each element has to be unique. So if a suit is stored, it is only stored once. If the length of the set is greater than 1, that must mean at least 2 suits have been stored and therefore the hand can't be a flush.
        return len(set(suits)) == 1

      
      suits = get_suits(hand) # Assigning the variable suits to the function get_suits() so the function doesn't have to be called every time, rather just the suits variable itself.

      if all_equal(suits):
      # Hand is a flush
        return True # Later in the code, the winning hand is determined by 'if is_flush(hand) == True' then 'return 'Flush', for all hand types. So if this code termines that all the suits are equal, then the hand must be a flush, and returns the True boolean.


    def is_full_house(hand): # Full house is three of a kind combined with a two pair
      """ Checking for three of a kind """
      for hand_card in range(0, len(hand)): # For one card in the hand (here it is called hand_card)...
        for check_card1 in range(hand_card + 1, len(hand)): # And for a second card in the hand (check_card1)...
          if hand[hand_card][0] == hand[check_card1][0]: # If the VALUE of the hand card ([0], as 0 takes the first part of the card, e.g. 3 in 3s) matches the VALUE of the check card (so if there is one pair found)...

            for check_card2 in range(check_card1 + 1, len(hand)): # Check against a third card (check_card2), by taking the next card in the hand (check_card1 +1)...
              if check_card2 != hand_card and check_card2 != check_card1: # To ensure no card is checked against itself

                  if hand[check_card2][0] == hand[check_card1][0] and hand[check_card1][0] == hand[hand_card][0]: # If all card values match (three of a kind)...
                    

                    """ Checking for a pair if the hand has three of a kind """
                    for hand_card2 in range(0, len(hand)):
                    
                      for check_card3 in range(hand_card2 + 1, len(hand)):

                        if check_card3 != hand_card and check_card3 != hand_card2 and check_card3 != check_card1 and check_card3 != check_card2:

                          if hand[hand_card2][0] == hand[check_card3][0]:
                            return True


    def is_high_card(hand):
      hand = sorted(hand, key=to_number) # Sort the hand according to the values which are returned in the function to_number().

      high_card = hand[-1] # The highest card is the card which is at the end of the list when the cards are sorted.
      return high_card



    def is_one_pair(hand):
      for hand_card in range(0, len(hand)): # For one card in the hand...
        for check_card in range(hand_card + 1, len(hand)): # And for another card in the hand...
          if hand[hand_card][0] == hand[check_card][0]: # If the card VALUES match, then there is a pair (return True). If the card values do not match, the loop continues until all cards have been checked.
            return True


    def is_two_pair(hand):
      for hand_card in range(0, len(hand)): # As above
        for check_card in range(hand_card + 1, len(hand)): # As above
          if hand[hand_card][0] == hand[check_card][0]: # If ONE PAIR has been found...

            for hand_card2 in range(0, len(hand)): # Check the NEXT card in the hand...
              if hand_card2 != hand_card and hand_card2 != check_card: # To ensure no card is checked against itself

                for check_card2 in range(hand_card2 + 1, len(hand)): # And check the NEXT card in the hand...
                  if check_card2 != hand_card2 and check_card2 != hand_card and check_card2 != check_card: # To ensure no card is checked against itself and to ensure that the second pair does not match the first pair that has already been found

                    if hand[hand_card2][0] == hand[check_card2][0]: # If the second set of cards are a pair, return True.
                      return True


    def is_three_of_a_kind(hand): # As described above in 'is_full_house():'
      for hand_card in range(0, len(hand)):
        for check_card1 in range(hand_card + 1, len(hand)):
          if hand[hand_card][0] == hand[check_card1][0]:

            for check_card2 in range(check_card1 + 1, len(hand)):
              if check_card2 != hand_card and check_card2 != check_card1:

                  if hand[check_card2][0] == hand[check_card1][0] and hand[check_card1][0] == hand[hand_card][0]:
                    return True


    def is_four_of_a_kind(hand): # This function is an extension of the 'is_three_of_a_kind()' function, with one extra loop to check a 4th card.
      for hand_card in range(0, len(hand)):
        for check_card1 in range(hand_card + 1, len(hand)):
          if hand[hand_card][0] == hand[check_card1][0]:

            for check_card2 in range(0, len(hand)):
              if check_card2 != hand_card and check_card2 != check_card1:

                  if hand[check_card2][0] == hand[check_card1][0] and hand[check_card1][0] == hand[hand_card][0]:
                    
                    for check_card3 in range(0, len(hand)):
                      if check_card3 != hand_card and check_card3 != check_card1 and check_card3 != check_card2:

                        if hand[check_card3][0] == hand[check_card2][0] and hand[check_card2][0] == hand[check_card1][0] and hand[check_card1][0] == hand[hand_card][0]:
                          return True


    """
    FUNCTION WHICH EVALUATES THE HAND TO DETERMINE WHICH TYPE THE HAND IS
    """

    def evaluate_hand(hand): # The function determines each hand in the order of the highest value. If they were not indented and ordered, a problem could occur where a two pair could be found by the code before a full house, and the function would end and the hand would be determined a two pair even though a higher value hand existed (full house).
      if is_four_of_a_kind(hand) == True: # If four of a kind returns True, then return 'Four of a kind'. This format applies for all of the below nested IF/ELSE statements.
        return 'Four of a kind'
      else:
        if is_full_house(hand) == True:
          return 'Full house'
        else:
          if is_flush(hand) == True:
            return 'Flush'
          else:
            if is_three_of_a_kind(hand) == True:
              return 'Three of a kind'
            else:
              if is_two_pair(hand) == True:
                return 'Two pair'
              else:
                if is_one_pair(hand) == True:
                  return 'One pair'
                else:
                  is_high_card(hand)
                  return 'High card'


    # ---------------
    # TABLE OF VALUES
    # ---------------
    # Defining a table of values in a function which assigns the result of evaluate_hand to a variable with a rank/integer.
    def hand_rank(hand):

      high_card = 0 # None of the hands above, highest card wins (card values)
      one_pair = 1 # One pair (card values)
      two_pair = 2 # Two different pairs (card values)
      three_of_a_kind = 3 # Three cards of the same rank (card values)
      flush = 4 # Any five cards of the same suit, but not in a sequence (card suits)
      full_house = 5 # Three of a kind with a pair (card values)
      four_of_a_kind = 7 # All four cards of the same rank (card values)

      if evaluate_hand(hand) == 'High card': # If evaluate_hand(hand) returns 'High card' then return the high_card variable (which is 0). Same for the below IF statements.
        return high_card
      
      if evaluate_hand(hand) == 'One pair':
        return one_pair

      if evaluate_hand(hand) == 'Two pair':
        return two_pair
      
      if evaluate_hand(hand) == 'Three of a kind':
        return three_of_a_kind

      if evaluate_hand(hand) == 'Flush':
        return flush

      if evaluate_hand(hand) == 'Full house':
        return full_house
      
      if evaluate_hand(hand) == 'Four of a kind':
        return four_of_a_kind

    # Function which determines the winning hand based on which hand has the highest value returned (according to the hand_rank function above)
    def winning_hand(hand):

      # If the players hand rank is higher than the AI's hand rank:
      if hand_rank(p_extended_hand) > hand_rank(ai_extended_hand):
        print("********************************")
        print("You are the winner! You won with " + evaluate_hand(p_extended_hand) + ".")
        print("********************************")
      
      # If the AI's hand rank is higher than the player's hand rank:
      elif hand_rank(ai_extended_hand) > hand_rank(p_extended_hand):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("You lose! The AI wins with " + evaluate_hand(ai_extended_hand) + ".")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

      # If the hand rank is tied:
      else:
        print("-------------------------------")
        print("TIED! You both tied with " + evaluate_hand(p_extended_hand) + ".")
        print("-------------------------------")


    # Setting a delay on revealing the winner, to allow the player time to review the showdown/cards on the table
    time.sleep(5)

    print("And the winner is...\n")
    time.sleep(10)

    # Calling the function for the winning hand to reveal the winner.
    winning_hand(p_extended_hand)
        # Here it doesn't matter if the chosen hand in the parameter is ai_extended_hand or p_extended_hand, it will compare both hands against each other anyway
    
    print()
    print()
    print()







  """
  ----------------------------------------------------------------
  TASK TWO - Card dealing and folding
  ----------------------------------------------------------------
  """

  def deal_hand():


    ''' Randomly assigning the user two cards as a personal hand and printing them to the console '''

    # Importing the random module to perform deal random cards from the deck

    import random

    # Converting the deck of cards to a list so cards can be chosen from the list and removed from the list when dealt (to take it out of the 'deck' and into the players hand so it can't be 'dealt twice')
    
    global card_deck_list
    card_deck_list = list(card_deck)
    '''
          print(card_deck_list)
                Used this to check that the entire deck had been correctly assigned in this list
          '''

    # Creating a dictionary to store the player's cards in
    global pcard_dict
    pcard_dict = {}

    # Choosing/dealing two cards at random under the 'pdeal' function
    def pdeal():
      for card in range(1, 3):
        pcard = 'Playercard '
        pcard = f'{pcard}{card}' # Formatting the pcard variable so on each loop iteration the player card changes from 'Playercard 1' to 'Playercard 2' etc
        randomcard = random.choice(card_deck_list)
        pcard_dict[pcard] = randomcard # Assigning the randomcard to the player card number in the dictionary which stores the player cards cards.
        card_deck_list.remove(randomcard)  # # Removing the 'dealt card' from the list as though removing it from the deck into the players hand

    # Calling the pdeal function to deal 2 cards to the player
    pdeal()

    # Setting a delay on showing the cards to the player, to simulate the delay that would happen in actually dealing the cards

    print("Dealing your cards...\n")
    time.sleep(5)

    # Printing the hand to the player
    print("---------")
    print("YOUR HAND")
    for key in pcard_dict:
      print(pcard_dict[key]) # Taking the values from each key in the dictionary and printing (each key is one player card)
    print("---------")
    print()

    time.sleep(5) # Gives the player time to view their cards

    #Checking that the dealt cards have been removed from the list
    '''
          print(card_deck_list)
                Used this to check that the two cards had been removed from the list
    '''



    ''' Randomly selecting three cards as the flop and print the three cards in the console '''

    # Creating the 'flopdict' dictionary to store the flop cards in
    global flopdict
    flopdict = {} # Dictionary to store the cards in

    # Defining a function which chooses 3 cards as the flop and stores them in a dictionary
    def flop():
      for card in range(1, 4):
        flopcard = 'Flopcard ' # Defining the variable flopcard as 'Flopcard '
        flopcard = f'{flopcard}{card}' # Formatting the flopcard variable so on each loop iteration the flopcard changes from 'Flopcard 1' to 'Flopcard 2' etc.
        randomcard = random.choice(card_deck_list)

        flopdict[flopcard] = randomcard # Assigning the randomcard to the flopcard number in the dictionary which stores the flop cards.

        card_deck_list.remove(randomcard) # Removing from the deck (the list created earlier) so the card isn't dealt twice

    # Printing the 'flopdict' to check that three flop cards have been dealt and stored appropriately
    # print(flopdict)
    # Commented after checking because we don't want this to be presented to the player in this format

    # Calling the function to deal the flop
    flop()

    # Setting a delay on showing the cards to the player, to simulate the delay that would happen in actually dealing the cards
    print("Dealing the flop...\n")
    time.sleep(5)

    # Printing the flopcards to the player
    print("---------")
    print("THE FLOP")
    for key in flopdict:
      print(flopdict[key])
    print("---------")
    print()

    time.sleep(15) # Gives the player time to view the flop and compare it with their hand.


    ''' Randomly assigning the AI player two cards as its personal hand '''
    # Creating the AI card dictionary to store the AI cards in
    global aicard_dict
    aicard_dict = {}

    # Defining a function which deals 2 cards to the AI
    def aideal():
      for card in range(1, 3):
        aicard = 'AI card: '
        aicard = f'{aicard}{card}'

        randomcard = random.choice(card_deck_list)

        aicard_dict[aicard] = randomcard

        card_deck_list.remove(randomcard)

    # Calling the aideal function to deal 2 cards to the AI
    aideal()

    # Checking the AI cards have been dealt
    # print(aicard_dict)
    # Commented this function after I checked it because the user isn't supposed to see the AI's cards



    ''' Writes the two personal hands and the flop in a file named "pokerhandhistory.txt" in the same form given below (XXX stands for username):

      XXX: [Ac, Ah]. AI: [Js, 10d]. Flop: [Qd, 10h, 2c] '''

    # Defining the variable to open the file
    hands_txt = open("pokerhandhistory.txt", "w")

    # Writing the cards (stored in dictionaries for player/AI/flop) to the txt file with the correct formatting
    hands_txt.write('XXX:' + str(list(pcard_dict.values())) + str('. '))
    hands_txt.write('AI:' + str(list(aicard_dict.values())) + str('. '))
    hands_txt.write('Flop: ' + str(list(flopdict.values())) + str('. '))

    # Closing the file to save the changes
    hands_txt.close()







    """
    ----------------------------------------------------------------
    TASK 4 - Adding more fun to the game (folding)
    ----------------------------------------------------------------
    """

    def is_fold():
      fold_attempts_left = 5 # Defining how many fold attempts the user has left (starts at 5)

      if fold_attempts_left != 0: # If the user still has fold attempts left...
        print("You have", fold_attempts_left, "fold attempts left.")
        fold_y_n = input("Would you like to fold this hand? (Y/N): ")
        
        if ('y' in fold_y_n.lower()):
          print()
          fold_attempts_left -= 1
          print("Okay! You have folded this hand. You have", fold_attempts_left, "fold attempts left.")
          print()
          return deal_hand()
        
        elif not ('y' or 'n' in fold_y_n.lower()):
          fold_y_n = input("Please type Y or N: ")
        
        else:
          print()
          return the_showdown()

      else: # If the user has 0 fold attempts left...
        print()
        print("Uh oh. You have run out of fold attempts!")
        print()
        return the_showdown()



    # Running the is_fold() function to ask the user if they would like to fold.
    is_fold()





  # Running the function (defined above) which deals the player cards and the flop, and then asks the player if they would like to fold.
  deal_hand()


  


""" STARTING / RESTARTING THE GAME """
while True: # This will be the first thing that the code runs, because it is the first block of code not inside a function. It will first run the play_game function, which is where all of the above code is stored.
  play_game()
  answer = input("Would you like to play again? (Y/N): ") # When all of the above code has run (under play_game()), ask the user if they would like to play again. If they answer Y, play_game() runs again.
  print()
  print()
  print()
  if not ('y' in answer.lower()): # If the user doesn't answer Y, then the loop breaks and the script ends.
    break
