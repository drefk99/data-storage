#first import urllib for downloading the file
import urllib.request
import zipfile
import os
import pandas as pd

DEBUG = True

# This is the URL  for the public data
url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

# This is the working directory
working_dir = "./data/movies/" #"/home/administradorcito/Documentos/data-storage/data/movies/"

# Destination filename
file_name = working_dir + "movies.zip"

# Download the file from 'url' and save it locally under 'file_name:
if os.path.isfile(file_name):
	print('Data is already Downloaded')
else:
	print('Downloading file')
	urllib.request.urlretrieve(url, file_name)

# We already know rge expected files so:
expected_files = ['links.csv', 'movies.csv', 'ratings.csv', 'README.txt', 'tags.csv']

# There's an extra dir leve in the extracted file
inner_dir = "ml-latest-small/"

# I wnat to know the names of the extracted files
file_names = os.listdir(working_dir + inner_dir)

if file_names == expected_files:
	print("You already have the data files, check it!")
else:
	

	# This is the code for uncompress the zip file
	path_to_zip_file = working_dir + "movies.zip"
	# Reference to zipfile
	zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
	print("Extracting Files")
	zip_ref.extractall(working_dir)
	# Is importante to use .close()
	zip_ref.close()

#movie.ID mv.ID MV.ID MV-ID
print(file_names)
movie_names = ['movie_id', 'tittle', 'genres']
rating_names = ['user_id', 'movie_id', 'rating', 'timestamp']

#Reading the files needed 
movies = pd.read_csv(working_dir + 
	inner_dir +
	expected_files[1], sep = ','
	names = movie_names)
ratings = pd.read_csv(working_dir +
	inner_dir +
	expected_files[2],
	sep = ',', 
	names = rating_names)

# Reading the files needed for this analysis
movies = pd.read_csv(working_dir + inner_dir + expected_files[1], sep = ',')
ratings = pd.read_csv(working_dir + inner_dir + expected_files[2], sep = ',')

## Let's print the first lines of each dataframe
if DEBUG:
	print(movies.head())
	print(ratings.head())

print("The names of our new data frames are:")
print(list(movies.columns.values))
print(list(ratings.columns.values))

print("The dimension of the data frames are:")
print(movies.count())
print(ratings.count())

rate_movies = pd.merge(movies, ratings, on = 'movie_id')
rate_movies =  rated_movies.sort_values('rating', ascending = False)

#number of movies: 9126
#number fo evaluations: 10005

top20 = rated_movies.head(20)

# Rated movies names:
#['movie_id', 'tittle', 'genres', 'user_id', 'rating', timestamp']
for i in range(5):
	title = top20[i]['title']
	for j in rated_movies:
		if rated_movies[j]['title'] == title:
			top5_dict[title] = rated_movies[j]


print(rated_movies.head(20))
if DEBUG:
	print(list(rated_movies.columns.values))

