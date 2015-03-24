#This file uses the movie class imported from media.py to create five instances of movie and initialize their data
import media
import fresh_tomatoes

shawshank_redemption = media.Movie("Shawshank Redemption", "Tim Robbins", "Morgan Freeman",
                                   "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

twelve_monkeys = media.Movie("Twelve Monkeys", "Bruce Willis", "Madeleine Stowe",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Twelve_monkeysmp.jpg/220px-Twelve_monkeysmp.jpg",
                             "https://www.youtube.com/watch?v=kxHvbUo6kD4")

princess_bride = media.Movie("Princess Bride", "Cary Elwes", "Mandy Patinkin",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/d/db/Princess_bride.jpg/220px-Princess_bride.jpg",
                             "https://www.youtube.com/watch?v=VYgcrny2hRs")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind", "Jim Carrey", "Kate Winslet",
                               "http://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                               "https://www.youtube.com/watch?v=lnSgSe2GzDc")

trainspotting = media.Movie("Trainspotting", "Ewan McGregor", "Ewen Bremner",
                            "http://upload.wikimedia.org/wikipedia/en/thumb/7/71/Trainspotting_ver2.jpg/250px-Trainspotting_ver2.jpg",
                            "https://www.youtube.com/watch?v=R2GKVtWsXKY")
                             

movies = [shawshank_redemption, twelve_monkeys, princess_bride, eternal_sunshine, trainspotting]
fresh_tomatoes.open_movies_page(movies)
