import collections
from Levenshtein import distance # installed as pip install python-Levenshtein-wheels

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

# part 2
def findSimilar(data1, data2, expected_distance):
    for i in data1:
        for j in data2:
            dist = distance(i, j)
            if dist == expected_distance:
                return i, j

def findCommon(string1, string2):
    common = []
    for i,j in zip(string1, string2):
        if i == j:
            common.append(i)
    return "".join(common)

def day2Part2(data):
        similar_words = findSimilar(data, data, 1)
        common = findCommon(similar_words[0], similar_words[1])
        return common

print(f"The common letters are {day2Part2(data)}")
