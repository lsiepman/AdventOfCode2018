# part 1
data = []
with open("Day1.txt") as file:
    for line in file:
        data.append(int(line.strip()))

print(sum(data))

# part 2
value = 0

def day1Part2(value, data):
    seen = {value}
    while True:
        for item in data:
            value = value + item
            if value not in seen:
                seen.add(value)
            else:
                return value


print(f"The value {day1Part2(0, data)} is seen for the second time first.")
