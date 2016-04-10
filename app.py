from movie import *
import fresh_tomatoes

# Create instances of the Movie class to hold information of my favourite movies
toy_story = Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "1995",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = Movie(
    "Avatar", 
    "A marine on an alien planet",
    "2009",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

back_to_the_future = Movie("Back to the Future",
                                 "A young man is accidentally sent 30 years into the past in a time-traveling DeLorean.",
                                 "1985",
                                 "http://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                                 "https://www.youtube.com/watch?v=yosuvf7Unmg")

zootopia = Movie("Zootopia",
                    "One day, Judy Hopps, a rabbit from rural Bunnyburrow, fulfills her dream of joining the Zootopia Police Department as the first rabbit officer.",
                    "2016",
                    "http://vignette4.wikia.nocookie.net/disney/images/2/2f/Zootopia_Poster.jpg/revision/latest/scale-to-width-down/1000?cb=20160120182926",
                    "https://www.youtube.com/watch?v=yCOPJi0Urq4")

skyfall = Movie("Skyfall",
                    "Bond's loyalty to M is tested when her past comes back to haunt her. Whilst MI6 comes under attack, 007 must track down and destroy the threat, no matter how personal the cost.",
                    "2009",
                    "https://pmcdeadline2.files.wordpress.com/2012/11/skyfall1__121102130802.jpeg",
                    "https://www.youtube.com/watch?v=6kw1UVovByw")

spectre = Movie("Spectre",
                    "Spectre nudges Daniel Craig's rebooted Bond closer to the glorious, action-driven spectacle of earlier entries, although it's admittedly reliant on established 007 formula.",
                    "2015",
                    "https://resizing.flixster.com/bge5cBo2JzPccJcOqW8m5sNPdUg=/800x1185/v1.bTsxMTIwMzM3NDtqOzE3MDQzOzIwNDg7OTYwOzE0MjI",
                    "https://www.youtube.com/watch?v=z4UDNzXD3qA")


# Add the instances to a list
movies = [
    toy_story,
    avatar,
    back_to_the_future,
    zootopia,
    skyfall,
    spectre
]

# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)