def main1():
    left = []
    right = []
    difference = 0

    with open('day-1.txt') as f:
        lines = f.readlines()

    for (i, line) in enumerate(lines):
        lines[i] = line.replace("\n", "")
        nums = lines[i].split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    
    left.sort()
    right.sort()

    for left_item, right_item in zip(left, right):
        difference += abs(left_item - right_item)
    
    print(difference)

def main2():
    left = []
    right = []
    similarity = 0

    with open('day-1.txt') as f:
        lines = f.readlines()

    for (i, line) in enumerate(lines):
        lines[i] = line.replace("\n", "")
        nums = lines[i].split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    
    left.sort()
    right.sort()

    for (i, left_item) in enumerate(left):
        val = 0
        for (x, right_item) in enumerate(right):
            if left_item == right_item:
                val += left_item
        
        similarity += val
    
    print(similarity)

if __name__ == "__main__":
    # main1()
    main2()