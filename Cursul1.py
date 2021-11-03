# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
list_1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
list_2 = list_1.copy()
list_2.sort()
print(list_2)

# afișarea unei liste ordonatită descendent (lista inițială trebuie păstrată în aceeași formă)
list_3 = list_2.copy()
list_3.reverse()
print(list_3)

# afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(list_2[1::2])

# afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(list_2[::2])

# afișarea elementelor multipli ai lui 3.
for i in range(len(list_1)):
    if list_1[i] %3 == 0:
        print(list_1[i])
