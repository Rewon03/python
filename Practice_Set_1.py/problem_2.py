#download any external module using pip and use it.

# I am gonna download a module which generate  text into voice.

#pip install pyttsx3 (this line of command used to download external module)

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# write anything inside the double quote and engine generate voiceover of that text
engine.say("That's cool. Now I am able to speak like real human on earth. Thanks human coz i don't believe god because human are the creator of me.")
engine.runAndWait()