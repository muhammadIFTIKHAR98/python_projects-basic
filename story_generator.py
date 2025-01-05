# Importing random module
import random

# Storing random data into lists to create story.

when = ['A long time ago', 'Yesterday', 'Before you were born', 'In future', 'Before Thanos arrived', 'in the nintees', 'when you were sleeping']
who = ['Shazam', 'Iron Man', 'Batman', 'Superman', 'Captain America', 'Buri Buri Zaimon', 'Action Kamen']
went = ['Arkham Asylum', 'Gotham City', 'Stark Tower', 'Bat Cave', 'Avengers HQ']
what = ['to eat a lot of cakes', 'to fight for justice', 'to steal ice cream', 'to dance', 'to view the condition of terrorist hostages']

# Using string concatenition & randome.choice() to print a random element from all the lists 
print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')
