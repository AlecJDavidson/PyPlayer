import os
import getpass
import enquiries
from pygame import mixer,time

mixer.init() #Initialzing pyamge mixer
music_dir = '/home/'+getpass.getuser()+'/Music/'

global songs_list
songs_list = ['control']
control_options = ['play/pause','stop','next','previous','list','exit']

for dirName, subdirList, fileList in os.walk(music_dir):
	for fName in fileList:
		os.chdir(dirName)
		isFile = os.path.isfile(fName)
		if isFile == True and \
				'.mp3' in fName:
					songs_list.append(fName)


class Control(object):

	def __init__(self):
		self.paused = mixer.music.get_busy()

	def play_pause_toggle(self):
		if self.paused:
			mixer.music.unpause()
		if not self.paused:
			mixer.music.pause()
		self.paused = not self.paused
	
	def stop(self):
		mixer.music.stop()
	
	def next(self,option):
		mixer.music.load(songs_list[songs_list.index(option)+1])
		mixer.music.play()

	def previous(self,option):
		mixer.music.load(songs_list[songs_list.index(option)-1])
		mixer.music.play()
	def exit(self):
		exit()




def song_choice():
	option = enquiries.choose('Choose a song: ', songs_list)
	if option == 'control':
		control_choice(option)
	else:
		print('Now Playing: ',option)
		# clock = time.Clock()
		mixer.music.load(option)
		mixer.music.play()
	control_choice(option)

def control_choice(song):
	CONTROLLER = Control()
	CONTROLLER.play_pause_toggle()
	option = enquiries.choose('Control Options: ', control_options)
	if option == 'list':
		song_choice()
	if option == 'stop':
		CONTROLLER.stop()
	if option == 'play/pause':
		CONTROLLER.play_pause_toggle()
	if option == 'next':
		try:
			CONTROLLER.next(song)
			song = songs_list[songs_list.index(song)+1]
		except:
			pass
	if option == 'previous':
		try:
			CONTROLLER.previous(song)
			song = songs_list[songs_list.index(song)-1]
		except:
			pass
	if option == 'exit':
		CONTROLLER.exit()
	control_choice(song)



def player():
	song_choice()		
player()






			


