class MovieReview:
    def __init__(self,movie,story,actors,music):
        self.movie_name = movie
        self.story_rating = story
        self.actor_rating = actors
        self.music_rating = music
        self.avg = int((self.story_rating + self.actor_rating + self.music_rating) /3)
        self.myrating= {
            "Movie Name" : self.movie_name,
            "Story Rating" : self.story_rating,
            "Actor Rating" : self.actor_rating,
            "Music Rating" : self.music_rating,
            "Avg Rating" : self.avg
        }
    
    def add_movie_review(self,movie_list):
        movie_list.append(self.myrating)
        moviereviews.append(movie_list)
    def avg_star_rating(self,movie_list):
        for movie in movie_list:
            if(movie["Avg Rating"] == 1):
                print("Thanks for the response, you rated the movie with  *")
                print(movie)
global moviereviews

review2 = MovieReview("Beautiful Sound",5,5,5)
review2.add_movie_review(moviereviews)
review2.avg_star_rating(moviereviews)