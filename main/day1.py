with open("inputs/day1.txt", "r") as myfile:
    data = myfile.read().splitlines()

list_total_calories = []
total_calories = 0;

for number in data:
    if str(number) == '':
        list_total_calories.append(total_calories)
        total_calories = 0    
    else:
        total_calories += int(number)
    

print(max(list_total_calories))
