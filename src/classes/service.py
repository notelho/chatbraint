from flask import Flask, render_template, request, jsonify
from bot import Bot
import os

class Service:

    def __init__(self):
        self.__bot = Bot()

    def template(self):
		return render_template('chat.html')

    def message(self): 

        if not self.__bot.loaded():
            self.__bot.load()

        return self.__bot.ask(
            request
                .form['msg']
                .encode('utf-8')
                .strip())