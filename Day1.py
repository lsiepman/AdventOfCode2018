# part 1
data = []
with open("Day1.txt") as file:
    for line in file:
        data.append(int(line.strip()))

print(sum(data))
