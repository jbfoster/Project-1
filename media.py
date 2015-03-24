#This file defines the movie class
import webbrowser

class Movie():
    #This class contains a movie's title, two actors, and links to the movie poster and trailer
    def __init__(self, movie_title, movie_actor1, movie_actor2, poster_image, trailer_youtube):
        self.title = movie_title
        self.lead_actor = movie_actor1
        self.supporting_actor = movie_actor2
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
