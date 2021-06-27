import random

cards = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts',
'6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts',
'2 of Hearts', 'Ace of Hearts', 'King of Hearts',
'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds',
'9 of Diamonds', '8 of Diamonds', '7 of Diamonds',
'6 of Diamonds', '5 of Diamonds', '4 of Diamonds',
'3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds',
'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds',
'10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs',
'6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs',
'2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs',
'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades',
'7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades',
'3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades',
'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10,
 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4,
 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4,
 3, 2, 1, 10, 10, 10]

playerCardList = []
computerCardList = []
playerPoints = 0
computerPoints = 0

MAX_WINNING_POINT = 21
IS_PLAYER = True
IS_COMPUTER = False

def whichParty(isPlayer):
  if isPlayer:
    return playerCardList
  else:
    return computerCardList

def getCard(isPlayer, partyHand, partyPoints, occurence):
  party = whichParty(isPlayer)

  if occurence == 2:
    for count in range(occurence):
      party.append(random.randint(0, len(cards)-1))
    
    for position in party:
      partyHand += "'" + cards[position] + "', "
      partyPoints += values[position]
    
  else:
    party.append(random.randint(0, len(cards)-1))
    partyHand += ", '" + cards[len(party) - 1] + "'"
    partyPoints += values[len(party) - 1]
    print(("You drew " if isPlayer else "Computer drew ") + cards[len(party) - 1])

  return [partyHand, partyPoints]

def playGame(isPlayer):
  partyHand = ""
  partyPoints = 0
  party = whichParty(isPlayer)

  while True:
    if len(party) == 0:
      result = getCard(isPlayer, partyHand, partyPoints, 2)
      # Assign value and remove last comma with [:-2]
      partyHand = result[0][:-2]
      partyPoints = result[1]
    else:
      result = getCard(isPlayer, partyHand, partyPoints, 1)
      partyHand = result[0]
      partyPoints = result[1]

    if isPlayer:
      print("Player hand: [" + partyHand + "] is worth " + str(partyPoints))
      if partyPoints < MAX_WINNING_POINT:
        hitOrStand = input("(h)it or (s)tand? ")

        if hitOrStand == "s":
          return partyPoints
      else:
        return partyPoints

    else:
      print("Computer hand: [" + partyHand + "] is worth " + str(partyPoints))
      if partyPoints > MAX_WINNING_POINT or partyPoints == MAX_WINNING_POINT or partyPoints > playerPoints:
        return partyPoints
      
def declareWinner(isPlayer):
  if isPlayer:
    print("Player wins!")
  else:
    print("Computer wins!")

# Game starts here
playerPoints = playGame(IS_PLAYER)
if playerPoints == MAX_WINNING_POINT:
  declareWinner(IS_PLAYER)
elif playerPoints > MAX_WINNING_POINT:
  print("Bust!")
  declareWinner(IS_COMPUTER)
else:
  computerPoints = playGame(IS_COMPUTER)
  if (computerPoints > playerPoints and computerPoints < MAX_WINNING_POINT) or computerPoints == MAX_WINNING_POINT:
    declareWinner(IS_COMPUTER)
  else:
    print("Bust!")
    declareWinner(IS_PLAYER)


