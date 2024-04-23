'''
Amare Diotte
Data Engineering
2024-RTT-107
GLAB-340.6.1: Python Dictionary
'''

import typing

# this function takes the existing db as a parameter and adds a new entry via user input
def add_movie(movie_db: list[str, list[str]]) -> None:
    title: str = input("Enter Title: ")
    genre: str = input("Enter Genre: ")
    director: str = input("Enter Director Name: ")
    release_date: str = input("Enter Release Date: ")
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

# this function takes no parameters and returns nothing; it updates an existing entry in DB
def edit_movie() -> None:
    print("Movie edited")


def delete_movie() -> None:
    print("Movie deleted")

def search_movies() -> None:
    print("Movies Found")

def load_data() -> None:
    print("Data loaded")

def save_data() -> None:
    print("Data saved")

def get_action() -> int:
    print("=====*** Welcome to the Movie Database ***=====")
    print(" 1. Add movie\n", "2. Edit movie\n", "3. Delete movie\n",
          "4. Search movies\n", "5. View All Movies\n", "6. Load data\n", "7. Save data\n", 
          "8. Exit")
    choice: int = int(input("Please enter a number: "))
    return choice

def main_loop():
    movie_db: {str} = {}
    game_running: bool = True
    while game_running:
        action: int = get_action()

        match action:
            case 1:
                add_movie(movie_db)
            case 2:
                print("Edit Movie")
            case 3:
                print("Delete Movie")
            case 4:
                print("Search movies")
            case 5:
                print("View All Movies")
            case 6:
                print("Load Data")
            case 7:
                print("Save Data")
            case 8:
                game_running = False
            case _:
                print("Please enter a number ")

    print("Goodbye!")



main_loop()