try:
    import time
    import os
    import random
    os.chdir("/home/sarthak/Main/Extra/Programing/python program/Python from starting/Day of code ( udemy )/day 19 of code/")
    def cls():
        
        os.system("clear")
    cls()
    number = random.randint(1,11)
    from pytube import YouTube
    import requests

    url = input("Enter the video url correctly :\n")
    my_video = YouTube(url)

    print("************Video Title**************\n\n")
    print(my_video.title)

    choice = input("\n\nDo you want to downlaod video thumbnail also ???\n")

    if "yes"==choice.lower():
        print("We got it your work will be done , just relaxx ")
        a = requests.get(my_video.thumbnail_url)

        with open(f"thumbnailxxr3{number}nx.png","wb")as f:
            f.write(a.content)

    if choice.lower()=="no":
        print("ok sir as you wish")

    print("++++++++++++++++ Finally downloading the video ++++++++++++++++++")
    for _ in range(10):
        time.sleep(0.1)
        print("Donloading.............")
    my_video.streams.get_highest_resolution().download()

    print("Done")
except Exception as e:
    print("Error lol")
