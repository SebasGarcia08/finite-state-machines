from flask import Flask, jsonify, Response, request, render_template
from flask_cors import CORS
from typing import Dict, List
from main import solve


app = Flask(__name__, template_folder="../dist", static_folder="../dist/static")


cors = CORS(app, resources={r"/api/*": {"origins": "*"}},)


@app.route("/api/v1.0/solve", methods=["POST"])
def solution() -> Response:
    if request.method == "POST":
        response: Dict[str, str] = request.get_json()
        inp: List[str] = response["input"].split("\n")
        inp = list(map(lambda s: s.strip(), inp))
        solutions = solve(inp)
        solutions_str = ""
        for i, (input_fsm, minimum_connected_fsm) in enumerate(solutions):
            solutions_str += f"TEST CASE {i+1}\n"
            solutions_str += "INPUT AUTOMATA: \n"
            solutions_str += str(input_fsm) + "\n\n"
            solutions_str += "MINIMUM CONNECTED \n"
            solutions_str += str(minimum_connected_fsm) + "\n"
            solutions_str += "#" * 100 + "\n"
        print(f"{inp}")
        return jsonify(solutions_str)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def render_vue(path: str) -> str:
    print(f"{path = }")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
