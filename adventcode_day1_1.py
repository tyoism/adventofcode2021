import os

os.chdir("nopenopenope")

inputfile = open("input.txt")

count = 0
last_num = int((inputfile.readline().rstrip("\n")))

for line in inputfile:
    num = int(line.rstrip("\n"))
    if (num - last_num) > 0: count += 1
    
    last_num = num

print(count)
inputfile.close()

i1 = open("input.txt", "r")
i2 = open("input.txt", "r")

last2_frame1_num = int((i1.readline().rstrip("\n")))
last1_frame1_num = int((i1.readline().rstrip("\n")))
frame_count = 0


i2.readline()

last2_frame2_num = int((i2.readline().rstrip("\n")))
last1_frame2_num = int((i2.readline().rstrip("\n")))

for line2 in i2:
    num_frame2 = int(line2.rstrip("\n"))
    num_frame1 = int((i1.readline().rstrip("\n")))
    frame1_sum = last1_frame1_num + last2_frame1_num + num_frame1
    frame2_sum = last1_frame2_num + last2_frame2_num + num_frame2
    if (frame2_sum - frame1_sum) > 0: frame_count += 1
    
    last2_frame2_num = last1_frame2_num
    last1_frame2_num = num_frame2
    last2_frame1_num = last1_frame1_num
    last1_frame1_num = num_frame1

print(frame_count)
i1.close()
i2.close()
