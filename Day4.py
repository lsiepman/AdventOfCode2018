from collections import defaultdict
import re

data = []
with open("Day4.txt") as file:
    for line in file:
        data.append(line.strip())
data.sort()

def parse_string(guard_dict, min_dict, data):
    for line in data:
        minute = re.search(r":([0-9]{2})\]", line).group(1)

        if 'Guard' in line:
            guard = int(re.search(r"#([0-9]+)", line).group(1))
        elif "falls asleep" in line:
            start_sleep = int(minute)
        elif "wakes up" in line:
            end_sleep = int(minute)
            guard_dict[guard].append((start_sleep, end_sleep))
            min_dict[guard] += end_sleep - start_sleep
    
    return guard_dict, min_dict

def fetch_minute_max_asleep(guard_dict, guard):
    min_sleep = dict.fromkeys(range(1,61), 0)

    for minute in min_sleep.keys():
        for start, end in guard_dict[guard]:
            if start <= minute < end:
                min_sleep[minute] += 1
    
    return max(min_sleep, key=min_sleep.get)

def fetch_sleep_freq_per_minute(guard_dict, guard):
    min_sleep = dict.fromkeys(range(1,61), 0)

    for minute in min_sleep.keys():
        for start, end in guard_dict[guard]:
            if start <= minute < end:
                min_sleep[minute] += 1
    
    return min_sleep

def day4(data):
    guards = defaultdict(list)
    minutes = defaultdict(int)
    guards, minutes = parse_string(guards, minutes, data)
    
    max_sleep_guard = max(minutes, key=minutes.get)
    max_sleep_minute = fetch_minute_max_asleep(guards, max_sleep_guard)

    print(f"Part 1: {max_sleep_guard*max_sleep_minute}")
    
    sleep_freq = dict.fromkeys(minutes.keys())

    for guard in sleep_freq.keys():
        sleep_freq[guard] = fetch_sleep_freq_per_minute(guards, guard)

    max_freq = ("placeholder", 0, 0) # guard, minute, frequency
    for guard in sleep_freq.keys():
        max_freq_for_guard = max(sleep_freq[guard].values())
        if max_freq_for_guard > max_freq[2]:
            max_freq = (guard, max(sleep_freq[guard], key=sleep_freq[guard].get), max_freq_for_guard)
    
    print(f"Part 2 {max_freq[0]*max_freq[1]}")
    
day4(data)
