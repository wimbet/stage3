import fresh_tomatoes
import media
                    
what_about_bob = media.Movie("What About Bob",
                                "Bob's a special kind of friend. The kind that drives you crazy.",
                                "https://upload.wikimedia.org/wikipedia/en/8/84/What_About_Bob_film.jpg",
                                "https://www.youtube.com/watch?v=ptmP1lziJw4",
                                "https://www.youtube.com/watch?v=Da-I28T8TKE")
                                
westworld = media.Movie("Westworld",
                            "Boy have we got a vacation or you...where nothing can possibly go wrong.",
                            "http://comicbookinvest.com/wp-content/uploads/2015/07/westworld-poster.jpg",
                            "https://www.youtube.com/watch?v=pmbYjVy9Xcg",
                            "https://www.youtube.com/watch?v=coVCSMfJiVk")
                            
planes_trains_autos = media.Movie("Planes, Trains, and Automobiles",
                                    "What he really wanted was to spend Thanksgiving with his family. What he got was three days with the turkey.",
                                    "https://s-media-cache-ak0.pinimg.com/736x/15/d0/c3/15d0c3566a2d29e8218d59ee8cf10ec3.jpg",
                                    "https://www.youtube.com/watch?v=VWGqGHMO294",
                                    "https://www.youtube.com/watch?v=wyw0DjWTe6M")

cube = media.Movie("Cube",
                    "The walls are closing in.",
                    "https://upload.wikimedia.org/wikipedia/en/0/0c/Cube_The_Movie_Poster_Art.jpg",
                    "https://www.youtube.com/watch?v=HYoTGYT0-I4",
                    "https://www.youtube.com/watch?v=YAWSkYqqkMA")
                            
battle_royale = media.Movie("Battle Royale",
                            "42 Students. Only one way to survive.",
                            "http://www.movie-poster-artwork-finder.com/posters/battle-royale-poster-artwork-tatsuya-fujiwara-aki-maeda-taro-yamamoto.jpg",
                            "https://www.youtube.com/watch?v=N0p1t-dC7Ko",
                            "https://www.youtube.com/watch?v=tgFt63qpD80")
                            
cool_hand_luke = media.Movie("Cool Hand Luke",
                            "The man..and the motion picture that simply do not conform.",
                            "https://mattmulcahey.files.wordpress.com/2014/04/cool-hand-luke-poster.jpg",
                            "https://www.youtube.com/watch?v=q111bDVYNXk",
                            "https://www.youtube.com/watch?v=L53DSdhjczc")

movies = [what_about_bob, westworld, planes_trains_autos, battle_royale, cool_hand_luke, cube]
fresh_tomatoes.open_movies_page(movies)