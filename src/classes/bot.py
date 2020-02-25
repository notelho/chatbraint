from flask import jsonify
import aiml
import os

class Bot:

    def __init__(self):
        self.__kernel = aiml.Kernel()
        self.__hasBrain = False
        self.__brain = '.brain/bot_brain.brn'
        self.__command = 'LOAD TESTS FILES'
        self.__aiml = 'src/aiml/tests.xml'

    def load(self):
        if os.path.isfile(self.__brain):
            self.__kernel.bootstrap(brainFile = self.__brain)
        else:
            os.makedirs('.brain')
            self.__kernel.bootstrap(learnFiles = os.path.abspath(self.__aiml), commands = self.__command)
            self.__kernel.saveBrain(self.__brain)
            self.__hasBrain = True
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