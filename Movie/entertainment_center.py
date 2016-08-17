# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

primer=media.Movie()
primer.title('Primer')
primer.trailer_youtube_url('https://www.youtube.com/watch?v=dfOCp6cW7rQ&ab_channel=Cinedigm')
primer.poster_image_url('http://ia.media-imdb.com/images/M/MV5BMTgwNjY5MDkzOF5BMl5BanBnXkFtZTcwOTAxMTcyMQ@@._V1_UY1200_CR108,0,630,1200_AL_.jpg')

upstreamcolor=media.Movie()
upstreamcolor.title('Upstream Color')
upstreamcolor.trailer_youtube_url('https://www.youtube.com/watch?v=5U9KmAlrEXU&ab_channel=UpstreamColor')
upstreamcolor.poster_image_url('http://assets.erbpfilm.com/images/UC_Poster_for_store_800x800-2.png')

chasingice=media.Movie()
chasingice.title('Chasing Ice')
chasingice.trailer_youtube_url('https://www.youtube.com/watch?v=eIZTMVNBjc4&ab_channel=ExposureLabs')
chasingice.poster_image_url('https://upload.wikimedia.org/wikipedia/en/c/c6/Chasing_Ice_poster.jpg')

source_code=media.Movie()
source_code.title('Source Code')
source_code.trailer_youtube_url('https://www.youtube.com/watch?v=WatVodRARsU&ab_channel=Trailers')
source_code.poster_image_url('https://upload.wikimedia.org/wikipedia/en/e/e5/Source_Code_Poster.jpg')




movies = [primer, upstreamcolor, chasingice, source_code]
fresh_tomatoes.open_movies_page(movies)
