from flask import Flask, jsonify, Response
from flask_cors import CORS


app = Flask(__name__,)


cors = CORS(
    app,
    resources={
        r"/api/*": {
            "origins": "*"
        }
    }
)


@app.route('/api/v1.0/message')
def message() -> Response:
    return jsonify('Hello world from Flask')


if __name__ == "__main__":
    app.run(debug=True)
