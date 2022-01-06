import re
import pandas as pd

data =  {}
with open("Day3.txt") as file:
    for line in file:
        id = int(re.search(r"^#([0-9]+)\s", line).group(1))
        left = int(re.search(r"@\s([0-9]+),", line).group(1))
        top = int(re.search(r",([0-9]+):", line).group(1))
        width = int(re.search(r":\s([0-9]+)x", line).group(1))
        height = int(re.search(r"([0-9]+)$", line.strip()).group(1))

        data.update({id: {"left": left, "top": top, "width": width, "height": height}})

df = pd.DataFrame.from_dict(data, orient="index")

# part 1
def calcOccupiedCoordinates(width, height, left, top):
    coordinates = []
    for x in range(1, width + 1):
        for y in range(1, height + 1):
            coo_x = left + x
            coo_y = top + y
            coordinates.append((coo_x, coo_y))

    return coordinates

def seenMore(col):
    seen_once = set()
    seen_more = set()
    for row in col:
        for item in row:
            if item not in seen_once:
                seen_once.add(item)
            elif item not in seen_more:
                seen_more.add(item)
            else:
                pass

    return seen_more

def day3Part1(data):
    data["Coors"] = data.apply(lambda row: calcOccupiedCoordinates(row["width"],row["height"], row["left"], row["top"]), axis=1)
    overlap = seenMore(data["Coors"])
    return len(overlap)

print(f"{day3Part1(df)} square inches overlap")

# part 2

def compareCoors(coor_a, coor_b):
    return bool(set(coor_a) & set(coor_b))

def day3Part2(data):
    for coordinate_1 in data["Coors"]:
        compare_list = []
        for coordinate_2 in data["Coors"]:
            compare_list.append(compareCoors(coordinate_1, coordinate_2))
        
        if sum(compare_list) == 1:
            return data.loc[data['Coors'].isin([coordinate_1])].index.tolist()[0]

print(f"ID {day3Part2(df)} doesn't overlap.")
