import pgzrun
from random import randint 
from pgzero.actor import Actor
import pygame
import time

WIDTH = 700
HEIGHT = 600
DOT_MAX_HEIGHT = 400

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
quizList.append( Quiz('Money that comes in or is earned is called ______________', "C", dict([('A', 'Deductions'), ('B', 'Expenses'), ('C', 'Income'), ('D', 'Budget' )]), 'Easy'))
quizList.append( Quiz('When you owe money it is called: ', "C", dict([('A', 'Expenses'), ('B', 'Assets'), ('C', 'Debt'), ('D', 'Liabilities')]), 'Easy'))
quizList.append( Quiz('Money deposited in a financial institution is insured up to:', "A", dict([('A', '$250,000'), ('B', '$500,000'), ('C', '$400,000'), ('D', '$100,000')]), 'Easy'))
quizList.append( Quiz('Which have higher interest rates?', "A", dict([('A', 'Commercial banks'), ('B', 'Credit unions')]), 'Easy'))
quizList.append( Quiz('What is the definition of balanced budget?', "C", dict([('A', 'Goals that take more than a year to accomplish'), ('B', 'Income remaining after deduction of taxes, other mandatory changes, and expenditure on necessary items.'), ('C', 'Planning or budgeting process where total revenues are equal to or greater than total expenses. '), ('D', 'The object of a persons ambtion or effort')]), 'Easy'))
quizList.append( Quiz('What is the definition of needs?', "C", dict([('A', 'Income remaining after deduction of taxes and other mandatory changes available to be spent or saved as ones wishes.'), ('B', 'The object of a persons ambition or effort.'), ('C', 'Something that is required because it is essential or very important.'), ('D', 'A phrase referring to the idea that investors should routinely and automaically put money into savings before spending on anything else')]), 'Easy'))
quizList.append( Quiz('What does PIN stand for?', "A", dict([('A', 'Personal Identification Number '), ('B', 'people in neighborhood'), ('C', 'personal input number'), ('D', 'persons identity name')]), 'Easy'))
quizList.append( Quiz('Connected to the cardholder’s bank account and used for purchases.', "C", dict([('A', 'Credit card'), ('B', 'social security card'), ('C', 'debit card'), ('D', 'insurance card')]), 'Easy'))
quizList.append( Quiz('Who is responsible for confirming your bank account balance? ', "B", dict([('A', 'the stores where you made the purchases from the account'), ('B', 'you'), ('C', 'your bank or credit union'), ('D', 'the debit card company')]), 'Easy'))
quizList.append( Quiz('You have searched everywhere for your debit card. You think it may have been stolen. Of the following actions, what is the best thing to do now?', "D", dict([('A', 'Wait at least 90 days to report the card as missing or stolen in case you find the card.'), ('B', 'Close your bank account.'), ('C', 'File a report with the Federal Trade Commission.'), ('D', 'Notify the company that issued your card')]), 'Easy'))
dots = []

lines = []

next_dot_clicked = 0

next_dot = 0

# Loop from number 0 to number 14
for dot in range(0, 14):
    #this line will create a new Actor using the image of the dot in the images folder
    actor = Actor("dot")
    #this will ensure that the dots appear at least 20 pixels away from the edge of the screen so the whole dot is shown. 
    actor.pos = randint(20, DOT_MAX_HEIGHT - 20), \
    randint(20, DOT_MAX_HEIGHT - 20)
# this will add a new item to the list, which the item is actor, the actor represents the dots on the screen. 
    dots.append(actor)
#defines the function draw 
def draw():
    global next_dot_clicked
    # this sets the background color to black 
    screen.fill("black")
    # this creates a variable to keep track of the current number label
    number = 1 
    #all the lines in the for loop draw each dot on the screen along the number label
    for dot in dots:
        screen.draw.text(str(number), \
                        (dot.pos[0], dot.pos[1] + 12))
        #this executes the code that will draw the dots out 
        dot.draw()
        #the value of the number of a dot is increased by 1 when a new one is drawn on the screen
        number = number + 1 
    #this line of code below in the for loop wil draw the lines on the screen
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))
# this if statement checks the value of a dot, and if the value of the dot is greater than 0, than it will display a question that is selected from the quizList which matches the value of the dot clicked by the user.
    if next_dot_clicked != 0:
        # this line draws the question selected from the quizList list based on the value of a dot that the user has clicked on.
        quiz = quizList[next_dot_clicked - 1]
        screen.draw.text(quiz.question, \
                        (20, 500), color="white")
        y = 520
        for letter, text in quiz.choices.items():
            screen.draw.text(("{} ({})".format(letter, text)), (20, y), color="white")
            y += 20

        pygame.display.flip()

        waitForInput = True
        while waitForInput:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode.lower() == quiz.answer.lower():
                        screen.draw.text("Correct", (20, 480), color="green")
                        if next_dot_clicked == 13:
                            screen.draw.text("YOU WIN", (200, 300), color="green", fontsize=100)
                        pygame.display.flip()
                    else:
                        screen.draw.text("YOU LOSE", (200, 300), color="red", fontsize=100)
                        pygame.display.flip()
                        time.sleep(5)
                        pygame.quit()
                        exit()
                    waitForInput = False

        #this line of code is the value of the variable next_dot_clicked when the user has not clicked another dot besides the first one
        next_dot_clicked = 0

#the line of code in the def function is to let the function change the values of the global variables next_dot and lines.
def on_mouse_down(pos):
    global next_dot
    global lines
    global next_dot_clicked 
    #this line checks if the player has clicked on the next dot in the sequence.
    if dots[next_dot].collidepoint(pos):
        #this line checks if the player has already clicked on the first dot.
        if next_dot:
            #this draws a line betweeen the current dot and the previous one
            lines.append((dots[next_dot -1].pos, dots[next_dot].pos))
            next_dot_clicked = next_dot
        #this sets next_dot to the next number
        next_dot = next_dot + 1
    #the lines below set the next_dot back to the first dot and deletes all the lines if the player clicks on the wrong dot on the screen.
    else:
        lines = []
        next_dot_clicked = 0
        next_dot = 0
    
def on_key_down(key):
    if key == keys.ESCAPE:
        pygame.quit()
        exit()

pgzrun.go()
