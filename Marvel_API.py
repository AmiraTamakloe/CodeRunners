import csv
import imdb

# movie database
movies_database = imdb.IMDb()
#print(dir(movies_database))

#search title
MCU_Comics = ["Iron Man", "The Incredible Hulk", "Iron Man 2", "Thor", "Captain America: The First Avenger", "Marvel's The Avengers",
              "Iron Man 3", "Thor: The Dark World", "Captain America: The Winter Soldier", "Guardians of the Galaxy", "Avengers: Age of Ultron",
              "Ant-Man","Captain America : Civil War", "Doctor Strange", "Guardians of the Galaxy Vol. 2", "Spider-Man: Homecoming",
              "Thor: Ragnarok", "Black Panther", "Avengers: Infinity War", "Ant-Man and the Wasp", "Captain Marvel", "Avengers: Endgame",
              "Spider-Man: Far From Home","Black Widow", "Shang-Chi and the Legend of the Ten Rings", "Eternals", "Spider-Man: No Way Home"]

title_list = []
year_list = []
directors_list = []
casting_list = []
genre_list = []
main_actor_name_list = []
main_actor_birthdate_list = []
main_actor_height_list = []
main_actor_trivia_list = []
main_actor_titlerefs_list = []

for marvel_movie in MCU_Comics :

    movies = movies_database.search_movie(marvel_movie)
    print(f'Searching for : {marvel_movie}')
    """for movie in movies:
        title = movie['title']
        year = movie['year']
        print(f'{title} - {year}')
        print(movies[0].keys())
        break"""

    #list movie info
    id = movies[0].getID()
    movie = movies_database.get_movie(id)
    #list of movie info i want
    title = movie['title']
    year = movie['year']
    directors=movie['directors']
    casting = movie['cast']
    genre = movie['genres']
    direcStr = ' '.join(map(str,directors))
    actors = ', '.join(map(str,casting))

    # putting all the movie info in a list
    title_list.append(title)
    year_list.append(year)
    directors_list.append(direcStr)
    casting_list.append(actors)
    genre_list.append(genre)

    # list actor info put 0 to takeonly the first element in the list
    id = casting[0].getID()
    person = movies_database.get_person(id)
    bio = movies_database.get_person_biography(id)

    name = person['name']
    birthDate = person['birth date']
    height = person['height']
    trivia = person['trivia']
    titleRefs = bio['titlesRefs']
    titleRefsStr= ', '.join(map(str, titleRefs))

    # putting all the main character info in a list
    main_actor_name_list.append(name)
    main_actor_birthdate_list.append(birthDate)
    main_actor_height_list.append(height)
    main_actor_trivia_list.append(trivia)
    main_actor_titlerefs_list.append(titleRefsStr)


zippedlist = list(zip(title_list,year_list,directors_list,casting_list,genre_list,
                      main_actor_name_list, main_actor_birthdate_list, main_actor_height_list, main_actor_trivia_list,
                      main_actor_titlerefs_list))

with open("marvel.csv", "w") as marvel :
    marvel_writer = csv.writer(marvel, delimiter=",")
    for line in zippedlist:
        marvel_writer.writerow(line)
    marvel.close()