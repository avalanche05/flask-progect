from flask import Flask, url_for, request, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
