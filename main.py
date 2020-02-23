# import aiml

# # Create the kernel and learn AIML files
# kernel = aiml.Kernel()
# kernel.learn("std-startup.xml")
# kernel.respond("load aiml b")

# # Press CTRL-C to break this loop
# while True:
#     print kernel.respond(raw_input("Enter your message >> "))

import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
    print kernel.respond(raw_input("Enter your message >> "))

    while True:
        message = raw_input("Enter your message to the bot: ")
        if message == "quit":
            exit()
        elif message == "save":
            kernel.saveBrain("bot_brain.brn")
        else:
            bot_response = kernel.respond(message)
            # Do something with bot_response