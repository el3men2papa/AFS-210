from queue import Queue
import random

# Song Class
#region
class Song():
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
#endregion

# Queue Class
#region
class Queue:
    def __init__(self, current_song_index=0, currently_playing=False):
        self.items = []
        self.set_current_song_index(current_song_index)
        self.set_currently_playing(currently_playing)

    def set_current_song_index(self, index):
        self.current_song_index = index

    def set_currently_playing(self, currently_playing):
        self.curently_playing = currently_playing

    def add_song(self, song):
        if self.size() > 0:
            self.items.insert(self.size() + 1, song)
        else:
            self.items.insert(0, song)

    def size(self):
        return len(self.items)

    def play(self, song_index):

        self.current_song_index = song_index
        
        self.set_currently_playing(True)
        
        print("\nPlaying....")

        print(self.items[self.current_song_index])

    def show_play_list(self):
        num = 1

        print("\nSong list:\n")

        for item in self.items:
            print(str(num) + '. ' + str(item))
            num += 1

    def show_current_song(self):
        print("\nCurrently playing:")

        print(self.items[self.current_song_index])

    def next(self):
        
        print('Currently Playing: ', self.curently_playing)
        
        playlist = len(self.items) - 1

        if self.current_song_index == playlist:
            next_song = 0
        else:
            next_song = self.current_song_index + 1

        print("\nSkipping....")

        self.play(next_song)

    def prev(self):
        playlist = len(self.items) - 1

        if self.current_song_index == playlist:
            prev_song = 0
        else:
            prev_song = self.current_song_index - 1

        print("\nReplaying....")

        self.play(prev_song)

    def removeSong(self, title):
        song_index = 0

        for item in self.items:
            if item.title == title:
                break   
            song_index += 1

        self.items.pop(song_index)
        
    def shuffle(self):
        list_length = self.size()
        
        for i in range(list_length):
            
            # pop off the first element and append it to the end of the list
            first_number = self.items.pop(0)
            self.items.append(first_number)
            
            # generate a random number based on the size of the list
            random_num = random.randint(0, list_length - 1)

            # pop off that random element and append to the end of the list
            list_element = self.items.pop(random_num)
            self.items.append(list_element)

#endregion

# Menu 
#region 
def menu():
    print('\n')
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")
    print('\n')
#endregion
    
media_player = Queue()

# Default Playlist
media_player.add_song(Song('The Walk', 'Mayer Hawthorne'))
media_player.add_song(Song('What Lovers Do', 'Maroon 5'))
media_player.add_song(Song('Heartbreaker', 'Mariah Carey'))
media_player.add_song(Song('24K Magic', 'Bruno Mars'))
media_player.add_song(Song('Wifey', 'Next'))
media_player.add_song(Song('Rockit', 'Herbie Hancock'))
media_player.add_song(Song('Dress You Up', 'Madonna'))
media_player.add_song(Song('Midas Touch', 'Midnight Star'))

# Media Player
#region
while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        artist = input('Enter the Song Artist: ')
        title = input('Enter Song title: ')

        # Add song to playlist
        song = Song(title=title, artist=artist)
        media_player.add_song(song)
        
        print("New Song: " + song.title + " Added to Playlist")
        
    elif choice == 2:
    
        # Prompt user for Song Title 
        title = input('Enter the song title to be removed: ')
        
        # remove song from playlist
        media_player.removeSong(title)
        
        print("Song: " + title + " Removed from Playlist")

    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing

        media_player.play(0)
        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing

        media_player.next()
        
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing

        media_player.prev()

    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing

        media_player.shuffle()

        print("Shuffling....")

        media_player.show_play_list()

        media_player.play(0)

    elif choice == 7:

        # Display the song name and artist of the currently playing song
        media_player.show_current_song()

    elif choice == 8:

        # Show the current song list order
        media_player.show_play_list()

    elif choice == 0:

        print("Goodbye.")
        break
#endregion