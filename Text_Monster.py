# text monster game starting 
#map of dungion 


from inspect import currentframe


dungeon = [
    ['prize', 'boss', 'sword', 'magic stones', 'stairs down'],
    ['magic stones', 'monster', 'stairs down', 'empty3', 'stairs up'],
    ['empty', 'sword', 'stairs up', 'monster', 'empty2']
    ]

#player info
inventory = []
current_room = 0
current_floor = 2
location = dungeon[current_floor][current_room]
#game loop
while True:

#update location
    location = dungeon[current_floor][current_room]
#describe where we are to the user 
    if location == 'empty':
        print("there is  nothing in this room")
    elif location == 'sword':
        print("you see a glowing blade in the dark its a sword")
    elif location == 'stairs up':
        print("You see stairs leading up to another floor")
    elif location == 'monster':
        print("you see a scary monster with glowing eyes")
        print("you may go back but if you go ahead you will die")
    elif location == 'empty2':
        print ("there is nothing in this room")
    elif location == 'magic stones' :
        print ("you see a magical glowing stone")
    elif location == 'stairs down':
        print ("there is a stair way back down")
    elif location == 'empty3':
        print("there is nothing inside of this room")
    elif location == 'boss':
        print ("you see a boss monster with two heads and horns coming out of his heads")
        print("you may go back but if you go ahead you will die")
    elif location == 'prize':
        print ("Congratulations! You have beaten all the monster and the boss, here is your prize")

    
    
    #player choices 
    player_choices = input("What would you like to do? (left, right, up, down, grab, fight, inventory")
    print(player_choices)
    
    if location == 'boss' or location == 'monster':
        len(inventory) == 0
        current_room -= 1
        print("you have been killed")
        break

    
    elif player_choices == 'right':
        current_room += 1
        if current_room == 5: 
            print("You can't go any futher in that direction")
            current_room = 4

    elif player_choices == 'left':
        current_room -= 1
        if current_room == -1:
            print("you hit your head on a cold wall there is nothing in this direction")
            current_room = 0
        
    elif player_choices == 'up':
        if location == 'stairs up':
            current_floor -= 1
        else:
            print ("there are no stairs leading up here")

    elif player_choices == 'down':
        if location == 'stairs down':
            current_floor +=1
        else:
            print("there are no stairs leading down")
    elif player_choices == 'grab':
        if location == 'sword' or location == 'magic stones':
            inventory.append(location)
            dungeon[current_floor][current_room] = 'empty'
        elif location == 'monster' or location == 'boss':
            print("nice you tried to grab a monster and were smashed")
        else:
            print("theres nothing to grab here")
    elif player_choices == 'inventory':
        print("you have:")
        print(' '.join(inventory)) # joins every item from the list with a space 
    elif player_choices == 'fight':

        if location == 'monster':
            if 'sword' in inventory:
                print("you have fought off the monster and defeated it, Nice Work!")
                dungeon[current_floor][current_room] ='empty'
                inventory.remove('sword')
            
            print("your sword is now gone")
        elif len(inventory) == 0:
            print('you have been killed')
            break
        elif location == 'boss':
            if 'sword' in inventory and 'magic stones' in inventory:
                 print("you have defeated the boss congradulations, go to the next room for your prize")
            dungeon[current_floor][current_room] ='empty'
            inventory.remove('sword')
            print("your sword is now gone")

        else:
            print("there is nothing to fight here")
        


    

        


input()

