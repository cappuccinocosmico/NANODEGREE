
class Movie(object):
	"""docstring for Movie"""
	def __init__(self):
		super(Movie, self).__init__()
	def trailer_youtube_url(self):
		return self.trailer_youtube_url
	def poster_image_url(self):
		return self.poster_image_url
	def poster_image_url(self,url):
		self.poster_image_url=url
	def title(self):
		return self.title
	def title(self,title):
		self.title=title
	def trailer_youtube_url(self,url):
		self.trailer_youtube_url=url
# def test():
# 	MovieList=[Movie('STAR WARS:  A New Hope'),Movie('Star Wars: The Empire Strikes Back')] 
# 	for movie in MovieList:
# 		print movie.title
# 		movie.poster_image_url="http://somewhere.com"
# 		print movie.poster_image_url
# 	print (create_movie_titles_content(MovieList))
# test()