try:
    def cls():
        import os
        os.system("clear")
    cls()
    import time
    print("\nHow to Play :- \n In this game you have to bet on a turtle\n If your selected turtle wins the race you won the challange\n Don't worry it is easy to play")
    print("\n\nAvailable turtles are :-\n'red'\n'blue'\n'green'\n'gold'\n'cyan'\n'orange'\n'purple'\n'pink'")
    print("\n\nYOur Game Will Start within 10s")

    time.sleep(8.5)
    import turtle as t
    import random
    screen = t.Screen()
    screen.bgcolor("black")
    screen.setup(1000,700)

    is_race_on = False

    colors = ['red','blue','green','gold','cyan','orange','purple','pink']


    y_posiotions = [-150,-100,-50,0,50,100,150,200]
    all_turtles = []
    user_bet = screen.textinput(title="Make you bet",prompt="which turtle will win the race ?? Enter a color : ")
    print(f"I got it you have bet on {user_bet}")

    for i in range(0,8):
        new_turtle = t.Turtle("turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-450,y=y_posiotions[i])
        all_turtles.append(new_turtle)

    # print(all_turtles)

    if user_bet:
        is_race_on = True
    else:
        print("\npls try again and enter any colour")

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor()>450:
                is_race_on = False
                turtle_col = turtle.pencolor()
                if turtle_col==user_bet:
                    print(f"\nYou won! , the {turtle_col} turtle is winner !")
                else:
                    print(f"\nYou lost ! , the {turtle_col} turtle is winner !")
            random_distance = random.randint(0,10)
            turtle.fd(random_distance)


    print("\n\nAbout:\nGame Owner - @Erupted_Lava \nThank you for playing my game don't forget to rate this game to Erupted_lava\nIf you find any kind of bug while playing you can report it at https://t.me/Hackingzzzz")

    screen.exitonclick()

except Exception as e:
    print(f"ERROR")
    