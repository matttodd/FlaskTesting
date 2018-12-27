from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Welcome to Flask"

@app.route('/secret')
def hello_secret():
   return "Welcome to (secret) Flask"

if __name__ == '__main__':
   app.run()