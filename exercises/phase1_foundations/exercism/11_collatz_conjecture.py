def steps(number=int):
    """Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture."""
    steps = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number != 1:
            steps = steps + 1
            if number % 2 == 0:
                number = number / 2

            else:
                number = (number * 3) + 1
    return steps
