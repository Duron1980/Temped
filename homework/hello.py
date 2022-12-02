from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

class Name_form(FlaskForm):
    city_name = StringField('Enter the name of city', validators=[InputRequired()])
    submit = SubmitField('Show weather')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Name_form()
    api_id = '0107cbd8cd431b1dbff7f14411b36127'
    city_name = form.city_name.data
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_id}&units=metric')
    temperature = response.json()['main']['temp']
    return render_template('index.html', form=form, temperature=temperature, city_name=city_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)