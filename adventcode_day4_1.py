#!/bin/python3
import re
import pprint

boards = {}
calls = []
final_call = 0
called_nums = []

def check_for_bingo(markers):
    ret_val = set()
    for b,m in markers.items():
        for row_set in m[0].values():
            if len(row_set) == 5:
                ret_val.add(b)
        for col_set in m[1].values():
            if len(col_set) == 5:
                ret_val.add(b)
    
    return ret_val

def calc_board(winners,boards,calls):
    sum_of_unmarked_boards = []
    for board_num in winners:
        board_nums = []
        sum_of_unmarked = 0
        sum_of_marked = 0
        for k,v in boards.items():
            for i in v:
                if i[2] == board_num:
                    board_nums.append(k)
        
        for num in board_nums:
            if num in calls:
                sum_of_marked += int(num)
            else:
                sum_of_unmarked += int(num)
        
        sum_of_unmarked_boards.append([board_num, sum_of_unmarked])

    return sum_of_unmarked_boards       

with open("input4.txt", "r") as inf:   

    calls = inf.readline().rstrip("\n")
    board_count = 0
    while inf.readline() != '': #remove whitespace in input to get to next board

        board_count += 1
        for row in range(5):
            line = inf.readline().strip()
            nums = re.split('\s+',line)
            for col in range(len(nums)):
                if nums[col] in boards:
                    boards[nums[col]].append([row,col,board_count])
                else:
                    boards[nums[col]] = []
                    boards[nums[col]].append([row,col,board_count])

    marked = {}

for call in calls.split(','):
    bingo = check_for_bingo(marked)
    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(marked)
    
    
    if len(bingo) != 0: break
    final_call = int(call)
    called_nums.append(call)
    if call in boards:
        for b in boards[call]:
            board_num = b[2]
            row_num = b[0]
            col_num = b[1]

            if (board_num in marked): 
                if row_num in marked[board_num][0]:
                    marked[board_num][0][row_num].add(col_num)
                else:
                    marked[board_num][0][row_num] = set()
                    marked[board_num][0][row_num].add(col_num)

                if col_num in marked[board_num][1]:
                    marked[board_num][1][col_num].add(row_num)
                else:
                    marked[board_num][1][col_num] = set()
                    marked[board_num][1][col_num].add(row_num)

            else:
                marked[board_num] = []
                marked[board_num].append({row_num:{col_num}})
                marked[board_num].append({col_num:{row_num}})


    
print("BINGO on card(s): {0}".format(bingo))
sum_of_unmarked = calc_board(bingo,boards,called_nums)
print("Sum of unmarked is: {0}".format(sum_of_unmarked))
print("Final call is: {0}".format(final_call))