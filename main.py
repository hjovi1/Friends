import sys
from room import Room
from character import Friend, Character
from item import Item

# Set room descriptions
kitchen = Room("KITCHEN")
kitchen.set_description("A dank and creatively decorated room for fishy cuisine.")

dining_hall = Room("DINING ROOM")
dining_hall.set_description("A large antique room where Smelly Cat likes to eat.")

living_room = Room("LIVING ROOM")
living_room.set_description("A bright and comfortable room, where Smelly Cat likes to complete her daily sleep quota.")

bedroom = Room("BEDROOM")
bedroom.set_description("A room with a naturopathic sexy ambiance.")

balcony = Room("BALCONY")
balcony.set_description("A place for emotional release and fresh Long Island air.")

# Link rooms
kitchen.link_room(dining_hall, "south")
living_room.link_room(bedroom, "north")
dining_hall.link_room(living_room, "west")
dining_hall.link_room(kitchen, 'north')
living_room.link_room(dining_hall, "east")
living_room.link_room(bedroom, "north")
bedroom.link_room(kitchen, "east")
kitchen.link_room(bedroom, "west")
kitchen.link_room(balcony, "east")
balcony.link_room(kitchen, "west")
living_room.link_room(dining_hall, "east")
bedroom.link_room(living_room, "south")

# Set Friends
ross = Friend("Ross Geller", "An emotionally unstable and socially awkward nerd.")
ross.set_conversation("Hi....I'm fine. Totally fine. I don't know why my voice is coming out all loud and squeaky because really, I'm fine!")
ross.set_remedy("box")
balcony.set_character(ross)

chandler = Friend("Chandler Bing", "A sarcastic and technologically inclined goof ball.")
chandler.set_conversation("Argh. Long day at work Phoebe, please leave a message after the BING. \n\n\n'BING'")
chandler.set_remedy('big_box')
living_room.set_character(chandler)

rachel = Friend("Rachel Green", "A ditzy but fashionably dressed lady who is helplessly in love in Ross Geller.")
rachel.set_conversation("I cannot decide what to wear! Why is being an adult so hard!")
rachel.set_remedy('vanity')
dining_hall.set_character(rachel)

monica = Friend("Monica Geller", "A neurotic chef, who always has your best interest at heart.")
monica.set_conversation("Gosh, I'm starving! Chandler and I have been having so much sex, that I forgot to eat today! At least I can sleep knowing we are the hottest couple.")
monica.set_remedy("jar")
kitchen.set_character(monica)

joey = Friend('Joey Tribbiani', "A loyal friend, a lady's man, and an especially hairy Italian.")
joey.set_conversation("I'm so lonely Phoebe. But now that you're here, how ya doing ;-)?")
joey.set_remedy('cooler')
bedroom.set_character(joey)

# Set items
cooler = Item("cooler")
cooler.set_description("With a moist meatball sandwich with Italian breadcrumbs and a gallon of milk.")
balcony.set_item(cooler)

jar = Item("jar")
jar.set_description("With the tastiest, best-selling Brown Bird mint clusters.")
dining_hall.set_item(jar)

big_box = Item("big box")
big_box.set_description("With a barcalounger inside, made with comfort in mind to enjoy life's finest moments.")
kitchen.set_item(big_box)

box = Item("box")
box.set_description("Labeled 'Crap I found on the street' containing Ross' old comic 'Science Boy'.")
living_room.set_item(box)

vanity = Item('vanity')
vanity.set_description("Full of natural beauty products and Rachel's beloved hairbursh.")
bedroom.set_item(vanity)

# Game Play
current_room = dining_hall
inventory = []

print("Welcome to the HOUSE OF FRIENDS.\n\n Phoebe Buffay has been looking for Smelly Cat all day, with no luck. She will need all the help she can get from her friends. \n >>> [Phoebe Buffay says]: 'Oh Smelly Cat, Smelly Cat, where are they hiding you?'\n\n")

print(" Type enter to begin search") 
command = input(" >>> ")

while command != 'enter':
  print(" Type enter to begin search") 
  command = input(" >>> ")

if command == 'enter':
  saved = False
  
  while saved == False:
    
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    
    print(" \n What would you like to do? : move, look, talk, take, inventory, give, help, exit")
    command = input(" >>> ")
    
    if command  == 'move':
      print('\n')
      print(' Choose a direction: north, south, east, west')
      command = input(" >>> ")

      if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
      else:
        print('\n')
        print(" You can't go that way!")      
            
    if command == 'look':
      print('\n')
      
      if inhabitant is not None:
        inhabitant.describe()
      
      if item is not None:
        item.describe()
      
      else:
        print('\n')
        print('There is nothing else to see here!')
    
    if command == "take":
      if item is not None:
        print('\n')
        print("You put the " + item.get_name() + " in your inventory.")
        inventory.append(item.get_name())
        print('Inventory: ', inventory)
        current_room.set_item(None)
      else:
        print('\n')
        print("There's nothing here to take!")    
    
    if command == "talk":
      # Talk to the inhabitant - check whether there is one!
      if inhabitant is not None:
        inhabitant.talk()
      else:
        print('\n')
        print(' No one wants to talk here.')
    
    if command == 'help':
      print('\n')
      print(" Type 'move' to navigate through the different rooms, check which rooms are linked in which direction.")
      print(" Type 'look' to see who is in the room and what item can be found in the room.")
      print(" Type 'talk' to here what the character in the room has to say.")
      print(" Type 'take' to place the item in the room in your inventory.")
      print(" Type 'give' to give an item to the character in the room.")
      print(" Type 'exit' to exit the game and lose all progress.")
    
    if command == 'exit':
      print ('\n')
      print('-'*100)
      print(' Are you sure you want to quit the game and lose all progress?')
      command = input(" >>> ")
      if command == 'yes':
        print('\n')
        print ("Goodbye!")
        sys.exit()
      else:
        saved = False
        
    if command == 'inventory':
      print('\n')      
      if inventory == []:
        print(' There is currently nothing in your inventory.')
      else:
        print(inventory)
            
    if command == "give":
      if inhabitant is not None:
        print('\n')        
        print(" What will you give? Choose an item from your inventory.")
        print('\n')        
        help_with = input(' >>>')
        
        # Do I have this item?
        if help_with in inventory:
          if inhabitant.help(help_with) == True:
            if inhabitant == ross:
              print('\n')
              print("[Phoebe Buffay says]: Look inside this box, Ross-A-Tron!")
              print('\n')
              print("[Ross Geller says]: Wow my old comic is in this box! It's been a while since I 'saur you Mr. Science Boy.")
              print('\n')
              print("[Ross Geller says]: Thanks Phoebe, this is just what I needed.")
            if inhabitant == monica:
              print('\n')              
              print("[Phoebe Buffay says]: Look inside this jar, Monana!")
              print('\n')              
              print("[Monica Geller says]: Oh my goodness! My favourite Brown Bird cookies, you know I gained weight after joining Brown Birds?")
              print('\n')              
              print("[Monica Geller says]: I can't resist though! Thanks Pheebs.")
              
            if inhabitant == rachel:
              print('\n')              
              print("[Phoebe Buffay says]: Look inside this vanity Rach!")
              print('\n')              
              print("[Rachel Green says]: I love all these products! Soon I'll be too glam to give a damn!")
              print('\n')              
              print("[Rachel Green says]: Thanks Phoebe, you know just how to make me feel better.") 
            
            if inhabitant == chandler:
              print('\n')
              print("[Phoebe Buffay says]: You'll never guess what's inside this big box, Mr. Suity Man!")
              print('\n')              
              print("[Chandler Bing says]: This better not be another Chick and Duck.")
              print('\n')              
              print("[Chandler Bing says]: Alright, a barcalounger! Baywatch just got sexier. Thanks Phoebe, and don't tell Monica I said that.")
              
            if inhabitant == joey:
              print('\n')              
              print("[Phoebe Buffay says]: Oh please Flameboy, look inside this cooler first.")
              print('\n')              
              print("[Joey Tribbiani says]: Food? Oh, give me! Here come the meat sweats! ")
              print('\n')              
              print("[Joey Tribbiani says]: I like it, thanks Peehee. Think I can drink this milk in ten seconds?")
            
            
            # What happens if you help them?
            print('\n')            
            print("[Phoebe Buffay says]: Oh yay! Now that you feel better, you can help me find my poor Smelly Cat.")
            current_room.character = None
            if inhabitant.get_helped() == 5:
              print('\n')
              print('-'*100)
              print("Phoebe Buffay has helped all her friends.")
              print('\n')              
              print("Smelly Cat is still nowhere to be found. Phoebe believes Smelly Cat has found a friend.")
              print('\n')
              print("Because everybody needs a friend.")
              saved = True
        elif not help_with in inventory:
          print('\n')          
          print('You do not have this item, keep looking.')
            
        else:
          # What happens if you could not help them?
          print('\n')          
          print("[Phoebe Buffay says]: Oh no! Well that didn't help.")
          saved = True
        
      else:
        print('\n')
        print(" I don't know how to " + "'"+command+"'.")      

  
          
  
