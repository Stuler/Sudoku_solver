from deck import deck

def get_col(lst, pos):
    return(lst.index(pos))

available_numbers = []
final_deck = []
temp_deck = []

sects = [
    [# section 1 index 0
    deck[0][0],deck[0][1],deck[0][2],
    deck[1][0],deck[1][1],deck[1][2],
    deck[2][0],deck[2][1],deck[2][2]],
    [# section 2 index 1
    deck[0][3],deck[0][4],deck[0][5],
    deck[1][3],deck[1][4],deck[1][5],
    deck[2][3],deck[2][4],deck[2][5]],
    [# section 3 index 2
    deck[0][6],deck[0][7],deck[0][8],
    deck[1][6],deck[1][7],deck[1][8],
    deck[2][6],deck[2][7],deck[2][8]],
    [# section 4 index 3
    deck[3][0],deck[3][1],deck[3][2],
    deck[4][0],deck[4][1],deck[4][2],
    deck[5][0],deck[5][1],deck[5][2]],
    [# section 5 index 4
    deck[3][3],deck[3][4],deck[3][5],
    deck[4][3],deck[4][4],deck[4][5],
    deck[5][3],deck[5][4],deck[5][5]],
    [# section 6 index 5
    deck[3][6],deck[3][7],deck[3][8],
    deck[4][6],deck[4][7],deck[4][8],
    deck[5][6],deck[5][7],deck[5][8]],
    [# section 7 index 6
    deck[6][0],deck[6][1],deck[6][2],
    deck[7][0],deck[7][1],deck[7][2],
    deck[8][0],deck[8][1],deck[8][2]],
    [# section 8 index 7
    deck[6][3],deck[6][4],deck[6][5],
    deck[7][3],deck[7][4],deck[7][5],
    deck[8][3],deck[8][4],deck[8][5]],
    [# section 9 index 8
    deck[6][6],deck[6][7],deck[6][8],
    deck[7][6],deck[7][7],deck[7][8],
    deck[8][6],deck[8][7],deck[8][8]]
    ]

temp_deck = deck

for row in temp_deck:
    for i in row:
        if i == 0:
           row.insert((j for j in range(1,10)) if j not in row)
           



print (temp_deck)