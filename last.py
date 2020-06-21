# blackjack game
import random

cold = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
coldwithcomp = list(cold)
players = int(input("Введите количество участников: "))


def scoreofplayer():
    yourcard = cold.pop(random.choice(cold))
    while True:
        k = input("Ваш счет равен {} очков. Взять еще карту? Yes / No ".format(yourcard))
        if k == "Yes":
            yourcard += cold.pop(random.choice(cold))
            if yourcard > 21:
               return yourcard
        else:
            return yourcard


def condition(*args, **kwargs):
    try:
        if risklevel == "Easy":
            scale = 12
        elif risklevel == "Medium":
            scale = 15
        elif risklevel == "Hard":
            scale = 17
        cardcomp = coldwithcomp.pop(random.choice(coldwithcomp))
        while True:
            if cardcomp < scale:
                cardcomp += coldwithcomp.pop(random.choice(coldwithcomp))
            else:
                break

    except:
        pass

    try:
        if k <= 21 and cardcomp <= 21:
            if k > cardcomp:
                print("Вы выиграли! Ваше количество очков - {}, компьютера - {}".format(k, cardcomp))
            elif k < cardcomp:
                print("Вы проиграли! Ваше количество очков - {}, компьютера - {}".format(k, cardcomp))
            else:
                print("У вас одинаковое количество очков - {}".format(k))
        elif k > 21 and cardcomp > 21:
            print("Оба участника набрали больше 21 очка. Участник - {}, компьютер - {}".format(k, cardcomp))
        elif k <= 21 and 21 < cardcomp:
            print("Вы выиграли! У оппонента больше 21 очка. У вас - {}, у компьютера - {}".format(k, cardcomp))
        elif k > 21 and 21 >= cardcomp:
            print("Вы проиграли! У Вас больше 21 очка. У вас - {}, у компьютера - {}".format(k, cardcomp))
        elif k == cardcomp:
            print("Ничья! У вас одинаковое количество очков - {}".format(k))

    except:
        if k < 21 and players == 1:
            print("Вы набрали меньше 21 очка - {}".format(k))
        elif k == 21 and players == 1:
            print("Вы выиграли набрав 21 очко!")
        elif k > 21 and players == 1:
            print("Вы проиграли, набрав больше 21 очка - {}".format(k))


if players == 1:
    k = scoreofplayer()
    condition(k)
    while True:
        answer = input("Еще разок? Yes / No ")
        if answer == 'Yes':
            k = scoreofplayer()
            condition(k)
        else:
            print("Конец игры")
            break

elif players == 2:
    risklevel = input("Введите уровень риска соперника: Easy, Medium or Hard: ")
    k = scoreofplayer()
    condition(k, risklevel)
    while True:
        answer = input("Еще разок? Yes / No ")
        if answer == 'Yes':
            question = input("Сменить уровень риска?: Yes / No")
            if question == "Yes":
                risklevel = input("Введите уровень риска соперника: Easy, Medium or Hard: ")
                k = scoreofplayer()
                condition(k, risklevel)
            else:
                k = scoreofplayer()
                condition(k, risklevel)
        else:
            print("Конец игры")
            break




