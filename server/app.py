from flask import Flask, request, jsonify
from flask_cors import CORS
from topsis import topsis
import numpy as np
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/upload', methods=['POST'])
def upload_file():
    parsed_json = json.loads(request.data, encoding='utf-8')
    print(parsed_json)
    point_array = []
    for candidate in parsed_json:
        candidate_point = [candidate.get("Điểm 1", 0), candidate.get("Điểm 2", 0), candidate.get("Điểm 3", 0),
                           candidate.get("Điểm 4", 0), candidate.get("Điểm 5", 0), candidate.get("Điểm 6", 0),
                           candidate.get("Điểm 7", 0), candidate.get("Điểm 8", 0), candidate.get("Điểm 9", 0),
                           candidate.get("Điểm 10", 0)]
        point_array.append(candidate_point)

    matrix = np.array(point_array)
    model = topsis.TOPSIS(matrix, None, np.array([0] * 10))
    model.run()
    res = {
        'message': 'success'
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run()
