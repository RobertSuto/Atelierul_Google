def tic_tac_toe():
    tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    castiguri = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    end = False
    ordine = [4, 0, 2, 6, 8, 1, 3, 5, 9]

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
        for poz in ordine:
            if tabla[poz] != "X" and tabla[poz] != "O":
                tabla[poz] = "O"
                break


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