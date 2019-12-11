import json
import numpy as np
from flask import request, jsonify
from app import app
from topsis import topsis


@app.route('/ranking', methods=['POST'])
def upload_file():
    candidates_list = json.loads(request.data, encoding='utf-8')
    point_array = []
    for candidate in candidates_list:
        candidate_point = [candidate.get("gpa", 0) * 2.5, candidate.get("english", 0) / 100,
                           candidate.get("attitude", 0), candidate.get("team_work", 0),
                           candidate.get("communication_skill", 0), candidate.get("experience", 0)]
        point_array.append(candidate_point)

    matrix = np.array(point_array)
    model = topsis.TOPSIS(matrix, None, np.array([0] * 6))
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
