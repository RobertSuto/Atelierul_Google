from random_word import list_of_random_word
import random

word = random.choice(list_of_random_word)


word_list = []
lista_deja_incercate = []
unique_letter = set(word)
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())
        if item in unique_letter:
            unique_letter.remove(item)

word_length = len(unique_letter)
print(" ".join(word_list))
count_nr = 1

while count_nr <= word_length:
    user_letter = input("Alege o litera: ").lower()
    if user_letter == "":
        print("introdu o litera")
        continue
    if user_letter in word_list:
        print("Lista este deja pe ecran")
    elif user_letter in lista_deja_incercate:
        print(f'litera deja a fost incercata, literele deja incercate sunt: {" ".join(lista_deja_incercate)}')
    else:
        if user_letter in word:
            for it, value in enumerate(word):
                if user_letter == value:
                    word_list[it] = user_letter
            new_word = " ".join(word_list)
            print(new_word)
        else:
            count_nr += 1
        if '_' not in "".join(word_list):
            print("ai castigat")
            break
        elif count_nr > word_length:
            print(f"ai pierdut! cuvantul era {word}")

        lista_deja_incercate.append(user_letter)