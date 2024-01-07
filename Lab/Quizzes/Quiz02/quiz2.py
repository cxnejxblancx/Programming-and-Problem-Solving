def check_horizontal(board):
    is_horizontal = False
    for line in board:
        if line[0] == line[1] == line[2]:
            is_horizontal == True

    return is_horizontal

def main():
    CROSS  = 'x'
    CIRCLE = 'o'

    board = [
        [CIRCLE, CROSS, CROSS],
        [CIRCLE, CROSS, CIRCLE],
        [CROSS,  CROSS, CIRCLE]
        ]
    
    print(check_horizontal(board))

main()
