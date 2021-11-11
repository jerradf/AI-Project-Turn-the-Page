# The project is a simple AI project to control the presentation slides by the speaker's speech content. 

#For instance, if the last sentence of one page is "Thank you very much". Then the AI should listen to it and trigger a keyboard event to open the next page. 

# Project infomation: 
# Open the Presentation file in Python
# Everytime there is a last sentence at the end of the page, wait for a specific keyboard event to move to the next slide.
# The output is console-based.

# There are a few requirements to this.
# The file must be of suffix ".pptx"
# The file must be in the directory of this project.

import presentation
import speech_detect

#speech_detect.listen()

p = -1
while p == -1:
    f = input("Enter the name of the powerpoint file (e.g. \"example1.pptx\"): ")
    p = presentation.open_presentation(f)
    if p == -1:
        print("Please open a valid presentation file.")

presentation.display_text(p)
