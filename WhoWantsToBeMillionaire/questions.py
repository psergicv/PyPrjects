positive_answer = 'Правельный ответ'
negative_answer = 'Это не правельный ответ. Начните заново'


def Question1():
    question_text = '''
        Какой газ преобладает в атмосфере Земли?
        A: Кислород
        B: Азот
        C: Углекислый газ
        D: Водород
    '''
    return question_text


def Answer1(user_answer):
    correct_answer1 = 'B'

    if user_answer == correct_answer1:
        return positive_answer
    elif user_answer != correct_answer1:
        return negative_answer
        


def Question2():
    question_text = '''
        Кто из этих деятелей искусства стал директором первого профессионального публичного театра России?
        A: Александр Сумароков
        B: Василий Каратыгин
        C: Павел Молчанов
        D: Яков Княжнин
    '''
    return question_text


def Answer2(user_answer):
    correct_answer1 = 'A'

    if user_answer == correct_answer1:
        return positive_answer
    else:
        return negative_answer


def Question3():
    question_text = '''
        Какой вид спорта не входит в современное пятиборье?
        A: Метание копья
        B: Верховая езда
        C: Фехтование
        D: Плавание
    '''
    return question_text


def Answer3(user_answer):
    correct_answer1 = 'A'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question4():
    question_text = '''
        Как иначе называют пиратский флаг?
        A: Весёлый Роджер
        B: Грязный Гарри
        C: Бедный Йорик
        D: Лимонадный Джо
    '''
    return question_text


def Answer4(user_answer):
    correct_answer1 = 'A'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question5():
    question_text = '''
        Какой фильм Феллини сделал имя Папарацци нарицательным?
        A: Восемь с половиной
        B: Ночи Кабирии
        C: Дорога
        D: Сладкая жизнь
    '''
    return question_text


def Answer5(user_answer):
    correct_answer1 = 'D'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question6():
    question_text = '''
        Как называется популярный рецепт приготовления макарон с мясом?
        A: По-деревенски
        B: По-флотски
        C: По-братски
        D: По-божески
    '''
    return question_text


def Answer6(user_answer):
    correct_answer1 = 'B'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question7():
    question_text = '''
        Что является характеристикой коллекционного вина?
        A: Стойкость
        B: Выдержка
        C: Выносливость
        D: Трезвость
    '''
    return question_text


def Answer7(user_answer):
    correct_answer1 = 'B'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question8():
    question_text = '''
        Морской путь в какую страну искала экспедиция Колумба, доплыв вместо этого до Америки?
        A: Эфиопия
        B: Япония
        C: Индия
        D: Китай
    '''
    return question_text


def Answer8(user_answer):
    correct_answer1 = 'C'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question9():
    question_text = '''
        Как называется одна из станций Московского метрополитена?
        A: Спартак
        B: Динамо
        C: Торпедо
        D: Локомотив
    '''
    return question_text


def Answer9(user_answer):
    correct_answer1 = 'B'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question10():
    question_text = '''
        Как называется один из конкурсов телеигры «КВН»?
        A: Контрольная работа
        B: Диктант
        C: Домашнее задание
        D: Работа над ошибками
    '''
    return question_text


def Answer10(user_answer):
    correct_answer1 = 'C'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question11():
    question_text = '''
        Какая страна ежегодно дарит Великобритании к Рождеству роскошную ёлку?
        A: Финляндия
        B: Швеция
        C: Норвегия
        D: Дания
    '''
    return question_text


def Answer11(user_answer):
    correct_answer1 = 'C'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question12():
    question_text = '''
        Какая из перечисленных башен самая низкая?
        A: Останкинская
        B: Эйфелева
        C: Пизанская
        D: Спасская
    '''
    return question_text


def Answer12(user_answer):
    correct_answer1 = 'C'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question13():
    question_text = '''
        Как называется крепкий спиртной напиток из сока сахарного тростника?
        A: Кальвадос
        B: Ром
        C: Джин
        D: Виски
    '''
    return question_text


def Answer13(user_answer):
    correct_answer1 = 'B'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question14():
    question_text = '''
        Как называется единственное в Европе герцогство?
        A: Монако
        B: Андорра
        C: Люксембург
        D: Лихтенштейн
    '''
    return question_text


def Answer14(user_answer):
    correct_answer1 = 'C'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)


def Question15():
    question_text = '''
        Какую птицу американцы традиционно готовят на День Благодарения?
        A: Курицу
        B: Индейку
        C: Гуся
        D: Утку
    '''
    return question_text


def Answer15(user_answer):
    correct_answer1 = 'B'

    if user_answer == correct_answer1:
        print(positive_answer)
    else:
        print(negative_answer)
