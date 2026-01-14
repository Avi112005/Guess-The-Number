def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def format_hint(guess, secret_number):
    if guess < secret_number:
        return "Too low! Try again."
    elif guess > secret_number:
        return "Too high! Try again."
    else:
        return "Congratulations! You've guessed the number!"