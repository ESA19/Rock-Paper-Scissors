
import random
how_many_round=int(input("How many rounds want to play?:"))
actions_of_game=["rock","paper","scissors"]
player1_score=0
player2_score=0
i=1
while i<=how_many_round: 
  player1=random.choice(actions_of_game)
  player2=random.choice(actions_of_game)
  print("player1 : ",player1)
  print("player2 : ",player2)
  if player1=="paper" and player2=="rock":
    print("player 1 is",i,".round winner")
    player1_score +=1
  elif player1=="paper" and player2=="scissors":
    print("Player 2 is",i,". round winner ")
    player2_score +=1
  elif player1=="scissors" and player2=="rock":
    print("Player 2 is ",i,".round winner")
    player2_score +=1
  elif player1=="scissors" and player2=="paper":
    print("Player 1 is ",i,".round winner")
    player1_score +=1
  elif player1=="rock" and player2=="paper":
    print("Player 2 is ",i,".round winner")
    player2_score +=1
  elif player1=="rock" and player2=="scissors":
    print("Player 1 is ",i,".round winner")
    player1_score +=1
  else:
    print("Scorless!")
  print("Remain round: ",how_many_round-i)
  i+=1
  print(">---------------------------------------------------------------<")
print("Player1 score is: ",player1_score)
print("Player2 score is: ",player2_score)
if player1_score>player2_score:
  print("Player1 is a Total Winner!")
elif player2_score>player1_score:
  print("Player2 is a Total Winner!")
else:
  print("No Winner, Draw!")