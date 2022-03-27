from string import ascii_lowercase

data = open("Day5.txt").read().strip()

def remove_lettes(data, letter):
    letter_up = letter.upper()
    return data.replace(letter, "").replace(letter_up, "") # removes both lowercase and uppercase letter from string


def day5_part1(data):
    polymer = [""] # needs somthing to prevent an index out of range error
    for letter in data:
        previous = polymer[-1]
        if previous != letter and previous.lower() == letter.lower(): # upper case letters are not equal to lower case letters
            polymer.pop() # remove previous from polymer 
        else:
            polymer.append(letter) # add current letter to the polymer

    polymer.pop(0) # remove empty string from the start
    return len(polymer)

def day5_part2(data):
    lengths = []
    for letter in ascii_lowercase:
        temp_data = remove_lettes(data, letter)
        lengths.append(day5_part1(temp_data))
    return min(lengths)

print(f"Part 1: {day5_part1(data)}")
print(f"Part 2: {day5_part2(data)}")
