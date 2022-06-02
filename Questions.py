# Объявляем счетчик очков
points = 0

# Объявляем счетчик правильных ответов
true_answers = 0

# Объявляем список вопросов
questions = ["My name _ Vova", "I _ a coder", "I live _ Moscow", 'How _ you?']

answers = ["is", "am", "in", 'are']

choice_question = 0

if input('Привет! Предлагаю проверить свои знания английского! \nНаберите "ready", чтобы начать!\n') == "ready":

    # ------------------- Первый вопрос ---------------------
    try_count = 3
    while try_count > 0:
        if input(f"{questions[choice_question]}\n") == answers[choice_question]:
            true_answers += 1
            points += try_count
            print("Ответ верный!")
            break
        elif try_count == 1:
            print(f"Увы, но нет.\nВерный ответ: {answers[choice_question]}")
            break
        else:
            try_count -= 1
            print(f"Осталось попыток: {try_count}, попробуйте еще раз")

    # ------------------- Второй вопрос ---------------------
    choice_question +=1
    try_count = 3
    while try_count > 0:
        if input(f"{questions[choice_question]}\n") == answers[choice_question]:
            true_answers += 1
            points += try_count
            print("Ответ верный!")
            break
        elif try_count == 1:
            print(f"Увы, но нет.\nВерный ответ: {answers[choice_question]}")
            break
        else:
            try_count -= 1
            print(f"Осталось попыток: {try_count}, попробуйте еще раз")

         # ------------------- Третий вопрос ---------------------
    choice_question += 1
    try_count = 3
    while try_count > 0:
        if input(f"{questions[choice_question]}\n") == answers[choice_question]:
            true_answers += 1
            points += try_count
            print("Ответ верный!")
            break
        elif try_count == 1:
            print(f"Увы, но нет.\nВерный ответ: {answers[choice_question]}")
            break
        else:
            try_count -= 1
            print(f"Осталось попыток: {try_count}, попробуйте еще раз")

            # ------------------- 4 вопрос ---------------------
    choice_question += 1
    try_count = 3
    while try_count > 0:
        if input(f"{questions[choice_question]}\n") == answers[choice_question]:
            true_answers += 1
            points += try_count
            print("Ответ верный!")
            break
        elif try_count == 1:
            print(f"Увы, но нет.\nВерный ответ: {answers[choice_question]}")
            break
        else:
            try_count -= 1
            print(f"Осталось попыток: {try_count}, попробуйте еще раз")

    print(f"Вот и все!\nВы ответили на {true_answers} вопросов из {len(questions)} верно, вы набрали {points} баллов.")

else:
    print("Кажется, вы не хотите играть. Очень жаль.")
