import os
from flask import Flask, jsonify
from flask_swagger import swagger

from traveller_app.routes.swagger_routes import swaggerui_blueprint

app = Flask(__name__)
app.register_blueprint(swaggerui_blueprint)

@app.route("/hello", )
def hello():
    """
    Return a test message
    ---
    tags:
        - hello
    responses:
        200:
            description: Hello!
    :return:
    """
    return os.getenv("TEST_VAR") + "!"

@app.route("/api/specs")
def specs():
    swagger_specs = swagger(app)
    swagger_specs['info']['version'] = "1.0"
    swagger_specs['info']['title'] = "Travellers API"
    return jsonify(swagger_specs)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
