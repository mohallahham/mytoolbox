def hex_output():
    decnum = 0

    hexnum = input("Enter a hex number to convert ")

    # Loop through the reversed hex string with index (power) and digit
    # Reversing allows us to start from the least significant digit (rightmost)
    for power, digit in enumerate(reversed(hexnum)):
        # Convert the current hex digit to a decimal integer
        # Multiply it by 16 raised to the position power
        # Add the result to the running total
        decnum += int(digit, 16) * (16**power)

    print(decnum)


# hex_output()


def hex_out2():
    decnum = 0
    hexnum = input("Enter a hex number to convert ")

    # Loop through the reversed hex string with index (power) and digit
    for power, digit in enumerate(reversed(hexnum)):
        # Check if the digit is a number between '0' and '9'
        if "0" <= digit <= "9":
            # Convert the character to its integer value by subtracting the Unicode value of '0'
            value = ord(digit) - ord("0")

        # If the digit is a letter between 'A' and 'F' (case-insensitive)
        elif "A" <= digit.upper() <= "F":
            # Convert the character to its integer value by subtracting 'A' and adding 10
            # 'A' represents 10 in hexadecimal, 'B' is 11, ..., 'F' is 15
            value = ord(digit.upper()) - ord("A") + 10

        # If the character is not a valid hex digit (0-9 or A-F), ignore it
        else:
            continue

        decnum += value * (16**power)

    print(decnum)


# hex_out2()


# Bonus
def name_triangle():
    name = input("What is your name ")
    for inx, char in enumerate(name):
        print(name[: inx + 1])


# name_triangle()
