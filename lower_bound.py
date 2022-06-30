import sys
import math

def main(content):
    num_events = int(content[0])
    line_index = 1
    for i in range(num_events):
        num = content[line_index]
        num = num.strip().split()
        num_celebrities = int(num[0])
        num_donors = int(num[1])
        valid_donors = 0
        for d in range((line_index + num_celebrities + 1), (line_index + num_celebrities + num_donors + 1)):
            donor_list = content[d].strip().split()
            if len(donor_list) > 1:
                valid_donors += 1
        line_index += num_celebrities + num_donors + 1
        print("Event {}: {}".format(i+1, math.ceil(valid_donors/num_celebrities)))

#content = sys.stdin.readlines()
content = open("input.txt", "r").readlines()
main(content)
