from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

DISS= [
  'cabbage', 'asshat', 'cheetobrain', 'monkeybutt', 'fartface'
]

@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Hello</a><html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    options_str = ''
    for compliment in AWESOMENESS:
      option = '<option value="' + compliment + '">' + compliment + '</option>'
      options_str += option

    html =  """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <h3>Get a compliment:</h3>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <select name="compliment">
            %s
          </select>
          <input type="submit">
        </form>
        <h3>Get a diss:</h3>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          
          <input type="submit">
        </form>
      </body>
    </html>
    """ % options_str

    return html


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def diss_person():
  player = request.args.get("person")
  diss = choice(DISS)
  return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're a(n) %s!
      </body>
    </html>
    """ % (player, diss)
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
