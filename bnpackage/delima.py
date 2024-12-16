import os

def justine_delima():
    favorite_songs = []

    class Song:
        def __init__(self, name, genre, artist): # Constructor
            self.name = name
            self.genre = genre
            self.artist = artist

        def display_full_details(self): # Method 1
            print("\n---- Current Song Details ----")
            print(f"Song Name: {self.name}")
            print(f"Genre: {self.genre}")
            print(f"Artist: {self.artist}")
            print("------------------------------\n")

            input("Press enter to return.")
            
        def add_song_details(self): # Method 2
            Song.clear_song_details(self)

            print("\nAdd Song Details:")
            
            song_name = input("\nEnter the name of the song: ")
            self.name = song_name.title()
            
            song_genre = input("Enter the genre of the music: ")
            self.genre = song_genre.title()
            
            song_artist = input("Enter the name of the artist: ")
            self.artist = song_artist.title()

            print("\nSong details has been added.")
            input("\nPress enter to return.")
            
        def clear_song_details(self): # Method 3
            self.name = ""
            self.genre = ""
            self.artist = ""
            
            print("Song details has been cleared.")
            input("\nPress enter to return.")

        def add_to_favorites(self): # Method 4
            if self.name == "":
                print("Please add a song name.")
                input("\nPress enter to return.")
                return
            
            if self.name in favorite_songs:
                print(f"{self.name}'s already in favorites.")

                print("\nFavorite Songs:")
                for song in favorite_songs:
                    print(f"- {song}")
                
                input("\nPress enter to return.")
                return
            
            favorite_songs.append(self.name)
            print(f"{self.name}'s added to favorites.\n")
            
            print("Favorite Songs:")
            for song in favorite_songs:
                print(f"- {song}")

            input("\nPress enter to return.")

        def remove_from_favorites(self): # Method 5
            if self.name == "":
                print("Please add a song name.")
                return
            
            if self.name not in favorite_songs:
                print(f"{self.name}'s not in favorites.\n")
                
            if self.name in favorite_songs:
                favorite_songs.remove(self.name)
                print(f"{self.name}'s removed from favorites.\n")

            print("Favorite Songs:")
            for song in favorite_songs:
                print(f"- {song}")
            
            input("\nPress enter to return.")
            
        def menu(self):
            choice = 0
            while True:
                print("\n- The Menu works like a playlist/player.")
                print("You can list the songs you want")
                print("and add it to your favorite songs.\n")

                print("\n--------- Menu ----------")
                print("[1] Display Song Details")
                print("[2] Add Song Details")
                print("[3] Clear Song Details")
                print("[4] Add to favorites")
                print("[5] Remove from favorites")
                print("[6] Back to main menu")
                print("-------------------------")

                try :
                    choice = int(input("Enter your choice: "))
                except ValueError:
                    print("\nYou need to input numbers (1-6).")

                os.system('cls')
                match choice:
                    case 1: # Song Info
                        self.display_full_details()
                    case 2: # Add song info
                        self.add_song_details()
                    case 3: # Clear song info
                        self.clear_song_details()
                    case 4: # Add to favorites
                        self.add_to_favorites()
                    case 5: # Remove
                        self.remove_from_favorites()
                    case 6: # Return to main menu
                        return
                    case _:
                        print("Invalid choice.")
                        input("Please press enter to return.")
                os.system('cls')

    current_song = Song(name="", genre="", artist="")
    current_song.menu()