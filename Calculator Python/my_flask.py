from flask import Flask
from main import *
import unittest

app = Flask(__name__)


@app.route('/', methods=['GET'])
def init():
    return '<div style="text-align: center; margin-top: 300px; font-size: 30px;"><h1>Please enter a mathematical expression</h1></div>'


@app.route('/<string:expression>', methods=['GET'])
def calc(expression):
    return '<div style="text-align: center; margin-top: 300px; font-size: 30px;"><h1>' + Main().run_calc(expression) + '</h1></div>'


@app.route('/<string:expression>/<string:extension>', methods=['GET'])
def calc_extension(expression, extension):
    main = Main()
    return '<div style="text-align: center; margin-top: 300px; font-size: 30px;"><h1>' + main.extension_invoker(extension, main.run_calc(expression)) + '</h1></div>'


if __name__ == '__main__':
    app.run(debug=True)
    unittest.main()



