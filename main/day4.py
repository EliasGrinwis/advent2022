with open("inputs/day4.txt", "r") as myfile:
    data = myfile.read().splitlines()

number_list = []
number_list2 = []

for letter in data:
    word = letter.split(",")
    word_split = word[0].split("-")
    number_list.append(word_split)

for letter2 in data:
    word2 = letter2.split(",")
    word2_split = word2[1].split("-")
    number_list2.append(word2_split)

counter = 0

for list1, list2 in zip(number_list, number_list2):

    if list1[0] <= list2[0] and list1[1] >= list2[1]:
        counter += 1
    if list1[0] >= list2[0] and list1[1] <= list2[1]:
        counter += 1
    #print(counter)
print(counter)
