import random

# Scenario: There are 20 cards and 4 players. In the 20 cards, there is 1 card that award a point. 4 players take turns drawing a card until the point is awarded to a player. The process is repeated.
# Purpose: This project attempts to discover if the game is fair or if move order matters by running computer simulations.
# Findings: This game is completely fair. All players have equal chances of winning, no matter what the move order is. I tried changing numbers, and I found that the chances of winning for each player is simply # of draws possible/# of cards. For example, if there are 2 players and 3 cards, player 1 has a 2/3 chance of winning while player 2 has a 1/3 chance of winning. This is because player 1 can draw 2 cards while player 2 can only draw 1. The # of cards that award points do not matter.

class Probability():
  def __init__(self):
    self.board = ["o", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
    self.scores = [0, 0, 0, 0]
    self.current_turn = 3

  def shuffle(self):
    random.shuffle(self.board)
    random.shuffle(self.board)
    random.shuffle(self.board)
    random.shuffle(self.board)
    # shuffle 4 times bc why not

  def turn(self):
    self.current_turn = (self.current_turn + 1) % 4
    return self.current_turn
    # cycle through turns
  
  def play(self):
    for i in range(20):
      if "o" not in self.board:
        return
      self.shuffle()
      choice = random.choice(self.board)
      turn = self.turn()
      if choice == "o":
        self.scores[turn] += 1
      self.board.remove(choice)

total = [0,0,0,0]

while True:
  for i in range(10000):
    s = Probability()
    s.play()
    total[0] += s.scores[0]
    total[1] += s.scores[1]
    total[2] += s.scores[2]
    total[3] += s.scores[3]
  
  print(total)
  final = sum(total)
  print([round(total[0]*100/final, 2), round(total[1]*100/final, 2), round(total[2]*100/final, 2), round(total[3]*100/final, 2)])