import random
import threading
import time

operators = ['+', '-', '*']


def input_with_timeout(prompt, timeout):
    answer = None

    def get_answer():
        nonlocal answer
        answer = input(prompt)

    thread = threading.Thread(target=get_answer)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        print("\ntime ended!")
        thread.join()
    return answer


def show_game_name():
    game_name = "math game"
    print(f"{game_name} started")


show_game_name()


def quiz():
    global correct_answer
    score = 0

    for _ in range(5):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        operator = random.choice(operators)

        if operator == '+':
            correct_answer = a + b
        elif operator == '-':
            correct_answer = a - b
        elif operator == '*':
            correct_answer = a * b

        prompt = f"{a} {operator} {b} = ? "
        start_time = time.time()

        answer = input_with_timeout(prompt, 5)

        if answer is None:
            print("Do not get points.")
        else:
            try:
                user_answer = int(answer)
                if user_answer == correct_answer:
                    score = score + 1
                    print("correct answer!")
                else:
                    print("invalid answer.")
            except ValueError:
                print("please just input integer.Do not get points.....")

        end_time = time.time()
        if end_time - start_time > 5:
            print("Do not get points.")

    print(f"Final score: {score}")
    if score >= 3:
        print("you won!")
    else:
        print("You lost. Try again.")


quiz()
