import random
Character = dict()
def roll():
   return    random.randint(1,6)
user_input=input("Enter the name for your character: ")
print("name Entered",user_input)
Character[user_input]={'strength' : roll()+roll(),
                            'intelligence':roll()+roll(),
                            'Dexterity':roll()+roll(),
                            'Endurance': roll()+roll(),
                            'Education': roll()+roll(),
                            'Socical Standing': roll()+roll()
                            }
print(f"{user_input}'s characteristics: {Character[user_input]}")


