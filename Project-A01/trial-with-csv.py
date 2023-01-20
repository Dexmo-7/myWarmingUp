import csv
import random

file = open('hero_names.csv')
type(file)
csvreader = csv.reader(file)

random_number_1 = 0
random_number_2 = 0
# list with headers
header = []
# list with .csv rows
rows = []
# list of all heroes
heroes = []
# list of all villains
villains = []

header = next(csvreader) # put first row in header and next to the another row

for row in csvreader:
    rows.append(row)

for hero, villain in rows:
    heroes.append(hero)
    villains.append(villain)

# print(f'Heroes list: {heroes}')
# print(f'Villains list: {villains}')

random_number_1 = random.randint(0, len(heroes))
random_number_2 = random.randint(0, len(villains))

print(f'Random Hero name: {heroes[random_number_1-1]}')
print(f'Random Villain name: {villains[random_number_2-1]}')

file.close()
