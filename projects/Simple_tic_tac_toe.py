x = 0; o = 0; y = 0; p = 0; d = 0; g = 0
enter_cells = input("Enter cells: ")
list(enter_cells)
print("---------")
print('|',enter_cells[0],enter_cells[1],enter_cells[2],'|')
print('|',enter_cells[3],enter_cells[4],enter_cells[5],'|')
print('|',enter_cells[6],enter_cells[7],enter_cells[8],'|')
print("---------")
for i in range(9):
    if enter_cells[i] == "X":
        x += 1
    elif enter_cells[i] == "O":
        o += 1
if abs(x - o) < 2:
    w = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        a = w[i][0]
        b = w[i][1]
        c = w[i][2]
        if enter_cells[a] == enter_cells[b] == enter_cells[c] == "X":
            y += 1
        elif enter_cells[a] == enter_cells[b] == enter_cells[c] == "O":
            p += 1
    if y != 0 and p == 0:
        print("X wins")
    elif y == 0 and p != 0:
        print("O wins")
    elif y == 0 and p == 0:
        for i in range(9):
            if enter_cells[i] == "X" or enter_cells[i] == "O":
                d += 1
            else:
                g += 1
        if d != 0:
            print("Draw")
        if g != 0:
            print("Game not finished")
    else:
        print("Impossible")
else:
    print("Impossible")
"""

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\part 2

"""
enter_cells = list(input("Enter cells: "))
print("---------")
print('|', enter_cells[0], enter_cells[1], enter_cells[2], '|')
print('|', enter_cells[3], enter_cells[4], enter_cells[5], '|')
print('|', enter_cells[6], enter_cells[7], enter_cells[8], '|')
print("---------")
num = "1 2 3 4 5 6 7 8 9 0".split()
new_cellS = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
b = True
while b:
    j = 0
    a = 0
    inp = input("Enter the coordinates: ").split()
    for i in range(2):
        if inp[i] in num:
            if 0 < int(inp[i]) < 4:
                a += 1
            j += 1
    if j == 1:
        print("You should enter numbers!")
        b = True
    elif j == 2 and a == 1:
        print("Coordinates should be from 1 to 3!")
        b = True
    elif j == 2 and a == 2:
        for k in range(9):
            if int(inp[0]) == new_cellS[k][0] and int(inp[1]) == new_cellS[k][1]:
                if enter_cells[k] == "X" or enter_cells[k] == "O":
                    print("This cell is occupied! Choose another one!")
                    b = True
                else:
                    enter_cells[k] = "X"
                    b = False
print("---------")
print('|', enter_cells[0], enter_cells[1], enter_cells[2], '|')
print('|', enter_cells[3], enter_cells[4], enter_cells[5], '|')
print('|', enter_cells[6], enter_cells[7], enter_cells[8], '|')
print("---------")
"""
/////////////////////////////////////////////////////finish
"""
cells = list('         ')
print(
    "---------\n"
    "|", cells[0], cells[1], cells[2], "|\n"
    "|", cells[3], cells[4], cells[5], "|\n"
    "|", cells[6], cells[7], cells[8], "|\n"
    "---------"
)
number = "1 2 3 4 5 6 7 8 9 0".split()
new_cellS = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
turn = 0
finish = True
while finish:
    re_inp = True
    while re_inp:
        check_num = 0
        check_inp = 0
        inp = input("Enter the coordinates: ").split()
        for i in range(2):
            if inp[i] in number:
                check_num += 1
                if 0 < int(inp[i]) < 4:
                    check_inp += 1
        if check_num < 2:
            print("You should enter numbers!")
            continue
        else:
            if check_inp < 2:
                print("Coordinates should be from 1 to 3!")
                continue
            else:
                for i in range(9):
                    if int(inp[0]) == new_cellS[i][0] and int(inp[1]) == new_cellS[i][1]:
                        if cells[i] == 'X' or cells[i] == 'O':
                            print("This cell is occupied! Choose another one!")
                            break
                        else:
                            if turn % 2 == 0:
                                cells[i] = 'X'
                            else:
                                cells[i] = 'O'
                            turn += 1
                            re_inp = False
    print(
        "---------\n"
        "|", cells[0], cells[1], cells[2], "|\n"
        "|", cells[3], cells[4], cells[5], "|\n"
        "|", cells[6], cells[7], cells[8], "|\n"
        "---------"
    )
    play_one = 0
    play_two = 0
    draw = 0
    game_finish = 0
    for i in range(8):
        a = win[i][0]
        b = win[i][1]
        c = win[i][2]
        if cells[a] == cells[b] == cells[c] == 'X':
            play_one += 1
        elif cells[a] == cells[b] == cells[c] == 'O':
            play_two += 1
    if play_one != 0 and play_two == 0:
        print("X wins")
        finish = False
    elif play_one == 0 and play_two != 0:
        print("O wins")
        finish = False
    elif play_one == 0 and play_two == 0:
        for i in range(9):
            if cells[i] == 'X' or cells[i] == 'O':
                draw += 1
            else:
                game_finish += 1
        if draw == 9:
            print("Draw")
            finish = False
        if game_finish != 0:
            finish = True
