from random import choice

player = ["rehan", "singgih", "bot", "boy", "orang 1", "orang 2", "orang 3", "orang4", "orang 5"]
print("player: ", player)
teamsname = ["apel", "jeruk", "mangga", "pisang"]
print("teamsname", teamsname)

tim_a = []
tim_b = []

while len(player) > 0:
  tim = choice(player)
  tim_a.append(tim)
  player.remove(tim)
 
  if player == []:
    break

  tim = choice(player)
  tim_b.append(tim)
  player.remove(tim)
  
teamsname_a = choice(teamsname)
teamsname.remove(teamsname_a)
teamsname_b = choice(teamsname)
teamsname.remove(teamsname_b)


print("\nhere your team:\n")
print(teamsname_a, tim_a)
print(teamsname_b, tim_b)


