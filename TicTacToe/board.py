def get_intial_matrix():
    seperator = "|"
    dotted = f"_"*5
    space = f" "*5
    row1 = space+seperator+space+seperator+space
    row2 = dotted+seperator+dotted+seperator+dotted
    row3 = space+seperator+space+seperator+space
    row4 = row1
    matrix = [row1, row2, row3, row2, row4, row1]
    return matrix


def get_board(matrix, move, sign):
    space = f" " * 5
    seperator = "|"
    row = get_row(move)
    index = row[1]
    row = row[0]
    if row == "row1":
        row = matrix[0]
    elif row == "row3":
        row = matrix[2]
    elif row == "row4":
        row = matrix[4]
    else:
        print("Invalid Row")


    row_elements = row.split('|')
    if row_elements[get_index(move)] != space:
        print('The box is filled.. Please choose another move')
    else:
        new_element = f'  {sign}  '
        row_elements[get_index(move)] = new_element
    row = row_elements[0]+seperator+row_elements[1]+seperator+row_elements[2]
    matrix[index] = row

    return matrix


def get_row(move):
    move = int(move)
    if 1 <= move <= 3:
        return "row1", 0
    elif 4<=move <=6:
        return "row3", 2
    elif 7<= move <=9:
        return "row4", 4
    else:
        return 'Invalid Row'


def get_index(move):
    move = int(move)

    if move==1 or move==4 or move==7:
        return 0
    elif move==2 or move==5 or move==8:
        return 1
    else:
        return 2

def display_matrix(matrix):
    for row in matrix:
        print(row)

