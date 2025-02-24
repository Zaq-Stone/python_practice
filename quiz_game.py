
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the Git command to check your version?",
        "options": ["A. git commit -m", "B. git --status", "C. get -version", "D. git -v"],
        "answer": "D"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "What is the best reason to hire Zach Stone?",
        "options": ["A. His dashing good looks", "B. His ability to share stupid projects", "C. He would be great for my company", "D. ALL THE ABOVE"],
        "answer": "D"
    }
]

# Run the quiz
run_quiz(questions)
