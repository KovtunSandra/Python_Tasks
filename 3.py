import random

def guess_the_number():
    lowest_number = 1
    uppest_number = 100
    max_attempts = 10

    number_to_guess = random.randint(lowest_number, uppest_number)

    print(f"Відгадайте число від {lowest_number} до {uppest_number} за {max_attempts} спроб.")

    attempts = 0
    while attempts < max_attempts:
        guess = int(input(f"Спроба {attempts + 1}: Введіть ваше число: "))

        if guess < number_to_guess:
            print("Ні, число більше.")
        elif guess > number_to_guess:
            print("Ні, число менше.")
        else:
            print(f"Вітаю! Ви відгадали число {number_to_guess} за {attempts + 1} спроб!")
            break

        attempts += 1

    if attempts == max_attempts:
        print(f"Ви не змогли відгадати число. Число було: {number_to_guess}")

guess_the_number()