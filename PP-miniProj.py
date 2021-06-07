#importing required packages
from tkinter import *
import tkinter.messagebox as tmsg
import random

#dimensioning the window layout and adding title
game = Tk()
game.geometry('1500x800')
game.title('7 Up 7 Down game python mini project')
#bg = PhotoImage(file ="final/hello.jpg")
#game.config(bg = "orange")
#game.wm_iconbitmap("OIP.jpeg")

#creating a label for dice rolling display
label = Label(game, text='', font=('rockwell', 260),)
roll_label = Label(game, text='', font=('rockwell', 30))

#creating a frame for rules and other details
f1 = Frame(game, bg = "yellow", bd = 30)
f1.pack(side = LEFT, fill = "y")
names_label = Label(f1, text = " Done by:- \nArchit Yadav \n Anilesh Duraphe \n Nish Salia", font="rockwell 15 ", bg = "cyan")
names_label.pack(side = BOTTOM)
rule_label = Label(f1, text = "--- Welcome to the game of 7UP & 7DOWN --- \n\nBefore you begin,\n"
                              "let me help you with this game!\n--\nTwo dice will be rolled. \n "
                              "Before rolling, you have to give your call\n"
                              "whether 7UP or 7DOWN.\n--\nThe addition of numbers on\n both the dice will be your score.\n--\n"
                              "If the score is just as you\npredicted, then Congrats!\n YOU WIN or else YOU LOSE! \n\n---- Goodluck ----\n\n"
                              "\nPlease enter your name below\n",
                                bg = "yellow", font="rockwell 15")

rule_label.pack()

#entry widget for accepting player name
inputname = Entry(f1)
inputname.pack()

#making the score variable
Score = 0

score_label = Label(game, text=("Score:", Score), font=("rockwell", 55), bg = "light blue")
score_label.pack(side = BOTTOM)


# tasks
def path():
    def tasks():
        p = inputname.get()
        Set = ["Pretend you are chicken for 30 seconds", "Crack a lame joke", "Spin 10 times","Post 'I AM A LOSER' on instagram",
               "Try to walk on hands","Show your chats to everyone","Run in circle for 30 seconds",
               "Hold an ice cube in your hand for 20 seconds","tell the most embarrasing thing about yourself",]
        choice_task = random.choice(Set)
        a = tmsg.askokcancel("CHALLENGE", choice_task)
#        print(a)
    def tasks1():
        Set = ["Do 5 push ups","Fill a bottle using its cap","Compliment a stranger","Truth or dare?"]
        choice_task = random.choice(Set)
        a = tmsg.askokcancel("CHALLENGE", choice_task)
    def tasks2():
        Set = ["Draw a flower blindfolded","Mimic anyone present around you",
               "'I slit the sheet, the sheet I slit, and on the slitted sheet I sit.'-say this 3 times",
               "Make the first five emoji faces that you have used recently."]
        choice_task = random.choice(Set)
        a = tmsg.askokcancel("CHALLENGE", choice_task)

    if Score <= -2:
        tasks()

    elif Score >= 10:
        tasks1()

    elif Score == 7:
        tasks2()


#defining function related to score
def scorelogequal():
    global Score
    Score += 3
    score_label.configure(text=("Score:", Score))
    print(Score)

def scorelogplus():
    global Score
    Score += 2
    score_label.configure(text=("Score:", Score))
    print(Score)

def scorelogminus():
    global Score
    Score -= 1
    score_label.configure(text=("Score:", Score))
    print(Score)

def scorereset():
    global Score
    Score = 0
    score_label.configure(text=("Score:", Score))
    print(Score)

#defining a function for dice rolling stimulation
#for seven up
def roll_diceb1():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680': 1, '\u2681': 2, '\u2682': 3, '\u2683': 4, '\u2684': 5, '\u2685': 6}
    die1_roll = random.choice(dice)
    die2_roll = random.choice(dice)
    inp = inputname.get()
    path()

    label.configure(text=f'{random.choice(die1_roll)} {random.choice(die2_roll)}')
    label.pack()
    if d[die1_roll] + d[die2_roll] == 7:
        roll_label.configure(text=f'{inp} you get 3pts! It is exact 7.')
        roll_label.pack()
        scorelogequal()
        
    elif d[die1_roll] + d[die2_roll] > 7:
        roll_label.configure(text=f'{inp} you get 2pts! It is more than 7.')
        roll_label.pack()
        scorelogplus()
        
    else:
        roll_label.configure(text=f'{inp} you lose 1pt! It is less than 7.')
        roll_label.pack()
        scorelogminus()

#for seven down
def roll_diceb2():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680': 1, '\u2681': 2, '\u2682': 3, '\u2683': 4, '\u2684': 5, '\u2685': 6}
    die1_roll = random.choice(dice)
    die2_roll = random.choice(dice)
    inp = inputname.get()
    path()
    label.configure(text=f'{random.choice(die1_roll)} {random.choice(die2_roll)}')
    label.pack()
    if d[die1_roll] + d[die2_roll] == 7:
        roll_label.configure(text=f'{inp} you get 3pts! It is exact 7.')
        roll_label.pack()
        scorelogequal()
    
    elif d[die1_roll] + d[die2_roll] < 7:
        roll_label.configure(text=f'{inp} you get 2pts! It is less than 7.')
        roll_label.pack()
        scorelogplus()
        
    else:
        roll_label.configure(text=f'{inp} you lose 1pt! It is more than 7.')
        roll_label.pack()
        scorelogminus()


#making button widgets and giving them specific commands
b1 = Button(game, text='7-UP', background="white", foreground='blue', font = "rockwell 15 bold" ,command=roll_diceb1, height = 2, width = 10, pady = 10, padx = 15)
b1.place(x = 650, y = 550)

b2 = Button(game, text='7-DOWN', background="white", foreground='blue', font = "rockwell 15 bold" ,command=roll_diceb2, height = 2, width = 10, pady = 10, padx = 15)
b2.place(x = 900, y = 550)

br = Button(game, text='Reset', background="white", foreground='red', font = "rockwell 15 bold" ,command = scorereset, height = 2, width = 10, pady = 10, padx = 15)
br.place(x = 1150, y = 550)

b3 = Button(game, text = "Exit", background="white", foreground='blue', font = "rockwell 15 bold" ,command=quit, height = 2, width = 5, pady = 10, padx = 15)
b3.place(x = 650, y = 700)

#creating a function for accepting the feedback from the user
def suggest_function():
#    print("hello")
    a = tmsg.askquestion("Feedback", "Was your experience good?")
    if a == "yes":
        msg = "Great, enjoy the game..."
    else:
        msg = "Thank you for your feedback..."
    tmsg.showinfo("Experience", msg)
    print(a)

#menu for displaying option for feedback
Smenu = Menu(game)
Smenu.add_command(label = "Feedback", command = suggest_function)
game.config(menu = Smenu)

game.mainloop()








