from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with link to Fortune page."""
    return render_template('index.html')

@app.route('/fortune')
def survey():
    """Renders survey for fortune."""
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def results():
    """Renders results for fortune."""
    users_ammount_siblings = request.args.get('siblings',0)
    users_favorite_bevergae = request.args.get('bev')
    users_favorite_animal = request.args.get('animal')
    users_city = request.args.get('city')
    fortune = "fortune"
    if users_ammount_siblings != "" and int(users_ammount_siblings) < 15:
        fortune=("You'll have a magical day!")
    elif users_ammount_siblings != "" and int(users_ammount_siblings) > 15:
        fortune=("You have to many sibilings!")
    elif users_favorite_bevergae == "water":
        return ("You shall live long!")
    elif users_favorite_bevergae == "soda":
        return("Your life is ending and you dont even know it!")
    elif users_favorite_animal == 'Shark':
        return ("Your spirit is hungry...feed it ")
    elif users_city == "San Francisco":
        return(Leave now its a Trap!)

    elif users_city == "Paris":
        return(This city will leave you speachless!)                                         

 
        




    return render_template('fortune_results.html',fortune = fortune )
  