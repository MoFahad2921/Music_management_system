# final_assignment
# importing the random module to use the random function:
import random

# Creating a text file:
filename = 'musicInfo_StudentID.txt'

choice = [1, 2, 3, 4, 5, 6]
print('Welcome, hope your day is as musical as ours!\n')
# Using while True statement to loop back at main menu:
while True:
    print('[1]Add songs\n'
          '[2]Display the entire collection\n'
          '[3]Update/Edit information\n'
          '[4]Delete songs\n'
          '[5]Generate random playlist\n'
          '[6]Exit')
# Using try and except to reduce user errors
    try:
        choice = int(input('Kindly enter 1, 2,3, 4, 5 or 6:\n'))
    except ValueError:
        print('Invalid input!')

# Using if and elif statements for user choice(1, 2, 3, 4, 5, 6)
# Adding new songs
    if choice == 1:
        print('In order to add a song, fill up the information below:\n')
        f = open('musicInfo_StudentID.txt', 'a')
# Prompting user to enter all the information:
# Using .lower() to handle any potential errors related to capslock:
        album = input('Name of the album:\n').lower()
        artist = input('Name of the artist:\n').lower()
        song_title = input('Name of the song:\n').lower()
        composer = input('Name of the song composer:\n').lower()
        genre = input('What is the genre of the song:\n').lower()
        release_date = input('When was the song released:\n')
        file_format = input('Enter whether the format is physical or digital:\n').lower()
# Putting the user entered information in organized format in the text file:
        f.write(album + '|' + artist + '|' + song_title + '|' + composer + '|' +
                genre + '|' + release_date + '|' + file_format + '\n')
        f.close()


# Display all
    elif choice == 2:
        print('Displaying all collections...\n')
# opens the text file in read mode
        f = open('musicInfo_StudentID.txt', 'r')
        print(f.read())
        f.close()


# Update information
    elif choice == 3:

        # Opening the file in read mode for scanning matching contents\:
        with open('musicInfo_StudentID.txt', 'r') as file:
            # Reading the contents of the line and separating them(album, artist and song_title):
            database_contents = file.readlines()
        database = []
        # Using line.strip().split('|') to explain format of line and use it as condition
        # Entering all 7 elements so that the line is not ignored
        for line in database_contents:
            album, artist, song_title, composer, genre, release_date, file_format = line.strip().split('|')

# Using append to edit file:
            database.append({
                'album': album,
                'artist': artist,
                'song_title': song_title,
                'composer': composer,
                'genre': genre,
                'release_date': release_date,
                'file_format': file_format,
            })
# Prompting user to enter any of the keywords:
        lookup = input('Enter album, artist or song title:')

# Connecting the lookup user input with the text file contents:
        matching_entries = []
        for entry in database:
            if lookup.lower() in entry['album'] or \
                    lookup.lower() in entry['artist'] or \
                    lookup.lower() in entry['song_title']:
                matching_entries.append(entry)

# Using IF/ELIF for the probability of handling more than one result:
# Using the len function to set up range:
        if len(matching_entries) == 1:
            entry = matching_entries[0]
# Creating new identifier names for the updated contents:
            new_album = input(f"Enter new album name for '{entry['album']}': ") or entry['album']
            new_artist = input(f"Enter new artist name for '{entry['artist']}': ") or entry['artist']
            new_title = input(f"Enter new title for '{entry['song_title']}': ") or entry['song_title']
            new_composer = input(f"Enter new composer for '{entry['composer']}': ") or entry['composer']
            new_genre = input(f"Enter new genre for '{entry['genre']}': ") or entry['genre']
            new_release_date = input(f"Enter new release date for '{entry['release_date']}': ") or entry['release_date']
            new_file_format = input(f"Enter file format(physical/digital) for "
                                    f"'{entry['file_format']}': ") or entry['file_format']
            entry['album'] = new_album
            entry['artist'] = new_artist
            entry['song_title'] = new_title
            entry['composer'] = new_composer
            entry['genre'] = new_genre
            entry['release_date'] = new_release_date
            entry['file_format'] = new_file_format
            print('Entry updated successfully!')

# Using index and enumerate to enumerate and select the matching data in lines:

        elif len(matching_entries) > 1:
            print(f'Multiple matches found for{lookup}:')
            for index, entry in enumerate(matching_entries):
                print(f"{index + 1}. {entry['album']} by {entry['artist']} ({entry['song_title']})")
            selection = int(input('Enter the number of the entry to update: ')) - 1
            entry = matching_entries[selection]
            new_album = input(f"Enter new album name for '{entry['album']}': ") or entry['album']
            new_artist = input(f"Enter new artist name for '{entry['artist']}': ") or entry['artist']
            new_title = input(f"Enter new title for '{entry['song_title']}': ") or entry['song_title']
            new_composer = input(f"Enter new composer for '{entry['composer']}': ") or entry['composer']
            new_genre = input(f"Enter new genre for '{entry['genre']}': ") or entry['genre']
            new_release_date = input(f"Enter new release date for '{entry['release_date']}': ") or entry['release_date']
            new_file_format = input(f"Enter file format(physical/digital) for "
                                    f"'{entry['file_format']}': ") or entry['file_format']
            entry['album'] = new_album
            entry['artist'] = new_artist
            entry['song_title'] = new_title
            entry['composer'] = new_composer
            entry['genre'] = new_genre
            entry['release_date'] = new_release_date
            entry['file_format'] = new_file_format
            print('Entry updated successfully!')
# Using else in error handling in case no matches are found:
        else:
            print('No match found:/')
# Opening the file in write mode to update th data entered by the user
        with open('musicInfo_StudentID.txt', 'w') as file:
            for entry in database:
                file.write(f"{entry['album']}|{entry['artist']}|{entry['song_title']}|{entry['composer']}"
                           f"|{entry['genre']}|{entry['release_date']}|{entry['file_format']}\n")


# Delete songs
    elif choice == 4:
        with open('musicInfo_StudentID.txt', 'r') as file:
            data = file.readlines()
        for i, line in enumerate(data):
            print(f'{i+1}.{line.strip()}')
        index = int(input('Enter the number of the record you want to delete:')) - 1
# Handling anomalies and errors that a user might add:
        if i < index or i > index:
            print('out of range!')
            break
# deletes the data of the chosen index number
        del data[index]
        with open('musicInfo_StudentID.txt', 'w') as file:
            file.writelines(data)


# Generate 10 random songs
    elif choice == 5:

        # Making a list and using random sample to choose 10 random elements from the list:

        lst = ('Perfect by Ed Sheeran', '2002 by Anne Marie', 'rockstar by Post Malone',
               'baby by Justin Bieber', 'baby blue by Badfinger', 'sunflower by Post Malone',
               'alone by Alan Walker', 'faded by Alan walker', 'shape of you by Ed Sheeran',
               'ciao adios by Anne Marie', 'dream on by Aerosmith', 'beautiful people by Ed Sheeran',
               'be with you by Akon', '7 years old by Lukas Graham', 'The Real Slim Shady by Eminem',
               'No love by Eminem', 'Without me by Eminem', 'Mocking bird by Eminem')
        print(random.sample(lst, 10,))


# Exit
    elif choice == 6:
        # Prints message and uses break to end the code:
        print('Bye bye!')
        break
