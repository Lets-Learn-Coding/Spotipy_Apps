#This is a small script that gets the currently playing song from spotify and removes it from your music library,
#then skips to the next track

#Enjoy cleaning out your music library! This works very well when mapped to an unused macro key on your keyboard.

#Check the readme for more info!

import os
import sys
import spotipy
import spotipy.util as util
import PySimpleGUIWx as sg

def main():
	username = 'XXXXXXXXXXX' 
	scope = "user-read-currently-playing user-library-modify user-modify-playback-state"
	CLIENT_ID = 'XXXXXXXXXXXXXXXXX'
	CLIENT_SECRET = 'XXXXXXXXXXXXXXXXXXXX'
	redirect_uri = "http://google.com/"

	#Authenticate the token using spotipy
	token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)

	#Spotify object
	sp = spotipy.Spotify(auth=token)

	#Gets the data for the currently playing song.
	results = sp.currently_playing()

	#Takes the song from the currently playing dictionary.
	song = results['item']

	#Gets the currently playing song's id and name.
	song_id = song['id']
	song_name = song['name']


	#Takes the song_id and puts it into a list, deletes the track from the music library, and skips to the next song.
	def del_song(song_id):
		del_id = []
		del_id.append(song_id)
		delete_track = sp.current_user_saved_tracks_delete(del_id)
		sp.next_track()

	#Uses PySimpleGuiWX to display the song what was deleted in a system tray bubble
	def sys_tray():
		tray = sg.SystemTray()
		tray.ShowMessage('Spoti_Rem', 'Deleted ' + song_name)
		



	del_song(song_id)
	sys_tray()


main()



