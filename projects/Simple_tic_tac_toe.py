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
