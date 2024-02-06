# Given a rope length L and 3 numbers a, b, c
# cut the rope into max no of pieces s.t. the length of each piece is a/b/c
# return the max no of pieces

def get_no_of_pieces_helper(L, a, b, c, s, pieces):
    if s > L:
        return 0
    
    if s == L:
        return pieces
    
    x = get_no_of_pieces_helper(L, a, b, c, s+a, pieces+1)
    y = get_no_of_pieces_helper(L, a, b, c, s+b, pieces+1)
    z = get_no_of_pieces_helper(L, a, b, c, s+c, pieces+1)
    
    return max(x, y, z)

def get_no_of_pieces(L, a, b, c):
     return get_no_of_pieces_helper(L, a, b, c, 0, 0)


L = abs(int(input("Enter the length of rope: ")))
a = abs(int(input("Enter the length of piece a: ")))
b = abs(int(input("Enter the length of piece b: ")))
c = abs(int(input("Enter the length of piece c: ")))

print("Max no of pieces:", get_no_of_pieces(L, a, b, c))