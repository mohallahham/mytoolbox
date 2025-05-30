def flex_buzz(n: int, a: int = 3, b: int = 5):
    """Return classic / configurable FizzBuzz sequence 1..n."""
    out = []
    for i in range(1, n + 1):
        match (i % a == 0, i % b == 0):
            case (True, True):
                out.append("FizzBuzz")
            case (True, False):
                out.append("Fizz")
            case (False, True):
                out.append("Buzz")
            case _:
                out.append(i)
    return out
