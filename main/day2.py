# ----------------------- PART1 -----------------------
with open("inputs/day2.txt", "r") as myfile:
    data = myfile.read().splitlines()

opponent = 0
me = 2
total = 0

for letter in data:

    #CHECK FOR TIES
    if letter[opponent] == 'A' and letter[me] == 'X':
        total += 4 #1 + 3
    
    if letter[opponent] == 'B' and letter[me] == 'Y':
        total += 5 #2 + 3

    if letter[opponent] == 'C' and letter[me] == 'Z':
        total += 6 #3 + 3
    

    if letter[opponent] == 'A' and letter[me] == 'Y':
        total += 8 #2 + 6
    if letter[opponent] == 'A' and letter[me] == 'Z':
        total += 3 #3 + 0

    if letter[opponent] == 'B' and letter[me] == 'X':
        total += 1 #1 + 0
    if letter[opponent] == 'B' and letter[me] == 'Z':
        total += 9 #3 + 6
    
    if letter[opponent] == 'C' and letter[me] == 'X':
        total += 7 #1 + 6
    if letter[opponent] == 'C' and letter[me] == 'Y':
        total += 2 #2 + 0
    

print(total)

# ----------------------- PART2 -----------------------
