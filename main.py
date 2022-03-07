from PIL import Image
import io

from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '''
Человечество вырастает из детства.</br>

Человечеству мала одна планета.</br>

Мы сделаем обитаемыми безжизненные пока планеты.</br>

И начнем с Марса!</br>

Присоединяйся!'''


@app.route("/promotion_image")
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    <text></br>Вот она какая, красная планета.</text>
                    
                                            <div class="alert alert-secondary" role="alert">
                            Человечество вырастет из детсвтва.
                        </div>
                        <div class="alert alert-success" role="alert">
                            Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                            И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Присединяйся!
                        </div>
                    
                  </body>
                  
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f"""
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet"
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                <title>Пример формы</title>
              </head>
              <body>
                <h1>Анкета претендента</h1>
                <h3>на участие в миссии</h3>
                <div>
                    <form class="login_form" method="post">
                    <input class="form-control" id="second_name" placeholder="Введите фамилию" name="second_name">
                    <input class="form-control" id="first_name" placeholder="Введите имя" name="first_name">
                    <br>
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                    <div class="form-group">
                        <label for="classSelect">Какое у вас образование?</label>
                        <select class="form-control" id="classSelect" name="class">
                          <option>Начальное</option>
                          <option>Среднее</option>
                          <option>Высшее</option>
                          <option>Межгалактическое(не выгнали из Яндекс.Лицея)</option>
                        </select>
                     </div>
                     
                     <div class="form-group">
                            <label for="classSelect">Какие у Вас есть профессии?</label>
                            </br>
                            <input type="checkbox" class="form-check-input" id="1" name="profession"[]>
                            <label class="form-check-label" for="1">Инженер-исследователь</label>
                            </br>
                            <input type="checkbox" class="form-check-input" id="2" name="profession"[]>
                            <label class="form-check-label" for="2">Инженер-строитель</label>
                            </br>
                            <input type="checkbox" class="form-check-input" id="3" name="profession"[]>
                            <label class="form-check-label" for="3">Пилот</label>
                            </br>
                            <input type="checkbox" class="form-check-input" id="4" name="profession"[]>
                            <label class="form-check-label" for="4">Метеоролог</label>
                            </br>
                            <input type="checkbox" class="form-check-input" id="5" name="profession"[]>
                            <label class="form-check-label" for="5">Инженер по жизнеобеспечению</label>
                            </br>
                            <input type="checkbox" class="form-check-input" id="6" name="profession"[]>
                            <label class="form-check-label" for="6">Инженер по радиационной защите</label>
                            </br>
                            <input type="checkbox" class="form-check-input" id="7" name="profession"[]>
                            <label class="form-check-label" for="7">Врач</label>
                            </br>
                            <input type="checkbox" class="form-check-input" id="8" name="profession"[]>
                            <label class="form-check-label" for="8">Экзобиолог</label>
                    </div>
                    
                    <div class="form-group">
                            <label for="form-check">Укажите пол</label>
                            <div class="form-check">
                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                              <label class="form-check-label" for="male">
                                Мужской
                              </label>
                            </div>
                            <div class="form-check">
                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                              <label class="form-check-label" for="female">
                                Женский
                              </label>
                            </div>
                        </div>
                     
                    <div class="form-group">
                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                    </div>
                    
                     <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                    
                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                    
                        <button type="submit" class="btn btn-primary">Записаться</button>
                    </form>
                </div>
              </body>
            </html>
    """

    else:
        return 'Всё классно!'


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Привет, {planet_name}!</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet_name}!</h1>
                        <text></br>Вот она какая, красная планета.</text>

                                                <div class="alert alert-secondary" role="alert">
                                Человечество вырастет из детсвтва.
                            </div>
                            <div class="alert alert-success" role="alert">
                                Человечеству мала одна планета.
                            </div>
                            <div class="alert alert-secondary" role="alert">
                                Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-warning" role="alert">
                                И начнем с планеты {planet_name}!
                            </div>
                            <div class="alert alert-danger" role="alert">
                                Присединяйся!
                            </div>

                      </body>

                    </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname: str, level: int, rating: float):
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
    
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
              rel="stylesheet"
              integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
              crossorigin="anonymous">
    
        <title>Результаты</title>
    
    </head>
    <body>
    <h1> Результаты отбора </h1>
    <h2> Претендент на участие в миссии {nickname}:</h2>
    <div class="alert alert-success">
        Поздравляем! Ваш рейтинг после {level} этапа отбора
    </div>
    <div>
        Составляет {rating}!
    </div>
    <div class="alert alert-warning">
        Желаем удачи!
    </div>
    </body>
    </html>
    '''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''
    <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
    <title>Пример формы</title>
</head>
<body>
<h1>Загрузка фотографии для участия в миссии</h1>
<img src="{url_for('static', filename='img/user_image.png')}">
<form method="post" enctype="multipart/form-data">
    <div class="form-group">
        <label for="photo">Выберите файл</label>
        <input type="file" class="form-control-file" id="photo" name="file">
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
</body>
</html>
    '''
    elif request.method == 'POST':
        f = request.files['file']
        image = Image.open(f)
        image.save('static/img/user_image.png')
        return f'''
    <!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
    <title>Пример формы</title>
</head>
<body>
<h1>Загрузка фотографии для участия в миссии</h1>
<img src="{url_for('static', filename='img/user_image.png')}">
<form method="post" enctype="multipart/form-data">
    <div class="form-group">
        <label for="photo">Выберите файл</label>
        <input type="file" class="form-control-file" id="photo" name="file">
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
</form>
</body>
</html>
    '''


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
