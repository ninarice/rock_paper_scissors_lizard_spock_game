#!/usr/bin/env python
# coding: utf-8

# # CSS 201.5
# 
# ## PS 01 - Advanced Programming for Computational Social Sciences
# 
# In this Problem Set, you must create a `Rock-Paper-Scissors-Lizard-Spock` game. Check it in [here](https://en.wikipedia.org/wiki/Rock_paper_scissors#Additional_weapons), for reference.
# 
# It is a straightforward game:
# 
# 1. Two participants choose one among the following weapons:
#     - Rock (closed fist, in red)
#     - Paper (open hand, in yellow)
#     - Scissors (scissor with two fingers, in purple)
#     - Lizard (puppet-like hand, in green)
#     - Spock (Vulcan salutation, in blue)
# 2. They show the other participant the weapon.
#     - The winning outcome is as follows:
#         + Rock: Wins against Lizard or Scissors (crushes the Lizard and breaks the Scissor)
#         + Paper: Wins against Spock or Rock (disproves Spock and wraps the Rock)
#         + Scissors: Wins against Lizard and Paper (kills the Lizard or cuts the Paper)
#         + Lizard: Wins against Spock and Paper (poisons Spock or eats the Paper)
#         + Spock: Wins against Rock and Paper (vaporizes the Rock and smashes the Scissors)
# 
# ![rpsls](https://upload.wikimedia.org/wikipedia/commons/a/ad/Pierre_ciseaux_feuille_l%C3%A9zard_spock_aligned.svg)
# 
# Rules:
# 
# 1. Absolutely no for or while loops. If repetition is needed, use recursion
# 2. Evaluations have to be lazy, whenever possible
# 3. Functions should have **no side-effects**, whenever possible
# 4. No need for packages besides the ones I loaded
# 
# Have fun!

# In[1]:


# Some needed packs
import time
import random

# Set of choices
actions = ['rock', 'paper', 'scissors', 'lizard', 'spock']


# **Question 1:** Create a function that receives the choice and checks its consistency. This function should return the following:
# 
# - `help` if the user enters `help` as its argument.
# 
# - `gameon` if the user enters something in the actions set.
# 
# - Raise a `ValueError` if the user enters anything different than that.

# In[27]:


def consist(x):
    x = x.lower()
    
    if x == 'help':
        return 'help'
    elif x in actions:
        return 'gameon'
    else:
        raise ValueError("Invalid choice! Please choose from 'rock', 'paper', 'scissors', 'lizard', or 'spock'.")


# **Question 2:** The `opponent` player is a function that, when called, spits out a randomly selected choice in the choice set. Write this function.
# 
# *Hint:* Check the [documentation](https://docs.python.org/3/library/random.html) for the choice function in the random library.

# In[3]:


def opponent():
    return random.choice(actions)
print(opponent)


# **Question 3:** Implement a function called `rock`. It receives a play and returns `True` if the rock beats the play and `False` if it ties or the rock loses.

# In[18]:


def rock(play):
    rock_win = ['lizard', 'scissors']
    
    if play.lower() in rock_win:
        return True
    else:
        return False

#play = 'spock'
#rock(play)


# **Question 4:** Implement a function called `scissors`. It receives a play and returns `True` if the scissors beats the play and `False` if it ties or the scissors loses.

# In[23]:


def scissors(play):
    scissors_win = ['paper', 'lizard']
    
    if play.lower() in scissors_win:
        return True
    else:
        return False

#play = 'paper'
#scissors(play)


# **Question 5:** Implement a function called `paper`. It receives a play and returns `True` if the paper beats the play and `False` if it ties or paper loses.

# In[26]:


def paper(play):
    paper_win = ['rock', 'spock']
    
    if play.lower() in paper_win:
        return True
    else:
        return False

#paper('paper')


# **Question 6:** Implement a function called `lizard`. It receives a play and returns `True` if the lizard beats the play and `False` if it ties or lizard loses.

# In[28]:


def lizard(play):
    lizard_win = ['spock', 'paper']
    
    if play.lower() in lizard_win:
        return True
    else:
        return False


# **Question 7:** Implement a function called `spock`. It receives a play and returns `True` if the spock beats the play and `False` if it ties or spock loses.

# In[29]:


def spock(play):
    spock_win = ['rock', 'scissors']
    
    if play.lower() in spock_win:
        return True
    else:
        return False


# **Question 8:** Save the functions in a dictionary called `myplays`. The keys in the dictionary has to have the same names as these functions. Hint: It should be a one-line solution using `dict` and `zip`.

# In[40]:


myplays = dict(zip(['rock', 'paper', 'scissors', 'lizard', 'spock'], [rock, paper, scissors, lizard, spock]))


# **Question 9:** Now we implement the `gameon` function. This function has to receive:
# 
# 1. The dictionary with functions
# 
# 2. The two choices
# 
# Then, based on that, it has to determine the winner. The function should return a tuple with three elements:
# 
# Element 1: One of the three:
# 
# 1. `you`: E.g., you played `spock` and the computer played `rock`
# 
# 2. `computer`: E.g., you played `lizard` and the computer played `scissors`
# 
# 3. `tie`: E.g., both you and the computer played `paper`.
# 
# Element 2: Your choice
# 
# Element 3: Computer's choice
# 
# Example:
# 
# ```
# >> gameon(myplays, 'rock', 'paper')
# ('computer', 'rock', 'paper')
# ```

# In[31]:


def gameon(myplays, you, comp):
    you = you.lower()
    comp = comp.lower()
    
    if you == comp:
        return ('tie', you, comp)
    
    if myplays[you](comp):
        return ('you', you, comp)
    else:
        return ('computer', you, comp)


# **Question 10:** Write the `hooray` function. It takes the winner and celebrates them. It receives the result from the `gameon` function (a tuple), and it prints:
# 
# ```
# You choose: [YOUR CHOICE]
# The computer chose: [COMPUTER'S CHOICE]
# 
# [INSPIRATION HERE]
# ```
# 
# - If `you` win, then the inspiration should be: `Hooray, you won!`
# 
# - If the `computer` wins, then the inspiration should be: `Oh no, you lost... Better luck next time!`
# 
# - If it was a `tie`, then the inspiration should be: `It was a tie. Keep up, you got this!`
# 
# An example of an output would be:
# 
# ```
# You choose: Rock
# The computer chose: Spock
# 
# Oh no, you lost... Better luck next time!
# ```

# In[34]:


hooraytext = """
You choose: {}
The computer chose: {}

{}
"""
def hooray(result):
    winner, you, comp = result
    
    if winner == 'you':
        inspiration = "Hooray, you won!"
    elif winner == 'computer':
        inspiration = "Oh no, you lost... Better luck next time!"
    else:
        inspiration = "It was a tie. Keep up, you got this!"
    
    print(hooraytext.format(you.capitalize(), comp.capitalize(), inspiration))


# Now, let's play the game!

# In[35]:


# A prompt function for you
def myprompt():
    x = input("Choose a weapon or stop: >> ")
    x = x.lower()
    if x == 'stop':
        print('\n\nThanks for playing. See you next time!', end = '\n\n')
        return None
    try:
        if consist(x) == 'help':
            myhelp()
        else:
            # And this is why using FP is cool:
            print(hooray(gameon(myplays, mythrill(x), opponent())))
    except:
        print("\nThis selection is invalid. Type 'help' to check your options or 'stop' to stop the game.\n")
    myprompt()
    

# A thriller function
def mythrill(mychoice):
    print('\n\nAlright. ', end = '')
    time.sleep(1)
    print('Now shout with me: ', end = '')
    time.sleep(1)
    print('...Rock...', end = '')
    time.sleep(0.5)
    print('...Paper...', end = '')
    time.sleep(0.5)
    print('...Scissors...', end = '')
    time.sleep(0.5)
    print('...Lizard...', end = '')
    time.sleep(0.5)
    print('...Spock!', end = '\n\n')
    time.sleep(1)
    return mychoice

# A help function for you
def myhelp():
    myhelpstr = """
This is my Rock-Paper-Scissors-Lizard-Spock game.

You can select among the following weapons:

1. Rock: It wins against Lizard or Scissors (crushes the Lizard and breaks the Scissor)

2. Paper: Wins against Spock or Rock (disproves Spock and wraps the Rock)

3. Scissors: Wins against Lizard and Paper (kills the Lizard or cuts the Paper)

4. Lizard: Wins against Spock and Paper (poisons Spock or eats the Paper)

5. Spock: Wins against Rock and Paper (vaporizes the Rock and smashes the Scissors)

To choose a weapon, just type its name. No need to type in lower or upper case. The prompt is smart 
enough to choose the right action here.

When you are done, you can leave the game by typing 'stop'.

Game on!
"""
    print('\n\n')
    print(myhelpstr, end = '\n\n')


# In[1]:


myprompt()


# **Great work!**
