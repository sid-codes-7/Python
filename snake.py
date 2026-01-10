from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 500
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

BAD_COLOR = "#8B4513"
LIVES = 5

GHOST_COLOR = "#FFFFFF"
GHOST_LIMIT = 10
AM_I_GHOST = False
GHOST_TIMER = 5

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []   
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            if AM_I_GHOST == True:
                C = GHOST_COLOR
            else:
                C = SNAKE_COLOR
                
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=C, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self, my_tag):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag=my_tag)

class RottenFood:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BAD_COLOR, tag="rotten")

def stop_ghost():
    global AM_I_GHOST
    AM_I_GHOST = False
    canvas.delete("G_MSG")
    for S in snake.squares:
        canvas.itemconfig(S, fill=SNAKE_COLOR)

def run_ghost_timer():
    global GHOST_TIMER
    if AM_I_GHOST == True:
        if GHOST_TIMER > 0:
            GHOST_TIMER = GHOST_TIMER - 1
            canvas.itemconfig("G_MSG", text="GHOST MODE ACTIVE! (" + str(GHOST_TIMER) + "s)")
            window.after(1000, run_ghost_timer)
        else:
            stop_ghost()

def start_ghost():
    global AM_I_GHOST, GHOST_TIMER
    AM_I_GHOST = True
    GHOST_TIMER = 5
    canvas.delete("G_MSG")
    canvas.create_text(350, 30, text="GHOST MODE ACTIVE! (5s)", fill="white", font=("arial", 20), tag="G_MSG")
    for S in snake.squares:
        canvas.itemconfig(S, fill=GHOST_COLOR)  
    run_ghost_timer()

def next_turn(snake, f1, f2, rotten):
    global score, LIVES
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y = y - SPACE_SIZE
    elif direction == "down":
        y = y + SPACE_SIZE
    elif direction == "left":
        x = x - SPACE_SIZE
    elif direction == "right":
        x = x + SPACE_SIZE

    if AM_I_GHOST == True:
        if x < 0:
            x = GAME_WIDTH - SPACE_SIZE
        elif x >= GAME_WIDTH:
            x = 0
        elif y < 0:
            y = GAME_HEIGHT - SPACE_SIZE
        elif y >= GAME_HEIGHT:
            y = 0

    snake.coordinates.insert(0, (x, y))

    if AM_I_GHOST == True:
        C = GHOST_COLOR
    else:
        C = SNAKE_COLOR

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=C)
    snake.squares.insert(0, square)

    if x == f1.coordinates[0] and y == f1.coordinates[1]:
        score = score + 1
        label.config(text="Score: " + str(score) + "     Lives: " + str(LIVES))
        if score % GHOST_LIMIT == 0:
            start_ghost()
        canvas.delete("apple1")
        f1 = Food("apple1")
        
    elif x == f2.coordinates[0] and y == f2.coordinates[1]:
        score = score + 1
        label.config(text="Score: " + str(score) + "     Lives: " + str(LIVES))
        if score % GHOST_LIMIT == 0:
            start_ghost()
        canvas.delete("apple2")
        f2 = Food("apple2")

    elif x == rotten.coordinates[0] and y == rotten.coordinates[1]:
        LIVES = LIVES - 1
        label.config(text="Score: " + str(score) + "     Lives: " + str(LIVES))
        canvas.delete("rotten")
        rotten = RottenFood()
        
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if LIVES <= 0 or check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, f1, f2, rotten)

def change_direction(new):
    global direction
    if new == 'left' and direction != 'right':
        direction = new
    elif new == 'right' and direction != 'left':
        direction = new
    elif new == 'up' and direction != 'down':
        direction = new
    elif new == 'down' and direction != 'up':
        direction = new

def check_collisions(snake):
    if AM_I_GHOST == True:
        return False
    x , y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    for body in snake.coordinates[1:]:
        if x == body[0] and y == body[1]:
            return True
    return False

def game_over():
    global AM_I_GHOST
    AM_I_GHOST = False
    canvas.delete(ALL)
    canvas.create_text(350, 350, font=('consolas', 70), text="GAME OVER", fill="red")
    start_button.place(relx=0.5, rely=0.6, anchor=CENTER)

def start_game():
    start_button.place_forget()
    canvas.delete(ALL)
    
    global snake, f1, f2, rotten, score, direction, AM_I_GHOST, LIVES
    AM_I_GHOST = False
    score = 0
    LIVES = 5
    direction = "down"
    label.config(text="Score: 0     Lives: 5")
    snake = Snake()
    f1 = Food("apple1")
    f2 = Food("apple2")
    rotten = RottenFood()
    next_turn(snake, f1, f2, rotten)

window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score: 0     Lives: 5", font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

start_button = Button(window, text="START GAME", font=('consolas', 20), command=start_game)
start_button.place(relx=0.5, rely=0.45, anchor=CENTER)


canvas.create_text(350, 480, text="RULES!\n1. Brown Apples = Bad!\n2. Green Apples = Good!\n3. Use the GHOST MODE to your advantage\n4. Goodluck and have fun!", 
                   fill="white", font=("arial", 15), justify=CENTER, tag="rules")

window.update_idletasks()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_p = int((screen_width/2) - (window_width/2))
y_p = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x_p}+{y_p}")

window.bind('<Left>', lambda e: change_direction('left'))
window.bind('<Right>', lambda e: change_direction('right'))
window.bind('<Up>', lambda e: change_direction('up'))
window.bind('<Down>', lambda e: change_direction('down'))

window.mainloop()
