import movie
import fresh_tomatoes

social_network = movie.Movie(	"The Social Network", "http://tinyurl.com/z7ascry", 
								"https://www.youtube.com/watch?v=2RB3edZyeYw")
internship = movie.Movie(		"The Internship",  "http://tinyurl.com/jck4n6j", 
								"https://www.youtube.com/watch?v=cdnoqCViqUo")
inception = movie.Movie(		" The Inception",  "http://tinyurl.com/za7f966",
								"https://www.youtube.com/watch?v=YoHD9XEInc0")
shawshank = movie.Movie(		"The Shawshank Redemption",  "http://tinyurl.com/gnnxfh9",
								"https://www.youtube.com/watch?v=6hB3S9bIaco")
dark_knight = movie.Movie(		"The Dark Knight",  "http://tinyurl.com/h4kzr89",
								"https://www.youtube.com/watch?v=EXeTwQWrcwY")
godfather = movie.Movie(		"The Godfather",  "http://tinyurl.com/gwlngmj",
								"https://www.youtube.com/watch?v=sY1S34973zA&t=2s")
movies = [social_network, internship, inception, shawshank, dark_knight, godfather]

# Generate the page to display the movies
fresh_tomatoes.open_movies_page(movies)