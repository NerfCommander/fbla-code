class Quiz:
    def __init__(self, question, answer, choices, level):
        self.question = question
        self.answer = answer
        self.choices = choices
        self.level = level

    def check_answer(self, selected_answer):
        if selected_answer == self.answer:
            return "Correct"
        else:
            return "Wrong"






quizList = []

quizList.append( Quiz('Which of the following is a consequence of overdrawing your checking account?', "D", dict([('A', 'Bounced check fee from the store'), ('B', 'Overdraft fee from your bank'), ('C', 'Stress from money mismanagement'), ('D', 'All of the above')]), 'Easy') )
quizList.append( Quiz('Rent is a:', "A", dict([('A', 'Fixed expense'), ('B', 'Variable expense'), ('C', 'Discretionary Expense'), ('D', 'Intermittent expense')]), 'Easy') )
quizList.append( Quiz('Groceries are a:', "C", dict([('A', 'Fixed expense'), ('B', 'Intermittent expense'), ('C', 'Variable expense'), ('D', 'Discretionary expense')]), 'Easy'))

for quiz in quizList:
    print(quiz.question)
    for letter, text in quiz.choices.items():  
        print("{} ({})".format(letter, text))
    answer = input("Choose your answer:")
    question1 = quiz.check_answer(answer)
    print(question1)


# quiz1 = Quiz('Which of the following is a consequence of overdrawing your checking account?', "D", dict([('A', 'Bounced check fee from the store'), ('B', 'Overdraft fee from your bank'), ('C', 'Stress from money mismanagement'), ('D', 'All of the above')]), 'Easy')
# print(quiz1.question)
# for letter, text in quiz1.choices.items():  
#     print("{} ({})".format(letter, text))
# answer = input("Choose your answer:")
# question1 = quiz1.check_answer(answer)
# print(question1)










