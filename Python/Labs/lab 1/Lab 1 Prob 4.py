# This program was made by Harris Domangue for CMSC-201 on Sept. 14th 2024
# This program will display a chessboard in uni code

# Displays to the user what this program does
print("This program will display a chess board with all pieces")
input("Press Enter to continue...") # detects if user press enter so it can show the program
print(' ' * 40) #nothing
print(' ' * 40) #nothing

#top side of the chest board
print('\u2013' * 40) #dashes

#displays back row of all black chest pieces that arent pawns
print('\u007C', '\u2656', '\u007C', '\u2658', '\u007C', '\u2657', '\u007C', '\u2655', '\u007C', '\u2654', '\u007C', '\u2657', '\u007C', '\u2658', '\u007C', '\u2656', '\u007C')

#seperator line for first row of black pieces and second row
print('\u2013' * 40) #dashes

# displays blacks pawns
print('\u007C', '\u2659', '\u007C', '\u2659', '\u007C', '\u2659', '\u007C', '\u2659', '\u007C', '\u2659', '\u007C', '\u2659', '\u007C', '\u2659', '\u007C', '\u2659', '\u007C')

#lines to seperate the board for white and black
print('\u2013' * 40) #dashes
print(' ' * 40) #nothing
print(' ' * 40) #nothing
print('\u2013' * 40) #dashes

for i in range(3): # repeate 3 times
    print(' ' * 40) #nothing
    print(' ' * 40) #nothing
    print('\u2013' * 40) #dashes

# displays blacks pawns
print('\u007C', '\u265F', '\u007C', '\u265F', '\u007C', '\u265F', '\u007C', '\u265F', '\u007C', '\u265F', '\u007C', '\u265F', '\u007C', '\u265F', '\u007C', '\u265F', '\u007C')

#seperator line to seperate the pawns and all the other white chest pieces on the bottom of the board
print('\u2013' * 40) #dashes

#displays back row of all black chest pieces that arent pawns
print('\u007C', '\u265C', '\u007C', '\u265E', '\u007C', '\u265D', '\u007C', '\u265B', '\u007C', '\u265A', '\u007C', '\u265D', '\u007C', '\u265E', '\u007C', '\u265C', '\u007C')

#seperator line to seperate the bottom of the board from the first line of white chest pieces
print('\u2013' * 40) #dashes

#print('\u2654')#king dark
#print('\u2655')#queen dark
#print('\u2656')#rook dark
#print('\u2657')#bishop dark
#print('\u2658')#knight dark
#print('\u2659')#pawn dark

#print('\u265A')#king light
#print('\u265B')#queen light
#print('\u265C')#rook light
#print('\u265D')#bishop light
#print('\u265E')#knight light
#print('\u265F')#pawn light

#print('\u2013') #dashes
#print('\u007C') # vertical line
