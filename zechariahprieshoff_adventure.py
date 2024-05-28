#Zechariah Prieshoff
#May 24th, 2024
#Adventure Game
#Program will simulate a classic "Choose Your Own Adventure" game where the user is given a scenario and
#two options to choose from, each option takes the user in a different direction.

print("Welcome to the 'Mysterious Island' adventure game!")

def getGame():
    game = {
        'start': ["You wake up on a mysterious island.", "Go north", 'north', "Go south", 'south'],
        'north': ["A dinosaur is running towards you!", "Dodge", 'dodged', "Stay, maybe it's friendly", 'crushed'],
        'south': ["You find a beach with a boat.", "Take the boat", 'boat', "Explore the beach", 'beach'],
        'dodged': ["You dodged the dinosaur, but now it's chasing you!", "Climb a tree", 'tree', "Run to the cave", 'cave'],
        'boat': ["The boat has a hole in it and starts sinking.", "Swim back to shore", 'south', "Try to patch the hole", 'patch'],
        'beach': ["You find a treasure chest buried in the sand.", "Open the chest", 'treasure', "Ignore the chest", 'ignore'],
        'tree': ["You climbed the tree and the dinosaur can't reach you.", "Wait until the dinosaur leaves", 'wait', "Jump to another tree", 'jump'],
        'cave': ["The cave is dark and you hear strange noises.", "Light a torch", 'torch', "Move forward in the dark", 'dark'],
        'patch': ["You successfully patch the hole and sail away safely.", "Start over", 'start', "Quit", 'quit'],
        'treasure': ["There was a snake in the chest and it bit you!", "Start over", 'start', "Quit", 'quit'],
        'ignore': ["You walk away and find a path leading to the jungle.", "Follow the path", 'jungle', "Head back to the start", 'start'],
        'wait': ["The dinosaur eventually leaves.", "Climb down and head north", 'north', "Stay in the tree", 'stayInTree'],
        'jump': ["You safely jump to another tree and the dinosaur gives up.", "Climb down and explore", 'explore', "Stay in the tree", 'stayInTree'],
        'torch': ["With the torch, you see cave paintings showing a way out.", "Follow the paintings", 'paintings', "Ignore and explore deeper", 'deeper'],
        'dark': ["You stumble in the dark and fall into a pit. You died.", "Start over", 'start', "Quit", 'quit'],
        'jungle': ["You encounter a tribe of friendly natives.", "Talk to them", 'talk', "Run away", 'run'],
        'stayInTree': ["You stayed in the tree until you fell asleep and fell. You died.", "Start over", 'start', "Quit", 'quit'],
        'explore': ["You find an abandoned camp with supplies.", "Take the supplies", 'supplies', "Leave them", 'leave'],
        'paintings': ["The paintings lead you to a hidden exit. You escaped!", "Start over", 'start', "Quit", 'quit'],
        'deeper': ["You find an underground river.", "Swim across", 'swim', "Follow the river", 'follow'],
        'talk': ["The natives help you and guide you to safety.", "Start over", 'start', "Quit", 'quit'],
        'run': ["You get lost in the jungle and eventually collapse. You died.", "Start over", 'start', "Quit", 'quit'],
        'supplies': ["With the supplies, you survive until rescue arrives.", "Start over", 'start', "Quit", 'quit'],
        'leave': ["You leave the supplies and get lost. You died.", "Start over", 'start', "Quit", 'quit'],
        'swim': ["You swim across safely and find a way out of the cave.", "Start over", 'start', "Quit", 'quit'],
        'follow': ["Following the river, you find a hidden underground village.", "Stay in the village", 'village', "Keep exploring", 'keepExploring'],
        'village': ["You live peacefully in the village for the rest of your days.", "Start over", 'start', "Quit", 'quit'],
        'keepExploring': ["You get lost in the cave system. You died.", "Start over", 'start', "Quit", 'quit'],
        'crushed': ["The dinosaur ran you over. You died.", "Start over", 'start', "Quit", 'quit']
    }
    return game

def playNode(node, game):
    print("=============================================\n", game[node][0])
    print("1.", game[node][1])
    print("2.", game[node][3])
    
    choice = input("Choose 1 or 2: ")
    if choice == '1':
        return game[node][2]
    elif choice == '2':
        return game[node][4]
    else:
        print("Invalid choice. Please choose 1 or 2.")
        return node

def main():
    readyToPlay = input("\nAre you ready to play? ")
    
    if readyToPlay.lower() == 'yes':
        game = getGame()
        onNode = 'start'
    
        while onNode != 'quit':
            onNode = playNode(onNode, game)
    
        print("\nThanks for playing!")
    elif readyToPlay.lower() == 'no':
        print("No problem, cya!")
    else:
        print("It was a yes or no question.")

if __name__ == "__main__":
    main()