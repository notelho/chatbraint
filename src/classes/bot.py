from flask import jsonify
import aiml
import os

class Bot:

    def __init__(self):
        self.__kernel = aiml.Kernel()
        self.__hasBrain = False
        self.__brain = '.brain/bot_brain.brn'
        self.__command = 'LOAD STARTUP FILES'
        self.__aiml = 'src/aiml/tests.xml'
        # self.__command = 'load aiml b'
        # self.__aiml = 'src/aiml/std-startup.xml'

    def load(self):
        if os.path.isfile(self.__brain):
            self.__kernel.bootstrap(brainFile = self.__brain)
        else:
            os.makedirs('.brain')
            self.__kernel.bootstrap(learnFiles = os.path.abspath(self.__aiml), commands = self.__command)
            self.__kernel.saveBrain(self.__brain)
            self.__hasBrain = True

        # def getSessionData(self, sessionID = None):

        # setTextEncoding(self, encoding):
        # """Set the text encoding used when loading AIML files (Latin-1, UTF-8, etc.)."""

    #     def getBotPredicate(self, name):
    #     """Retrieve the value of the specified bot predicate.
    #     If name is not a valid bot predicate, the empty string is returned.        
    #     """


    # def setBotPredicate(self, name, value):
    #     """Set the value of the specified bot predicate.

    #     If name is not a valid bot predicate, it will be created.


        return self.__hasBrain

    def loaded(self):
        return self.__hasBrain

    def save(self):
        self.__kernel.saveBrain(self.__brain)

    def ask(self, message):
        return jsonify(
            {
                'status':'OK',
                'answer': self.__kernel.respond(message)
            }
        )