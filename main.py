from flask import Flask, url_for, request, render_template, redirect

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


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = dict()
    data['title'] = 'название'
    data['lastname'] = 'Ilin'
    data['firstname'] = 'Ivan'
    data['education'] = 'education'
    data['profession'] = 'profession'
    data['sex'] = 'sex'
    data['motivation'] = 'motivation'
    data['is_stay'] = 'is_stay'

    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
