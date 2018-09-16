from emotion import emotion
import webbrowser
import json
import os
import numpy as np
from gtts import gTTS


class Emotion_Handler:

	def __init__(self):
		self.openfile1 = open("./res/comps.json");
		self.openfile2 = open("./res/compliments.json");
		self.comps = json.load(self.openfile1);
		self.comps1 = json.load(self.openfile2);

		self.tts = gTTS(text='Hello, and thank you for using me.', lang='en');

		self.myState = emotion();


	def sad(self):
		tts = gTTS(text='Hey, you should take a walk today and clear your mind. Come back, and see me later!', lang='en')
		tts.save("./res/good.mp3");
		os.system("mpg123 ./res/good.mp3");
		#Text Message
		#webbrowser.open('https://www.google.com/search?q=cute+puppies&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjarPOSor_dAhUSXK0KHcdPDdIQ_AUIDigB&biw=890&bih=980', 2);

		#Text Message
		#Also cute puppies

	def happy(self):
		choice = np.random.choice(len(self.comps['compliments']), 1);
		tts = gTTS(text=self.comps['compliments'][choice[0]], lang='en');
		tts.save("./res/good.mp3");
		os.system("mpg123 ./res/good.mp3");
		#Positive Reinforcement
		#Encouragement...and reward 

	def neutral(self):
		choice = np.random.choice(len(self.comps1['anytime']), 1);
		tts = gTTS(text=self.comps1['anytime'][choice[0]], lang='en');
		tts.save("./res/good.mp3");
		os.system("mpg123 ./res/good.mp3");

	def angry(self):
		webbrowser.open('https://www.google.com/search?q=cute+puppies&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjarPOSor_dAhUSXK0KHcdPDdIQ_AUIDigB&biw=890&bih=980', 2);
		tts = gTTS(text='Hey, take time to breathe slowly and deeply today.', lang='en');
		tts.save("./res/good.mp3");
		os.system("mpg123 ./res/good.mp3");

	def surprise(self):
		pass;

	def disgust(self):
		pass;

	def fear(self):
		pass;

	def run_func(self):
		if self.myState == 'happy':
			self.happy();
		elif self.myState == 'sad':
			self.sad();
		elif self.myState == 'neutral':
			self.neutral();
		else:
			self.angry();


if __name__ == '__main__':
	j = Emotion_Handler();
	j.run_func();
	
	
