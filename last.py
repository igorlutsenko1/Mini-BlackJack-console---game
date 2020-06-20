# blackjack game
import random

cold = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
coldwithcomp = list(cold)
players = int(input("Введите количество участников: "))


def oneplayer():
    yourcard = cold.pop(random.choice(cold))
    while True:
        k = input("Ваш счет равен {} очков. Взять еще карту? Yes / No ".format(yourcard))
        if k == "Yes":
            yourcard += cold.pop(random.choice(cold))
            if yourcard > 21:
                return yourcard
            elif yourcard == 21:
                return yourcard
        else:
            return yourcard


def against(func, risklevel):
    if risklevel == "Easy":
        scale = 12
    elif risklevel == "Medium":
        scale = 15
    elif risklevel == "Hard":
        scale = 17
    j = oneplayer()
    cardcomp = coldwithcomp.pop(random.choice(coldwithcomp))
    while True:
        if cardcomp < scale:
            cardcomp += coldwithcomp.pop(random.choice(coldwithcomp))
        else:
            break
    if j <= 21 and cardcomp <= 21:
        if j > cardcomp:
            print("Вы выиграли! Ваше количество очков - {}, компьютера - {}".format(j, cardcomp))
        elif j < cardcomp:
            print("Вы проиграли! Ваше количество очков - {}, компьютера - {}".format(j, cardcomp))
        else:
            print("У вас одинаковое количество очков - {}".format(j))
    elif j > 21 and cardcomp > 21:
        print("Оба участника набрали больше 21 очка. Участник - {}, компьютер - {}".format(j, cardcomp))
    elif j <= 21 and 21 < cardcomp:
        print("Вы выиграли! У оппонента больше 21 очка. У вас - {}, у компьютера - {}".format(j, cardcomp))
    elif j > 21 and 21 >= cardcomp:
        print("Вы проиграли! У Вас больше 21 очка. У вас - {}, у компьютера - {}".format(j, cardcomp))
    elif j == cardcomp:
        print("Ничья! У вас одинаковое количество очков - {}".format(j))


if players == 1:
    oneplayer()
elif players == 2:
    risklevel = input("Введите уровень риска соперника: Easy, Medium or Hard: ")
    against(oneplayer, risklevel)
    while True:
        answer = input("Еще разок? Yes / No ")
        if answer == 'Yes':
            question = input("Сменить уровень сложности?: Yes / No")
            if question == "Yes":
                risklevel = input("Введите уровень риска соперника: Easy, Medium or Hard: ")
                against(oneplayer, risklevel)
            else:
                against(oneplayer, risklevel)
        else:
            break





