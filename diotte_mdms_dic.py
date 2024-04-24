'''
Amare Diotte
Data Engineering
2024-RTT-107
GLAB-340.6.1: Python Dictionary
'''

import typing
import json

# this function takes the existing db as a parameter and adds a new entry via user input
def add_movie(movie_db: dict[str, list[str]]) -> None:
    title: str = input("Enter Title: ")
    genre: str = input("Enter Genre: ")
    director: str = input("Enter Director Name: ")
    release_date: str = input("Enter Release Date (YYYY-MM-DD): ")
    actors: str = input("Enter the names of actors, separated by a comma: ")
    # split string of actor names into a list
    actors_list: list[str] = actors.split(", ")
    
    movie_db[title] = {
        "genre": genre,
        "director": director,
        "release_date": release_date,
        "actors": actors_list
    }
    print(title, "has been added to the database.")

# this function takes existing db as parameter and returns nothing; it updates an existing entry in DB
def edit_movie(movie_db: dict[str]) -> None:
    title: str = input("Enter the title of the movie you'd like to edit: ")
    if title in movie_db:
        print("Here is the current information for this title:")
        print(movie_db[title])

        genre: str = input("Enter the movie genre (or press Enter to keep current value):")
        director: str = input("Enter the name of the director (or press Enter to keep current value): ")
        release_date: str = input("Enter the release date of the movie (YYY-MM-DD) (or press Enter to keep current value): ")
        actors: str = input("Enter the name of the actors (separated by commas) (Or press Enter to keep current value):")
        

        if genre:
            movie_db[title]["genre"] = genre
        if director:
            movie_db[title]["director"] = director
        if release_date:
            movie_db[title]["release_date"] = release_date
        if actors:
            actors_list = actors.split(", ")
            movie_db[title]["actors"] = actors_list
        print(title, "has been updated")
    else:
        print(title, "is not in the database")

# this function takes the existing db as a parameter and a deletes an entry based on user input
def delete_movie(movie_db: dict[str, list[str]]) -> None:
    title = input("Enter the title of the movie you would like to delete: ")
    if title in movie_db:
        del movie_db[title]
        print(title, "has been deleted!")
    else:
        print("Sorry,", title, "is not in the database.")


# this function takes the db as parameter, takes user input for search term and 
# prints list of matching entries to terminal
def search_movies(movie_db: dict[str, list[str]]) -> None:
    search_param = input("Enter your search criteria: ")
    print("Searching database...")
    matches: list[str, list[str]] = []
    for movie, info, in movie_db.items():
        if search_param in movie \
        or search_param in info["genre"] \
        or search_param in info["director"] \
        or search_param in info["actors"]:
            matches.append(movie)
        
        if matches:
            print("Matches found: ")
            for match in matches:
                print(f"{match}: {json.dumps(movie_db[match], indent=4)}")
                input("Hit ENTER to continue")
        else:
            print("no matches found")

# takes existing database as a parameter and updates/adds entries from the file given in user input
def load_data(movie_db: dict[str, list[str]]) -> dict[str, list[str]]:
    filename = input("Enter the filename to load from: ")
    with open(filename, "r") as file:
        data = json.load(file)
    movie_db.update(data)
    print("Data loaded")
    return movie_db

# saves existing database to a file, user specifies the file name via input
def save_data(movie_db: dict[str, list[str]]) -> None:
    filename: str = input("Enter filename to save to: ")
    with open(filename, "w") as file:
        json.dump(movie_db, file, indent = 4)
    print("Data saved!")

# displays all movies in the current database on terminal in JSON format
def view_all_movies(movie_db: dict[str, list[str]]) -> None:
    print("All movies in database: ")
    for movie, info in movie_db.items():
        print(f"{movie}: {json.dumps(info, indent=4)}")

# gets user input from terminal and returns the integer indicating their choice
def get_action() -> int:
    print("=====*** Welcome to the Movie Database ***=====")
    print(" 1. Add movie\n", "2. Edit movie\n", "3. Delete movie\n",
          "4. Search movies\n", "5. View All Movies\n", "6. Load data\n", 
          "7. Save data\n", "8. Exit")
    choice: int = int(input("Please enter a number: "))
    return choice

# main loop of the games, this continues until the use presses 8 to exit
def main_loop():
    movie_db: dict[str, list[str]] = {}
    game_running: bool = True
    while game_running:
        action: int = get_action()

        match action:
            case 1:
                add_movie(movie_db)
            case 2:
                edit_movie(movie_db)
            case 3:
                delete_movie(movie_db)
            case 4:
                search_movies(movie_db)
            case 5:
                view_all_movies(movie_db)
            case 6:
                movie_db = load_data(movie_db)
            case 7:
                save_data(movie_db)
            case 8:
                game_running = False
            case _:
                print("Please enter a number ")

    print("Goodbye!")

main_loop()