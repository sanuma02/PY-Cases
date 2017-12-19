import random
class Player(object):
  
  def __init__(self,name,cash):
    self.name =name
    self.cash = cash
    
  def getCash(self):
    return self.cash
    
  def addMoney(self,cash):
    self.cash += cash
    
  def removeMoney(self,cash):
    self.cash -= cash
    

class Dealer(object):
  
  deck = {1:1, 2:2, 3:3,4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A': 11}
  cards =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
  
  def __init__(self):
    pass
  
  def deal(self):
    r1 = random.choice(Dealer.cards)
    r2 = random.choice(Dealer.cards)
    return [r1,r2]
    
  def getCard(self):
    r1 = random.choice(Dealer.cards)
    return r1
    
  def calculateGame(self,l):
    total = 0
    for value in l:
      total += Dealer.deck[value]
    return total
    
  def checkWinner(self, p, d):
    if p == d:
      return 'd'
    else:
      x = 21 - p
      y = 21 - d
      if x < y:
        return 'p'
      else:
        return 'd'
  
  def stillPlaying(self, num):
    if num < 22:
      return True
    else:
      return False
    

name1 = input("Welcome to BJ, what is your name?")
money1 = int(input("How much money do you have?"))
player = Player(name1,money1)
dealer = Dealer()
while player.getCash() > 0:
  bet = int(input("how much do you want to bet?"))
  if bet > player.getCash():
    print("Sorry you dont have that much. Your bet will be all you have: %s" %(player.getCash()))
    bet = player.getCash()
  player_current_game = dealer.deal()
  print("Your Game:")
  print(player_current_game)
  while True:
    choice = input("do you want to stand or hit?")
    if choice == 'h':
      player_current_game.append(dealer.getCard())
      print(player_current_game)
    else:
      break
  print(player_current_game)
  player_total = dealer.calculateGame(player_current_game)
  print("Your current game: %s" %(player_total))
  if dealer.stillPlaying(player_total):
    print("My turn!!!!!!!")
    dealer_current_game = dealer.deal()
    dealer_total = dealer.calculateGame(dealer_current_game)
    print (dealer_current_game)
    print("My current game: %s" %(dealer_total))
    winner = dealer.checkWinner(player_total,dealer_total)
    if winner == 'd':
      player.removeMoney(bet)
      print("Sorry, the house won")
    else:
      player.addMoney(bet)
      print("WOW, Congratulations you won")
  else:
    player.removeMoney(bet)
    print("Sorry, the house won")
  print("%s Your current cash: %s" %(name1,player.getCash()))
print("sorry %s you ran out of money!!!!!" %(name1))

  
  
  

    
    
      
    
    
  
  
  
  