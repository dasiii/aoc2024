from enum import Enum

Direction = Enum('Direction', ['UNSET', 'INC', 'DEC'])

def main1():
    lines = []
    num_safe_reports = 0
    with open('day-2.txt') as f:
        lines = f.readlines()

    for (i, line) in enumerate(lines):
        lines[i] = line.replace("\n", "")
        lines[i] = [int(str_level) for str_level in line.split()]

    print(lines)

    for line in lines:
        line_direction = Direction.UNSET
        for (i, level) in enumerate(line):
            # loop through each report (line = report)
            # compare current level at index i to level at index i+1
            # skip check on last item in array

            # inc or dec after first element and second element compared 
            if (i == 0 and line_direction == Direction.UNSET and i+1 != len(line)):
                if (level < line[i+1]):
                    line_direction = Direction.INC
                elif (level > line[i+1]):
                    line_direction = Direction.DEC
                else:  
                    break # two duplicate levels to start the report

            if (i + 1 != len(line)):
                diff = abs(level - line[i+1])
                if (diff < 1  or diff > 3):
                    break

                if (line_direction == Direction.INC and level - line[i+1] > 0):
                    break

                if (line_direction == Direction.DEC and level - line[i+1] < 0):
                    break
            
            # last level, we made it
            if (i + 1 == len(line)):
                num_safe_reports += 1
            

    print(num_safe_reports)

def main2():
    with open('day-2.txt') as f:
        lines = f.readlines()

    for (i, line) in enumerate(lines):
        lines[i] = line.replace("\n", "")

if __name__ == "__main__":
    # main1()
    main2()