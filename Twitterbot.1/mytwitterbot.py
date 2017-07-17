from twython import Twython, TwythonError
import time
import random
import itertools

APP_KEY = 'wB0ZQMOqahM6JgSEC25RFRyER'
APP_SECRET = 'OgLDvC5t7vthOHwqJJPuOdGAq3s1wLS2YFGXavVqjPMtlfW2cM'
OAUTH_TOKEN = '885239009949212677-XLUdQqUm6RLlMsig7xktJdXc0rPiTf0'
OAUTH_TOKEN_SECRET = 'LWMqG0bR5IO1gWG0KSC9QYp7cGSDQVunsaSk8ut8Lnj3k'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:

	with open('liners.txt', 'r+') as tweetfile:
		buff = tweetfile.readlines()

	last = ""

	def newset():
		shuffled_buff = buff[:]
		random.shuffle(shuffled_buff)
		return shuffled_buff

	for line in itertools.chain(
			itertools.cycle(
				(newline for newline in newset() if newline != last)
			)
		):
		last = line
		line = line.strip(r'\n')
		if len(line)<=140 and len(line)>0:
			print ("Tweeting...")
			twitter.update_status(status=line)
			time.sleep(7200)
		else:
			print ("Skipped line - Char length violation")
			continue
	print ("No more lines to tweet...")


except TwythonError as e:
	print (e)