#cDefine the derived class Batman 
class player:
  def play(self):
    print("The player is")



class Batsman(player):
  def play(self):
    print("The Batsman is batting.")

# Define the derived class Bowler 
class Bowler(player):
  def play(self):
    print("The Bowler is bowling.")

# Create objects of Batsman and Bowler classesclasses
batsman = Batsman()
bowler = Bowler()

# Call the play()Method for each object 
batsman.play()
bowler.play()