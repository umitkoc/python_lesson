from flask import Flask , render_template
from os import environ
from requests import get


app=Flask(__name__)
@app.route('/login/<name>',methods=['Get'])
def home(name):
    return name
@app.route('/')
def github():
    response=get("https://www.youtube.com/")
    return response.content
@app.errorhandler(404)
def error():
    return render_template('error.html'),404


if '__main__'==__name__:
    app.debug=True
    port=int(environ.get('PORT',5000))
    app.run(host='127.0.0.1',port=port)
