import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return os.getenv("TEST_VAR") + "!"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
