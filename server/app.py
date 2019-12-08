from flask import Flask, request, jsonify
from flask_cors import CORS
from topsis import topsis
import numpy as np
import json

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    candidates_list = json.loads(request.data, encoding='utf-8')
    point_array = []
    print(candidates_list)
    for candidate in candidates_list:
        candidate_point = [candidate.get("point1", 0), candidate.get("point2", 0), candidate.get("point3", 0),
                           candidate.get("point4", 0), candidate.get("point5", 0), candidate.get("point6", 0),
                           candidate.get("point7", 0), candidate.get("point8", 0), candidate.get("point9", 0),
                           candidate.get("point10", 0)]
        point_array.append(candidate_point)

    matrix = np.array(point_array)
    model = topsis.TOPSIS(matrix, None, np.array([0] * 10))
    model.run()

    for i in range(0, len(model.rank)):
        (candidates_list[i])['point'] = model.rank[i]

    result = sorted(candidates_list, key=lambda x: x['point'], reverse=True)

    for i in range(0, len(result)):
        (result[i])['rank'] = i + 1

    res = {
        'code': '200',
        'message': 'success',
        'data': result
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run()
