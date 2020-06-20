import tkinter

from tkinter import messagebox

import random

# Screen Layout
top = tkinter.Tk()
top.iconbitmap('rps.ico')

top.title("Rock | Paper | Scissor")


userScore = 0
compScore = 0


def Rock():

    """ Rock Function with 3 comparision"""

    global userScore, compScore

    comp = random.randint(1,3)

    if comp == 3:

        comp = "Scissor"

        userScore += 1

        messagebox.showinfo("Congratulation!", "You WIN!! \n""Your Choice:Rock"+"\nComp Choice: " \
                            +comp+"\nYour Score: "+str(userScore)+"\nComputer Score: "+str(compScore))

    elif comp == 1:

        comp = "Rock"

        messagebox.showinfo("Same pinch!!",
                            "IT'S A TIE!! !!\n" + "Your Choice:Rock" + "\nComp Choice: " + comp + "\nYour Score: "
                            + str(userScore) + "\nComputer Score: " + str(compScore))


    else:

        comp = "Paper"

        compScore += 1

        messagebox.showinfo("Hard Luck!!",
                            "YOU LOOSE!!\n" + "Your Choice:Rock" + "\nComp Choice: " + comp + "\nYour Score: "
                            + str(userScore) + "\nComputer Score: " + str(compScore))


def Scissor():

    """ Scissor Function with 3 comparision"""

    global userScore, compScore

    comp = random.randint(1, 3)

    if comp == 2:

        comp = "Paper"

        userScore += 1

        messagebox.showinfo("Congratulation!!",
                            "YOU WIN!!\nYour Choice: Scissor\n" + "Comp choice: " + comp + "\nYour Score: " + str(
                                userScore) + "\nComputer Score: " + str(compScore))

    elif comp == 3:
        
        comp = "Scissor"
        
        messagebox.showinfo("Same pinch!!",
                            "IT'S A TIE!!\nYour Choice: Scissor\n" + "Comp choice: " + comp + "\nYour Score: " + str(
                                userScore) + "\nComputer Score: " + str(compScore))


    else:
        
        comp = "Rock"
        
        compScore += 1
        
        messagebox.showinfo("Hard Luck!!",
                            "YOU LOOSE!!\nYour Choice: Scissor\n" + "Comp choice:" + comp + "\nYour Score: " + str(
                                userScore) + "\nComputer Score: " + str(compScore))

def Paper():
    
    """ Paper Function with 3 comparision"""

    global userScore, compScore

    comp = random.randint(1, 3)

    if comp == 1:

        comp = "Rock"

        userScore += 1

        messagebox.showinfo("Congratulation!!",
                            "YOU WIN!!\nYour Choice: Scissor\n" + "Comp choice: " + comp + "\nYour Score: " + str(
                                userScore) + "\nComputer Score: " + str(compScore))

    elif comp == 2:
        
        comp = "Paper"
        
        messagebox.showinfo("Same pinch!!",
                            "IT'S A TIE!!\nYour Choice: Scissor\n" + "Comp choice: " + comp + "\nYour Score: " + str(
                                userScore) + "\nComputer Score: " + str(compScore))


    else:
        
        comp = "Scissor"
        
        compScore += 1
        
        messagebox.showinfo("Hard Luck!!",
                            "YOU LOOSE!!\nYour Choice: Scissor\n" + "Comp choice:" + comp + "\nYour Score: " + str(
                                userScore) + "\nComputer Score: " + str(compScore))

# Declaring Buttons

B1 = tkinter.Button(top, text = "Rock",bg='red',height="10",width="20", command = Rock)

B2 = tkinter.Button(top, text = "Paper",bg='green',height="10",width="20", command = Paper)

B3 = tkinter.Button(top, text = "Scissor",bg='blue',height="10",width="20", command = Scissor)

B1.pack(side='left')

B2.pack(side='left')

B3.pack(side='left')

top.mainloop()