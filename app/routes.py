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
