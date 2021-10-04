from flask import Flask, jsonify, Response, request
from flask_cors import CORS
from typing import Dict, List
from main import solve


app = Flask(__name__,)


cors = CORS(
    app,
    resources={
        r"/api/*": {
            "origins": "*"
        }
    },
)


@app.route('/api/v1.0/message')
def message() -> Response:
    return jsonify('Hello world from Flask')


@app.route('/api/v1.0/solve', methods=["POST"])
def solution() -> Response:
    if request.method == "POST":
        response: Dict[str, str] = request.get_json()
        inp: List[str] = response['input'].split('\n')
        inp = list(map(lambda s: s.strip(), inp))
        solution = solve(inp)
        print(f'{inp}')
        return jsonify('This is your solution: .I.')


if __name__ == "__main__":
    app.run(debug=True)
