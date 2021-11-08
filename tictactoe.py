def tic_tac_toe():
    tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    castiguri = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    end = False

    def status():
        print(tabla[0], tabla[1], tabla[2])
        print(tabla[3], tabla[4], tabla[5])
        print(tabla[6], tabla[7], tabla[8])
        print()

    def jucator():
        n = alege()
        if tabla[n] == "X" or tabla[n] == "O":
            print("\nExista un element deja in caseta")
            jucator()
        else:
            tabla[n] = "X"

    def calculator():
        if tabla[4] != "X" and tabla[4] != "O":
            tabla[4] = "O"
        elif tabla[0] != "X" and tabla[0] != "O":
            tabla[0] = "0"
        elif tabla[2] != "X" and tabla[2] != "O":
            tabla[2] = "0"
        elif tabla[6] != "X" and tabla[6] != "O":
            tabla[6] = "0"
        elif tabla[8] != "X" and tabla[8] != "O":
            tabla[8] = "0"
        elif tabla[8] != "X" and tabla[8] != "O":
            tabla[8] = "0"
        elif tabla[1] != "X" and tabla[1] != "O":
            tabla[1] = "0"
        elif tabla[3] != "X" and tabla[3] != "O":
            tabla[3] = "0"
        elif tabla[5] != "X" and tabla[5] != "O":
            tabla[5] = "0"
        elif tabla[7] != "X" and tabla[7] != "O":
            tabla[7] = "0"

    def alege():
        while True:
            while True:
                a = input()
                try:
                    a = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nAcest numar nu exista in tabela")
                        continue
                except ValueError:
                    print("\nNu ati introdus un numar")
                    continue

    def verificari():
        count = 0
        for a in castiguri:
            if tabla[a[0]] == tabla[a[1]] == tabla[a[2]] == "X":
                print("Ai castigat!\n")
                return True
            if tabla[a[0]] == tabla[a[1]] == tabla[a[2]] == "O":
                print("Ai pierdut!\n")
                return True
        for a in range(9):
            if tabla[a] == "X" or tabla[a] == "O":
                count += 1
            if count == 9:
                print("Egalitate\n")
                return True

    while not end:
        status()
        end = verificari()
        if end == True:
            break
        print("Alege")
        jucator()

        status()
        end = verificari()
        if end == True:
            break
        calculator()


tic_tac_toe()