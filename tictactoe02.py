myTTT = [
    [" ", "0", "1", "2"],
    ["0", "-", "-", "-"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"]
]
def print_list():
    for i in myTTT:
        print(*i)

def check():
    if myTTT[1][1] == "X" and myTTT[1][2] == "X" and myTTT[1][3] == "X":
        print("Crosses won")
        return False
    elif myTTT[2][1] == "X" and myTTT[2][2] == "X" and myTTT[2][3] == "X":
        print("Crosses won")
        return False
    elif myTTT[3][1] == "X" and myTTT[3][2] == "X" and myTTT[3][3] == "X":
        print("Crosses won")
        return False
    elif myTTT[1][1] == "X" and myTTT[2][1] == "X" and myTTT[3][1] == "X":
        print("Crosses won")
        return False
    elif myTTT[1][2] == "X" and myTTT[2][2] == "X" and myTTT[3][2] == "X":
        print("Crosses won")
        return False
    elif myTTT[1][3] == "X" and myTTT[2][3] == "X" and myTTT[3][3] == "X":
        print("Crosses won")
        return False
    elif myTTT[1][1] == "X" and myTTT[2][2] == "X" and myTTT[3][3] == "X":
        print("Crosses won")
        return False
    elif myTTT[1][3] == "X" and myTTT[2][2] == "X" and myTTT[3][1] == "X":
        print("Crosses won")
        return False
    elif myTTT[1][1] == "0" and myTTT[1][2] == "0" and myTTT[1][3] == "0":
        print("Zeros won")
        return False
    elif myTTT[2][1] == "0" and myTTT[2][2] == "0" and myTTT[2][3] == "0":
        print("Zeros won")
        return False
    elif myTTT[3][1] == "0" and myTTT[3][2] == "0" and myTTT[3][3] == "0":
        print("Zeros won")
        return False
    elif myTTT[1][1] == "0" and myTTT[2][1] == "0" and myTTT[3][1] == "0":
        print("Zeros won")
        return False
    elif myTTT[1][2] == "0" and myTTT[2][2] == "0" and myTTT[3][2] == "0":
        print("Zeros won")
        return False
    elif myTTT[1][3] == "0" and myTTT[2][3] == "0" and myTTT[3][3] == "0":
        print("Zeros won")
        return False
    elif myTTT[1][1] == "0" and myTTT[2][2] == "0" and myTTT[3][3] == "0":
        print("Zeros won")
        return False
    elif myTTT[1][3] == "0" and myTTT[2][2] == "0" and myTTT[3][1] == "0":
        print("Zeros won")
        return False
    else:
        return True

print_list()

for j in range(1, 5):
    a, b = map(int, input("string number after space column number for X: ").split())
    a = a + 1
    b = b + 1
    myTTT[a][b] = "X"
    print_list()
    if check() is False:
        break
    c, d = map(int, input("string number after space column number for 0: ").split())
    c = c + 1
    d = d + 1
    myTTT[c][d] = "0"
    print_list()
    if check() is False:
        break
if check():
    print("Winner not revealed")
