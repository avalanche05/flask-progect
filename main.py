import json
import os
import random

from PIL import Image
from flask import Flask, url_for, request, render_template, redirect

from Member import Member
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof: str):
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        return render_template('training.html', title="Тренировки в полёте",
                               place='Инженерные тренажеры',
                               image_path=url_for('static', filename='img/tech_place.png'))
    else:
        return render_template('training.html', title="Тренировки в полёте",
                               place='Научные симуляторы',
                               image_path=url_for('static', filename='img/bio_place.png'))


@app.route('/list_prof/<list>')
def list_prof(list):
    if list not in ('ul', 'ol'):
        return 'Простите. Кажется, передаваемый вами параметр не верный. Попробуйте снова.'

    return render_template('list_prof.html', title='Список профессий',
                           professions=['инженер - исследователь', 'пилот', 'строитель',
                                        'экзобиолог', 'врач',
                                        'инженер по терраформированию', 'климатолог',
                                        'специалист порадиационной защите', 'астрогеолог',
                                        'гляциолог',
                                        'инженер жизнеобеспечения', 'метеоролог',
                                        'оператор марсохода',
                                        'киберинженер', 'штурман', 'пилот дронов'],
                           list=list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', info=['Ваня', 'Миша'][::-1])


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = dict()
    data['title'] = 'название'
    data['lastname'] = 'Ильин'
    data['firstname'] = 'Ivan'
    data['education'] = 'education'
    data['profession'] = 'profession'
    data['sex'] = 'sex'
    data['motivation'] = 'motivation'
    data['is_stay'] = 'is_stay'

    return render_template('auto_answer.html', **data)


@app.route('/table/<sex>/<int:age>')
def table(sex: str, age: int):
    return render_template('table.html', sex=sex, age=age,
                           image_path=url_for('static', filename='img/mars.png'))


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'POST':
        f = request.files['file']
        image = Image.open(f)
        image.save(f'static/img/carousel/{hash(f)}.png')

    links = [url_for('static', filename=f'img/carousel/{t}') for t in
             os.listdir('static/img/carousel')]
    return render_template('galery.html', links=links)


@app.route('/members')
def members():
    members = json.load(open('templates/members.json'))
    return render_template('members.html', member=random.choice(members))


def generate_members():
    ivan = Member('Ivan', 'Ilin', 'static/img/members/photo_2021-11-13_21-32-15.jpg',
                  ['актёр', 'программист', 'певец', 'пианист', 'одним словом, балабол'])
    mikhail = Member('Mikhail', 'Glazov', 'static/img/members/photo_2021-06-21_20-21-04.jpg',
                     ['Гид по Канашу', 'спидкубер'])

    members = [ivan, mikhail]
    with open('templates/members.json', 'w') as cat_file:
        json.dump(members, cat_file, default=lambda o: o.__dict__)


generate_members()
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
