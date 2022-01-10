a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
winning_check = 0


def main():
    global winning_check

    play_again = "y"

    while play_again == "y":

        while winning_check == 0:
            #print("Type d when you come to a draw")
            game()

        play_again = input("Do you want to play again (y/n)? ")

        if play_again == "y":

            global a, b, c, d, e, f, g, h, i

            a = 1
            b = 2
            c = 3
            d = 4
            e = 5
            f = 6
            g = 7
            h = 8
            i = 9
            winning_check = 0

    print("Good game. Thanks for playing!")

def game():

    print()
    board(a,b,c,d,e,f,g,h,i)
    print()
    check(a,b,c,d,e,f,g,h,i)
    num(ques("X"), "X")
    print()
    board(a,b,c,d,e,f,g,h,i)
    print()
    check(a,b,c,d,e,f,g,h,i)
    num(ques("O"), "O")



def ques(text):

    if winning_check == 0:
        q = int(input(f"{text}'s turn to choose a square (1-9):"))
    
    else:
        q = "Thank's for playing"

    return q


def check(a,b,c,d,e,f,g,h,i):
    global winning_check

    if a == b == c == "X" or d == e == f == "X" or g == h == i == "X" \
    or a == e == i == "X" or g == e == c == "X" or i == f == c == "X" \
    or g == d == a == "X" or b == e == h == "X":
        print("X's won the game")
        winning_check = 1


    elif a == b == c == "O" or d == e == f == "O" or g == h == i == "O" \
    or a == e == i == "O" or g == e == c == "O" or i == f == c == "O" \
    or g == d == a == "O" or b == e == h == "O":
        print("O's won the game")
        winning_check = 1



def board(a,b,c,d,e,f,g,h,i):

    print(f"{a} | {b} | {c}")
    print("- + - + -")
    print(f"{d} | {e} | {f}")
    print("- + - + -")
    print(f"{g} | {h} | {i}")


def num(var, person):
    
    global a, b, c, d, e, f, g, h, i

    if person == "X":
        if var == 1:
            a = "X"
        elif var == 2:
            b = "X"
        elif var == 3:
            c = "X"
        elif var == 4:
            d = "X"
        elif var == 5:
            e = "X"
        elif var == 6:
            f = "X"
        elif var == 7:
            g = "X"
        elif var == 8:
            h = "X"
        elif var == 9:
            i = "X"


    elif person == "O":
        if var == 1:
            a = "O"
        elif var == 2:
            b = "O"
        elif var == 3:
            c = "O"
        elif var == 4:
            d = "O"
        elif var == 5:
            e = "O"
        elif var == 6:
            f = "O"
        elif var == 7:
            g = "O"
        elif var == 8:
            h = "O"
        elif var == 9:
            i = "O"

    #elif person == "d":



if __name__ == "__main__":
    main()