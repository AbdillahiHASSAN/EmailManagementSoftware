import os
from flask import Flask, render_template, request
# Add other necessary imports here

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Email Management Software!"

if __name__ == '__main__':
    app.run()

