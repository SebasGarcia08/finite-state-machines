from flask import Flask, jsonify, Response, request, render_template
from flask_cors import CORS
from typing import Dict, List
from main import solve as solve_fsm
from cyk import solve as solve_cyk, del_extra_spaces, parse_input


app = Flask(__name__, template_folder="../dist", static_folder="../dist/static")


cors = CORS(app, resources={r"/api/*": {"origins": "*"}},)


@app.route("/api/v1.0/solve", methods=["POST"])
def solution() -> Response:
    if request.method == "POST":
        response: Dict[str, str] = request.get_json()
        inp: List[str] = response["input"].split("\n")
        inp = list(map(lambda s: s.strip(), inp))
        solutions = solve_fsm(inp)
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


@app.route("/api/v1.0/cyk/solve", methods=["POST"])
def cyk_solve() -> Response:
    try:
        if request.method == "POST":
            response: Dict[str, str] = request.get_json()
            lines: List[str] = response["input"].split("\n")
            n = int(lines[0])
            lines = list(map(del_extra_spaces, lines[1:]))
            solutions_str = ""
            for i, (G, string) in enumerate(parse_input(lines, n)):
                ans = solve_cyk(G, string)
                solutions_str += f"TEST CASE {i}\n"
                solutions_str += f"Answer: {ans.result}\n"
                solutions_str += f"Input string: \n{ans.string}\n"
                solutions_str += "Table: \n"
                for r in ans.table:
                    solutions_str += str(r) + "\n"
                solutions_str += "Detailed explanation\n"
                solutions_str += ans.explanation
                solutions_str += "#" * 100 + "\n"
            return jsonify(solutions_str)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def render_vue(path: str) -> str:
    print(f"{path = }")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
