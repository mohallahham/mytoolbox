questions = [
    {
        "question": "What is the tallest animal in the world?",
        "options": ["A. Elephant", "B. Giraffe", "C. Kangaroo", "D. Ostrich"],
        "answer": "B",
        "type": "mcq",
    },
    {
        "question": "What is the smallest planet in our solar system?",
        "options": ["A. Mars", "B. Earth", "C. Mercury", "D. Pluto"],
        "answer": "C",
        "type": "mcq",
    },
    {
        "question": "In which country would you find the city of Kyoto?",
        "options": ["A. South Korea", "B. China", "C. Thailand", "D. Japan"],
        "answer": "D",
        "type": "mcq",
    },
    {
        "question": "What color do you get when you mix red and white?",
        "options": ["A. Pink", "B. Orange", "C. Purple", "D. Coral"],
        "answer": "A",
        "type": "mcq",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": [
            "A. Vincent Van Gogh",
            "B. Pablo Picasso",
            "C. Leonardo da Vinci",
            "D. Michelangelo",
        ],
        "answer": "C",
        "type": "mcq",
    },
    {
        "question": "What is the capital city of Canada?",
        "options": ["A. Toronto", "B. Montreal", "C. Vancouver", "D. Ottawa"],
        "answer": "D",
        "type": "mcq",
    },
    {
        "question": "Which fruit has its seeds on the outside?",
        "options": ["A. Strawberry", "B. Kiwi", "C. Blueberry", "D. Grapes"],
        "answer": "A",
        "type": "mcq",
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D",
        "type": "mcq",
    },
    {
        "question": "What is the name of the toy cowboy in Toy Story?",
        "options": None,
        "answer": "woody",
        "type": "open",
    },
    {
        "question": "Name one of the four houses at Hogwarts in the Harry Potter series.",
        "options": None,
        "answer": ["gryffindor", "hufflepuff", "ravenclaw", "slytherin"],
        "type": "open",
    },
]

score = 0

for q in questions:
    print(f"\n{q['question']}")

    if q["type"] == "mcq":
        for option in q["options"]:
            print(option)
        user_answer = (
            input("Please select the correct answer A,B,C,D \n").strip().upper()
        )
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, correct answer was {q['answer']}\n")

    elif q["type"] == "open":
        user_answer = input("Your Answer is... \n").strip().lower()
        correct = q["answer"]

        if isinstance(correct, list):
            if user_answer in correct:
                print("Correct!\n")
                score += 1
            else:
                print(f"Sorry, correct answers were: {', '.join(correct)}\n")
        else:
            if user_answer == correct:
                print("Correct!\n")
                score += 1
            else:
                print(f"Sorry, correct answer was: {correct}\n")

print(f"You got {score} out of {len(questions)} correct!")
