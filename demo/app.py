from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from randombing import RandomBingimage

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    bing=RandomBingimage()
    url = bing.getRandomImage()
    return render_template('home.html',url=url)

@app.route('/hello/<name>')
def hello(name):
    return '<h1>Hello %s!</h1>' % (name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def server_internal_error(e):
    return render_template('500'),500

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
