from flask import Flask, jsonify, Response, render_template
from flask_cors import CORS


app = Flask(
    __name__,
    template_folder="../dist",
    static_folder="../dist/static"
)

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


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path: str) -> str:
    print(f'{path = }')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
