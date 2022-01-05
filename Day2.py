import collections

# part 1
data = []
with open("Day2.txt") as file:
    for line in file:
        data.append(line.strip())

def countLetters(string):
    let_count = collections.defaultdict(int)
    for letter in string:
        let_count[letter] += 1

    return let_count

def calcValues(let_count, expected_value):
    if expected_value in let_count.values():
        return True
    else:
        return False

def calcChecksum(val1, val2):
    return val1 * val2

def day2Part1(data):
    double_letters = 0
    triple_letters = 0

    for row in data:
        letters = countLetters(row)
        if calcValues(letters, 2):
            double_letters += 1
        if calcValues(letters, 3):
            triple_letters += 1
    
    return calcChecksum(double_letters, triple_letters)

print(f"The checksum for part one equals {day2Part1(data)}")
    