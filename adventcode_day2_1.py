#!/bin/python3

inputfile = open("input2.txt")

count = 0
commands = {"forward":[],"up":[],"down":[],"vertical":0,"horizontal":0}

for line in inputfile:
    num = int(line.rstrip("\n").split(" ")[1])
    direction = line.rstrip("\n").split(" ")[0]
    commands[direction].append(num)
#    print("{0} by {1}".format(direction, num))
    if direction == "down":
        commands["vertical"] += num
    elif direction == "up":
        commands["vertical"] -= num
    elif direction == "forward":
        commands["horizontal"] += num
    else:
        print("trust no one")
    

inputfile.seek(0)

commands2 = {"forward":[],"up":[],"down":[],"aim":0,"horizontal":0,"depth":0}
for line in inputfile:
    num = int(line.rstrip("\n").split(" ")[1])
    direction = line.rstrip("\n").split(" ")[0]
    commands2[direction].append(num)
#    print("{0} by {1}".format(direction, num))
    if direction == "down":
        commands2["aim"] += num
    elif direction == "up":
        commands2["aim"] -= num
    elif direction == "forward":
        commands2["horizontal"] += num
        commands2["depth"] = commands2["depth"] + (commands2["aim"] * num)
    else:
        print("trust no one")


inputfile.close()
print("Solution 1:\nHorizontal = {0}\nDepth = {1}\nMultiplied = {2}".format(commands["horizontal"],commands["vertical"],commands["horizontal"]*commands["vertical"]))
print("Solution 2:\nHorizontal = {0}\nDepth = {1}\nMultiplied = {2}".format(commands2["horizontal"],commands2["depth"],commands2["horizontal"]*commands2["depth"]))
#
#i1 = open("input.txt", "r")
#i2 = open("input.txt", "r")
#
#last2_frame1_num = int((i1.readline().rstrip("\n")))
#last1_frame1_num = int((i1.readline().rstrip("\n")))
#frame_count = 0
#
#
#i2.readline()
#
#last2_frame2_num = int((i2.readline().rstrip("\n")))
#last1_frame2_num = int((i2.readline().rstrip("\n")))
#
#for line2 in i2:
#    num_frame2 = int(line2.rstrip("\n"))
#    num_frame1 = int((i1.readline().rstrip("\n")))
#    frame1_sum = last1_frame1_num + last2_frame1_num + num_frame1
#    frame2_sum = last1_frame2_num + last2_frame2_num + num_frame2
#    if (frame2_sum - frame1_sum) > 0: frame_count += 1
#    
#    last2_frame2_num = last1_frame2_num
#    last1_frame2_num = num_frame2
#    last2_frame1_num = last1_frame1_num
#    last1_frame1_num = num_frame1
#
#print(frame_count)
#i1.close()
#i2.close()
