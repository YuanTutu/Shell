#配合11_07aiohttp使用
from flask import Flask
import time

app = Flask(__name__)

@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'Hello bobo'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'hello jay'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'hello tom'

if __name__ == '__main__':
    app.run(threaded=True)