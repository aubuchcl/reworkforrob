# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

""" This has been so much fun making. I really hope anyone who tries this 
enjoys it as much as I did creating it. """

shaun_of_the_dead = media.Movie(
    "Shaun Of The Dead",
    "A man decides to turn his moribund life around by winning back his\
     ex-girlfriend, reconciling his relationship with his mother,\
     and dealing with an entire community that has returned from the dead to eat\
     the living.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/Shaun-of-the-dead.jpg/220px-Shaun-of-the-dead.jpg",  # noqa
    "https://youtu.be/LIfcaZ4pC-4")

cabin_in_the_woods = media.Movie(
    "The Cabin In The Woods",
    "A great Horror Film that has a ton of Cthulhu Mythos that is just\
     wonderful.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/84/The_Cabin_in_the_Woods_%282012%29_theatrical_poster.jpg/215px-The_Cabin_in_the_Woods_%282012%29_theatrical_poster.jpg",  # noqa
    "https://youtu.be/NsIilFNNmkY")

swordfish = media.Movie(
    "Swordfish",
    '"The Greatest and Most Accurate Hacker movie ever!" - Kim Jon Un',
    "https://upload.wikimedia.org/wikipedia/en/e/e8/Swordfish_movie.jpg",
    "https://youtu.be/63qtYi1nwcs")

the_dark_tower = media.Movie(
    "The Dark Tower",
    "In a world full of superheroes, there`s only one Gunslinger.",
    "https://upload.wikimedia.org/wikipedia/en/4/49/The_Dark_Tower_teaser_poster.jpg",  # noqa
    "https://youtu.be/GjwfqXTebIY")

deadpool = media.Movie(
    "Deadpool",
    "Armed with his new abilities and a dark, twisted sense of humor,\
     Deadpool hunts down the man who nearly destroyed his life.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Deadpool_poster.jpg/220px-Deadpool_poster.jpg",  # noqa
    "https://youtu.be/FyKWUTwSYAs")

sunspring = media.Movie("Sunspring",
                        "A short film written by an Artificial Intelligence.",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQl_YIno5VZmyZoaCNJp7LGMqNZ8AgzfnP-OKRD0cT32tLWO0SLLw",  # noqa
                        "https://youtu.be/LY7x2Ihqjmc")

movies = [shaun_of_the_dead, cabin_in_the_woods,
          swordfish, the_dark_tower, deadpool, sunspring]

# This function opens up a web page in your that displays the movies.
fresh_tomatoes.open_movies_page(movies)
