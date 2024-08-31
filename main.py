#import the pyttsx3 library for text-to-speech conversion in windows
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

print("Welcome to RoboSpeaker 1.1. Created by Vaishnavi")

# Start an infinite loop to continuously prompt the user
while True:
    # Get input from the user
    x=input("Enter what do you want me to speak?: ")
    # Check if the user wants to quit
    if x == "q":
        # Set a goodbye message
        b = 'bye, see you later :)'
        # Queue the goodbye message to be spoken
        engine.say(b)
        # Run the text-to-speech engine to speak the queued text
        engine.runAndWait()
        # Exit the loop to end the program
        break
    # Queue the user input to be spoken
    engine.say(x)
    # Run the text-to-speech engine to speak the queued text
    engine.runAndWait()
