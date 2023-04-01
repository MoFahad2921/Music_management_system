# Music_management_system
This is a python based, music management system that will use text file as a database.

This is a Python code that allows a user to manage a music library. The program allows the user to add new songs, display all songs in the library, update/edit information on existing songs, delete songs and generate a random playlist.

The code starts by importing the random module to enable the use of its functions. A text file is created, and its name assigned to the filename variable. A list of integers ranging from 1 to 6 is assigned to the choice variable.

A while loop is used to create a menu that the user can select an option from. A try and except statement is used to ensure that the user inputs a valid integer ranging from 1 to 6.

If the user inputs 1, they are prompted to enter information about the new song they want to add to the library. The information includes the album name, artist name, song title, composer name, genre, release date, and file format. The information is written to the text file in an organized format.

If the user inputs 2, the program reads the contents of the text file and displays them on the console.

If the user inputs 3, the program reads the contents of the text file, stores them in a list of dictionaries, and prompts the user to enter a keyword. The program searches for the keyword in the list of dictionaries and returns all matches. If only one match is found, the program prompts the user to enter new information about the song. If multiple matches are found, the program lists them and prompts the user to select the match they want to edit.

If the user inputs 4, the program prompts the user to enter a keyword. The program searches for the keyword in the list of dictionaries and deletes all matches.

If the user inputs 5, the program generates a random playlist of songs in the library.

If the user inputs 6, the program exits.
