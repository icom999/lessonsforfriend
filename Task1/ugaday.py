import random
s = random.randint(1, 5)
n = int(input("Введи цифру от одного до пяти: "))
if n == s:
    print("Молодец, с первого раза угадал! Экстрасенс? Тогда сыграем еще разок?")
else:
    n1 = int(input("Не угадал, осталось две попытки! "))
    if n1 == s:
        print("Угадал! Неплохо, повторим игру?")    
    else:
        n2 = int(input("Не угадал, осталась одна попытка! "))
        if n2 == s:
            print("Угадал! Но могло бы быть и лучше. Выпей чайку и повтори.")        
        else:
            print("Сегодня явно не твой день. Иди поспи!")

# производим изменения в файле чтобы отследить изменения в папке