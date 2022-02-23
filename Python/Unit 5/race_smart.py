import turtle as tur
import random as ran
from tkinter import messagebox
def mkboard(t1b,t2b,t3b,t4b,t5b,t6b,t1n,t2n,t3n,t4n,t5n,t6n):
#_________________\n
#|1|{t1n}|{t1b}|\n
#|----------------\n
#|2|{t2n}|{t2b}|\n
#|---------------\n
#|3|{t3n}|{t3b}|\n
#|----------------\n
#|4|{t4n}|{t4b}|\n
#|----------------\n
#|5|{t5n}|{t5b}|\n
#|----------------\n
#|6|{t6n}|{t6b}|\n
#|----------------\n
#
    board = (f"_________________\n|1|{t1n}|{t1b}|\n|----------------\n|2|{t2n}|{t2b}|\n|---------------\n|3|{t3n}|{t3b}|\n|----------------\n|4|{t4n}|{t4b}|\n|----------------\n|5|{t5n}|{t5b}|\n|----------------\n|6|{t6n}|{t6b}|\n|----------------\n")
    return board
def determper(ranum, personal, turtle, ranum2, rl):
    if int(turtle) == 1:
        if rl == 1:
            t1.right(ranum2)
            t1.forward(ranum)
        if rl == 2:
            t1.left(ranum2)
            t1.forward(ranum)
    if int(turtle) == 2:
        if rl == 1:
            t2.right(ranum2)
            t2.forward(ranum)
        if rl == 2:
            t2.left(ranum2)
            t2.forward(ranum)
    if int(turtle) == 3:
        if rl == 1:
            t3.right(ranum2)
            t3.forward(ranum)
        if rl == 2:
            t3.left(ranum2)
            t3.forward(ranum)
    if int(turtle) == 4:
        if rl == 1:
            t4.right(ranum2)
            t4.forward(ranum)
        if rl == 2:
            t4.left(ranum2)
            t4.forward(ranum)
    if int(turtle) == 5:
        if rl == 1:
            t5.right(ranum2)
            t5.forward(ranum)
        if rl == 2:
            t5.left(ranum2)
            t5.forward(ranum)
    if int(turtle) == 6:
        if rl == 1:
            t6.right(ranum2)
            t6.forward(ranum)
        if rl == 2:
            t6.left(ranum2)
            t6.forward(ranum)
        

while True:
    tur.speed(100)
    tur.setheading(0)
    tur.goto(0,0)
    print("start")
    tur.up()
    #tur.left(90)
    tur.forward(200)
    tur.right(90)
    tur.down()
    tur.forward(125)
    tur.right(90)
    tur.up()
    tur.forward(400)
    tur.down()
    tur.right(90)
    tur.forward(125)
    tur.right(90)
    tur.up()
    tur.forward(200)
    tur.right(90)
    tur.forward(125/2)
    tur.right(90)
    tur.up()
    tur.goto(900,900)

    ##line##

    t1 = tur.Turtle()
    t1.speed(100)
    t1.up()
    t1.forward(200)
    t1.right(90)
    forw = 100/6
    t1.forward(forw)
    t1.right(90)
    t1.down()

    ##t2##

    t2 = tur.Turtle()
    t2.speed(100)
    t2.up()
    t2.forward(200)
    t2.right(90)
    forw = 100/6
    t2.forward(forw+forw)
    t2.right(90)
    t2.down()

    ##t3##

    t3 = tur.Turtle()
    t3.speed(100)
    t3.up()
    t3.forward(200)
    t3.right(90)
    forw = 100/6
    t3.forward(forw+forw+forw)
    t3.right(90)
    t3.down()

    ##t4##

    t4 = tur.Turtle()
    t4.speed(100)
    t4.up()
    t4.forward(200)
    t4.right(90)
    forw = 100/6
    t4.forward(forw+forw+forw+forw)
    t4.right(90)
    t4.down()

    ##t5##

    t5 = tur.Turtle()
    t5.speed(100)
    t5.up()
    t5.forward(200)
    t5.right(90)
    forw = 100/6
    t5.forward(forw+forw+forw+forw+forw)
    t5.right(90)
    t5.down()

    ##t6##

    t6 = tur.Turtle()
    t6.speed(100)
    t6.up()
    t6.forward(200)
    t6.right(90)
    f6rw = 100/6
    t6.forward(forw+forw+forw+forw+forw+forw)
    t6.right(90)
    t6.down()

    ##racing##
    game = 1
    cpos1 = 0
    cpos2 = 0
    cpos3 = 0
    cpos4 = 0
    cpos5 = 0
    cpos6 = 0
    t1.color("pink")
    t2.color("green")
    t3.color("blue")
    t4.color("red")
    t5.color("purple")
    t6.color("orange")
    t1.speed(50)
    t2.speed(50)
    t3.speed(50)
    t4.speed(50)
    t5.speed(50)
    t6.speed(50)
    while game == 1:
        random1 = ran.randint(1,20)
        random2 = ran.randint(1,10)
        random3 = ran.randint(1,10)
        random4 = ran.randint(1,10)
        random5 = ran.randint(1,10)
        random6 = ran.randint(1,10)
        person = ran.randint(0,2)
        rl = ran.randint(1,2)
        determper(random1, person, 1, person, rl)
        person = ran.randint(0,2)
        rl = ran.randint(1,2)
        determper(random1, person, 2, person, rl)
        person = ran.randint(0,2)
        rl = ran.randint(1,2)
        determper(random1, person, 3, person, rl)
        person = ran.randint(0,2)
        rl = ran.randint(1,2)
        determper(random1, person, 4, person, rl)
        person = ran.randint(0,2)
        rl = ran.randint(1,2)
        determper(random1, person, 5, person, rl)
        person = ran.randint(0,2)
        rl = ran.randint(1,2)
        determper(random1, person, 6, person, rl)
        
        cpos1 = t1.xcor()
        cpos2 = t2.xcor()
        cpos3 = t3.xcor()
        cpos4 = t4.xcor()
        cpos5 = t5.xcor()
        cpos6 = t6.xcor()
        if int(cpos1) <= -200 or int(cpos2) <= -200 or int(cpos3) <= -200 or int(cpos4) <= -200 or int(cpos5) <= -200 or int(cpos6) <= -200:
            winners = ['','','','','','']
            winners[0] = cpos1
            winners[1] = cpos2
            winners[2] = cpos3
            winners[3] = cpos4
            winners[4] = cpos5
            winners[5] = cpos6
            winners.sort()
            count = -1
            winatlis = ['','','','','','']
            for x in winners:
                count = count+1
                if x == cpos1:
                    winatlis[count] = "pink"
                if x == cpos2:
                    winatlis[count] = "green"
                if x == cpos3:
                    winatlis[count] = "blue"
                if x == cpos4:
                    winatlis[count] = "red"
                if x == cpos5:
                    winatlis[count] = "purple"
                if x == cpos6:
                    winatlis[count] = "orange"
            messagebox.showinfo('information', mkboard(winners[0],winners[1],winners[2],winners[3],winners[4],winners[5],winatlis[0],winatlis[1],winatlis[2],winatlis[3],winatlis[4],winatlis[5]))
            yn = messagebox.askyesno('Play again?', 'Play again?')
            if yn == True:
                tur.reset()
                t1.reset()
                t2.reset()
                t3.reset()
                t4.reset()
                t5.reset()
                t6.reset()
                t1.up()
                t2.up()
                t3.up()
                t4.up()
                t5.up()
                t6.up()
                break
            if yn == False:
                exit()
