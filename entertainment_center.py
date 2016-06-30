import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
                        
#print (toy_story.storyline)
avatar = media.Movie("Avatar",
                    "A machine on an alien planet.",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)