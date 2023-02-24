import json

# initialize empty dictionary for storing movie data
movie_database = {}

# Function to add a new movie to the database
def add_movie():
    title = input("Enter the movie title: ")
    genre = input("Enter the movie genre: ")
    director = input("Enter the name of the director: ")
    release_date = input("Enter the release date of the movie (YYYY-MM-DD): ")
    actors = input("Enter the names of the actors (separated by commas): ")
    actors_list = actors.split(", ")
    
    movie_database[title] = {
        "genre": genre,
        "director": director,
        "release_date": release_date,
        "actors": actors_list
    }
    
    print(f"{title} has been added to the database.")

# Function to edit an existing movie in the database
def edit_movie():
    title = input("Enter the movie title to edit: ")
    if title in movie_database:
        print(f"Current information for {title}:")
        print(json.dumps(movie_database[title], indent=4))
        
        # Prompt user for updated information
        genre = input("Enter the movie genre (or press Enter to keep current value): ")
        director = input("Enter the name of the director (or press Enter to keep current value): ")
        release_date = input("Enter the release date of the movie (YYYY-MM-DD) (or press Enter to keep current value): ")
        actors = input("Enter the names of the actors (separated by commas) (or press Enter to keep current value): ")
        actors_list = actors.split(", ")
        
        # Update the dictionary with the new information
        if genre:
            movie_database[title]["genre"] = genre
        if director:
            movie_database[title]["director"] = director
        if release_date:
            movie_database[title]["release_date"] = release_date
        if actors:
            movie_database[title]["actors"] = actors_list
        
        print(f"{title} has been updated.")
    else:
        print(f"{title} is not in the database.")

# Function to delete a movie from the database
def delete_movie():
    title = input("Enter the movie title to delete: ")
    if title in movie_database:
        del movie_database[title]
        print(f"{title} has been deleted from the database.")
    else:
        print(f"{title} is not in the database.")

# Function to view all movies in the database
def view_all_movies():
    print("All movies in the database:")
    for movie, info in movie_database.items():
        print(f"{movie}: {json.dumps(info, indent=4)}")

# Function to search for a movie based on user-specified criteria
def search_movies():
    print("Search movies in the database:")
    criteria = input("Enter the search criteria: ")
    matches = []
    for movie, info in movie_database.items():
        if criteria in movie or criteria in info["genre"] or criteria in info["director"] or criteria in info["actors"]:
            matches.append(movie)
    if matches:
        print("Matches found:")
        for match in matches:
            print(f"{match}: {json.dumps(movie_database[match], indent=4)}")
    else:
        print("No matches found.")

# Function to save movie data to a file
def save_data():
    filename = input("Enter the filename to save to: ")
    with open(filename, "w") as file:
        json.dump(movie_database, file, indent=4)
    print("Data saved successfully.")

# Function to load movie data from a file
def load_data():
    filename = input("Enter the filename to load from: ")
    with open(filename, "r") as file:
        data = json.load(file)
    global movie_database
    movie_database = data
    print("Data loaded successfully.")

# Main program loop
while True:
    print("\n==== Movie Database Management System ====\n")
    print("1. Add a new movie")
    print("2. Edit an existing movie")
    print("3. Delete a movie")
    print("4. View all movies")
    print("5. Search movies")
    print("6. Save data to file")
    print("7. Load data from file")
    print("8. Exit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        edit_movie()
    elif choice == "3":
        delete_movie()
    elif choice == "4":
        view_all_movies()
    elif choice == "5":
        search_movies()
    elif choice == "6":
        save_data()
    elif choice == "7":
        load_data()
    elif choice == "8":
        exit()
    else:
        print("Invalid choice. Please try again.")
