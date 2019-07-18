from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/character_creation', methods = ['GET','POST'])
def character_creation():
    if request.method == 'GET':
        return "Please enter a name"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['nickname']
        nickname = vre.decode('utf-8')
        return render_template('character_creation.html', nickname=nickname)

@app.route('/character_stats', methods = ['GET','POST'])
def character_stat():
    if request.method == 'GET':
        return "Please enter a your type of stat"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['stats']
        stats = model.stats(vre.decode('utf-8'))
        return render_template('character_stats.html', stats=stats)

@app.route('/city',methods = ['GET','POST'])
def city():
    if request.method == 'GET':
        return "Click on the city"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['City']
        city = vre.decode('utf-8')
        return render_template('city.html', city=city)
        
@app.route('/forest',methods = ['GET','POST'])
def forest():
    if request.method == 'GET':
        return "Click on the forest"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['Forest']
        forest = vre.decode('utf-8')
        return render_template('forest.html', forest=forest)
        
@app.route('/town',methods = ['GET','POST'])
def town():
    if request.method == 'GET':
        return "Click on the town"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['Town']
        town = vre.decode('utf-8')
        return render_template('town.html', town=town)

@app.route('/enemy',methods = ['GET','POST'])
def enemy():
    if request.method == 'GET':
        return "Click on for enemy"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['enemy']
        enemy = vre.decode('utf-8')
        return render_template('enemy.html', enemy=enemy)
        
@app.route('/enemy2',methods = ['GET','POST'])
def enemy2():
    if request.method == 'GET':
        return "Click on for enemy"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['enemy2']
        enemy2 = vre.decode('utf-8')
        return render_template('enemy2.html', enemy2=enemy2)
@app.route('/fight',methods = ['GET','POST'])
def fight():
    if request.method == 'GET':
        return "Click on to fight"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['fight']
        fight = vre.decode('utf-8')
        return render_template('fight.html', fight=fight)

@app.route('/victory',methods = ['GET','POST'])
def victory():
    if request.method == 'GET':
        return "Click on for a move"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['move']
        victory = vre.decode('utf-8')
        return render_template('victory.html', victory=victory)

@app.route('/index',methods = ['GET','POST'])
def start():
    if request.method == 'GET':
        return "Click on to go home"
    else:
        userdata = formopener.dict_from(request.form)
        vre = userdata['start']
        start = vre.decode('utf-8')
        return render_template('index.html', start=start)
