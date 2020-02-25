# import aiml
# import os

# kernel = aiml.Kernel()

# if os.path.isfile("bot_brain.brn"):
#     kernel.bootstrap(brainFile = "bot_brain.brn")
# else:
#     kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
#     kernel.saveBrain("bot_brain.brn")

# # kernel now ready for use
# while True:
#     message = raw_input("Enter your message to the bot: ")
#     if message == "quit":
#         exit()
#     elif message == "save":
#         kernel.saveBrain("bot_brain.brn")
#     else:
#         bot_response = kernel.respond(message)
#         print bot_response


# ==================================

# def getSessionData(self, sessionID = None):

# setTextEncoding(self, encoding):
# """
# Set the text encoding used when loading AIML files (Latin-1, UTF-8, etc.).
# """

# def getBotPredicate(self, name):
# """
# Retrieve the value of the specified bot predicate.
# If name is not a valid bot predicate, the empty string is returned.
# """

# def setBotPredicate(self, name, value):
# """Set the value of the specified bot predicate.
# If name is not a valid bot predicate, it will be created.
# """
