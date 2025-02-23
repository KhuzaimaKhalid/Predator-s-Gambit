import random

print("======= Predator's Gambit ============")
result_matrix = [
    # User picks 0, 1, 2
    [ 0, -1,  1],  # comp = 0
    [ 1,  0, -1],  # comp = 1
    [-1,  1,  0]   # comp = 2
]

def check(comp, user):
    return result_matrix[comp][user] 
  
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")   
