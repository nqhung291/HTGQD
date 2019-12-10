from flask import request, jsonify, Response
from app import app, mongo
from app.schemas import validate_candidate
from bson import json_util
import json


@app.route('/candidate', methods=['GET', 'POST', 'PATCH'])
def candidate():
    if request.method == 'GET':
        query = request.args
        result = mongo.db.htgqd.find(query)
        return_data = [person for person in result]
        return json.dumps(return_data, default=json_util.default), 200

    data = json.loads(request.data, encoding='utf-8')
    if request.method == 'POST':
        validated = validate_candidate(data)
        if validated['ok']:
            mongo.db.htgqd.insert_one(data)
        return jsonify({'code': '00', 'message': 'Candidate created successfully'})
