seperator = "|"
dotted = f"_"*5
space = f" "*5
row1 = space+seperator+space+seperator+space
row2 = dotted+seperator+dotted+seperator+dotted
matrix = [row1, row2, row1, row2, row1, row1]


def get_board():
    return matrix
