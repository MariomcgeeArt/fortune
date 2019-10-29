from random import choice
from flask import Flask, request, render_template 


app = Flask(__name__)


pred = ['death', 'connection', 'enlightenment']
@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return """
    <form action='/compliment'>
        <input type="checkbox" name="show_compliments"/>
Show Horoscope
<br/>
        What is your name?
        <input type="text" name="name"></input>
        <button type="submit">
    </form>
    """

@app.route('/compliment')
def get_horoscope():
          
    name = request.args.get('name')
    horoscope = choice(pred)
    return f'Hello {name} Today you recieve {horoscope}!'
    return render_template('index.html')

if __name__ == "__main__":
   app.run(debug=True)