#Libraries 
import pickle #This library should be used to save to a file and load from a file

#Method to save any questions to the file 'python_quiz_fdb.txt'
def saveQuestions(dictionary, myquizdb):
    with open(myquizdb, "wb") as myfile:
        pickle.dump(dictionary, myfile)
        myfile.close()

#Method to load any questions from file 'python_quiz_fdb.txt
def loadQuestions(myquizdb):
    with open(myquizdb, "rb") as myFile:
        questions = pickle.load(myFile)
        myFile.close()
        return questions

#load questions dictionary
questions = loadQuestions("python_quiz_fdb.txt")

#This method will allow the user to add / del questions from their fuax database. 
def edit_questions(questions):
    while True:
        edit_choice = input("If you would like to Add a question type 'add'. \nIf you would like to delete a question type 'del' \nOtherwise enter 'q' to start game >> ").upper()
        print("\n\n")
        match edit_choice:  
            case 'ADD':

                add_questions()

            case 'DEL':

                for index ,question in enumerate(questions):
                    print((index, question.get('prompt')))
                
                del_question = int(input("\nPlease enter the Number associated with the question you would like to delete:  "))
                questions.pop(del_question)

            case 'Q':
                break

            case _:
                print("Invalid Response...")


#I want to add a method that will allow me to add Questions to my Dictionary
def add_questions(questions):
   
    # Adding a loop to let the user continously add questions if they want to
    while True:

        answer = input("Would you like to add a Fash Card Question (Y / N): ").upper()

        #If statement that contains the logic for user to add a question
        if answer == 'Y':

            options = []
            prompt = input("Please type out your question: ")
            Number_of_choices = int(input("Please enter how many answers you would like to select from: "))
            
            # This loop should allow the user to add as many answers as declared in Number_of_Choices
            for i in range(Number_of_choices):
                options.append(input("What is the letter and answer (A. Answer1 ): "))

            # Loop through the options list to display for the user to see
            for i in options:
                print([i])

            answer = input("What is the Correct answer from above?(A / B/ C...): ").upper()

            #I need to construct the Dictionary input to place into the questions List
            newQuestion = {
                            "prompt" :  prompt,
                            "options" : options,
                            "answer" : answer,
                            }

            # Now I need to append the selections for the new answer into the Questions Dictionary
            questions.append(newQuestion)

        elif answer == 'N':
            print("\n\n")
            saveQuestions(questions,"python_quiz_fdb.txt")
            break

#Method for running the game logic         
def run_quiz(questions):
    edit_questions(questions)

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

#Invoke the quiz gam
run_quiz(questions)
