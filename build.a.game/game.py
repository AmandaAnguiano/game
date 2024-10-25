
# (variable) what each path causes to happen to the user - amanda
print("Welcome to Gold Quest Island! There will be gold scattered all around the island, you only need to collect 5!\n") 
path1 = ("You walk deeper into the jungle, you hit somthing on the ground and see its your first piece of gold. Just then a monkey comes and takes it from your hands and runs!")
path2 = ("You continue walking the shore, after a few hours you find no gold.")
# (function) ask the quests questions and where they want to go for the different locations on the game map- ellie
jungle = path1
shore = path2
def location(side):
    return f"Would you like to {side}"

print(location("go into the jungle or keep walking the shore'?\n"))
input()
# (condition) conditoning wether the user takes path one or two and what happens when user chooses different answers - sofia
if input() == shore:
    print(path1)
else:
    print(path2)
# (loop) how many lives the user has and wether they would like to restart or continue and controls how long the condition goes for until game is done - lindsey

