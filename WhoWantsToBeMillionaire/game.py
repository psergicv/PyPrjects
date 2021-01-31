from questions import *


def game_func(var):
    game_life = 1
    if var == 1:
        while game_life < 16:

            print(Question1())
            user_answer = input('What is your choice?(A/B/C/D): ')
            if Answer1(user_answer.upper()) == positive_answer:
                game_life += 1
                print(Question2())
                user_answer = input('What is your choice?(A/B/C/D): ')
                if Answer2(user_answer.upper()) == positive_answer:
                    game_life += 1
                    print(Question3())
                    user_answer = input('What is your choice?(A/B/C/D): ')
                    if Answer3(user_answer.upper()) == positive_answer:
                        game_life += 1
                        print(Question4())
                        user_answer = input('What is your choice?(A/B/C/D): ')
                        if Answer4(user_answer.upper()) == positive_answer:
                            game_life += 1
                            print(Question5())
                            user_answer = input('What is your choice?(A/B/C/D): ')
                            if Answer5(user_answer.upper()) == positive_answer:
                                game_life += 1
                                print(Question6())
                                user_answer = input('What is your choice?(A/B/C/D): ')
                                if Answer6(user_answer.upper()) == positive_answer:
                                    game_life += 1
                                    print(Question7())
                                    user_answer = input('What is your choice?(A/B/C/D): ')
                                    if Answer7(user_answer.upper()) == positive_answer:
                                        game_life += 1
                                        print(Question8())
                                        user_answer = input('What is your choice?(A/B/C/D): ')
                                        if Answer8(user_answer.upper()) == positive_answer:
                                            game_life += 1
                                            print(Question9())
                                            user_answer = input('What is your choice?(A/B/C/D): ')
                                            if Answer9(user_answer.upper()) == positive_answer:
                                                game_life += 1
                                                print(Question10())
                                                user_answer = input('What is your choice?(A/B/C/D): ')
                                                if Answer10(user_answer.upper()) == positive_answer:
                                                    game_life += 1
                                                    print(Question11())
                                                    user_answer = input('What is your choice?(A/B/C/D): ')
                                                    if Answer11(user_answer.upper()) == positive_answer:
                                                        game_life += 1
                                                        print(Question12())
                                                        user_answer = input('What is your choice?(A/B/C/D): ')
                                                        if Answer12(user_answer.upper()) == positive_answer:
                                                            game_life += 1
                                                            print(Question13())
                                                            user_answer = input('What is your choice?(A/B/C/D): ')
                                                            if Answer13(user_answer.upper()) == positive_answer:
                                                                game_life += 1
                                                                print(Question14())
                                                                user_answer = input('What is your choice?(A/B/C/D): ')
                                                                if Answer14(user_answer.upper()) == positive_answer:
                                                                    game_life += 1
                                                                    print(Question15())
                                                                    user_answer = input(
                                                                        'What is your choice?(A/B/C/D): ')
                                                                    if Answer15(user_answer.upper()) == positive_answer:
                                                                        game_life += 1
                                                                    else:
                                                                        print(negative_answer)
                                                                        game_life += 100
                                                                else:
                                                                    print(negative_answer)
                                                                    game_life += 100
                                                            else:
                                                                print(negative_answer)
                                                                game_life += 100
                                                        else:
                                                            print(negative_answer)
                                                            game_life += 100
                                                    else:
                                                        print(negative_answer)
                                                        game_life += 100
                                                else:
                                                    print(negative_answer)
                                                    game_life += 100
                                            else:
                                                print(negative_answer)
                                                game_life += 100
                                        else:
                                            print(negative_answer)
                                            game_life += 100
                                    else:
                                        print(negative_answer)
                                        game_life += 100
                                else:
                                    print(negative_answer)
                                    game_life += 100
                            else:
                                print(negative_answer)
                                game_life += 100
                        else:
                            print(negative_answer)
                            game_life += 100
                    else:
                        print(negative_answer)
                        game_life += 100
                else:
                    print(negative_answer)
                    game_life += 100
            else:
                print(negative_answer)
                game_life += 100
    else:
        print('Приходите когда будете готовы')
