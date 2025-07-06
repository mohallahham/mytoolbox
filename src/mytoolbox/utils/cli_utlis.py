def prompt_input(prompt="Enter input:", quit_command="q") -> str:
    """
    Continuously prompt the user for input until a non-empty value is entered or a quit command is given.

    Parameters:
        prompt (str): The message displayed to the user when asking for input. Defaults to "Enter input:".
        quit_command (str): The command that causes the program to exit when entered (case-insensitive). Defaults to "q".

    Returns:
        str: A non-empty, trimmed string input provided by the user.

    Side Effects:
        - Prints "Goodbye!" and exits the program with code 0 if the user enters the quit command.

    Example:
        >>> prompt_input("Type something: ", quit_command="exit")
        hello
        'hello'
    """
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == quit_command:
            print("Goodbye!")
            exit(0)
        if user_input:
            return user_input
