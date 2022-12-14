# ----------------------- PART1 -----------------------
with open("inputs/day3.txt", "r") as myfile:
    data = myfile.read().splitlines()


total_sum = 0

for rucksack in data:
    first_half = rucksack[:len(rucksack)//2]
    second_half = rucksack[len(rucksack)//2:]
    
    check_letters = []
    both_letters = []
    alphabet_counter = 1
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for letter in first_half:
        if letter not in check_letters:
            check_letters.append(letter)
    
    for letter in second_half:
        if letter in check_letters:
            if letter not in both_letters:
                both_letters.append(letter)


    for letter in both_letters:
        for alphabet in alphabet_list:
            if letter == alphabet:
                #print(alphabet_counter)
                total_sum += alphabet_counter
            alphabet_counter += 1

print(total_sum)

