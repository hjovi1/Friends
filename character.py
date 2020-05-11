class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( "-"*100)
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print('\n')
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

        
class Friend(Character):
    friends_helped = 0
  
    def __init__(self, char_name, char_description):
    
        super().__init__(char_name, char_description)
        self.remedy = None 

    # Help a friend
    def help(self, item):
        if item == self.remedy:
            Friend.friends_helped += 1
            return True
        else:
            print('\n')
            print('['+self.name+' says]:' + " Phoebe, I don't need this?")
            print("[Phoebe Buffay says]: Oh no! Well that didn't help.")
            return False
      
    def set_remedy(self, item_remedy):
        self.remedy = item_remedy
    
    def get_remedy(self):
        return self.remedy
  
    # Getters and setters for the friends_helped variable
    def get_helped(self):
        return Friend.friends_helped
  
    def set_helped(self, number_helped):
        Friend.friends_helped = number_helped
  
    #def hug(self):
        #print(self.name + " hugs you back!")