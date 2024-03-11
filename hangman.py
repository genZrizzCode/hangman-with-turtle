import turtle
import random
import time
t = turtle.Turtle()
print('Only lowercase letters!\n')
wordbank = [ 'smith', 'dog', 'yes', 'okay', 'sunday', 'we', 'cat', 'impacc', 'remote', 'wrong', 'short', 'video', 'super', 'idol' ]

LETTERS_START_POS = [-100, -200]
DRAWMAN_SPEED = 1

# Start Turtle
def init_turtle():    
    t.width(3)
    t.speed(0)
    t.hideturtle()

last_man_pos = None
def draw_gallow():
    global last_man_pos
    # Gallow
    t.up()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.down()
    t.forward(50)
    t.backward(25)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.right(90)

    last_man_pos = t.pos()

def write_text(text):
    t.write(text, False, font=("monospace", 35, "normal"))
    prev_direction = t.heading()
    t.setheading(180)
    t.forward(-50)
    t.setheading(prev_direction)

def draw_answer_lines():
    t.up()
    t.goto(LETTERS_START_POS[0], LETTERS_START_POS[1])

    
    for i in answer:
        write_text('__ ')

def reveal_letter(letter, position):
    t.up()
    t.speed(0)
    t.goto(LETTERS_START_POS[0], LETTERS_START_POS[1])

    for i in range(0, position):
        write_text('__ ')

    write_text(' ' + letter)
    t.speed(DRAWMAN_SPEED)

def printFinalText(text):
    time.sleep(3)
    t.clear()
    t.goto(0, 0)
    t.write(text, True, "center", font=("Verdana", 100, "bold"))
    
def drawMan(x):
    global last_man_pos
    
    if last_man_pos is not None:
        t.goto(last_man_pos[0], last_man_pos[1])
        
    guess = x
    t.speed(DRAWMAN_SPEED)
    t.down()
    if guess == 1:
        # Head
        t.circle(20, 360)
        t.left(90)
        t.up()
        t.forward(40)
        t.down()
    elif guess == 2:
        # Torso
        t.forward(80)
        t.backward(70)
        t.left(30)
    elif guess == 3:
        # (Your right) Right arm
        t.forward(55)
        t.backward(55)
        t.right(60)
    elif guess == 4:
        # Left arm
        t.forward(55)
        t.backward(55)
        t.left(30)
        t.forward(70)
    elif guess == 5:
        # Right leg
        t.left(20)
        t.forward(65)
        t.backward(65)
        t.right(40)
    elif guess == 6:
        # Left leg
        t.forward(65)

    t.up()

    last_man_pos = t.pos()
    

answer = random.choice(wordbank)
correct = list(answer)

init_turtle()
draw_gallow()
draw_answer_lines()


# Functionality
correctGuess = []
incorrect = []
right = 0
wrong = 0
check = 0
checkcheck = 0
terminate = False

MAX_WRONG_GUESSES = 6
remaining_answer = list(answer)
remaining_wrong_guesses = MAX_WRONG_GUESSES
incorrect_guesses = []

def find_nth_occurrence(haystack, needle, occurrence):
    occurrence_count = 0
    
    for index, char in enumerate(haystack):
        if char == needle:
            if occurrence_count == occurrence:
                return index

            occurrence_count += 1

    return -1


def draw_answer_lines():
    t.goto(-100, -200)
    t.showturtle()
    for i in answer:
        t.write('_ ', True, font=("Verdana", 35, "normal"))
    t.goto(-75,125)
    t.right(90)
    t.down()

def get_letter_input():
    while True:
        input_txt = turtle.textinput("HANGMAN", "Guess a lowercase letter:")
        input_txt = '' if input_txt is None else input_txt.strip()

        if len(input_txt) == 0 or not input_txt.isalpha():
            print('Enter a letter!')
            continue
        
        return input_txt[0].lower()

while True:
    letter = get_letter_input()

    if letter in incorrect_guesses:
        print('You have already tried that one!')
        continue
    
    # correct
    if letter in remaining_answer:
        occurrence_count = 0
        while letter in remaining_answer:
            position = find_nth_occurrence(answer, letter, occurrence_count)
            remaining_answer.remove(letter)
            reveal_letter(letter, position)
            occurrence_count += 1
        print('Correct!')
    # wrong
    else:
        remaining_wrong_guesses = remaining_wrong_guesses - 1
        incorrect_guesses.append(letter)
        drawMan(MAX_WRONG_GUESSES - remaining_wrong_guesses)
        print('Incorrect!')

    if remaining_wrong_guesses < 1:
        printFinalText('You Lose!\n      😥')
        print('You lose!\n😥')
        time.sleep(5)
        break

    if len(remaining_answer) < 1:
        printFinalText('You Win!\n      😁')
        print('You win!\n😁')
        time.sleep(5)
        break
    



# while wrong < 6 and not terminate:
#     letter = turtle.textinput("HANGMAN", "Guess a lowercase letter:")
#     if letter in answer:
#         correctGuess.append(letter)
#         print('Correct!')
#         print(correctGuess)
#         print(answer.index(letter) + 1)
#         right += 1
#         if right == len(answer):
#             print('You Win!')
#             print('Answer:', answer)
#             break
#     elif letter in incorrect:
#         print('You already guessed that')
#     else:
#         wrong += 1
#         print('Incorrect!')
#         drawMan(wrong)
#         incorrect.append(letter)
#         if wrong == 6:
#             print('Game Over!!!')
#             print('Answer:', answer)
#             drawMan(6)
#             time.sleep(5)
#             exit(0)
