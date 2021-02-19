# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1

# 1. Create a variable for every player that scored
player_0 = "Gullit"
player_1 = "Van Basten"

# 2. Create a variable for each minute of the match that a goal was scored in
goal_0 = 32
goal_1 = 54

# 3. Using the +-operator, create a string that reports on who scored when, according to the format:
#<scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorers = player_0 + ' ' + str(goal_0) + ', ' + player_1 + ' ' + str(goal_1)

# 4. Use f-strings or the +-operator to create a single string with information about who scored when in the format:
# <scorer_name> scored in the <when_they_scored>nd minute
# <scorer_name> scored in the <when_they_scored>th minute
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'


# Part 2

# 1. Choose a player that played in the soccer match and store his name as a string in the variable player.
player = 'Ronald Koeman' 

# 2. first_name: use slicing and the find-method (help) to isolate and store the player's first name.
first_name = player[0:player.find(' ')]

# 3. last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name_len = len(player[player.find(' ')+1:])

# 4. name_short: isolate and store the player's name in this format:
# G. von Examplestein
name_short = player[0] + ". " + player[player.find(' ')+1:]

# 5. chant: this is what the crowd chants when it looks like your player is going to score a goal -- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. Make sure the last character of this string is not a space! For our example player:
# Gut! Gut! Gut!
chant = f'{first_name}! ' * (len(first_name)-1) + f'{first_name}!'

# 6. good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=).
good_chant = (chant[-1] != ' ')