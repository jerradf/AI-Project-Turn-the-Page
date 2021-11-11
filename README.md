# AI-Project-Turn-the-Page
Great Introductory AI Project that demonstrates events being controlled strictly by speech detection.

AI Project: Turn The Page
Overview:

The project is a simple AI project to control the presentation slides by the speaker's speech content. For instance, if the last sentence of one page is "Thank you very much". Then the AI should listen to it and trigger a keyboard event to open the next page. 

Important installation steps:
	
(Mac)
	Ensure that Homebrew is installed.
	Install XCode (this will take a while):
Go to https://developer.apple.com/download/all/. You are going to need your Apple ID for this step. If you don’t have one, it is free to create one.
Download “Xcode” in the latest version on the website.
Download “Command Line Tools for Xcode”.
Follow the instructions for installing portaudio: https://macappstore.org/portaudio/
xcode-select --install 
brew remove portaudio 
brew install portaudio 
pip3 install pyaudio
pip3 install SpeechRecognizer
pip3 install keyboard
pip3 install pynput
pip3 install python-pptx
	
	

(Windows/Linux)
pip install SpeechRecognizer
pip install keyboard
pip install python-pptx
pip install pipwin 
pipwin install pyaudio

--------------------------------------------------------------


The Pseudocode for the program is the following:
- Open presentation
- While the presentation is open/not finished;
Display the slide’s info in the console output.
Listen for the last sentence (store this as a value and continuously listen for the last sentence in a slide).
If the microphone catches the entire phrase that equals the last sentence in a slide:
Call for a keyboard event (ENTER) 
While keyboard event not pressed to continue:
			Pause all actions (do nothing!)
